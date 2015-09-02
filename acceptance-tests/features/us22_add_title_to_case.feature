@add_title_to_case

Feature: Add Title to Case
    As a Conveyancer/lender
    I want add a title number to my case list
    So that I can register the borrowers mortgage

Background:
    Given I have created the following case:
    """
    {
      "conveyancer_id": "1"
    }
    """
    And I add the following property to the case:
    """
    {
       "property": {
         "locality": "Plymouth",
         "tenure": "freehold",
         "postcode": "PL6 5DP",
         "title_number": "DN513498",
         "street": "18 Janner Lane",
         "type": "Property",
         "extended": "St. Budeaux"
       }
    }
    """

Scenario: Add Title to Case
    When I retrieve the property for the created case
    Then the correct property details are returned

Scenario: Try to Add Two Titles to a Case
    When I try to add another property to the case
    Then a status code of "403" is returned
