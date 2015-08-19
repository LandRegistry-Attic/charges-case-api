@add_borrowers_to_case

Feature: Add Borrowers to Case
    As a lender/conveyancer  for a remortgage
    I want to fill in my clients details
    So that I have them on my records

Background:
    Given I have created a case

Scenario: Add Borrowers to Case
    When I add the following borrowers to a case:
      | FIRST NAME  | MIDDLE NAME | LAST NAME | ADDRESS                           | MOBILE NUMBER | EMAIL ADDRESS       |
      | Peter       |             | Smith     | 80 Mayorly Place, London, N12 5AZ | 07113889900   | psmith@yahoo.co.uk  |
      | Sarah       | Jane        | Smith     | 83 Lordship Park, London, N16 5UP | 07970112233   | sjsmith@gmail.com   |
    And I call the case API
    Then the correct borrowers details are returned

Scenario: Add Borrower to Case with Missing Mandatory Information
    When I try to add a borrower with missing mandatory information
    Then a status code of "400" is returned
