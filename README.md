# Playwright API Framework

A production-grade API test automation framework built with Python, pytest, and Playwright.

## Tech Stack

- **Python 3.11**
- **pytest** — test runner
- **requests** — HTTP client
- **Pydantic** — response schema validation
- **Faker** — dynamic test data generation
- **Allure** — test reporting
- **GitHub Actions** — CI/CD

## Architecture

```
playwright-api-framework/
├── core/
│   ├── client/         # HTTP client (requests wrapper with logging + error handling)
│   ├── config/         # Environment-based configuration
│   ├── data/           # Static test data constants
│   ├── factories/      # Dynamic test data generation (Faker)
│   ├── models/         # Pydantic response models for schema validation
│   ├── services/       # API service layer (one class per resource)
│   └── validators/     # Reusable assertion helpers
├── fixtures/           # pytest fixtures
├── tests/
│   └── api/            # API test suites
└── .github/workflows/  # CI/CD pipeline
```

## Setup

**Prerequisites:** Python 3.11+, pip

```bash
git clone <repo-url>
cd playwright-api-framework
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env.dev` file in the project root:
```
BASE_URL_API=https://reqres.in/api
BASE_URL_UI=https://reqres.in
API_KEY=your_api_key
```

## Running Tests

Run all API tests (default: dev environment):
```bash
pytest -m api -v
```

Run against a specific environment:
```bash
ENV=staging pytest -m api -v
ENV=prod pytest -m api -v
```

Run with Allure reporting:
```bash
pytest -m api -v --alluredir=allure-results
allure serve allure-results
```

## CI/CD

Tests run automatically on every push and pull request to `main` via GitHub Actions. The pipeline:
1. Spins up a clean Ubuntu environment
2. Installs all dependencies
3. Runs the API test suite against staging
4. Uploads Allure results as a downloadable artifact

## Key Design Decisions

- **Layered architecture** — client, service, validator, and factory layers are separate concerns, making the framework easy to extend without modifying existing code
- **Dynamic test data** — Faker generates unique data per run, avoiding test pollution and data collisions
- **Schema validation** — Pydantic models validate full response structure (field names + types), not just individual keys
- **Multi-environment support** — switching environments requires no code changes, only an `ENV` variable
- **Error handling** — network failures (timeout, connection error) are caught and logged with context before re-raising
