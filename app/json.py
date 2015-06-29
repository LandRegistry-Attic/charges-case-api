import json as pythonjson


def deserialiseFailed(name, recovered):
    return Exception(
        "Would deserialise {} not {}".format(name, recovered)
    )


class Serialisable(object):

    def json_format(o):
        return NotImplemented

    def object_hook(dct):
        return NotImplemented

    @staticmethod
    def __subclass(name):

        def filter_by_name(cls):
            return cls.__name__ == name

        classes = filter(filter_by_name, Serialisable.__subclasses__())
        return [cls for cls in classes]

    @staticmethod
    def _object_hooks(jsondata):
        cls_name = jsondata.get('type')
        sublclasses = Serialisable.__subclass(cls_name)
        return sublclasses[0].object_hook(jsondata)

    @staticmethod
    def _defaults(obj):
        cls_name = type(obj).__name__
        json_dct = Serialisable.__subclass(cls_name)[0].json_format(obj)
        json_dct['type'] = cls_name
        return json_dct

    @classmethod
    def from_json(cls, jsondata):
        if isinstance(jsondata, dict):
            jsondata = pythonjson.dumps(jsondata)

        recovered = pythonjson.loads(
            jsondata,
            object_hook=Serialisable._object_hooks
        )

        if not cls == recovered.__class__:
            raise deserialiseFailed(cls.__name__, recovered.__class__.__name__)

        return recovered

    def to_json(self):
        return Serialisable._defaults(self)
