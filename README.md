# pycalc-cli

A robust command-line calculator in Python with a REPL, unit tests, and GitHub Actions CI enforcing **100% test coverage**.

## Features
- REPL interface for continuous calculations
- Addition, subtraction, multiplication, division
- Clear prompts, input validation, and error handling
- DRY, typed, small, testable functions
- Pytest with parameterized tests
- GitHub Actions CI that **fails** below 100% coverage

## Quick Start

```bash
# 1) Create and activate a virtual environment
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run the app
python -m calcapp.cli

# 4) Run tests with coverage (must be 100%)
pytest --cov=calcapp --cov-report=term-missing --cov-fail-under=100
```

## Usage

Run `python -m calcapp.cli` and follow the prompts. Examples:

```
Enter operation (+, -, *, /), or 'help'/'quit': +
Enter two numbers (e.g. 2 3 or 2,3): 2 3
Result: 5.0
```

## Repository Setup

```bash
git init
git add .
git commit -m "Initial commit: calculator with tests & CI"
# Create a new GitHub repo, then add it as a remote:
git remote add origin https://github.com/<your-username>/pycalc-cli.git
git branch -M main
git push -u origin main
```

## CI (GitHub Actions)

This repo includes `.github/workflows/ci.yml` which runs `pytest` and **fails** when coverage < 100%.
