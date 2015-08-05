Given(/^I have created the following case:$/) do |case_json|
  @case = create_case_data(case_json)
end

When(/^I call the case API$/) do
  @retrievedCase = get_case_data(@case['id'])
end

Then(/^the "([^"]*)" is returned in the response$/) do |json_key|
  assert(@case[json_key], "Error: The #{json_key} was not returned "\
                              "in the response")
end

Then(/^the "([^"]*)" of "([^"]*)" is returned in the response$/) do |json_key, value|
  if @case[json_key]
    assert_equal(value, @case[json_key].to_s)
  else
    fail "Error: The #{json_key} was not returned in the response"
  end
end

Then(/^the "([^"]*)" of todays date is returned in the response$/) do |json_key|
  if @case[json_key]
    assert_match(Time.now.strftime("%Y-%m-%d"), @case[json_key].to_s)
  else
    fail "Error: The #{json_key} was not returned in the response"
  end
end
