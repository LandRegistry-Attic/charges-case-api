Given(/^I have created the following case:$/) do |case_json|
  @created_case = create_case_data(case_json)
end

When(/^I retrieve the created case$/) do
  @retrieved_case = get_case_data(@created_case['id'])
end

Given(/^I create the following deed:$/) do |deed_json|
  @created_deed = create_deed_data(deed_json)
end

Given(/^I link the created deed to the case$/) do
  update_case_deed(@created_deed['id'], @created_case['id'])
end

Given(/^I sign the deed$/) do
  sign_the_deed(@created_deed['id'], 'Peter Smith', '1')
end

Given(/^make the deed effective$/) do
  make_deed_effective(@created_deed['id'])
end

When(/^I add the following borrowers to a case:$/) do |borrower_json|
  add_borrowers_to_case(@created_case['id'], borrower_json)
end

Then(/^a status code of "([^"]*)" is returned$/) do |status_code|
  assert_equal(status_code, @response.code.to_s)
end
