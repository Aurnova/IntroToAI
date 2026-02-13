# Course skeleton template

Standard structure for MSAI / Certificate courses delivered via GitHub Classroom + Codespaces. Use this to create or audit a new course repo.

---

## Repo layout

```
course-repo/
├── README.md                    # Course name, Codespaces + AI setup, student instructions
├── .devcontainer/
│   ├── devcontainer.json        # Image, features, postCreateCommand
│   └── setup-ide-tutor.sh       # (Optional) Install Continue + Tutor AI
├── docs/
│   ├── index.md                 # (Optional) Course landing / Jekyll index
│   ├── syllabus.md              # Syllabus with schedule and assignment links
│   ├── readings.md              # (Optional) Readings list
│   └── COURSE_SKELETON.md       # (Optional) This file for reference
├── assignments/
│   ├── README.md                # Assignment index table + submission instructions
│   ├── 01-<slug>/README.md       # One README per assignment
│   ├── 02-<slug>/README.md
│   └── ...
└── .github/
    ├── CLASSROOM_SETUP.md       # (Optional) GitHub Classroom one-time setup
    ├── GOOGLE_CLASSROOM_SETUP.md # (Optional) Google Classroom + Classroom mapping
    └── INSTITUTE_OPENROUTER_KEYS.md # (Optional) Bulk OpenRouter key script
```

---

## 1. Root README.md (skeleton)

```markdown
# [Course name]

A GitHub Classroom–ready course repo. Use **GitHub Codespaces** for a consistent environment and optional **AI assistants** (Continue + Tutor) via OpenRouter.

---

## For students

### 1. Accept the assignment
- Use the **GitHub Classroom invitation link** from your instructor.

### 2. Open in Codespaces
- In your repo: **Code** → **Codespaces** → **Create codespace on main**.

### 3. Do the work
- Assignments are in `assignments/`. Open each folder’s README for tasks.
- **Submit:** Commit and push to the default branch by the deadline.

---

## For instructors

- **Syllabus:** [docs/syllabus.md](docs/syllabus.md)
- **Classroom setup:** [.github/CLASSROOM_SETUP.md](.github/CLASSROOM_SETUP.md) (and optionally GOOGLE_CLASSROOM_SETUP.md)
```

---

## 2. docs/syllabus.md (skeleton)

```markdown
---
layout: default
title: Syllabus
---

# Syllabus — [Course name]

*(Instructor: replace with your syllabus.)*

---

## Course overview

**[Course name]** [one sentence]. Students use GitHub Codespaces and optional AI assistants (Continue, Tutor) via OpenRouter.

---

## Learning objectives

By the end of the course, students will be able to:

- [Objective 1]
- [Objective 2]
- [Objective 3]

---

## Schedule (1 lecture per week)

| Week | Topic | Assignment |
|------|--------|------------|
| 1 | [Topic] | 1: [Assignment title](https://github.com/ORG/REPO/blob/main/assignments/01-<slug>/README.md) |
| 2 | [Topic] | 2: [Assignment title](https://github.com/ORG/REPO/blob/main/assignments/02-<slug>/README.md) |
| … | … | … |

---

## Assignments and grading

- Work lives in `assignments/`; submit by pushing to the default branch.
- *(Add: weights, late policy, etc.)*

---

## Tools and resources

- **Environment:** GitHub Codespaces.
- **AI:** Continue (coding) and Tutor AI (concepts), via OpenRouter.
- **Readings:** [docs/readings.md](readings.md) *(if used)*

---

## Policies

*(Attendance, integrity, accommodations, contact.)*
```

---

## 3. assignments/README.md (skeleton)

```markdown
# Assignments

This folder contains **[N] assignments** for [Course name]. Do the work in each assignment’s folder and push to the default branch to submit.

| # | Folder | Topic |
|---|--------|--------|
| 1 | [01-<slug>](01-<slug>/README.md) | [Short description] |
| 2 | [02-<slug>](02-<slug>/README.md) | [Short description] |
| … | … | … |

## What to do

1. **Read the assignment** – Open the README for the assignment.
2. **Do the work** – Write answers or code in that folder as the README specifies.
3. **Commit and push** – Push to the default branch before the deadline.

## Submitting

- Push to the **default branch** by the deadline. Your instructor grades from this repo.

## Using the AI assistants

You can use **Continue** (coding) and **Tutor AI** (concepts). See the main [README](../README.md) for OpenRouter key setup.
```

---

## 4. Single assignment folder (skeleton)

**Folder name:** `assignments/NN-<slug>/` (e.g. `01-getting-started`, `02-prompting-basics`).

**README.md:**

```markdown
# Assignment [N]: [Title]

## Goals

- [Goal 1]
- [Goal 2]

## Tasks

1. **[Task title]**  
   [Instructions.]

---

**Prompt / question or placeholder:**  
*(Replace this line.)*

---

2. **[Next task]**  
   [Instructions.]

3. **Commit and push**  
   Commit your changes and push to the default branch. That’s your submission.
```

**Conventions:**

- One folder per assignment; number with zero-padding (`01-`, `02-`, …).
- Each folder has a `README.md` with: **Goals**, **Tasks**, and clear “commit and push” as submission.
- Optional: add `script.py`, `report.md`, `.ipynb`, or other deliverables in the same folder.

---

## 5. .github (optional)

- **CLASSROOM_SETUP.md** – Template repo, create assignment, invite link, roster.
- **GOOGLE_CLASSROOM_SETUP.md** – One Google Classroom assignment per repo assignment; table mapping GC # to `assignments/NN-<slug>/README.md`.
- **INSTITUTE_OPENROUTER_KEYS.md** – Script/instructions to set `OPENROUTER_API_KEY` on student repos.

---

## 6. .devcontainer (Codespaces)

- **devcontainer.json** – Base image, VS Code extensions, `postCreateCommand` to run setup script if used.
- **setup-ide-tutor.sh** (optional) – Clone/config Continue and install Tutor AI extension so the same CAA runs in every course.

---

## Checklist for a new course

- [ ] Repo created from template (or this skeleton).
- [ ] Root README: course name, student steps, link to syllabus.
- [ ] `docs/syllabus.md`: overview, objectives, schedule table (weeks → assignments), grading, policies.
- [ ] `assignments/README.md`: table of assignments, submit instructions.
- [ ] One folder per assignment (`01-<slug>` …) with README (Goals, Tasks, submit = push).
- [ ] Schedule links point to correct repo and paths.
- [ ] .devcontainer builds and (if used) installs Continue + Tutor.
- [ ] .github docs updated for Classroom and, if used, Google Classroom.
- [ ] Template repo enabled; GitHub Classroom assignment created; invitation link shared.
