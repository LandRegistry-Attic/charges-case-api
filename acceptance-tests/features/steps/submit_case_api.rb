
When(/^I send a submit request via the API$/) do
  @submitted_case = submit_case(@created_case['id'])
end

When(/^submit again$/) do
  @response = HTTP.post(Env.domain + '/case/' + @created_case['id'].to_s +
  '/application')
end

Then(/^an error message of (\d+) is returned$/) do |status_code|
  assert_equal(status_code, @response.code.to_s)
end
