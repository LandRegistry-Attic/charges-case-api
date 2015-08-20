When(/^I try to add a borrower with missing mandatory information$/) do
  borrower_json = {
    "borrowers"=>[
      {
        "first_name"=>"Paul",
        "last_name"=>"Smith",
        "email_address"=>"psmith@yahoo.co.uk",
        "type"=>"Borrower",
        "mobile_no"=>"",
        "middle_names"=>"",
        "address"=>[
          "83 Lordship Park",
          "London",
          "N16 5UT"
        ]
      }
    ]
  }
  @response = HTTP.post($CASE_API_URL + '/case/' + @created_case['id'].to_s + '/borrowers', json: borrower_json)
end
