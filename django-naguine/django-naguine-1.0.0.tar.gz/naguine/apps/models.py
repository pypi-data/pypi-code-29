"""Naguine helper objects for Django app models."""

from django.apps import apps


def get_model(app_dot_model):
    """
    Returns Django model class corresponding to passed-in `app_dot_model`
    string. This is helpful for preventing circular-import errors in a Django
    project.

    Positional Arguments:
    =====================
    - `app_dot_model`: Django's `<app_name>.<model_name>` syntax. For example,
                       the default Django User model would be `auth.User`,
                       where `auth` is the app and `User` is the model.
    """

    try:
        app, model = app_dot_model.split('.')
    except ValueError:
        msg = (f'Passed in value \'{app_dot_model}\' was not in the format '
               '`<app_name>.<model_name>`.')
        raise ValueError(msg)

    return apps.get_app_config(app).get_model(model)
