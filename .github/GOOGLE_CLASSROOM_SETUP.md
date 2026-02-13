# Set up Intro to AI with Google Classroom

Use **Google Classroom** for your course shell and roster, and **GitHub Classroom** so each student gets their own repo (with Codespaces + AI). Students do work in their GitHub repo and can submit the repo link or confirm completion in Google Classroom.

---

## 1. Create the Google Classroom

1. Go to [classroom.google.com](https://classroom.google.com) and sign in.
2. Click **Create** → **Class**.
3. **Class name:** e.g. `Intro to AI` or `IntroToAI`.
4. (Optional) Add section, subject, room. Click **Create**.
5. Share the **class code** with students so they join, or invite them by email.

---

## 2. Set up GitHub Classroom (one-time)

1. **Template repo:** On GitHub, make **Aurnova/IntroToAI** a template repo (Settings → General → Template repository).
2. **GitHub Classroom:** Go to [classroom.github.com](https://classroom.github.com). Create a **Classroom** (e.g. “Intro to AI”) linked to the **Aurnova** org.
3. **Create the assignment:** In that Classroom, click **New assignment**.
   - **Template:** Aurnova/IntroToAI
   - **Title:** e.g. `Intro to AI – Assignment repository`
   - **Individual** (or groups if you prefer)
   - **Repo name:** e.g. `intro-to-ai-{{ student_identifier }}`
   - **Visibility:** Private
   - Create the assignment and **copy the invitation link** (you’ll use it in Google Classroom).
4. **Import roster from Google Classroom:**
   - In GitHub Classroom, open your classroom → **Students** tab.
   - Click **Import from...** → **Google Classroom**.
   - Sign in to Google and select your **Intro to AI** class.
   - Choose the student identifier (e.g. email or name) and click **Import roster entries**.

After this, the same set of students is in both Google Classroom and GitHub Classroom.

---

## 3. Create assignments in Google Classroom

Create one Google Classroom assignment per unit. Each can include:

- **Instructions** (copy from the sections below).
- **Link** to the GitHub invitation (first assignment only) or to the course docs/syllabus.
- **Due date** and points if you use them.
- **Submission:** “Add link” or “Assignment (upload)” so students paste their repo URL or confirm they pushed.

### Assignment 1: Getting started (first assignment)

**Title:** Assignment 1 – Getting started  

**Instructions (paste into Google Classroom):**

```
1. Accept your GitHub assignment (one-time setup)
   • Open this link: [PASTE YOUR GITHUB CLASSROOM INVITATION LINK HERE]
   • Sign in to GitHub (create an account if needed) and accept the assignment.
   • This creates your private repo: intro-to-ai-YOUR_IDENTIFIER.

2. Open your repo in Codespaces
   • In your repo, click Code → Codespaces → Create codespace on main.
   • Wait for the dev container to finish building.

3. Complete the getting-started tasks
   • In the repo, open: assignments/01-getting-started/README.md
   • Do the tasks (add your name and one thing you want to learn, etc.).
   • Commit and push your changes (e.g. Source Control → Commit → Push).

4. Submit
   • Turn in the link to your GitHub repo (e.g. https://github.com/Aurnova/intro-to-ai-YOUR_IDENTIFIER).
   • Or write "Done" and paste the repo link in the private comment.
```

**Submission:** Students add a link (their repo URL). Due date: set as needed.

---

### Assignments 2–5 (use one per Google Classroom assignment)

| GC # | Title | Folder in repo |
|------|--------|----------------|
| 2 | Assignment 2 – What is AI? | `assignments/02-what-is-ai/README.md` |
| 3 | Assignment 3 – Prompting basics | `assignments/03-prompting-basics/README.md` |
| 4 | Assignment 4 – Coding with AI | `assignments/04-coding-with-ai/README.md` |
| 5 | Assignment 5 – Final project and reflection | `assignments/05-final-project-and-reflection/README.md` |

**Instructions (paste into each Google Classroom assignment and edit the folder name):**

```
Work in your Intro to AI repo (the one you accepted in Assignment 1).

1. Open your repo in Codespaces (Code → Codespaces → open your existing codespace or create new).
2. Complete the tasks in: assignments/[02-what-is-ai, 03-prompting-basics, 04-coding-with-ai, or 05-final-project-and-reflection]/README.md
3. Commit and push your work.
4. Submit: paste your repo link here, or write "Done" and add the link in the private comment.
```

---

## 4. Optional: OpenRouter keys for students

If your institution provides one OpenRouter key per student ($10/month):

- Run the script in [.github/INSTITUTE_OPENROUTER_KEYS.md](INSTITUTE_OPENROUTER_KEYS.md) **after** students have accepted the GitHub assignment (so their repos exist). Use a CSV with `student_id` and `repo` (e.g. `intro-to-ai-jane`). The script can set `OPENROUTER_API_KEY` on each repo so Codespaces has the key.

---

## 5. Course materials link

In Google Classroom, under **Classwork**, add a **Material** or **Assignment** that links to:

- **Course site (if you use GitHub Pages):** `https://aurnova.github.io/IntroToAI/`
- **Syllabus:** `https://aurnova.github.io/IntroToAI/syllabus.html`
- **Readings:** `https://aurnova.github.io/IntroToAI/readings.html`

Students can use this for syllabus, readings, and deadlines.

---

## Quick checklist

- [ ] Google Classroom “Intro to AI” created; students invited.
- [ ] Aurnova/IntroToAI set as a template repo on GitHub.
- [ ] GitHub Classroom created and linked to Aurnova org.
- [ ] One assignment created in GitHub Classroom (template: IntroToAI); invitation link copied.
- [ ] Roster imported into GitHub Classroom from Google Classroom (Students → Import from Google Classroom).
- [ ] In Google Classroom: Assignment 1 created with instructions above and the GitHub invitation link pasted in.
- [ ] (Optional) Later assignments created in Google Classroom pointing to the right `assignments/` folders.
- [ ] (Optional) OpenRouter keys created and set on student repos per INSTITUTE_OPENROUTER_KEYS.md.
