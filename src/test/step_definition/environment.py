from behave import fixture, use_fixture
from src.test.utilities.Driver import ChromeDriverManager

def before_all(context):
    """Called before all scenarios."""
    context.driver = ChromeDriverManager()  # Create an instance of the WebDriver

def after_all(context):
    """Called after all scenarios."""
    context.driver.quit()  # Quit the driver after all scenarios

def before_scenario(context, scenario):
    """Called before each scenario."""
    print(f"Starting scenario: {scenario.name}")

def after_scenario(context, scenario):
    """Called after each scenario."""
    print(f"Finished scenario: {scenario.name}")

# Optionally, you can use fixtures for more complex setups
@fixture
def browser(context):
    context.driver = WebDriver()
    yield context.driver
    context.driver.quit()

def before_feature(context, feature):
    """Called before each feature."""
    print(f"Starting feature: {feature.name}")

def after_feature(context, feature):
    """Called after each feature."""
    print(f"Finished feature: {feature.name}")
