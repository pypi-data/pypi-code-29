from django.contrib.sessions.backends import db

from django_raw_clearsessions import SessionStoreMixin


class SessionStore(SessionStoreMixin, db.SessionStore):
    pass
