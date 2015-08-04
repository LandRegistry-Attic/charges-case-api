Given(/^I have created the following case:$/) do |case_json|
  @case = create_case_data(case_json)
end

When(/^I call the case API$/) do
  @retrievedCase = get_case_data(@case['id'])
end
