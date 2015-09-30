@retrieve_case

Feature: Case API
    In order to
    Power the case list
    Will need to store and update cases in a case list

Acceptance Criteria:
    - A request to the API brings back a json array with following data:
      - id(int)
      - deed id(int)
      - status(str)
      - last updated(datetime)
      - created at(datetime)
      - conveyancer id(int)

@delete_test_data
Scenario: Retrieve case from case API
    Given I have created a case
    When I retrieve the created case
    Then the correct case details are returned
