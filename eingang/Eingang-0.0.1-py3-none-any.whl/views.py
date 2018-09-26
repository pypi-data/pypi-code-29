import logging
import os.path

from .util import get_random_alphanum_string
from flask import (
    Blueprint, current_app as app,
    redirect, render_template, url_for,
)
from flask_security import login_required

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Use a random name in order to prevent name collision
# between this blueprint and that of the parent blueprint(s).
#
#   name = 'eingang__' + get_random_alphanum_string(32)
#
# Unfortunately we can't use a dynamically generated random name
# because the blueprint is referenced in the templates (see url_for),
# so we have to know it at build time.
name = 'eingang'
static_folder = os.path.dirname(os.path.realpath(__file__))
static_folder = os.path.join(static_folder, 'static')
views = Blueprint(name, __name__, static_folder=static_folder)


@views.route('/')
def root():
    app.logger.debug('Eingang root view')
    return redirect(url_for('security.login'))


@views.route('/home')
@login_required
def home():
    app.logger.debug('Eingang home view')
    return render_template('eingang/home.html')


@views.route('/about')
def about():
    app.logger.debug('Eingang about view')
    return render_template('eingang/about.html')
