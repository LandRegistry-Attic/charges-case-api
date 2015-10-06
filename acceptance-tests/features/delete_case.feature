@delete_case

Feature: Delete Case using Case API
    These features were added later on in the project when it was discovered
    that some functions of the APIs were not being covered by acceptance tests

Scenario: Delete a Case with a Borrower and Property
    Given I have created a case with one borrower
    And I delete the created case
    When I attempt to retrieve the deleted case
    Then a status code of "404" is returned
    When I attempt to retrieve the borrower
    Then a status code of "404" is returned
    When I attempt to retrieve the property
    Then a status code of "404" is returned
