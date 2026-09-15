# Assignment - git revert • Modify/Delete Conflict • Revert Options • Comparison with reset & restore

---

## Instructions

- Use your **CodingGita_Assignment** repository for all practical work and submission.
- Complete the assignments in order.
- For theoretical questions → write a short and correct answer in your notebook.
- Take clear photos of the written answers.
- Take screenshots of terminal / GitHub where asked.
- Push your practical work to the repository and submit the repository link along with the required photos and screenshots.

**Before you start:** Make sure your working directory is clean (`git status`).

---

## Assignment 1 – Basic Revert Practice

**Goal:** Perform a simple revert and observe the new commit.

1. Create 2–3 commits on any file (for example `index.html` or `notes.txt`).
2. Using `git log --oneline`, note the commit hash of the latest commit.
3. Revert the latest commit:
   ```bash
   git revert HEAD
   ```
   (or use the commit hash)
4. Run `git log --oneline` and observe the new revert commit.

**Submit:**
- Screenshot of `git log --oneline` before revert
- Screenshot of `git log --oneline` after revert
- Repository link

---Answer
<img width="1265" height="858" alt="Screenshot 2026-09-14 184514" src="https://github.com/user-attachments/assets/834ed423-3dcf-428d-9275-34d392f88ea6" />
<img width="1490" height="876" alt="Screenshot 2026-09-14 184700" src="https://github.com/user-attachments/assets/b023e5a5-e16d-4ade-a476-bf1642497217" />

Repo link
https://github.com/twinklesharmacg-coder/git-revert-homework



## Assignment 2 – Modify/Delete Conflict during Revert

**Goal:** Face and resolve a Modify/Delete conflict while reverting.

1. Create a commit that **adds a new file**.
2. Make one more commit after that.
3. Try to revert the commit that added the file.
4. A Modify/Delete conflict should appear.
5. Resolve it (either delete the file or keep it with required content).
6. Use:
   ```bash
   git add .
   git revert --continue
   ```

**Submit:**
- Screenshot of the conflict (VS Code or terminal)
- Screenshot after successful `git revert --continue`
- Repository link

---Answers
<img width="1267" height="818" alt="Screenshot 2026-09-14 185646" src="https://github.com/user-attachments/assets/ffc71e62-142f-402f-913a-d447f722f28c" />
<img width="1298" height="906" alt="Screenshot 2026-09-14 185733" src="https://github.com/user-attachments/assets/22f9e0cc-c2d8-4f25-91c7-07c5f959e5a1" />

Repo link
https://github.com/twinklesharmacg-coder/git-revert-homework


## Assignment 3 – Revert Options + Conceptual Questions

**Goal:** Practice important flags and understand the concepts.

### Practical Part
1. Demonstrate any two of the following commands with a real commit:
   - `git revert --no-edit <commit_id>`
   - `git revert --no-commit <commit_id>`
   - `git revert --abort`
2. Take screenshots of the commands and their results.

### Theoretical Part (Write in Notebook)
Write short and correct answers for the following:

1. What does `git revert` do?
2. Why is `git revert` safer than `git reset` on a shared branch?
3. What is a Modify/Delete conflict? When can it occur during revert?
4. What is the difference between `git revert --abort` and `git revert --quit`?
5. Write one major difference each between:
   - `git restore`
   - `git reset`
   - `git revert`

**Submit:**
- Screenshots of the two practical commands you tried
- Clear photos of the written answers from your notebook
- Repository link

---Answers
<img width="1130" height="861" alt="Screenshot 2026-09-14 190209" src="https://github.com/user-attachments/assets/6d76e66c-613b-4354-83a8-9abea4d57a24" />

<img width="1313" height="883" alt="Screenshot 2026-09-14 190335" src="https://github.com/user-attachments/assets/82aabb07-f46f-4c10-92a6-84ecf7ebf76e" />

<img width="1381" height="878" alt="Screenshot 2026-09-14 190401" src="https://github.com/user-attachments/assets/d1d2927e-6b1c-4766-a83a-ca7936d2701d" />
<img width="894" height="1280" alt="image" src="https://github.com/user-attachments/assets/2fbd49c8-664f-42a3-b031-71bbf31f7420" />
<img width="1188" height="1281" alt="image" src="https://github.com/user-attachments/assets/89f4c6dc-b2af-431e-9050-1fee211f5644" />

https://github.com/twinklesharmacg-coder/git-revert-homework




## Submission Checklist

| # | Item | Required? |
|---|------|-----------|
| 1 | Assignment 1 – before & after log screenshots | Yes |
| 2 | Assignment 2 – conflict + resolution screenshots | Yes |
| 3 | Assignment 3 – practical screenshots + notebook photos | Yes |
| — | CodingGita_Assignment repository link | Yes |

**Important:**
- Push all practical work to your **CodingGita_Assignment** repository.
- Theoretical answers must be handwritten in notebook (photos required).
- Make sure screenshots and photos are clear and readable.

---
