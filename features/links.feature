Feature : Check the functionality of the home page links

  Background:
    Given Home Page: I am on the home page

    @T1
    Scenario Outline: Check that the links direct you to the correct page
      When Home Page: I click on the link "<link>"
      Then Home Page: I am taken to the page "<expected_url>"

      Examples:

      | link                | expected_url
      | FORM_AUTHENTICATION | https://the-internet.herokuapp.com/login
      | CHECKBOXES          | https://the-internet.herokuapp.com/checkboxes
      | DROPDOWN            | https://the-internet.herokuapp.com/dropdown