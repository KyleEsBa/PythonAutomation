Feature: My first feature
  Scenario: Successful login
    Given I visit the login page
    When I enter valid credentials
    Then I should see the dashboard