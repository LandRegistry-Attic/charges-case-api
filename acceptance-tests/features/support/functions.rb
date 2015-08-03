def create_case_data(case_file)
  ### Read data from the supplied json filename
  case_json = File.read(File.dirname(__FILE__) + '/../../data/' + case_file + '.json')
  ### Setup a POST request to the case API to insert the data
  url = URI.parse($CASE_API_URL + "/case")
  connection = Net::HTTP.new(url.host, url.port)
  request = Net::HTTP::Post.new(url, initheader={
    'Content-Type' =>'application/json'
  })
  request.body = "#{case_json}"
  ### Execute the created request against the case API and return the response
  response = connection.request(request)
  if response.code == "201"
    JSON.parse(response.body)
  else
    raise "Failed to create case with json #{case_json}. Got response #{response.code} - #{response.body}"
  end
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
