Feature: Greeting Users

  Scenario: Greet not-Bob with default greeting
    Given Alice is a user
    When they run the greeter application
    Then the application should respond with "Hi, Alice!"

  Scenario: Greet user with custom greeting
    Given Bob is a user
    And they have a custom greeting "Hello"
    When they run the greeter application
    Then the application should respond with "Hello, Bob!"