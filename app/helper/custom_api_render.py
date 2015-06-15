from flask.ext.api import renderers
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

        return json.dumps(data, cls=JSONEncoder,
                          ensure_ascii=False, indent=indent)
