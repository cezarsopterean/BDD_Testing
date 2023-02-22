Feature: Check the functionality of the login page

  Background:
    Given Login Page: I am on the Form Authentication login page

    @T1 @loginSuccessful
    Scenario: Check that you can login when providing correct credentials
      When Login Page: I insert the username "tomsmith" and the password "SuperSecretPassword!"
      When Login Page: I click the login button
      Then Secure Page: I can login and see the secure page

    @T2 @logoutAfterLogin
        Scenario: Check that you can logout after logging in
      When Login Page: I insert the username "tomsmith" and the password "SuperSecretPassword!"
      When Login Page: I click the login button
      When Secure Page: I can login and see the secure page
      When Secure Page: I click the logout button
      Then Login Page: I am taken back to the login page

    @T3 @invalidLogin
        Scenario Outline: Check that you cannot login into the application with invalid credentials
      When Login Page: I insert username "<username>" and password "<password>"
      When Login Page: I click the login button
      Then Login Page: I cannot login and I receive error message "<error_message>"

    @ex1 @incorrectCredentials
      Examples:
        | username       | password             | error_message
        | incorrect_user | SuperSecretPassword! | Your username is invalid!
        | tomsmith       | incorrect_pass       | Your password is invalid!
        | incorrect_user | incorrect_pass       | Your username is invalid!

    @ex2 @nullCredentials
      Examples:
        | username       | password             | error_message
        | tomsmith       |                      | Your username is invalid!
        |                | SuperSecretPassword! | Your username is invalid!
        |                |                      | Your username is invalid!