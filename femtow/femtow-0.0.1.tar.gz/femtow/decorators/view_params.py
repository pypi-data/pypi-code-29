from femtow.decorators.views import view_param


@view_param
def request(app):
    return app.current_request
