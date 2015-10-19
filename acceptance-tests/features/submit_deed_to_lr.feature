@submit_deed_to_lr

Feature: Submt Deed to LR
  As a Conveyancer I want to Submit my deed to Land Registry
  So that the Entries can be added to the register

@delete_test_data
Scenario: Submit a Case to Land Registry

  -A 200 response should be received for successful submission

  Given I have created a case and deed with one borrower that is effective
  When I submit the case via the API
  Then a status code of "200" is returned
