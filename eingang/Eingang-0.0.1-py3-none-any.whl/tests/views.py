import logging

from eingang.util import get_random_alphanum_string
from flask import Blueprint, current_app as app, render_template


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Use a random name in order to prevent name collision
# between this blueprint and that of the parent blueprint(s).
name = 'Test_' + get_random_alphanum_string(32)
views = Blueprint(name, __name__)


"""
@views.route('/')
def root():
    app.logger.debug('Test root view')
    return render_template('index.html')
"""


@views.route('/home')
def home():
    app.logger.debug('Test home view')
    return render_template('home.html')
