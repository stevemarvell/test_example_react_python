Feature: Greeting Users

  Scenario: Greet not-Bob with default greeting
    Given Alice is a user
    When they are greeted
    Then the greeting is "Hi, Alice!"

  Scenario: Greet user with custom greeting
    Given Bob is a user
    And they have a custom greeting "Hello"
    When they are greeted
    Then the greeting is "Hello, Bob!"