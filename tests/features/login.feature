@automated
Feature: Test Verify login basic functionality
  As a user
  I will send POST, GET, UPDATE, and DELETE requests
  I want to be able to see the expected response


  Background:
    Given I set the header param request content type as "application/json"


  @smoke
  Scenario: Verify login with valid credential
    Given I set the POST endpoint to "login"
    When I send a POST request to the login endpoint with the following data
      | email                    | password   |
      | test.rakesh@gmail.com    | Welcome@123|
    Then the response code should be 200
    And the response should contain the message "User exists"
