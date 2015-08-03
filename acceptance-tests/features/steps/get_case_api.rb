Given(/^I have created a case$/) do
  $case = create_case_data('new_case')
end

When(/^I call the case API$/) do
  response = Net::HTTP.get_response(URI($CASE_API_URL + '/case'))
  $apiData = MultiJson.load(response.body)
end

Then(/^the correct case details are returned$/) do
  targetCase = $apiData.select { |obj| obj['id'] == $case['id'] }.first

  assert_equal($case['id'], targetCase['id'], 'IDs don\'t match')
  assert_equal($case['status'], targetCase['status'])
  assert_equal($case['created_on'], targetCase['created_on'])
  assert_equal($case['last_updated'], targetCase['last_updated'])
  assert_equal($case['deed_id'], targetCase['deed_id'])
  assert_equal($case['conveyancer_id'], targetCase['conveyancer_id'])
end
