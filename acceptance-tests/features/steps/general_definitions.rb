Given(/^I have created the following case:$/) do |case_json|
  @case_id = create_case_data(case_json)
end
