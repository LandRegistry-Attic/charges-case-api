import os

DEBUG = True

try:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']
except KeyError:
    print("[ERROR] You need set the export variable for DATABASE_URI")
    raise