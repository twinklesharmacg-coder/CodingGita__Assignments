# Assignment - git restore • git restore --staged • rm vs git rm vs git rm --cached • .gitignore

---

## Instructions

- Use your CodingGita_assignments repository.
- Complete all assignments in order.
- Take screenshots where asked.
- Submit the **GitHub repository link** along with the required screenshots.

**Before you start:** Make sure your working directory is clean (`git status`).

---

## Assignment 1 – Practice `git restore` and `git restore --staged`

**Goal:** Understand how staging and unstaging works with `git restore`.

1. Create a new file named `profile.txt` and write 3–4 lines about your favorite programming topic.
2. Run `git status` and note that the file is **untracked**.
3. Try the command:
```bash
git restore profile.txt
```
Observe that it does **not** work (because the file is untracked).
4. Stage the file:
```bash
git add profile.txt
```
5. Unstage it using:
```bash
git restore --staged profile.txt
```
6. Run `git status` again and confirm the file is back to untracked / unstaged.
7. Now stage and commit the file properly:
```bash
git add profile.txt
git commit -m "Add profile.txt"
```

**Submit:**
- Screenshot of `git status` when the file was untracked
- Screenshot after using `git restore --staged`
- Repository link

--- Answers
<img width="1162" height="732" alt="Screenshot 2026-09-10 112939" src="https://github.com/user-attachments/assets/9bd477f7-b703-4ca7-8e02-05a2b823938d" />
<img width="1425" height="887" alt="Screenshot 2026-09-10 113250" src="https://github.com/user-attachments/assets/42bddff0-3d70-4787-ba55-cf2535f7b3cb" />
https://github.com/twinklesharmacg-coder/git--reset-command-practice


## Assignment 2 – `rm` vs `git rm`

**Goal:** Understand the difference between normal delete and Git delete.

1. Make sure `profile.txt` is committed on `main`.
2. Delete the file using normal system command:
```bash
rm profile.txt
```
3. Run `git status` and observe the output.
4. Recover the file using:
```bash
git restore profile.txt
```
5. Now delete it properly with Git:
```bash
git rm profile.txt
```
6. Run `git status` again and observe the difference.
7. Commit the deletion:
```bash
git commit -m "Remove profile.txt using git rm"
```
8. Create a short file named `delete-difference.txt` and write in your own words:
- What is the difference between `rm` and `git rm`?
- When should you use `git rm`?

**Submit:**
- Screenshots of `git status` after `rm` and after `git rm`
- Content of `delete-difference.txt`
- Repository link

---Answer
<img width="1442" height="862" alt="Screenshot 2026-09-10 135938" src="https://github.com/user-attachments/assets/20e65c39-74f2-45bc-9526-8440e202e2af" />
<img width="1495" height="897" alt="Screenshot 2026-09-10 140209" src="https://github.com/user-attachments/assets/3b44847c-cc6a-45af-8420-d94a41f38ac2" />
<img width="1083" height="352" alt="Screenshot 2026-09-10 141304" src="https://github.com/user-attachments/assets/a9cd69e9-91ed-4eb0-8b01-35ce94992808" />





## Assignment 3 – `.gitignore` + `git rm --cached`

**Goal:** Properly ignore sensitive files and practice stopping Git from tracking a file using `git rm --cached`.

1. Create a file named `config.env` with sample secret data:
```env
DB_PASSWORD=SuperSecretPass999
API_KEY=sk-test-abc123xyz789
```

2. **Intentionally** add and commit it (to practice the fix):
```bash
git add config.env
git commit -m "Accidentally commit config.env"
```

3. Create a folder named `vendor` and put any dummy file inside it.

4. Create a `.gitignore` file and add:
```gitignore
vendor/
config.env
```

5. Stop tracking `config.env` but **keep the file on your computer**:
```bash
git rm --cached config.env
```

6. Run `git status` and observe that `config.env` is staged for removal from Git (but the file still exists locally).

7. Commit the fix:
```bash
git add .gitignore
git commit -m "Stop tracking config.env and add .gitignore"
git push origin main
```

8. Confirm on GitHub that `config.env` is **no longer visible** in the repository, while the file still exists on your local machine.

9. Create a file named `why-gitignore.txt` and answer:
- Why should we ignore folders like `vendor` or `node_modules`?
- Why should we ignore files like `config.env` or `.env`?
- What does `git rm --cached` do?
- Why should we **not** add `.gitignore` inside `.gitignore`?

**Submit:**
- Screenshot of `git status` after using `git rm --cached`
- Screenshot showing that `config.env` is ignored / removed from GitHub
- Content of `why-gitignore.txt`
- Repository link (make sure `config.env` is **not** visible on GitHub)

---answer
<img width="1442" height="862" alt="Screenshot 2026-09-10 135938" src="https://github.com/user-attachments/assets/b30cc770-13b0-458f-92da-e6070d20ab36" />
<img width="1362" height="727" alt="image" src="https://github.com/user-attachments/assets/e6ddb503-90c5-413b-8059-fa46f1e18c61" />



https://github.com/twinklesharmacg-coder/git--reset-command-practice

## Bonus Assignment (Optional)

1. Modify a tracked file (create one if needed) and use `git restore <filename>` to discard the changes.
2. Stage a file and then unstage it using `git restore --staged`.
3. Take screenshots of both actions.

**Submit (optional):** Screenshots of both restore operations.

---

## Submission Checklist

| # | Item | Required? |
| --- | -------------------------------------------------------------- | ------------- |
| 1 | Assignment 1 – screenshots of restore practice | Yes |
| 2 | Assignment 2 – `rm` vs `git rm` screenshots + explanation file | Yes |
| 3 | Assignment 3 – `.gitignore` + `git rm --cached` practice + explanation file | Yes |
| 4 | Bonus restore practice assignment | No (optional) |
| — | GitHub repository link | Yes |

**Important:**
- Make sure `config.env` is **not** pushed to GitHub after Assignment 3.
- Your `.gitignore` file **should** be present in the repository.

---


