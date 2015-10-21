Given(/^I have created a new case$/) do
  case_json = {  'conveyancer_id' => '1'
  }
  @response = HTTP.post(Env.case_api + '/case', json: case_json)
end

And(/^the right details are returned$/) do
  assert(JSON.parse(@response.body)['id'],
         'Error: id not returned ' + @response.status_code.to_s)
  assert(JSON.parse(@response.body)['id'].is_a? Integer)
end
