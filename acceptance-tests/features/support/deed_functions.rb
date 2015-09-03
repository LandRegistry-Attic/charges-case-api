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

def sign_the_deed(deed_id, signature, borrower_id)
  signature_json = {
    'signature' => signature
  }
  response = HTTP.post(Env.deed_api + '/deed/' + deed_id.to_s +
                       '/' + borrower_id + '/signature/', json: signature_json)
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
