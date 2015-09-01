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
    And I add the following address to the case:
    """
    {
      "street_address": "83 Lordship Park",
      "extended_address": "",
      "locality": "London",
      "postcode": "N16 5UP"
    }
    """

Scenario: Add Title to Case
    When I retrieve the property for the created case
    Then the correct property details are returned

Scenario: Try to Add Two Titles to a Case
    When I try to add another address to the case
    Then a status code of "403" is returned
