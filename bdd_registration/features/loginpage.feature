Feature: Login for the Registration Page

#  Scenario: Login with invalid credentials on Login Page
#    Given User on a Login Page
#    When User Enters invalid "Test" and invalid "Test"
#    Then User should see the "incorrect"

  Scenario:  Login with valid credentials on Login Page
    Given User on a Login Page
    When User Enters valid "HariTwo" and valid "Haritwo@123"
    Then User should able to see login and url should be "https://www.globalsqa.com/angularJs-protractor/registration-login-example/#/"
    Then User should see "HariTwo!" and text "You're logged in!!" on the page


