@add_title_to_case

Feature: Add Title to Case
    As a Conveyancer/lender
    I want add a title number to my case list
    So that I can register the borrowers mortgage

Background:
    Given I have created a case with a property but no borrowers

@delete_test_data
Scenario: Add Title to Case
    When I retrieve the property for the created case
    Then the correct property details are returned

@delete_test_data
Scenario: Try to Add Two Titles to a Case
    When I try to add another property to the case
    Then a status code of "500" is returned
