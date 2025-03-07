# Project Name

A Python project combining **Playwright** for UI/API automation.

---

## Features
- Browser automation using Playwright (Chromium, Firefox, WebKit).
- HTTP requests via the `requests` package.
- Configurable logging for debugging and monitoring.
- Example test scripts for web interactions and API calls.

---

## Prerequisites
- Python 3.8+
- pip (Python package manager)

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MagaretQin/playwright-python-assurity.git
   cd your-repo
   
2. **Set up a virtual environment (recommended):**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   
3. **Install dependencies:**:
   ```bash
    pip install -r requirements.txt
    playwright install  # Install browsers for Playwright
   
## Running Playwright Tests

Example test (tests/assurity_api_tests.py):
   ```bash
   python -m pytest tests/assurity_api_test.py -s  # -s shows print/logging output