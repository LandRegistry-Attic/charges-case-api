import os

DEBUG = True

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'postgres:///case_api')
DEED_API_BASE_HOST = os.getenv('DEED_API_BASE_HOST',
                               'http://deedapi.dev.service.gov.uk')