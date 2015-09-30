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
  number_of_borrowers = @added_borrowers.count

  for i in 0..(number_of_borrowers - 1) do
    added_borrower = @added_borrowers[i]
    retrieved_borrower = @retrieved_borrowers[i]

    assert_equal(added_borrower['first_name'], retrieved_borrower['first_name'])
    assert_equal(added_borrower['middle_names'],
                 retrieved_borrower['middle_names'])
    assert_equal(added_borrower['last_name'], retrieved_borrower['last_name'])
    assert_equal(added_borrower['address'], retrieved_borrower['address'])
    assert_equal(added_borrower['email_address'],
                 retrieved_borrower['email_address'])
    assert_equal(added_borrower['mobile_no'], retrieved_borrower['mobile_no'])
  end
end
