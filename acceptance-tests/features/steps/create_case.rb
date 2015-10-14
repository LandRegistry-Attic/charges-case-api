Given(/^I have created a new case$/) do

  def create_case_test

        case_json = {
          'conveyancer_id' => '1'
        }
        response = HTTP.post(Env.case_api + '/case', json: case_json)

  end
  @case_test = create_case_test
end

When(/^a status code 201 is returned$/) do
  def check_status_code()

        if @case_test.code == 201
          JSON.parse(@case_test.body)
        else
          fail "Error: Couldn't create case, "\
                  "Received response #{@case_test.code}"
        end
  end
  @check_case_code = check_status_code
end


Then(/^the right details are returned$/) do

#deed_check = HTTP.post(Env.case_api + '/case', json: case_json)

assert_equal(@check_case_code['id'], JSON.parse(@case_test.body)['id'])
assert_equal(@check_case_code['status'], JSON.parse(@case_test.body)['status'])
assert_equal(@check_case_code['deed_id'], JSON.parse(@case_test.body)['deed_id'])
=begin
  assert_equal(@created_case['status'], @retrieved_case['status'])
  assert_equal(@created_case['created_on'], @retrieved_case['created_on'])
  assert_equal(@created_case['last_updated'], @retrieved_case['last_updated'])
  assert_equal(@created_case['deed_id'], @retrieved_case['deed_id'])
  assert_equal(@created_case['conveyancer_id'],
               @retrieved_case['conveyancer_id'])
=end

end
