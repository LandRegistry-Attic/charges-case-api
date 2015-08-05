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

Scenario: Create case on case API
    When I have created the following case:
    """
    {
      "conveyancer_id": "1",
      "deed_id": "1"
    }
    """
    Then the "id" is returned in the response
    And the "deed_id" of "1" is returned in the response
    And the "conveyancer_id" of "1" is returned in the response
    And the "status" of "Case created" is returned in the response
    And the "created_on" of todays date is returned in the response
    And the "last_updated" of todays date is returned in the response


Scenario: Retrieve case from case API
    Given I have created the following case:
    """
    {
      "conveyancer_id": "1",
      "deed_id": "1"
    }
    """
    When I call the case API
    Then the returned "id" matches the one created
    And the returned "deed_id" matches the one created
    And the returned "conveyancer_id" matches the one created
    And the returned "status" matches the one created
    And the returned "created_on" matches the one created
    And the returned "last_updated" matches the one created
