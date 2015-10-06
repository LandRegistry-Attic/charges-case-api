@US14 @add_borrowers_to_case

Feature: Add Borrowers to Case
    As a lender/conveyancer  for a remortgage
    I want to fill in my clients details
    So that I have them on my records

@delete_test_data
Scenario: Add Borrowers to Case
    Given I have created a case with two borrowers
    And I retrieve borrowers for the created case
    Then the correct borrowers details are returned

@delete_test_data
Scenario: Add Borrower to Case with Missing Mandatory Information
    Given I have created a case
    When I try to add a borrower with missing mandatory information
    Then a status code of "400" is returned
