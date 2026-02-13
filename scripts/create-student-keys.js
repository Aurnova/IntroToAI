#!/usr/bin/env node
/**
 * Create one OpenRouter API key per student with $10/month limit.
 * Optionally set OPENROUTER_API_KEY on each student's GitHub repo (requires gh CLI + GITHUB_TOKEN).
 *
 * Usage:
 *   export OPENROUTER_MANAGEMENT_KEY="sk-or-v1-..."
 *   export GITHUB_TOKEN="ghp_..."   # optional; used with gh CLI to set repo secrets
 *   node create-student-keys.js students.csv
 *
 * students.csv must have header: student_id,repo
 * repo = "repo-name" (same org as GITHUB_TOKEN) or "org/repo-name"
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const OPENROUTER_KEYS_URL = 'https://openrouter.ai/api/v1/keys';
const MANAGEMENT_KEY = process.env.OPENROUTER_MANAGEMENT_KEY;
const GITHUB_TOKEN = process.env.GITHUB_TOKEN;

if (!MANAGEMENT_KEY) {
  console.error('Set OPENROUTER_MANAGEMENT_KEY (from https://openrouter.ai/settings/management-keys)');
  process.exit(1);
}

const csvPath = process.argv[2];
if (!csvPath || !fs.existsSync(csvPath)) {
  console.error('Usage: node create-student-keys.js students.csv');
  console.error('CSV must have header: student_id,repo');
  process.exit(1);
}

const csv = fs.readFileSync(csvPath, 'utf8');
const lines = csv.trim().split('\n');
const header = lines[0].toLowerCase().split(',').map((h) => h.trim());
const studentIdx = header.indexOf('student_id');
const repoIdx = header.indexOf('repo');
if (studentIdx === -1 || repoIdx === -1) {
  console.error('CSV must have columns: student_id, repo');
  process.exit(1);
}

const rows = lines.slice(1).map((line) => {
  const parts = line.split(',').map((p) => p.trim());
  return { student_id: parts[studentIdx], repo: parts[repoIdx] };
}).filter((r) => r.student_id && r.repo);

async function createKey(name, limit = 10, limitReset = 'monthly') {
  const res = await fetch(OPENROUTER_KEYS_URL, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${MANAGEMENT_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ name, limit, limit_reset: limitReset }),
  });
  if (!res.ok) {
    const err = await res.text();
    throw new Error(`OpenRouter ${res.status}: ${err}`);
  }
  const data = await res.json();
  return data.key; // only time the raw key is returned
}

function setGitHubSecret(repo, secretValue) {
  try {
    execSync('gh secret set OPENROUTER_API_KEY -R ' + repo, {
      input: secretValue,
      env: { ...process.env, GH_TOKEN: GITHUB_TOKEN },
      stdio: ['pipe', 'pipe', 'pipe'],
    });
    return true;
  } catch (e) {
    return false;
  }
}

async function main() {
  const results = [];
  for (const row of rows) {
    const name = `Intro to AI - ${row.student_id}`;
    process.stderr.write(`Creating key for ${row.student_id}... `);
    try {
      const key = await createKey(name);
      results.push({ student_id: row.student_id, repo: row.repo, key });
      process.stderr.write('ok\n');

      if (GITHUB_TOKEN && row.repo) {
        process.stderr.write(`  Setting OPENROUTER_API_KEY on ${row.repo}... `);
        const ok = setGitHubSecret(row.repo, key);
        process.stderr.write(ok ? 'ok\n' : 'skip (install gh CLI and ensure token has repo access)\n');
      }
    } catch (e) {
      process.stderr.write(`error: ${e.message}\n`);
    }
  }

  const outPath = path.join(path.dirname(csvPath), 'keys.csv');
  const outCsv = 'student_id,api_key\n' + results.map((r) => `${r.student_id},${r.key}`).join('\n');
  fs.writeFileSync(outPath, outCsv, 'utf8');
  console.log(`\nWrote ${results.length} keys to ${outPath}. Do not commit this file.`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
