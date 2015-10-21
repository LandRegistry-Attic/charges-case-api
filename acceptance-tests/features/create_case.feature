@create_case

Feature: Create Case
    As a conveyancer
    I want to create a case
    So I can keep track of a mortgage application


Scenario: Create a new case
    Given I have created a new case
    Then a status code of "201" is returned
    And the right details are returned
