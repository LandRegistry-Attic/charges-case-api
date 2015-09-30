Given(/^I delete the created case$/) do
  delete_case_data(@created_case_id)
end

When(/^I attempt to retrieve the deleted case$/) do
  @response = HTTP.get(Env.case_api + '/case/' + @created_case_id.to_s)
end

When(/^I attempt to retrieve the borrower$/) do
  @response = HTTP.get(Env.case_api + '/case/' + @created_case_id.to_s +
                      '/borrowers')
end

When(/^I attempt to retrieve the property$/) do
  @response = HTTP.get(Env.case_api + '/case/' + @created_case_id.to_s +
                      '/property')
end
