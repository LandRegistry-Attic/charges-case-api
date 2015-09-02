Given(/^I add the following property to the case:$/) do |property_json|
  @added_property = JSON.parse(property_json)
  add_property_to_case(@created_case['id'], @added_property)
end
