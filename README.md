# Team Git & GitHub Actions CI/CD

This repository is a simple four-person team project used to demonstrate a basic CI/CD workflow with Git, GitHub, Pull Requests, and GitHub Actions.

### Two rules for `main`

A Pull Request can be merged into `main` only when:

1. **The CI workflow completes successfully.**
2. **At least one other teammate approves the Pull Request.**

---

# 1. Teammate 1: Configure the project repository

One teammate creates the GitHub repository.

The base repository should contain:

```text
README.md
requirements.txt
src/
tests/
.github/
    workflows/
        ci.yml
```

Teammate 1 then adds the other three teammates as collaborators.

On GitHub:

```text
Repository
→ Settings
→ Collaborators
→ Add people
```

Add Teammates 2, 3, and 4.

---

# 2. Configure the `main` ruleset

Teammate 1 configures the ruleset.

Go to:

```text
Repository
→ Settings
→ Rules
→ Rulesets
→ New ruleset
→ New branch ruleset
```

Create a ruleset for:

```text
main
```

Give it a name such as:

```text
Protect main
```

Set the ruleset to **Active**.

## Rule 1: Require a Pull Request

Enable:

```text
Require a pull request before merging
```

Set:

```text
Required approvals: 1
```

This means at least one teammate other than the person making the change must approve the Pull Request.

## Rule 2: Require the CI workflow

Enable:

```text
Require status checks to pass before merging
```

Select the CI check:

```text
test
```

The CI workflow contains a job named `test`.

The intended result is:

```text
CI passes ✓
+
1 teammate approval ✓
=
Merge allowed
```

### Important

The CI workflow must have run at least once before GitHub can offer its `test` check as a required status check.

If `test` is not available while creating the ruleset:

1. Push the repository to GitHub.
2. Create a test Pull Request.
3. Let GitHub Actions run.
4. Confirm that the `test` check appears.
5. Return to the ruleset.
6. Select `test` as the required status check.

---

# 3. Teammates: Clone the shared repository

After accepting the collaboration invitation, each teammate clones **Teammate 1's repository**.

Do not fork it.

Run:

```bash
git clone https://github.com/OWNER-USERNAME/REPOSITORY-NAME.git
```

Then enter the repository:

```bash
cd REPOSITORY-NAME
```

Everyone should be working with the same repository.

---

# 4. Download the requirements

Create a virtual environment.

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the requirements:

```bash
pip install -r requirements.txt
```

---

# 5. Test the existing project locally

Before making any changes, make sure the existing code works.

Run:

```bash
pytest
```

All existing tests must pass.


---

# 6. Create a feature branch

Before adding a feature, make sure your local `main` is current:

```bash
git checkout main
git pull origin main
```

Create a new feature branch:

```bash
git checkout -b feature/multiply
```

Every new feature must have its own feature branch.

Examples for this repoo:

```text
feature/multiply
feature/divide
feature/power
feature/average
```

Do not develop new features directly on `main`.

---

# 7. Add the new feature

Make the required code changes on your feature branch.

For example, to add multiplication, add the function to:

```text
src/utils.py
```

```python
def multiply(a, b):
    return a * b
```

Then add a corresponding test to:

```text
tests/test_utils.py
```

```python
def test_multiply():
    assert multiply(3, 4) == 12
```

If the feature needs to be demonstrated by the program, use it in:

```text
src/main.py
```

### Important

Every new feature should have a corresponding test.

---

# 8. Test everything locally again

After adding the feature, run:

```bash
pytest
```

Run the **complete test suite**, not just the new test.

The developer should not create the Pull Request until the local tests pass.

---

# 9. Commit the feature

Check your changes:

```bash
git status
```

Stage them:

```bash
git add .
```

Commit:

```bash
git commit -m "Add multiplication feature"
```

Use a commit message that describes the feature.

---

# 10. Push the feature branch

Push the branch to the shared GitHub repository:

```bash
git push -u origin feature/new-feature
```

---

# 11. Create a Pull Request to `main`

Go to the shared repository on GitHub.

Create a Pull Request:

```text
base: main
compare: feature/new-feature
```

The direction must be:

```text
feature branch → main
```

Create the Pull Request.

---

# 12. GitHub Actions runs automatically

After the Pull Request is created, GitHub Actions automatically runs the CI workflow.

The workflow performs:

```text
Checkout repository
        ↓
Set up Python
        ↓
Install requirements
        ↓
Run pytest
```

The required check is:

```text
test
```

The Pull Request must show:

```text
test ✓
```

before it can be merged.

If the tests fail:

```text
test ✗
```

the Pull Request cannot be merged.

Fix the code, commit the fix, and push it to the same feature branch:
GitHub Actions will run again automatically.

---

# 13. Another teammate reviews and approves

The teammate who created the Pull Request should not be the only person approving it.

Ask another teammate to review the Pull Request.

The teammate should check:

- The feature is implemented.
- A test was added.
- The tests are passing.
- The change is reasonable.

The teammate then selects:

```text
Review changes
→ Approve
→ Submit review
```

The Pull Request should now have:

```text
✓ test
✓ 1 approval
```

---

# 14. Merge into `main`

The Pull Request can now be merged because:

```text
CI workflow passed ✓
+
Another teammate approved ✓
```

Click:

```text
Merge pull request
```

The feature is now part of `main`.

---

# 15. Update your local `main`

After the Pull Request is merged:

```bash
git checkout main
git pull origin main
```

Your local `main` now contains the new feature.

---

# 16. Repeat for the next feature

For every new feature, repeat the same process.

```text
main
 ↓
git pull
 ↓
feature/new-feature
 ↓
add code + test
 ↓
pytest
 ↓
git add .
 ↓
git commit
 ↓
git push
 ↓
Pull Request → main
 ↓
GitHub Actions
 ↓
test ✓
 ↓
1 teammate approval
 ↓
merge
 ↓
main
```

---

# Git commands used in this exercise

| Command | Purpose |
|---|---|
| `git clone URL` | Clone the shared repository |
| `cd REPOSITORY-NAME` | Enter the repository |
| `git remote -v` | Check the repository remote |
| `git checkout main` | Switch to `main` |
| `git pull origin main` | Get the latest `main` |
| `git checkout -b feature/name` | Create and switch to a feature branch |
| `git status` | Check changed files |
| `git add .` | Stage changes |
| `git commit -m "message"` | Commit changes |
| `git push -u origin branch-name` | Push a new feature branch |
| `git push` | Push later changes |
| `pytest` | Run all tests |


