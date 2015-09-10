def create_case_data(case_json)
  case_json = JSON.parse(case_json)
  response = HTTP.post(Env.domain + '/case', json: case_json)
  if response.code == 201
    JSON.parse(response.body)
  else
    fail "Error: Couldn't create case #{case_json}, "\
            "received response #{response.code}"
  end
end

def get_case_data(case_id)
  response = HTTP.get(Env.domain + '/case/' + case_id.to_s)
  if response.code == 200
    JSON.parse(response.body)
  else
    fail "Error: Couldn't retrieve case #{case_id}, "\
            "received response #{response.code}"
  end
end

def add_borrowers_to_case(case_id, borrower_json)
  response = HTTP.post(Env.domain + '/case/' + case_id.to_s +
                      '/borrowers', json: borrower_json)
  if response.code == 200
    JSON.parse(response.body)
  else
    fail "Error: Couldn't add borrowers to case #{borrower_json}, "\
            "received response #{response.code}"
  end
end

def get_borrowers_for_case(case_id)
  response = HTTP.get(Env.domain + '/case/' + case_id.to_s + '/borrowers')
  if response.code == 200
    JSON.parse(response.body)
  else
    fail "Error: Couldn't retrieve borrowers for case #{case_id}, "\
            "received response #{response.code}"
  end
end

def add_property_to_case(case_id, property_json)
  property_json = JSON.parse(property_json)
  response = HTTP.post(Env.domain + '/case/' + case_id.to_s +
                      '/property', json: property_json)
  if response.code == 200
    JSON.parse(response.body)
  else
    fail "Error: Couldn't add property to case #{property_json}, "\
            "received response #{response.code}"
  end
end

def get_property_for_case(case_id)
  response = HTTP.get(Env.domain + '/case/' + case_id.to_s + '/property')
  if response.code == 200
    puts "Case #{case_id} has been deleted."
  else
    fail "Error: Couldn't retrieve property for case #{case_id}, "\
            "received response #{response.code}"
  end
end

def delete_case_data(case_id)
  response = HTTP.delete(Env.domain + '/case/' + case_id.to_s)
  if response.code == 200
    puts "Case #{case_id} has been deleted."
  else
    fail "Error: Couldn't delete case #{case_id}, "\
            "received response #{response.code}."
  end
end

def get_property_for_case(case_id)
  response = HTTP.get(Env.domain + '/case/' + case_id.to_s + '/property')
  if response.code == 200
    JSON.parse(response.body)
  else
    fail "Error: Couldn't retrieve property for case #{case_id}, "\
            "received response #{response.code}"
  end
end

def delete_case_data(case_id)
  response = HTTP.delete(Env.domain + '/case/' + case_id.to_s)
  if response.code == 200
    puts "Case #{case_id} has been deleted."
  else
    fail "Error: Couldn't delete case #{case_id}, "\
            "received response #{response.code}."
  end
end

def update_case_deed(deed_id, case_id)
  payload = {
    'deed_id' => deed_id
  }
  response = HTTP.post(Env.domain + '/case/' + case_id.to_s +
   '/deed', json: payload)
  if response.code == 200
    JSON.parse(response.body)['id']
  else
    fail "Error: Couldn't update case with deed_id #{payload}, "\
            "Received response #{response.code}"
  end
end

def submit_case(case_id)
  response = HTTP.post(Env.domain + '/case/' + case_id.to_s + '/application')
  if response.code == 200
    JSON.parse(response.body)
  else
    fail "Error: Couldn't submit case #{case_id}, "\
            "received response #{response.code}."
  end
end
