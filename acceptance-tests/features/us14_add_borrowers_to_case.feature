@add_borrowers_to_case

Feature: Add Borrowers to Case
    As a lender/conveyancer  for a remortgage
    I want to fill in my clients details
    So that I have them on my records

Background:
    Given I have created the following case:
    """
    {
      "conveyancer_id": "1"
    }
    """

Scenario: Add Borrowers to Case
    When I add the following borrowers to a case:
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
       },
       {
         "first_name": "Sarah",
         "last_name": "Smith",
         "email_address": "sjsmith@gmail.com",
         "type": "Borrower",
         "mobile_no": "07970445566",
         "middle_names": "Jane",
         "address": [
           "18 Mayorly Place",
           "London",
           "N12 5RS"
         ]
        }
      ]
    }
    """
    And I retrieve borrowers for the created case
    Then the correct borrowers details are returned

Scenario: Add Borrower to Case with Missing Mandatory Information
    When I try to add a borrower with missing mandatory information
    Then a status code of "400" is returned
