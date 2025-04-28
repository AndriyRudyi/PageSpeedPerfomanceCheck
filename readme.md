# Page Performance Check

[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![Selenium](https://img.shields.io/badge/Selenium-Automation-green.svg)](https://www.selenium.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-Testing-blue.svg)](https://docs.pytest.org/en/stable/)
[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE)

Automated performance tests to measure page load time using **Python**, **Selenium WebDriver**, and **Pytest**.

---

## Features
- Measures full page load time for each provided URL.
- Generates a detailed CSV report (`reports/performance_report.csv`) after each test run.
- Evaluates performance based on a threshold of **3000 ms** to determine **Passed** or **Failed**.
- Headless Chrome browser support.

---

## Technology Stack
- **Python 3.11**
- **Selenium WebDriver**
- **Pytest**

---

## Setup and Usage

Follow the steps below to install dependencies and run the tests:

```bash
# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate   -For Linux/Mac
.venv\Scripts\activate      -For Windows

# Install project dependencies
pip install -r requirements.txt
#Put your url in config.py

# Run the tests
pytest tests/ --maxfail=1 --disable-warnings -v


Notes
The tests use headless Chrome for faster execution.

Reports are automatically generated after every run.

Pages loading over 3000 ms are considered Failed.

Results can be analyzed by opening reports/performance_report.csv in Excel or any spreadsheet viewer.

Speed matters. Test it properly.
