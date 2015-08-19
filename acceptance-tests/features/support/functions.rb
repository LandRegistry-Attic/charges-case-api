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

def delete_case_data(case_id)
  url = URI.parse($CASE_API_URL + "/case/" + case_id.to_s)
  connection = Net::HTTP.new(url.host, url.port)
  request = Net::HTTP::Delete.new(url)
  response = connection.request(request)
  response.body
end
