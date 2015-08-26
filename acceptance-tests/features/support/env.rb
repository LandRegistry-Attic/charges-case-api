################################################################################
### This file contains the global variables for the various endpoints used   ###
### in acceptance tests, this abstracts the urls so that you will not        ###
### need to change every test when switching environments for example.       ###
################################################################################

# Environment variables for tests
class Env
  def self.deed_api
    (ENV['DEED_API_URL'] || 'http://deedapi.dev.service.gov.uk')
  end

  def self.domain
    (ENV['CASE_API_URL'] || 'http://case-api.dev.service.gov.uk')
  end
end
