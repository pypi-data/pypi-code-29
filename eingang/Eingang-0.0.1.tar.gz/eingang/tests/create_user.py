import sys

from flask_security.utils import hash_password

from app import app
from database import db_session, init_db, user_datastore

username = sys.argv[1]
email = sys.argv[2]
password = sys.argv[3]

init_db()
with app.app_context():
    if user_datastore.get_user(email):
        print('Error: User with that email already exists.')
        sys.exit(1)
    password = hash_password(password)

user_datastore.create_user(
    username=username,
    email=email,
    password=password,
)

db_session.commit()
