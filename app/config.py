import os

DEBUG = True

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'postgres:///case_api')

DEED_API_BASE_HOST = os.getenv('DEED_API_BASE_HOST',
                               'http://deedapi.dev.service.gov.uk')

CASE_API_BASE_HOST = os.getenv('CASE_API_BASE_HOST',
                               'http://10.10.10.10:9070')