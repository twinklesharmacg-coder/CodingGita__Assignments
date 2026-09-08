## Assignment 1 – Understanding HEAD and Basic Reset (Easy)

**Goal:** Practice viewing history and using a simple mixed reset.

1. Create or open your practice repository.
2. Make three simple commits (you can create/edit a file called `notes.txt`):
   - Commit 1: Add some text → commit message `"First note"`
   - Commit 2: Add more text → commit message `"Second note"`
   - Commit 3: Add more text → commit message `"Third note"`
3. Run:
   ```bash
   git log --oneline
   ```
4. Reset to the previous commit using:
   ```bash
   git reset HEAD~1
   ```
5. Run `git log --oneline` and `git status` again.
6. Observe what happened to the latest commit and the file changes.

**Submit:**
- Screenshot of `git log --oneline` **before** reset
- Screenshot of `git log --oneline` and `git status` **after** reset
- Repository link

---
Answers
<img width="1252" height="807" alt="Screenshot 2026-09-08 220111" src="https://github.com/user-attachments/assets/4820f530-f484-4b92-9799-f5f98fed0265" />
<img width="1282" height="813" alt="Screenshot 2026-09-08 220319" src="https://github.com/user-attachments/assets/7dfa63b2-603e-4b78-ba5b-0ee27d439acf" />
https://github.com/twinklesharmacg-coder/git--reset-command-practice



## Assignment 2 – Difference between --soft, --mixed and --hard (Medium)

**Goal:** Clearly see how the three reset modes behave differently.

1. Create a new file `demo.txt` and make **two commits** on it.
2. Perform the following one by one (create fresh commits each time if needed):

   **A. Soft Reset**
   ```bash
   git reset --soft HEAD~1
   git status
   ```

   **B. Mixed Reset**
   ```bash
   git reset --mixed HEAD~1
   git status
   ```

   **C. Hard Reset**
   ```bash
   git reset --hard HEAD~1
   git status
   ```
   Answer
   <img width="1258" height="837" alt="Screenshot 2026-09-08 221044" src="https://github.com/user-attachments/assets/be76722b-e416-4379-9492-b76ab3c7affd" />
   <img width="1296" height="860" alt="Screenshot 2026-09-08 221303" src="https://github.com/user-attachments/assets/2bef73a5-690f-4022-8684-9c445f2a8812" />
   <img width="1275" height="847" alt="Screenshot 2026-09-08 221428" src="https://github.com/user-attachments/assets/a6e2b2d7-1392-4646-8b86-71687a7bea25" />
   https://github.com/twinklesharmacg-coder/git--reset-command-practice




4. write the short answers in your own words in your notebook:
   - What is the difference between `--soft`, `--mixed`, and `--hard`?
   - Which one keeps changes staged?
   - Which one discards the changes completely?
   - When should you avoid `--hard`?

**Submit:**
- Screenshots of `git status` after each type of reset (`--soft`, `--mixed`, `--hard`)
- Photos of written answers.
- Repository link

---

## Assignment 3 – Practice git revert (Medium)

**Goal:** Safely undo a commit using `git revert` instead of reset.

1. Make sure you have at least 2–3 commits on `main`.
2. Choose the latest commit and revert it:
   ```bash
   git revert HEAD
   ```
   (Save the commit message that Git opens)
3. Run:
   ```bash
   git log --oneline
   ```
4. Observe that a **new commit** was created (the history was not deleted).
5. write the short answers in your own words in your notebook:
   - What does `git revert` do?
   - How is it different from `git reset`?
   - When is `git revert` safer than `git reset`?

**Submit:**
- Screenshot of `git log --oneline` showing the revert commit
- Photos of written answers.
- Repository link

---

## Assignment 4 – Combined Practice + Safety Rules (Hard)

**Goal:** Combine reset and revert knowledge and demonstrate safe practices.

1. Create a small project flow:
   - Make 3 commits on a file called `project.txt`.
2. Use `git reset --soft HEAD~1` and then create a new improved commit.
3. Later, use `git revert` on one commit and show that history is preserved.
4. Write short answers in your notebook:
   - When should you use `git reset --soft`?
   - When should you use `git reset --hard`? (and why be careful)
   - When should you prefer `git revert`?
   - What do `HEAD`, `HEAD~1`, and `HEAD~2` mean?

**Submit:**
- Screenshot of final `git log --oneline`
- Photos of written answers.
- Repository link

---

## Submission Checklist

| # | Item | Required? |
|---|------|-----------|
| 1 | Assignment 1 – before/after reset screenshots | Yes |
| 2 | Assignment 2 – three reset mode screenshots + written answer photos | Yes |
| 3 | Assignment 3 – revert screenshot + written answer photos | Yes |
| 4 | Assignment 4 – final log + written answer photos | Yes |
| — | GitHub repository link | Yes |

**Important Notes:**
- Be very careful with `git reset --hard` — it can delete your work.
- Prefer `git revert` when commits are already pushed to GitHub.
- Always check `git log --oneline` and `git status` before and after these commands.
