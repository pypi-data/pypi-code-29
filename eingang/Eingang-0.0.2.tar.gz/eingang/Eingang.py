import os

from flask import Flask
from flask_mail import Mail
from flask_security import Security
import jinja2

from .forms import (
    ExtendedChangePasswordForm,
    ExtendedForgotPasswordForm,
    ExtendedLoginForm,
    ExtendedResetPasswordForm,
)
from .views import views


class Eingang:

    def __init__(self, app, user_datastore):

        app.config['SECURITY_PASSWORD_HASH'] = 'pbkdf2_sha512'
        app.config['SECURITY_POST_LOGIN_VIEW'] = 'home'
        app.config['SECURITY_POST_LOGOUT_VIEW'] = '.'
        app.config['SECURITY_SEND_PASSWORD_CHANGE_EMAIL'] = False
        app.config['SECURITY_CHANGEABLE'] = True
        app.config['SECURITY_RECOVERABLE'] = True
        app.config['SECURITY_TRACKABLE'] = True

        app.config['MAIL_SERVER'] = 'smtp.gmail.com'
        app.config['MAIL_PORT'] = 465
        app.config['MAIL_USE_SSL'] = True

        # Email sender has to be set twice
        # (see https://github.com/mattupstate/flask-security/issues/685).
        app.config['MAIL_DEFAULT_SENDER'] = 'eingang@localhost'
        app.config['SECURITY_EMAIL_SENDER'] = 'eingang@localhost'

        # Register Eingang's views blueprint. Do this before creating
        # the Flask Security object. Once Security is created, it's routes
        # (e.g. /login) cannot be overriden.
        app.register_blueprint(views)

        # Append Eingang's templates directory (the one in this file's
        # directory) to the templates loader.
        templates_dir = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 'templates')
        my_loader = jinja2.ChoiceLoader([
            app.jinja_loader,
            jinja2.FileSystemLoader(templates_dir),
        ])
        app.jinja_loader = my_loader

        mail = Mail(app)

        security = Security(
            app,
            user_datastore,
            login_form=ExtendedLoginForm,
            forgot_password_form=ExtendedForgotPasswordForm,
            reset_password_form=ExtendedResetPasswordForm,
            change_password_form=ExtendedChangePasswordForm,
        )

if __name__ == '__main__':
    from os.path import dirname
    print(dirname(__file__))
