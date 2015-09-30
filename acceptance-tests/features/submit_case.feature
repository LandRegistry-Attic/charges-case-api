@submit_case

Feature: Case API ensure application cannot be re-submitted
    In order to
    Ensure an application cannot be submitted more than once
    Will need to attempt to resubmit a submitted application

Acceptance Criteria:
    - A request to the API brings back a json array with following data:
      - an error message of 403

@delete_test_data
Scenario: Attempt to submit a case with a status of submitted
    Given I have created a case and deed with one borrower that is effective
    When I send a submit request via the API
    And I submit the case again
    Then a status code of "403" is returned
