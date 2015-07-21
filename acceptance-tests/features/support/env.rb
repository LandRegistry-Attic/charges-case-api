################################################################################
### This file contains the global variables for the various endpoints used   ###
### in acceptance tests, this abstracts the urls so that you will not        ###
### need to change every test when switching environments for example.       ###
################################################################################

$CASE_API_URL = (ENV['CHARGES_API_URL'] || 'http://case-api.dev.service.gov.uk')
