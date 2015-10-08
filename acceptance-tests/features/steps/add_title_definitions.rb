When(/^I retrieve the property for the created case$/) do
  @retrieved_property = get_property_for_case(@created_case_id)
end

When(/^I try to add another property to the case$/) do
  path = File.expand_path('../../data/mortgage_property.json', __FILE__)
  property_json = File.read(path)
  @response = HTTP.post(Env.case_api + '/case/' + @created_case_id.to_s +
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
