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

def delete_case_data(case_id)
  response = HTTP.delete(Env.domain + '/case/' + case_id.to_s)
  if response.code == 200
    puts "Case #{case_id} has been deleted."
  else
    fail "Error: Couldn't delete case #{case_id}, "\
            "received response #{response.code}."
  end
end

def create_deed_data(deed_json)
  deed_json = JSON.parse(deed_json)
  response = HTTP.post(Env.deed_api + '/deed/', json: deed_json)
  if response.code == 200
    JSON.parse(response.body)
  else
    fail "Error: Couldn't create deed #{deed_json}, "\
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

def sign_the_deed(deed_id, signature, borrower_id)
  signature_json = {
    'signature' => signature
  }
  response = HTTP.post(Env.deed_api + '/deed/' + deed_id.to_s +
                       '/' + borrower_id + '/signature/',
                       json: signature_json)

  if response.code == 200
    puts "Deed #{deed_id} has been signed."
  else
    fail "Error: Couldn't sign deed #{deed_id}, "\
            "received response #{response.code}."
  end
end

def make_deed_effective(deed_id)
  signature_json = {
    'registrars-signature' => 'SIGNATURE'
  }
  response = HTTP.post(Env.deed_api + '/deed/' + deed_id.to_s + '/completion',
                       json: signature_json)

  if response.code == 200
    puts "Deed #{deed_id} has been made effective."
  else
    fail "Error: Couldn't make deed #{deed_id} effective, "\
            "received response #{response.code}."
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
