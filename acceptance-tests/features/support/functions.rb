def create_case_data(case_json)
  case_json = JSON.parse(case_json)
  response = HTTP.post($CASE_API_URL + '/case', json: case_json)
  if response.code == 201
    JSON.parse(response.body)
  else
    fail "Error: Couldn't create case #{case_json}, "\
            "received response #{response.code}"
  end
end

def get_case_data(case_id)
  response = HTTP.get($CASE_API_URL + '/case/' + case_id.to_s)
  if response.code == 200
    JSON.parse(response.body)
  else
    fail "Error: Couldn't retrieve case #{case_id}, "\
            "received response #{response.code}"
  end
end

def update_case_status(deed_id, case_status)
  response = HTTP.post($CASE_API_URL + 'case/' + deed_id + '/status')
end

def delete_case_data(case_id)
  response = HTTP.delete($CASE_API_URL + '/case/' + case_id.to_s)
  if response.code == 200
    puts "Case #{case_id} has been deleted."
  else
    fail "Error: Couldn't delete case #{case_id}, "\
            "received response #{response.code}."
  end
end
