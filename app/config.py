import os

DEBUG = True

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'postgres:///case_api')
