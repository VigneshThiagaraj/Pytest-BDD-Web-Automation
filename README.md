# Pytest-BDD-Web-Automation
This project demonstrates how to test a web application with Selenium WebDriver using Python, the Page Object Model design pattern, 
and BDD feature files using Pytest BDD.

# Getting Started
1. Clone this repository
2. Open the terminal in pycharm, install the dependencies for the project using the following command
   
   ``` pip install -r requirements.txt ```

## Test frameworks used:
- Pytest-BDD

## Reports
- Pytest-html 
- allure html 

## Running Tests
### All Tests
```pytest```
    
### Run Specific Test Stepfile
```pytest -m "<tagName>"  ```

## Report Generation
```pytest -m "smoke" --alluredir ./reports/allure-reports -v -s ```

```allure serve ./reports/allure-reports```
