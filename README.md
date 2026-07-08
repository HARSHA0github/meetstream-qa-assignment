# MeetStream AI - QA Engineering Internship Assignment

This repository contains my comprehensive submission for the QA Engineering Internship Assignment. It evaluates the quality, stability, and architectural integrity of the upcoming Online Event Registration Platform, alongside a functional UI automation project for verification.

## Repository Structure

The project is structured logically into documentation and executable automation suites:

```text
meetstream-qa-assignment/
├── README.md                          # Global overview, assumptions, and setup
├── docs/                              # Assignment Deliverables
│   ├── 01-qa-strategy.md              # Risk-based strategy & release criteria
│   ├── 02-test-cases.md               # 14 structured test cases & Top-5 priority
│   ├── 03-root-cause-analysis.md      # Debugging & root cause deep-dives
│   ├── 04-api-testing-approach.md     # API endpoint validation strategies
│   └── 05-ai-usage.md                 # AI tools usage and verification logs
└── automation/                        # UI Automation Framework
    ├── README.md                      # Automation-specific execution guide
    ├── requirements.txt               # Python package dependencies
    ├── pytest.ini                     # Pytest runner configurations
    ├── conftest.py                    # Playwright fixtures and page initializations
    ├── pages/                         # Page Object Model components
    │   ├── login_page.py
    │   ├── inventory_page.py
    │   └── cart_page.py
    └── tests/                         # Executable test cases
        └── test_cart_flow.py