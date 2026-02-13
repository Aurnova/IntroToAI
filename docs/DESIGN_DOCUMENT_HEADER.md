# Aurnova MSAI Codespaces-First Core Agent Architecture
## Design Document (v0.1)

**Owner:** Daniel McShan  
**Audience:** Aurnova University leadership, program ops, instructors/TAs, platform engineer(s)  
**Scope:** The standardized "Core Agent Architecture" (CAA) used across MSAI + Certificate, delivered via GitHub Classroom + Codespaces, integrated with Populi as system-of-record.

---

## 1. Executive summary

*(2–3 paragraphs: what CAA is, why Codespaces-first, how it serves MSAI + Certificate and ties to Populi.)*

---

## 2. Goals and principles

- **Goal 1:** *(e.g. Standardized, reproducible dev environment for all students.)*
- **Goal 2:** *(e.g. Single integration point with SIS for rosters and grades.)*
- **Goal 3:** *(e.g. …)*

**Principles:** *(e.g. Security, consistency, instructor control, auditability.)*

---

## 3. Architecture overview

### 3.1 Core components

| Component | Purpose |
|-----------|---------|
| *(e.g. GitHub Classroom)* | *(e.g. Assignment distribution, repo-per-student.)* |
| *(e.g. Codespaces)* | *(e.g. Browser-based dev environment.)* |
| *(e.g. CAA / agent stack)* | *(e.g. …)* |
| *(e.g. Populi)* | *(e.g. System of record, roster, grades.)* |

### 3.2 Data and identity flow

*(Short description or diagram placeholder: student → Classroom → Codespaces → Populi.)*

---

## 4. Delivery: GitHub Classroom + Codespaces

- **Classroom:** Template repos, assignment lifecycle, roster (optional import from Populi or CSV).
- **Codespaces:** Dev container definition, preinstalled tools, optional AI agents (e.g. Continue, Tutor).
- **Student experience:** *(Accept assignment → open in Codespaces → work → push → submit.)*

---

## 5. Integration with Populi

- **Roster:** *(How section/roster data flows from Populi to Classroom or vice versa, if applicable.)*
- **Grades / completion:** *(How assignment completion or grades are recorded in Populi, if applicable.)*
- **Single source of truth:** *(Populi as SIS; what stays in GitHub vs Populi.)*

---

## 6. Roles and responsibilities

| Role | Responsibilities |
|------|------------------|
| *Program / leadership* | *(e.g. Approval, resourcing, policy.)* |
| *Program ops* | *(e.g. Classroom setup, roster, deadlines.)* |
| *Instructors / TAs* | *(e.g. Assignments, grading, support.)* |
| *Platform engineer(s)* | *(e.g. Templates, dev containers, integrations, keys.)* |

---

## 7. Rollout and phases

- **Phase 1:** *(e.g. Pilot course, single cohort.)*
- **Phase 2:** *(e.g. Full MSAI core.)*
- **Phase 3:** *(e.g. Certificate, other programs.)*

---

## 8. Success criteria and metrics

- *(e.g. All students can open and use Codespaces without local install.)*
- *(e.g. Roster and submission status visible where needed.)*
- *(e.g. …)*

---

## 9. Risks and mitigations

| Risk | Mitigation |
|------|-------------|
| *(e.g. Codespaces availability / cost)* | *(e.g. …)* |
| *(e.g. Key management for AI)* | *(e.g. …)* |

---

## 10. Appendix and references

- *(Links to Classroom docs, Codespaces docs, Populi API or integration notes, internal runbooks.)*
