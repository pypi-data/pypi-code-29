import logging
# noinspection PyUnresolvedReferences
import types as python_types
import urllib.parse as urlparse
from typing import Optional

from apistar import Route, http, types, validators
# noinspection PyUnresolvedReferences
from apistar.exceptions import HTTPException, Forbidden
from apistar_jwt import JWTUser

log = logging.getLogger(__name__)


def create_model(model_name: str, attributes: dict):
    """ metaprogramming script that builds classes for input when given a name and a dictionary of attributes """
    return type(
        model_name,  # name of the class
        # (eval('types.Type'),),  # super class as tuple
        (types.Type,),  # super classes at a tuple
        attributes
    )


def create_fields(field_meta_data: list):
    """ metaprogramming script that returns the dictionary of attributes for a type model data class """
    # FIELD METADATA needs to follow the rules defined by apistar https://docs.apistar.com/api-guide/type-system/
    attributes = {}
    for field in field_meta_data:
        kw_args = []
        if 'title' in field.keys():
            kw_args.append('title="%s"' % field['title'])
        if 'description' in field.keys():
            kw_args.append('description="%s"' % field['description'])
        if 'default' in field.keys():
            if type(field['default']) == str:
                kw_args.append('default="%s"' % field['default'])
            else:
                kw_args.append('default=%s' % field['default'])
        # process attributes
        for k, v in field['attributes'].items():
            if k not in ('name', 'type'):
                if type(v) == str:
                    # if str wrap in quotes
                    kw_args.append('%s="%s"' % (k, v))
                else:
                    kw_args.append('%s=%s' % (k, v))
        validator = eval('validators.%s(%s)' % (field['type'], ', '.join(kw_args)))
        attributes[field['name']] = validator
    return attributes


# @lru_cache(maxsize=32, typed=True)  # add caching to reduce the hits to the database  # todo: create lru cache invalidator
# def user_permitted(user_id: int=None, permission_id: int=None, database=None):
def user_permitted(user_id: int=None, permission_id: int=None, database=None):
    query1 = "select is_permitted(%(permissionid)s, %(userid)s) as permitted"
    database.cursor.execute(query1, {'permissionid': permission_id, 'userid': user_id})
    permitted = database.cursor.fetchone()[0]
    if not permitted:
        raise Forbidden('User does not have permission for this activity')
    return True


class GetResponse(types.Type):
    """ default type for get request responses """

    count = validators.Integer(description="The number of objects matching this query.", allow_null=True)
    next = validators.String(description="The url for the next page of data.", allow_null=True)
    previous = validators.String(description="The url for the previous page of data.", allow_null=True)
    results = validators.Array(description="The list of objects returned by the query.", allow_null=True)


