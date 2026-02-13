# Institute OpenRouter keys (one key per student, $10/month limit)

Use OpenRouter’s **Management API** to create one API key per student with a **$10/month** spending limit. Students use their key in Codespaces for the Cursor-like AI and Tutor AI; the institute pays from a single OpenRouter account and caps each student at $10/month.

---

## 1. OpenRouter account and credits

1. Create (or use) an **OpenRouter account**: [openrouter.ai](https://openrouter.ai) → sign in.
2. Add **credits** (Settings → Credits): enough to cover the class, e.g. **$10 × number of students** per month (plus buffer). OpenRouter charges a small fee when you add credits; pricing is per use with no markup.
3. Create a **Management API key** (used only for creating/managing keys, not for AI calls):
   - Go to [Management API Keys](https://openrouter.ai/settings/management-keys).
   - Click **Create New Key**, name it e.g. `Intro to AI – key management`.
   - Copy and store the key securely (e.g. in a secret manager). You’ll use it as `OPENROUTER_MANAGEMENT_KEY` in the script below.

---

## 2. Create one key per student ($10/month limit)

Each student gets their own API key with:

- **Spending limit:** $10 USD  
- **Reset:** monthly (resets at midnight UTC on the 1st)

Use the script in this repo, or call the OpenRouter Key Management API yourself.

### Option A: Use the provided script (recommended)

From the repo root:

```bash
# Install deps once (Node 18+)
cd scripts && npm install

# Create keys and optionally push each key to the student's GitHub repo secret.
# Requires: OPENROUTER_MANAGEMENT_KEY, and for GitHub: GITHUB_TOKEN with repo secrets permission.
export OPENROUTER_MANAGEMENT_KEY="sk-or-v1-..."   # from step 1
export GITHUB_TOKEN="ghp_..."                     # optional; needed only to set repo secrets

# Students list: CSV with header student_id,repo (repo = org/repo-name or full URL)
# Example students.csv:
#   student_id,repo
#   jane,intro-to-ai-jane
#   bob,Aurnova/intro-to-ai-bob

node create-student-keys.js students.csv
```

- **students.csv** must have columns `student_id` and `repo`. `repo` can be `repo-name` (same org as the token) or `org/repo-name`.
- The script creates an OpenRouter API key per row with **limit 10**, **limit_reset monthly**, and name `Intro to AI - <student_id>`.
- If `GITHUB_TOKEN` is set and the token can write repo secrets, the script sets **OPENROUTER_API_KEY** on each repo. Otherwise it writes **keys.csv** (student_id, api_key) for manual or secure distribution.

Never commit `keys.csv` or any file containing API keys. Add `keys.csv` to `.gitignore` (already ignored if you use the suggested pattern).

### Option B: Call the Key Management API yourself

OpenRouter docs: [Management API Keys](https://openrouter.ai/docs/guides/overview/auth/management-api-keys), [Create API key](https://openrouter.ai/docs/api-reference/api-keys/create-api-key).

Example (create one key with $10/month limit):

```bash
curl -X POST "https://openrouter.ai/api/v1/keys" \
  -H "Authorization: Bearer YOUR_MANAGEMENT_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name":"Intro to AI - student-id","limit":10,"limit_reset":"monthly"}'
```

Response includes `key` (the secret) and `data` (hash, limit, limit_remaining, etc.). Create one key per student, then distribute the `key` value (e.g. set as repo secret `OPENROUTER_API_KEY` or send via a secure channel).

---

## 3. Give the key to the student

- **If you used the script with GITHUB_TOKEN:** Each student’s repo already has the secret `OPENROUTER_API_KEY`. They just open the repo in Codespaces; no copy-paste of keys.
- **If you have keys in keys.csv (or from your own API calls):** For each student, set the repo secret `OPENROUTER_API_KEY` to their key (GitHub repo → Settings → Secrets and variables → Actions → New repository secret), or send the key through a secure channel and have them add it in Codespaces as a **user** or **repository** secret.

Students never need to create an OpenRouter account unless you choose to let them use their own key instead.

---

## 4. Monitor usage

- In OpenRouter: [Activity](https://openrouter.ai/activity) and [Credits](https://openrouter.ai/settings/credits). You can filter by API key (label/hash) to see per-student usage.
- Each key’s limit is enforced by OpenRouter; when a student hits $10 in a month, that key stops working until the next monthly reset (or you raise the limit via the [Keys API](https://openrouter.ai/docs/api-reference/api-keys/update-api-key)).

---

## Summary

| Step | Action |
|------|--------|
| 1 | OpenRouter account → add credits → create **Management API key** |
| 2 | Run `scripts/create-student-keys.js` with a students CSV (or create keys via API) — each key: **$10 limit, monthly reset** |
| 3 | Script (or you) sets `OPENROUTER_API_KEY` on each student repo so Codespaces gets the key automatically |
| 4 | Students open repo in Codespaces; Continue and Tutor AI work with no extra setup |
