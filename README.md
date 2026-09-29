# Git & GitHub Demo Repository

Welcome to our **Git, GitHub, and GitHub Actions tools setup**!
This repository is designed for **hands-on learning** of version control and CI/CD concepts.

---

## What You'll Learn

- Git fundamentals (`clone`, `commit`, `push`, `pull`)
- GitHub collaboration (`fork`, `pull requests`)
- Branching strategies
- GitHub Actions CI/CD pipelines

---

## Exercises

### Exercise 1: Fork and Clone

1. Fork this repository to your GitHub account.
2. Clone your fork to your local machine:

   ```bash
   git clone https://github.com/YOUR-STUDENT-USERNAME/git-demo-repo.git
   cd git-demo-repo
   ```

3. Add your name to the `contributors.txt` file.
4. Commit and push your changes.
5. Create a pull request back to the original repository.

---

### Exercise 2: Feature Development

1. Create a new branch for your feature:

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Add a new function to `src/utils.py`.
3. Write corresponding tests in `tests/test_utils.py`.
4. Commit and push your branch.
5. Open a pull request describing your feature.

---

### Exercise 3: CI/CD Pipeline

1. Observe the GitHub Actions workflow in `.github/workflows/ci.yml`.
2. Make changes to code and push them to see the CI/CD pipeline in action.
3. Watch automated testing and code quality checks execute.

---

## Project Structure

```
git-demo/
├── README.md
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── tests/
│   └── test_utils.py
├── contributors.txt
└── .github/
    └── workflows/
        └── ci.yml
```

---

## Getting Started

### 1. Fork this repository

Click the **Fork** button at the top-right of this page.

### 2. Clone your fork

```bash
git clone https://github.com/YOUR-USERNAME/git-demo-repo.git
cd git-demo-repo
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements-dev.txt
```

### 5. Run tests

```bash
pytest
```

Coverage is collected automatically and written to `coverage/`.

### 6. Run the demo

```bash
python -m src.main
```

---

## Common Commands

| Command | Description |
| --- | --- |
| `pytest` | Run the test suite with coverage |
| `pytest -k multiply` | Run only tests matching a name |
| `pytest -x` | Stop at the first failure |
| `ruff check src/ tests/` | Lint |
| `ruff format src/ tests/` | Auto-format |

---

## Contributing

- Add your name to `contributors.txt`.
- Open a pull request with your changes.

---

## License

This project is intended **for educational purposes only**.

---

**Happy Learning!**
