Feature: Login for the Registration Page

  Scenario: user should able to register successfully
    Given User entered Login Page
    When User clicks on Register button
    And User Enter "HariAutomationTWO" "TestTWO" "Hari4" "Hari@4"
    And User Click on Register
    Then User should see text "successful"




