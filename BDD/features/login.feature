Feature: Check the login page functionality

  Scenario: Check that I can login into the application using the correct credentials
    Given I am on the Jules login page
    When I insert the correct email and correct password
    When I click the login button
    Then I can login into the application