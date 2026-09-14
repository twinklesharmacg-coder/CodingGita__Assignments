# Git Stash Assignments 

***

## Assignment A - Practical
**Title:** “My First Stash”

**Submit:** Repo with `assignmentA.md` (answers + 2–3 screenshots).

### Setup (5 mins)

```bash
# Create repo on GitHub: git-stash-A-<username>
git clone <repo-url>
cd git-stash-A-<username>

echo "# Stash Practice" > README.md
git add README.md
git commit -m "Initial commit"
git push -u origin main
```

***

### Task A1 — Basic Stash (10 mins)

1. On `main`:
   - Edit `README.md`.
   - Create `notes.txt` (don’t add it to Git).

2. Run:
   ```bash
   git stash
   git stash -u
   git stash list
   ```
   - Take 1 screenshot of `git stash list`.

3. Answer in `assignmentA.md`:
   - Q1: How many stashes do you see? Which is latest (`stash@{0}` or `stash@{1}`)?
   - Q2: Which stash has `notes.txt`? How do you know?

4. Run:
   ```bash
   git stash pop
   git stash list
   ```
   - Take 1 screenshot.

5. Answer:
   - Q3: What happened to the stash list after `pop`? (2 lines)

***

### Task A2 — Switch Branch with Half-Done Work (10 mins)

1. Create branch:
   ```bash
   git switch -c feature/login
   ```
2. In this branch:
   - Create `login.html` → commit it.
   - Create `login.css` → stage it (`git add login.css`).
   - Create `login.js` → leave it untracked.

3. You must switch to `main` urgently.  
   Stash your work (include untracked files) with a message:
   ```bash
   git stash -u -m "WIP: login page"
   ```

4. Switch to `main`, make a small change, commit, push:
   ```bash
   git switch main
   # edit README.md
   git add README.md
   git commit -m "Small update"
   git push
   ```

5. Go back and restore your work:
   ```bash
   git switch feature/login
   git stash pop
   ```

6. Answer:
   - Q4: Why did you need `git stash` before switching to `main`? (2–3 lines)
   - Q5: Show 1 screenshot of `git stash list` after pop. How many stashes remain?

***

### Task A3 — Simple Hygiene (5 mins)

1. Make a small change in `README.md`.
2. Stash it with a clear message:
   ```bash
   git stash push -m "BUGFIX: README typo"
   git stash list
   ```
3. Take 1 screenshot.

4. Answer:
   - Q6: Why is using `-m "message"` helpful? (2 lines)

***Answers
<img width="770" height="860" alt="Screenshot 2026-09-13 015434" src="https://github.com/user-attachments/assets/52a104ee-e038-4b02-91f6-08e4320c830d" />
<img width="760" height="806" alt="Screenshot 2026-09-13 015542" src="https://github.com/user-attachments/assets/63c58541-17ae-4c7c-956b-ff014628e546" />
<img width="755" height="862" alt="Screenshot 2026-09-13 022136" src="https://github.com/user-attachments/assets/60c47e6e-efaf-427d-90ce-91cad2a14048" />

<img width="666" height="597" alt="Screenshot 2026-09-13 022339" src="https://github.com/user-attachments/assets/b9eb03a5-d207-4182-b5a4-1b846218cc74" />



## Assignment B —  Theoretical  
**Title:** “Stash Concepts”

**Submit:** File `assignmentB.md` with short answers.

Answer in 2–4 lines each.

1. What is `git stash` in simple words? When do we use it?  
2. You have:
   - `app.js` (tracked, modified)
   - `test.js` (untracked)
   - `.env` (ignored)

   Which files are stashed by:
   - `git stash`
   - `git stash -u`
   - `git stash -a`

3. Explain the difference between:
   - `git stash apply`
   - `git stash pop`

4. When would you prefer `apply` over `pop`? Give one small example.

5. What do these commands do?
   - `git stash drop`
   - `git stash clear`

