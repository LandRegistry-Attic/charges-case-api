Then(/^the correct case details are returned$/) do
  assert_equal(@created_case['id'], @retrieved_case['id'])
  assert_equal(@created_case['status'], @retrieved_case['status'])
  assert_equal(@created_case['created_on'], @retrieved_case['created_on'])
  assert_equal(@created_case['last_updated'], @retrieved_case['last_updated'])
  assert_equal(@created_case['deed_id'], @retrieved_case['deed_id'])
  assert_equal(@created_case['conveyancer_id'],
               @retrieved_case['conveyancer_id'])
end
