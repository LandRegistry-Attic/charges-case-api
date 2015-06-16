@US32

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

Scenario: Retrieve case from case API
    Given I call the case API
    Then the correct case details are returned
