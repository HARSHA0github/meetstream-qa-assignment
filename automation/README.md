# MeetStream AI - QA Automation Task

This directory contains the automated UI tests for the SauceDemo checkout flow.

## Tech Stack
* **Language:** Python 3.10+
* **Framework:** Pytest
* **Automation Tool:** Playwright
* **Pattern:** Page Object Model (POM)

*Note: Playwright is chosen over Selenium because of its native auto-waiting mechanisms. It eliminates the need for flaky `time.sleep()` calls and handles dynamic DOM elements beautifully out of the box.*

## Setup Instructions
1. Navigate to this directory in your terminal.
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment:
   * Mac/Linux: `source venv/bin/activate`
   * Windows: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Install Playwright browsers: `playwright install chromium`

## Execution
Run the test in headed mode to watch it execute:
```bash
pytest tests/test_cart_flow.py --headed