Feature: Test Case 1 Check register user

  Background:
    Given registeruser: I am a user on Automation Exercise page

    @register_user
  Scenario: Check visible text and to register a new account and to delete the account
    When registeruser: Verify that home page is visible successfully
    When registeruser: Click on Signup / Login button
    When registeruser: Verify New User Signup! is visible
    When registeruser: Enter name "Anton"
    When registeruser: Enter email adress "anton@gmail.com"
    When registeruser: Click Signup button
    When registeruser: Verify that ENTER ACCOUNT INFORMATION is visible
    When registeruser: Fill details: Title, Name, Email, "password123", Date of birth "20","May","1991"
    When registeruser: Select checkbox Sign up for our newsletter!
    When registeruser: Fill details: First name "Ion", Last name "Popescu", Company "SC acasa SRL", Address "Str.Anton", Address2 "Nr.2 Bl.4", Country "United States", State "Arizona", City "Tucson", Zipcode "123456", Mobile Number "033451231"
    When registeruser: I click on Create Account button
    When registeruser: Verify that ACCOUNT CREATED! is visible
    When registeruser: Click on the Continue button
    When registeruser: Verify that Logged in as username is visible
    When registeruser: Click on the Delete Account button
    Then registeruser: Verify that ACCOUNT DELETED! is visible and click Continue button