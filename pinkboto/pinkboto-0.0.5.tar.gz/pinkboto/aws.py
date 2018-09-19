import boto3
import pinkboto.cache


class aws(object):
    def __init__(self, profile=None, region=None, cache=120):
        """
        Create connection.
        :param profile: AWS profile
        :param region: AWS region
        :param cache: Cache usage
        """
        self.profile = profile
        self.region = region
        self.session = boto3.Session(profile_name=profile, region_name=region)

        import os
        self.__package_folder__, _ = os.path.split(__file__)

        resources_file = os.path.join(self.__package_folder__, 'resources.yml')

        import yaml
        self.resources = yaml.load(open(resources_file, "r"))

        self.cache = pinkboto.cache.Cache(lifetime=cache)

    def pagination(self, params):
        """
        Make all pagination requests and return results
        :param params: query params
        :return: results
        """
        from copy import deepcopy
        method_params = deepcopy(params)
        resource = self.resources[method_params['resource']]
        del method_params['resource']

        client = self.session.client(resource['client'])
        method = getattr(client, resource['list_method'])
        step = method(**method_params)
        results = step[resource['list_property']]

        if 'next_property' in resource:
            while resource['next_property'] in step:
                kwargs = {
                    resource['next_parameter']: step[resource['next_property']]}
                kwargs.update(method_params)
                step = method(**kwargs)
                results += step[resource['list_property']]

        return results

    def find(self, query=None, projection=None):
        """
        Selects objects in a schema.
        :param query: Optional. Specifies selection filter. To return all
          objects in a schema, omit this parameter or pass an empty object ({}).
        :param projection: Optional. Specifies the fields to return in the
          objects that match the query filter.
          To return all fields in the matching objects, omit this parameter.
        :return:
        """
        query = query if query else {}
        if not isinstance(query, dict):
            raise TypeError("Query must be a dict")

        projection = projection if projection else []
        if not isinstance(projection, list):
            raise TypeError("Projection must be a list")

        if 'resource' not in query:
            raise KeyError('query must have "resource" field')

        resource = self.resources[query['resource']]

        if 'list_parameters' in resource:
            method_params = dict([(k, v) for k, v in query.items()
                                  if k in resource['list_parameters']])
            for m in method_params:
                del query[m]
        else:
            method_params = {}

        method_params['resource'] = query['resource']
        del query['resource']

        results = self.cache.caching(self.pagination, method_params)

        for k, v in query.items():
            results = [
                result for result in results if k in result and result[k] == v
            ]

        def path(field, obj):
            if '.' in field:
                data = obj
                nodes = field.split('.')
                for node in nodes:
                    data = data[node]
                return data
            else:
                return obj[field]

        if projection:
            if len(projection) > 1:
                output = [{k: path(k, obj) for k in projection}
                    for obj in results]

                # output = [{k: path(k, v) for k, v in obj.items() if k in projection}
                #           for obj in results]
            else:
                # output = [[v for k, v in obj.items() if k in projection]
                #           for obj in results]
                output = [path(k, obj) for k in projection
                          for obj in results]
                # output = [item for sublist in output for item in sublist]
        else:
            output = results

        if isinstance(output, list) and len(output) == 1:
            output = output[0]

        if isinstance(output, dict) and len(output) == 1:
            _, output = list(output.items())[0]

        return output

    def insert(self, objs, workers=10):
        """
        Inserts a object or objects into a schema.
        :param objs: A object or list of objects to insert into the schema.
        :param workers: Optional. If set to greater than 1, creates objects in
          parallel requests. default is serial(1).
        :return: inserted objects.
        """

        pass

        # if not (isinstance(objs, dict) or isinstance(objs, list)):
        #     raise TypeError("Query must be a object or list of objects")
        # objs = objs if isinstance(objs, list) else [objs]
        #
        # process output
        #
        # if isinstance(output, list) and len(output) == 1:
        #     output = output[0]
        #
        # if isinstance(output, dict) and len(output) == 1:
        #     _, output = list(output.items())[0]
        #
        # return output

    def update(self, query, update, upsert=False, multi=False):
        """
        Modifies an existing object or objects in a schema. The method can
          modify specific fields of an existing object or objects or replace an
          existing object entirely, depending on the update parameter.

        By default, the update() method updates a single object. Set the Multi
          Parameter to update all objects that match the query criteria.

        Update() method can insert a object when query criteria not returns data
          if upsert property is True.

        :param query: The selection criteria for the update.
        :param update: The modifications to apply.
        :param upsert: Optional. If set to true, creates a new object when no
        object matches the query criteria.
          The default value is false, which does not insert a new object when
        no match is found.
        :param multi: Optional. If set to true, updates multiple objs that meet
          the query criteria.
          If set to false, updates one object. The default value is false.
        :return: List of Elements
        """
        # query = query if query else {}
        # if not isinstance(query, dict):
        #     raise TypeError("Query must be a dict")
        #
        # update = update if update else {}
        # if not isinstance(update, dict):
        #     raise TypeError("Query must be a dict")

        pass

    def remove(self, query):
        """

        :param query: Specifies deletion criteria. To delete all objects in a
        schema, pass an empty object ({}).
        :return:
        """

        query = query if query else {}
        if not isinstance(query, dict):
            raise TypeError("Query must be a dict")

        # process output
        #
        # if isinstance(output, list) and len(output) == 1:
        #     output = output[0]
        #
        # if isinstance(output, dict) and len(output) == 1:
        #     _, output = list(output.items())[0]
        #
        # return output

        pass

    def sync(self, objs, keys=None, workers=10):
        """

        :param objs: A object or list of objects to insert into the schema
        :param keys:  Specifies a filter key list from object.
        :param workers: Optional. If set to greater than 1, creates objects in
        parallel requests. If is 1 is serial.
            default is 10.
        :return:
        """

        if not keys:
            keys = ['name']

        if not (isinstance(objs, list)):
           objs = [objs]

        # def step(obj):
        #     query = dict([(field, obj[field]) for field in obj if field in keys])
        #     return self.update(query, obj, upsert=True, multi=False)
        #
        # results = tmap(step, objs, workers=workers)
        # output = [item for result in results if result for item in result]
        #
        # if isinstance(output, list) and len(output) == 1:
        #     output = output[0]
        #
        # if isinstance(output, dict) and len(output) == 1:
        #     _, output = list(output.items())[0]
        #
        # return output

        pass


