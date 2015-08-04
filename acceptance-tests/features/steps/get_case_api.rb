Given(/^I have created a case$/) do
  @case = create_case_data
end

When(/^I call the case API$/) do
  @retrievedCase = get_case_data(@case['id'])
end

Then(/^the correct case details are returned$/) do
  assert_equal(@case['id'], @retrievedCase['id'])
  assert_equal(@case['status'], @retrievedCase['status'])
  assert_equal(@case['created_on'], @retrievedCase['created_on'])
  assert_equal(@case['last_updated'], @retrievedCase['last_updated'])
  assert_equal(@case['deed_id'], @retrievedCase['deed_id'])
  assert_equal(@case['conveyancer_id'], @retrievedCase['conveyancer_id'])
  assert_equal(@case['case_ref'], @retrievedCase['case_ref'])
end
