def LoggingRouter(alias="default"):
    class Router:

        def db_for_read(self, model, **hints):
            if model._meta.app_label == 'django_db_logging':
                return alias
            return None

        def db_for_write(self, model, **hints):
            if model._meta.app_label == 'django_db_logging':
                return alias
            return None

        def allow_migrate(self, db, app_label, model_name=None, **hints):
            if app_label == 'django_db_logging' and db == alias:
                return True

    return Router()
