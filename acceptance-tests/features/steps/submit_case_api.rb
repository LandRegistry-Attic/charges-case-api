When(/^I send a submit request via the API$/) do
  @submitted_case = submit_case_data(@created_case_id)
end

When(/^I submit the case again$/) do
  @response = HTTP.post(Env.case_api + '/case/' + @created_case_id.to_s +
  '/application')
end

When(/^I submit the case via the API$/) do
  @response = HTTP.post(Env.case_api + '/case/' + @created_case_id.to_s +
  '/application')
end
