@US07

Feature: Case API ensure application cannot be re-submitted
    In order to
    Ensure an application cannot be submitted more than once
    Will need to attempt to resubmit a submitted application

Acceptance Criteria:
    - A request to the API brings back a json array with following data:
      - an error message of 403

Scenario: Attempt to submit a case with a status of submitted
    Given I have created the following case:
    """
    {
      "conveyancer_id": "1"
    }
    """
    And I create the following deed:
    """
      {
      "id":"1",
      "mdref": "MD0149A",
      "title": {
        "title-number": "GHR67832",
        "address": {
          "street-address": "18 Lordly Place",
          "extended-address": "",
          "locality": "London",
          "postal-code": "N12 5TN"
        }
      },
      "lender": {
        "name": "Bank of England PLC",
        "company-number": "2347672",
        "address": {
          "street-address": "12 Trinity Place",
          "extended-address": "Regents Street",
          "locality": "London",
          "postal-code": "NW10 6TQ"
        }
      },
      "borrowers":[{
        "id": "1",
        "name": "Peter Smith",
        "address": {
          "street-address": "83 Lordship Park",
          "extended-address": "",
          "locality": "London",
          "postal-code": "N16 5UP"
        }
      }],
      "restrictions": ["This is my restriction"],
      "provisions": ["This Mortgage Deed incorporates the Lenders Mortgage Conditions and Explanation 2006, a copy of which has been received by the Borrower.",
        "The lender is under an obligation to make further advances and applies for the obligation to be entered in the register.",
        "No disposition of the registered estate by the proprietor of the registered estate is to be registered without a written consent signed by Bank of England Plc."]
     }
    """
    And I link the created deed to the case
    And I sign the deed
    And make the deed effective
    When I send a submit request via the API
    And submit again
    Then a status code of "403" is returned
