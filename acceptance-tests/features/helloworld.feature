Feature: Check helloworld API

Scenario: Check helloworld API
    Given I access the helloworld API
    Then the response contains Hello World
