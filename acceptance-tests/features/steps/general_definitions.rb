When(/^I retrieve the created case$/) do
  @retrieved_case = get_case_data(@created_case_id)
end

Then(/^a status code of "([^"]*)" is returned$/) do |status_code|
  assert_equal(status_code, @response.code.to_s)
end
