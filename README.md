
# Entrata Selenium Tests

This repository contains automated Selenium tests for exploring and validating the functionality of the website [entrata.com](https://www.entrata.com). The tests are written in Python using the Selenium WebDriver and Pytest framework.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Tests](#running-the-tests)
- [Test Cases](#test-cases)
- [Logging](#logging)
- [Contributing](#contributing)

## Prerequisites

Before running the tests, make sure you have the following installed:

1. **Python 3.x** - Download from [here](https://www.python.org/downloads/).
2. **Google Chrome Browser** - The tests are executed on Google Chrome.
3. **ChromeDriver** - Make sure the version of ChromeDriver matches your installed Chrome version. Download it [here](https://sites.google.com/chromium.org/driver/).

Alternatively, you can install **WebDriver Manager** to manage browser drivers automatically, as included in the project dependencies.

## Installation

1. **Clone the repository**:

   ```
   git clone https://github.com/yaminidubey/EntrataSeleniumTests.git
   cd EntrataSeleniumTests
   ```

2. **Set up a virtual environment** (optional but recommended):

   ```
   python -m venv venv
   source venv/bin/activate   # For Windows: venv\Scripts\activate
   ```

3. **Install the dependencies**:

   ```
   pip install -r requirements.txt
   ```

   This will install:
   - Selenium
   - Pytest
   - WebDriver Manager (to manage browser drivers automatically)

4. **Configure ChromeDriver**:

   Ensure you have the ChromeDriver installed, or use WebDriver Manager (included in this repo). The WebDriver Manager will download the correct ChromeDriver version automatically.

## Running the Tests

To execute the tests, run the following command in the root directory of the project:

```
pytest
```

This will:
- Launch a Chrome browser.
- Execute all test cases located in the \`tests/\` directory.
- Log results to the terminal and to the \`test_log.log\` file.

### Run Tests with Detailed Logs

You can generate detailed logs in both the console and the log file using the following command:

```
pytest -s --log-cli-level=INFO
```

## Test Cases

The repository includes the following Selenium test cases:

1. **Homepage Title Verification** - Validates the title of the homepage.
2. **Careers Page Navigation** - Navigates to the Careers page and validates its title.
3. **Dynamic Content Verification** - Verifies the visibility of the Resident Portal button after handling the cookies popup.

### Test Suite Structure

- **tests/test_entrata.py** - Contains the Selenium tests.
- **conftest.py** - Contains the browser setup and teardown functions.

## Logging

Test execution logs are stored in \`test_log.log\`. Logs contain information about test case execution, including which actions were performed, any errors encountered, and assertions.

Log levels used:
- **INFO** - General test flow information.
- **WARNING** - Potential issues.
- **ERROR** - Test failures or unhandled exceptions.

