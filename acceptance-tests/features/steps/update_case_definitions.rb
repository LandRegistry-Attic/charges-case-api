When(/^I update the case status to "([^"]*)"$/) do |case_status|
  update_case_status(case_status, "1")
end
