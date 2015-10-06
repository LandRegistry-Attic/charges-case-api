When(/^I retrieve borrowers for the created case$/) do
  @retrieved_borrowers = get_borrowers_for_case(@created_case_id)
end

When(/^I try to add a borrower with missing mandatory information$/) do
  borrower_json = {
    'borrowers' => [
      {
        'first_name' => 'Paul',
        'last_name' => 'Smith',
        'email_address' => 'psmith@yahoo.co.uk',
        'type' => 'Borrower',
        'mobile_no' => '',
        'middle_names' => '',
        'address' => [
          '83 Lordship Park',
          'London',
          'N16 5UT'
        ]
      }
    ]
  }
  @response = HTTP.post(Env.case_api + '/case/' + @created_case_id.to_s +
                        '/borrowers', json: borrower_json)
end

Then(/^the correct borrowers details are returned$/) do
  @added_borrowers.zip(@retrieved_borrowers).each do |added, retrieved|
    assert_equal(added['first_name'], retrieved['first_name'])
    assert_equal(added['middle_names'],
                 retrieved['middle_names'])
    assert_equal(added['last_name'], retrieved['last_name'])
    assert_equal(added['address'], retrieved['address'])
    assert_equal(added['email_address'],
                 retrieved['email_address'])
    assert_equal(added['mobile_no'], retrieved['mobile_no'])
  end
end