6. You see this `git stash list`:
   ```text
   stash@{0}: WIP on feature/login: ...
   stash@{1}: WIP on main: ...
   ```
   - Which is the latest stash?
   - If you run `git stash pop`, which one is removed?

7. Why is it good to use messages like:
   ```bash
   git stash push -m "WIP: login form"
   ```
   instead of just `git stash`? (2–3 lines)

8. Scenario:
   - You are on `feature/checkout`.
   - `checkout.html` is committed.
   - `checkout.css` is staged.
   - `checkout.js` is untracked.

   You must switch to `main` urgently.  
   Write the exact command(s) you will use to stash your work safely (include untracked files and a message).

***Answers
<img width="876" height="1279" alt="image" src="https://github.com/user-attachments/assets/2e88113b-a301-4f30-9a10-ce31fdfbf09f" />
<img width="898" height="1278" alt="image" src="https://github.com/user-attachments/assets/fd2b5184-70f9-4e14-a97f-ec75eba89c43" />
<img width="874" height="1280" alt="image" src="https://github.com/user-attachments/assets/7404f035-6ae6-46c2-8490-800011ccd702" />
<img width="836" height="1280" alt="image" src="https://github.com/user-attachments/assets/5dbdef11-ebc2-46fc-895e-f952950f7960" />






## Assignment C — (Short Practical + Theory)  
**Title:** “Stash in Action”

**Submit:** Repo with `assignmentC.md` (answers + 2 screenshots).

### Setup (5 mins)

```bash
# Create repo: git-stash-C-<username>
git clone <repo-url>
cd git-stash-C-<username>

echo "# Stash Mixed" > README.md
git add README.md
git commit -m "Initial commit"
git push -u origin main
```

***

### Part C1 — Practical (10 mins)

1. On `main`:
   - Edit `README.md`.
   - Create `temp.txt` (untracked).

2. Run:
   ```bash
   git stash
   git stash -u
   git stash list
   ```
   - Take 1 screenshot.

3. Answer:
   - Q1: How many stashes? Which one is latest?
   - Ans
   - 2 stash and stash@{0} is latest
   - Q2: Which stash has `temp.txt`?
   - stash@{0} is latest

4. Run:
   ```bash
   git stash pop
   git stash list
   ```
   - Take 1 screenshot.

5. Answer:
   - Q3: What changed in the stash list after `pop`? (2 lines)

***Answer
latest stash is restored

### Part C2 — Theory (10 mins)

Answer in 2–4 lines each in `assignmentC.md`.

6. In your own words, what is `git stash` and why is it useful?  

7. Explain with a small example:
   - `git stash apply`
   - `git stash pop`

8. Why should we use `-u` when stashing new files?  

9. Why are meaningful stash messages (like `"WIP: login form"`) important in team projects?  

10. Imagine:
    - You stashed 3 times.
    - You run `git stash pop`.
    - Then you run `git stash drop`.

    How many stashes remain if you started with 3? Explain briefly.

***

## How to Submit

- **Assignment A:**  
  - Repo: `git-stash-A-<username>`  
  - File: `assignmentA.md` with Q1–Q6 + 3 screenshots.

- **Assignment B:**  
  - Any repo or Google Doc.  
  - File: `assignmentB.md` with answers to Q1–Q8.

- **Assignment C:**  
  - Repo: `git-stash-C-<username>`  
  - File: `assignmentC.md` with Q1–Q10 + 2 screenshots.

***

### These three assignments together cover all important stash commands:

- `git stash`, `git stash push`  
- `git stash list`, `git stash show`  
- `git stash apply`, `git stash pop`  
- `git stash drop`, `git stash clear`  
- `-u` (untracked), `-a` (ignored)  
- `-m "message"` (hygiene)  

---Answers
<img width="1054" height="1280" alt="image" src="https://github.com/user-attachments/assets/54c9c389-cdf3-42b5-8666-6b7c771b9a6d" />
<img width="896" height="1278" alt="image" src="https://github.com/user-attachments/assets/c826a16e-9436-4a9b-8936-3128ea66f4ad" />


