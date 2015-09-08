Given(/^I add the following property to the case:$/) do |property_json|
  @added_property = add_property_to_case(@created_case['id'], property_json)
end

When(/^I retrieve the property for the created case$/) do
  @retrieved_property = get_property_for_case(@created_case['id'])
end

When(/^I try to add another property to the case$/) do
  property_json = {
    'property' => {
      'locality' => 'Plymouth',
      'tenure' => 'freehold',
      'postcode' => 'PL3 5ST',
      'title_number' => 'DN513498',
      'street' => '12 Granville Street',
      'type' => 'Property',
      'extended' => 'Cattedown'
    }
  }
  @response = HTTP.post(Env.domain + '/case/' + @created_case['id'].to_s +
                        '/property', json: property_json)
end

Then(/^the correct property details are returned$/) do
  assert_equal(@added_property['title_number'],
               @retrieved_property['title_number'])
  assert_equal(@added_property['street'], @retrieved_property['street'])
  assert_equal(@added_property['extended'], @retrieved_property['extended'])
  assert_equal(@added_property['locality'], @retrieved_property['locality'])
  assert_equal(@added_property['postcode'], @retrieved_property['postcode'])
  assert_equal(@added_property['tenure'], @retrieved_property['tenure'])
  assert_equal(@added_property['type'], @retrieved_property['type'])
end
