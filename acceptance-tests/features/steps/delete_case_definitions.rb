Given(/^I delete the created case$/) do
  delete_case_data(@created_case['id'])
end
