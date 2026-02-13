# Gradebook export schema

Export from GitHub (PR merge status, CI, rubric scores) to CSV for import into Populi.

## Suggested CSV columns

| Column | Description |
|--------|-------------|
| `student_id` | Populi or roster identifier |
| `github_username` | GitHub login |
| `repo` | e.g. msai-2026-agent-<username> |
| `a0_pass` | pass / fail |
| `a1_score` | 0–100 or points |
| `a2_score` | … |
| `last_pr_at` | Timestamp of last merged PR (optional) |

## Implementation

- Lived in **msai-infra** repo: scripts that map roster (Populi↔GitHub), query GitHub API or Classroom for PR/CI status, apply rubrics, output CSV.
- Import into Populi per institutional process.
