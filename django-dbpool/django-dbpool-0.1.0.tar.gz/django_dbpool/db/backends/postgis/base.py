from django_dbpool.db.backends.postgresql_psycopg2.base import DatabaseWrapper as PooledDatabaseWrapper
# from django.contrib.gis.db.backends.postgis.creation import PostGISCreation
# from django.contrib.gis.db.backends.postgis.introspection import PostGISIntrospection
# from django.contrib.gis.db.backends.postgis.operations import PostGISOperations


# class DatabaseWrapper(PooledDatabaseWrapper):
#     def __init__(self, *args, **kwargs):
#         super(DatabaseWrapper, self).__init__(*args, **kwargs)
#         self.creation = PostGISCreation(self)
#         self.ops = PostGISOperations(self)
#         self.introspection = PostGISIntrospection(self)


from django.db.backends.base.base import NO_DB_ALIAS
# from django.db.backends.postgresql.base import (
#     DatabaseWrapper as Psycopg2DatabaseWrapper,
# )

from django.contrib.gis.db.backends.postgis.features import DatabaseFeatures
from django.contrib.gis.db.backends.postgis.introspection import PostGISIntrospection
from django.contrib.gis.db.backends.postgis.operations import PostGISOperations
from django.contrib.gis.db.backends.postgis.schema import PostGISSchemaEditor


class DatabaseWrapper(PooledDatabaseWrapper):
    SchemaEditorClass = PostGISSchemaEditor

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs.get('alias', '') != NO_DB_ALIAS:
            self.features = DatabaseFeatures(self)
            self.ops = PostGISOperations(self)
            self.introspection = PostGISIntrospection(self)

    def prepare_database(self):
        super().prepare_database()
        # Check that postgis extension is installed.
        with self.cursor() as cursor:
            cursor.execute("CREATE EXTENSION IF NOT EXISTS postgis")
