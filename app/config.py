import os

DEBUG = True

DEFAULT_RENDERERS = ['app.helper.custom_api_render.JSONRenderer',
                     'flask.ext.api.renderers.BrowsableAPIRenderer']
# 'app.helper.custom_api_render.JSONRenderer'
try:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']
except KeyError:
    print("[ERROR] You need set the export variable for DATABASE_URI")
    raise