class ApistarDynamic(object):
    api_metadata = []
    get_response_class = GetResponse
    database_class = None
    readonly_database_class = None

    def __init__(self, api_metadata: Optional[list] = None, database_class=None, readonly_database_class=None):
        if api_metadata:
            self.api_metadata = api_metadata
        # setup database classes
        if database_class:
            self.database_class = database_class
        if readonly_database_class:
            self.readonly_database_class = readonly_database_class
        if not self.readonly_database_class:
            self.readonly_database_class = self.database_class
        # setup database connections
        self.database = self.database_class()
        self.readonly_database = self.readonly_database_class()
        # handlers
        self.HANDLER_DEFINERS = {
            'POST': self.define_post_handler,
            'GET': self.define_get_handler,
        }

    #
    # META VIEWS - these scripts generate classes and functions to run the views.
    #

    def authentication_function(self, user_id: int, permission_id: int):
        user_permitted(user_id=user_id, permission_id=permission_id, database=self.readonly_database)

    def define_post_handler(self, api_metadata):
        """ build a handler to handle post requests to insert data """
        name = api_metadata['name']
        data_name = api_metadata['data']
        field_metadata = api_metadata['fields']
        doc = api_metadata.get('doc')
        sql_list = api_metadata.get('sql', [])
        data_model = create_model(data_name, create_fields(field_metadata))
        authentication_function = self.authentication_function
        permission_id = api_metadata.get('permission_id')
        database_class = self.readonly_database_class

        def handler(data: data_model, path_params: http.PathParams, query_params: http.QueryParams, user: JWTUser) -> dict:
            params = {**dict(query_params), **dict(path_params)}  # build params out of path and query params
            payload = dict(data)
            payload.pop('id')  # remove id field
            database = database_class()
            # validate user
            authentication_function(user_id=user.id, permission_id=permission_id)
            # log.info(self.authentication_function.cache_info())

            for query in sql_list:
                database.cursor.execute(query, dict(data))
            database.conn.commit()
            database.cursor.execute('SELECT LASTVAL()')  # TODO: this is not returning the correct last entered value
            # TODO: this should return whatever is returned from the query. default should be RETURNING id
            return {
                "success": True,
                "id": database.cursor.fetchone().get('lastval')
            }  # this should return a 201 http status code

        handler.__name__ = name  # set the name of the new function
        handler.__doc__ = """ %s """ % doc

        return handler

    # noinspection PyProtectedMember
    @staticmethod
    def get_next_and_prev_urls(url: str, offset: int):
        """ build the pagination for get requests """
        parsed = urlparse.urlparse(url)
        next_queries = []
        prev_queries = []
        prev_url = None
        for pairs in parsed.query.split('&'):
            if 'offset=' not in pairs:
                next_queries.append(pairs)
                prev_queries.append(pairs)

        next_queries.append("offset=%s" % (offset + 1))
        if offset > 1:
            prev_queries.append("offset=%s" % (offset - 1))
        next_url = urlparse.urlunparse(parsed._replace(query="&".join(next_queries)))
        if offset > 0:
            prev_url = urlparse.urlunparse(parsed._replace(query="&".join(prev_queries)))
        return next_url, prev_url

    def create_get_response_class(self, model_name, response_object_class=validators.Object):

        return type(
            model_name,  # name of the class
            # (eval('types.Type'),),  # super class as tuple
            (self.get_response_class,),  # super classes at a tuple
            {
                'results': validators.Array(allow_null=True, items=response_object_class)
            }
        )

    def define_get_handler(self, api_metadata):
        """ build a handler to handle post requests """
        name = api_metadata['name']
        data_name = api_metadata['data']
        field_metadata = api_metadata['fields']
        authentication_function = self.authentication_function
        data_model = create_model(data_name, create_fields(field_metadata))
        # response_class = GetResponse
        # noinspection PyTypeChecker
        response_class = self.create_get_response_class("%sResponse" % data_name, data_model)  # build the response class with the data_model as the object
        doc = api_metadata.get('doc')
        sql = api_metadata.get('sql')
        permission_id = api_metadata.get('permission_id')
        if api_metadata['readonly']:
            database_class = self.readonly_database_class
        else:
            database_class = self.database_class

        def handler(path_params: http.PathParams, query_params: http.QueryParams, request: http.Request, user: JWTUser) -> response_class:
            db = database_class()
            url = request.url
            params = {**dict(query_params), **dict(path_params)}  # build params out of path and query params

            # validate user
            authentication_function(user_id=user.id, permission_id=permission_id)
            # log.info(user_permitted.cache_info())

            # PROCESS PAGINATION
            db.cursor.execute("SELECT COUNT(*)" + sql[sql.lower().index(' from '):], params)
            count = db.cursor.fetchone()['count']
            # set default limit
            try:
                limit = int(params.get('limit'))
            except TypeError:
                limit = 100
            # set default offset
            try:
                offset = int(params.get('offset'))
            except TypeError:
                offset = 0
            # set next_url and prev_url
            next_url, prev_url = self.get_next_and_prev_urls(url, offset=offset)
            if ((offset * limit) + limit) >= count:  # if there are no more pages.
                next_url = None
            params['limit'] = limit
            params['offset'] = offset

            # Process Query
            db.cursor.execute("{} limit %(limit)s offset %(offset)s".format(sql), params)
            data_payload = []
            for row in db.cursor.fetchall():
                data_payload.append(data_model(dict(row)))
            # SQL goes here
            return {
                'count': count,
                'next': next_url,
                'previous': prev_url,
                'results': data_payload
            }

        handler.__name__ = name  # set the name of the new function
        handler.__doc__ = """ %s """ % doc

        return handler

    def get_dynamic_routes(self) -> list:
        """ takes metadata definition, returns list of api* routes """
        routes = []
        for md in self.api_metadata:
            routes.append(
                Route(
                    md['path'],
                    method=md['method'],
                    handler=self.HANDLER_DEFINERS[md['method']](md)
                )
            )
        return routes
