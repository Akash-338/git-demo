# Introduction to GitHub and GitHub Actions FDP

This README provides a foundational understanding of **GitHub**, **GitHub Actions**, and how they work together to enable **CI/CD automation**. It also compares **GitHub Actions** with **Jenkins**, a popular CI/CD alternative.

---

## What is GitHub?

**GitHub** is a web-based platform for **version control**, **code collaboration**, and **project management**, built around the **Git** version control system.

### Key Features of GitHub:

* Repositories to host code and track its history
* Branching and Pull Requests for collaboration
* Code reviews and discussions
* Releases, issues, and project boards
* Role-based access control and permissions
* Integration with CI/CD tools like **GitHub Actions**

---

## What is GitHub Actions?

**GitHub Actions** is GitHub’s built-in **CI/CD platform** that allows you to **automate workflows** like:

* Running unit tests when code is pushed
* Building applications
* Deploying code to production
* Performing security scans
* Sending notifications

---

## How GitHub Actions Work

GitHub Actions use **YAML-based workflow files** stored in `.github/workflows/`. These files define:

* **Triggers** (e.g., push, pull request)
* **Jobs** (e.g., linting, testing, build, deploy)
* **Steps** (e.g., install dependencies, run tests)
* **Runners** (the machines that execute workflows)

### Basic Building Blocks

| Term       | Description                                                       |
| ---------- | ----------------------------------------------------------------- |
| `workflow` | Entire automation process                                         |
| `job`      | A group of steps that run in the same runner                      |
| `step`     | Individual tasks (e.g., `pip install`, `pytest`)                  |
| `runner`   | Virtual machine (Ubuntu, Windows, macOS) where jobs execute       |
| `action`   | Reusable packaged functionality (e.g., checkout code, setup Python) |
| `artifact` | Files created during jobs (e.g., build output, test coverage)     |

---

### CI/CD Pipeline Example

```yaml
on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: pip install -r requirements-dev.txt

      - name: Run tests
        run: pytest

      - name: Build app
        run: python -m compileall -q src/
```

This workflow:

* Runs on every push to the `main` branch
* Installs dependencies
* Runs tests
* Builds the application

---

## Comparison Summary

| Feature               | GitHub Actions                              | Jenkins                                     |
| --------------------- | ------------------------------------------- | ------------------------------------------- |
| **Hosted By**         | GitHub                                      | Self-hosted or via Jenkins server           |
| **Pipeline Format**   | YAML (`.yml`)                               | Groovy-like syntax (`Jenkinsfile`)          |
| **Trigger Mechanism** | `on: push`, `on: pull_request`              | `when { branch 'main' }`                    |
| **Environment Setup** | `uses: actions/setup-python`                | Manual with `pyenv` or OS-installed Python  |
| **Steps Declaration** | Under `jobs > steps`                        | Under `stages > stage > steps`              |
| **Secrets Handling**  | GitHub Secrets                              | Jenkins Credentials plugin                  |
| **Integration**       | Tightly integrated into GitHub repositories | Integrates with any SCM (Git, GitHub, etc.) |
| **UI Feedback**       | GitHub Actions UI in PRs and commits        | Jenkins UI (dashboard and job history)      |

---

## Summary

* **GitHub** helps developers collaborate on code.
* **GitHub Actions** automate workflows directly in your GitHub repo.

---

## Additional Learning Resources

* [GitHub Docs](https://docs.github.com/en)
* [GitHub Actions Documentation](https://docs.github.com/en/actions)
* [CI/CD Concepts](https://www.redhat.com/en/topics/devops/what-is-ci-cd)

---

> Recommended for student labs, hackathons, and professional onboarding documentation.
