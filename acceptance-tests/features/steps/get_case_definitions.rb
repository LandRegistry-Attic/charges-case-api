Then(/^the returned "([^"]*)" matches the one created$/) do |json_key|
  assert_equal(@case[json_key], @retrievedCase[json_key])
end
