from eingang import Eingang
from flask import Flask

from config import config
from database import user_datastore
from views import views


app = Flask(__name__)
app.register_blueprint(views)
app.config.update(config.items())
eingang = Eingang(app, user_datastore)

if __name__ == '__main__':
    app.run(debug=True)
