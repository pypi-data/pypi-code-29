import logging
from si.service import Service
from si.errors import handle_error


class Trademark(Service):
    def __create(self, image, sources=None, nice_codes=None):
        logging.debug('Creating search')

        if sources is None:
            sources = ["all"]

        if nice_codes is None:
            nice_codes = []

        with open(image, 'rb') as file_stream:
            files = {'0': file_stream}
            sources_str = ', '.join('"{0}"'.format(w) for w in sources)
            nice_codes_str = ', '.join('"{0}"'.format(w) for w in nice_codes)

            data_operations = '{"operationName":"createSearch","variables":{"name":"default","image":null,"sources":[%s],"niceCodes":[%s]},"query":"mutation createSearch($name: String!, $sources: [String!]!, $niceCodes: [String!]!, $image: Upload!) { createSearch(name: $name, sources: $sources, niceCodes: $niceCodes, image: $image) { id __typename }}"}' % (sources_str, nice_codes_str)
            data_map = '{"0":["variables.image"]}'

            response = self._session.post(None, data={'operations': data_operations, 'map': data_map}, files=files)

        if response.status_code == 200:
            return response.json()

        exc = handle_error(response)
        exc.__cause__ = None
        raise exc

    def __search(self, search_id):
        logging.debug('Getting search results id=%s', search_id)

        response = self._session.post(None, json={
            'operationName': "searchQuery",
            'variables': {'id': search_id},
            'query': "query searchQuery($id: ID!) {search(id: $id) {  id  name  sources  niceCodes  image {    name    base64    __typename  }  owner {    name    email    __typename  }  results {    data {      id      index      name      date      status      models {        id        name        score        rawScore        __typename      }      source {        name        __typename      }      holder {        name        __typename      }      brand {        name        __typename      }      industries {        id        source {          id          __typename        }        __typename      }      image {        name        src        base64        __typename      }      __typename    }    __typename  }  __typename}\n}\n"
        })

        if response.status_code == 200:
            return response.json()

        exc = handle_error(response)
        exc.__cause__ = None
        raise exc

    def search(self, image, sources, nice_codes):
        create_response = self.__create(image, sources, nice_codes)
        errors = create_response.get('errors', [])
        if len(errors):
            return create_response

        search_id = create_response['data']['createSearch']['id']
        search_response = self.__search(search_id)
        return search_response
