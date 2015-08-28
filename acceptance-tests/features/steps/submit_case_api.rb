When(/^I send a submit request via the API$/) do
  @submitted_case = submit_case(@created_case['id'])
end

When(/^submit again$/) do
  @response = HTTP.post(Env.domain + '/case/' + @created_case['id'].to_s +
  '/application')
end
