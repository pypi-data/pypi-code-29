from django.contrib.sessions.backends import cached_db

from django_raw_clearsessions import SessionStoreMixin


class SessionStore(SessionStoreMixin, cached_db.SessionStore):
    pass
