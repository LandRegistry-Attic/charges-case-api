from flask.ext.api import renderers
from types import *
import json
from flask.json import JSONEncoder


class JSONRenderer(renderers.BaseRenderer):
    media_type = 'application/json'

    def render(self, data, media_type, **options):

        try:
            indent = max(min(int(media_type.params['indent']), 8), 0)
        except (KeyError, ValueError, TypeError):
            indent = None

        indent = options.get('indent', indent)

        if isinstance(data, list):
            return json.dumps(data, cls=JSONEncoder, ensure_ascii=False, indent=indent)
        else:
            return json.dumps(data, cls=JSONEncoder, ensure_ascii=False, indent=indent)
