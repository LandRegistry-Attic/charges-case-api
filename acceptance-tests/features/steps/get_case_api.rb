Given(/^I call the case API$/) do
  response = Net::HTTP.get_response(URI($CHARGES_API_URL + '/case'))
  $apiData = MultiJson.load(response.body)
end

Then(/^the correct case details are returned$/) do
  assert_match('id', $apiData[1234], 'Couldnt find text bla')
  assert_match('status', $apiData['bla'], 'Couldnt find text bla')
  assert_match('created_on', $apiData[Date.parse('bla')], 'Couldnt find text bla')
  assert_match('last_updated', $apiData[Date.parse('bla')], 'Couldnt find text bla')
  assert_match('deed_id', $apiData[1234], 'Couldnt find text bla')
  assert_match('conveyancer_id', $apiData[1234], 'Couldnt find text bla')
end
