import json
import os
from jsonbass.config import config
from jsonbass.random_utils import get_random_string
from jsonbass.exceptions import NoSuchColumnException


class DB(object):

    @staticmethod
    def get_database():
        if not os.path.isfile(config['db_file']):
            data = {}
        else:
            with open(config['db_file']) as _file:
                data = _file.read()
            _file.close()

        return json.loads(data) if data else {}

    @staticmethod
    def write(data):
        with open(config['db_file'], 'w+') as _file:
            _file.write(json.dumps(data))
        _file.close()

    @staticmethod
    def _delete_documents(data, column, documents):
        for i, entity in enumerate(data[column]):
            if entity in documents:
                del data[column][i]

        return data

    @staticmethod
    def iterate_documents(
        column,
        document_filter=None,
        document_update=None,
        delete=False,
        first=False
    ):
        data = DB.get_database()

        data[column] = [] if delete and not document_filter\
            else data[column]

        try:
            entities = [
                document_update(x) if document_update else x
                for x in filter(document_filter, data[column])
            ]
        except KeyError:
            raise NoSuchColumnException('{} is not an existing column'.format(
                str(column)
            ))

        data = DB._delete_documents(data, column, entities)\
            if delete and document_filter else data

        data[column] = entities if document_update and not delete\
            else data[column]

        DB.write(data) if delete or document_update else None

        return entities[0] if (entities and first) else entities

    @staticmethod
    def insert_document(column, doc):
        data = DB.get_database()

        data[column] = [] if column not in data else data[column]

        doc['id'] = get_random_string(24) if 'id' not in doc else doc['id']

        if not DB.iterate_documents(
                column, lambda x: x['id'] == doc['id'], first=True):
            data[column].append(doc)
        else:
            raise KeyError('Document with id: {} already exists'.format(
                doc['id']
            ))

        DB.write(data)

        return doc
