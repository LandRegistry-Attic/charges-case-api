@delete_case

Feature: Delete Case using Case API
    These features were added later on in the project when it was discovered
    that some functions of the APIs were not being covered by acceptance tests

Scenario: Delete a Case with a Borrower and Property
    Given I have created the following case:
    """
    {
      "conveyancer_id": "1"
    }
    """
    And I add the following borrowers to a case:
    """
    {
      "borrowers": [
         {
           "first_name": "Paul",
           "last_name": "Smith",
           "email_address": "psmith@yahoo.co.uk",
           "type": "Borrower",
           "mobile_no": "07970112233",
           "middle_names": "",
           "address": [
             "83 Lordship Park",
             "London",
             "N16 5UT"
           ]
         }
       ]
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
    And I delete the created case
    When I attempt to retrieve the deleted case
    Then a status code of "404" is returned
    When I attempt to retrieve the borrower
    Then a status code of "404" is returned
    When I attempt to retrieve the property
    Then a status code of "404" is returned
