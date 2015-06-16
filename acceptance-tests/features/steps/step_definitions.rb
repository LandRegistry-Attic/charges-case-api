Given(/^I access the helloworld API$/) do
  response = Net::HTTP.get_response(URI($CHARGES_API_URL + '/helloworld'))
  $apiData = MultiJson.load(response.body)
end

Then(/^the response contains Hello World$/) do
  assert_match('World', $apiData['Hello'], 'Couldnt find text World')
end
