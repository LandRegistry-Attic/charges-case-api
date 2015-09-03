Given(/^I add the following property to the case:$/) do |property_json|
  @added_property = add_property_to_case(@created_case['id'], property_json)
end
