from behave import given, when, then
from src.test.utilities.Driver import ChromeDriverManager

@given('I visit the login page')
def step_impl(context):
    # Code to navigate to the login page
    print("Navigating to login page")
    ChromeDriverManager.get("https://www.usbank.com/index.html")

@when('I enter valid credentials')
def step_impl(context):
    # Code to enter credentials
    print("Entering valid credentials")

@then('I should see the dashboard')
def step_impl(context):
    # Code to verify dashboard visibility
    print("Dashboard is visible")