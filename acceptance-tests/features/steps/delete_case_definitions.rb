Given(/^I delete the created case$/) do
  delete_case_data(@created_case['id'])
end

When(/^I attempt to retrieve the deleted case$/) do
  @response = HTTP.get(Env.domain + '/case/' + @created_case['id'].to_s)
end

When(/^I attempt to retrieve the borrower$/) do
  @response = HTTP.get(Env.domain + '/case/' + @created_case['id'].to_s +
                      '/borrowers')
end

When(/^I attempt to retrieve the property$/) do
  @response = HTTP.get(Env.domain + '/case/' + @created_case['id'].to_s +
                      '/property')
end
