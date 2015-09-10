from flask import current_app


def register_routes(blueprint):

    @blueprint.route('/', methods=['GET'])
    def api_map():
        links = {}
        for rule in current_app.url_map._rules:
            links[rule.rule] = (strip_irrelevant_methods(rule))

        return links


def strip_irrelevant_methods(rule):

    return str(list(
        filter(
            lambda method:
            method != "OPTIONS" and method != "HEAD",
            list(rule.methods)
        )
    )[0])


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)
