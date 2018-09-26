import sys

from app import app
from database import db_session, init_db, user_datastore

email = sys.argv[1]

init_db()
with app.app_context():
    user = user_datastore.get_user(email)
    if not user:
        print('Error: User with that email does not exist.')
        sys.exit(1)

user_datastore.delete_user(user)
db_session.commit()
