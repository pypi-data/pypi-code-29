import requests

from xml.etree import ElementTree
from urllib.parse import urlencode
from typing import List
import mimetypes
import logging

from requests.adapters import HTTPAdapter

import pymicroconnectors.config as config

LOG = logging.getLogger(__name__)


# Exceptions
class PrestashopItemNotFoundException(Exception):
    pass


class PrestashopMultipleItemsFoundException(Exception):
    pass


class PrestashopErrorElement:
    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message


class PrestashopSearchElement:
    def __init__(self, id: str, ref: str):
        self.id = id
        self.ref = ref


class PrestashopOperationException(Exception):
    def __init__(self, input_message, errors: List[PrestashopErrorElement]):
        message = f'{input_message}\nError list: '
        for error in errors:
            message += f'\n{error.code} - {error.message}'
        super(PrestashopOperationException, self).__init__(message)
        self.errors = errors
        LOG.error(message)

class PrestashopHTTPAdapter(HTTPAdapter):

    def send(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None):
        if config.get_value('prestashop.printXml') is True:
            LOG.debug(f'Response: {request.body}')
        return super().send(request, stream, timeout, verify, cert, proxies)


class Prestashop:
    def __init__(self, api_url: str, api_key: str):
        self._api_url = api_url
        self._api_key = api_key
        self._session = requests.Session()
        adapter = PrestashopHTTPAdapter()
        self._session.mount('http://', adapter)
        self._session.mount('https://', adapter)

        if not self._api_url.endswith('/'):
            self._api_url += '/'

        if not self._api_url.endswith('/api/'):
            self._api_url += 'api/'

    def search_unique(self, resource: str, options: dict = None) -> PrestashopSearchElement:
        result = self.search(resource, options)
        if len(result) == 0:
            raise PrestashopItemNotFoundException('No result found')
        if len(result) > 1:
            raise PrestashopMultipleItemsFoundException('Multiple results found')
        return result[0]

    def search(self, resource: str, options: dict = None) -> List[PrestashopSearchElement]:
        xml = self.get(resource, options=options)
        result = []
        for element in xml[0]:
            result.append(
                PrestashopSearchElement(element.attrib['id'], element.attrib['{http://www.w3.org/1999/xlink}href']))
        return result

    def get(self, resource: str, resource_id: str = None, options: dict = None) -> ElementTree:
        full_url = self._api_url + resource
        if resource_id is not None:
            full_url += f'/{resource_id}'
        if options is not None:
            full_url += f'?{self._options_to_querystring(options)}'
        return self.get_with_url(full_url)

    def get_with_url(self, url) -> ElementTree:
        r = self._session.get(url, auth=(self._api_key, ''))
        return self._process_response(r, f'Getting data from url {url}')

    def add(self, resource, xml, optional_headers=None):
        LOG.debug(f'Adding resource [{resource}]')
        return self.add_with_url(self._api_url + resource, xml, optional_headers)

    def add_with_url(self, url, xml, optional_headers=None):
        if optional_headers is None:
            headers = {'Content-Type': 'text/xml'}
        else:
            headers = optional_headers
            headers['Content-Type'] = 'text/xml'
        r = self._session.post(url, data=xml.encode('utf-8'), headers=headers, auth=(self._api_key, ''))
        return self._process_response(r, f'Add data to url {url}')

    def edit(self, resource, content, optional_headers=None):
        full_url = f'{self._api_url}{resource}'
        return self.edit_with_url(full_url, content, optional_headers)

    def edit_with_url(self, url, xml, optional_headers=None):
        if optional_headers is None:
            headers = {'Content-Type': 'text/xml'}
        else:
            headers = optional_headers
            headers['Content-Type'] = 'text/xml'
        r = self._session.put(url, data=xml.encode('utf-8'), headers=headers, auth=(self._api_key, ''))
        return self._process_response(r, f'Editing data on url {url}')

    def delete(self, resource, id):
        return self.delete_with_url(f'{self._api_url}{resource}/{id}')

    def delete_with_url(self, url) -> ElementTree:
        headers = {'Content-Type': 'text/xml'}
        r = self._session.delete(url, headers=headers, auth=(self._api_key, ''))
        return self._process_response(r, f'Deleting data for url {url}')

    def delete_image(self, resource, id):
        full_url = f'{self._api_url}images/{resource}/{id}'
        headers = {'Content-Type': 'text/xml'}
        r = self._session.delete(full_url, headers=headers, auth=(self._api_key, ''))
        return self._process_response(r, f'Deleting image [{resource}] with id [{id}]')

    def add_image(self, resource, id, image=None, image_url=None):
        full_url = f'{self._api_url}images/{resource}/{id}'
        headers, body = self.encode_multipart_formdata(image, image_url)
        r = self._session.post(full_url, headers=headers, data=body, auth=(self._api_key, ''))
        return self._process_response(r, f'Add image [{resource}] with id [{id}]')

    @staticmethod
    def _process_response(r: ElementTree, input: str):
        if r.encoding is None:
            encoding = ''
        else:
            encoding = r.encoding
        content = r.content.decode(encoding)
        if config.get_value('prestashop.printXml') is True:
            LOG.debug(f'Response: {content}')
        if content == '':
            return None
        xml = ElementTree.fromstring(content)
        Prestashop._validate(input, xml)
        return xml

    @staticmethod
    def _options_to_querystring(options):
        return urlencode(options)

    @staticmethod
    def _validate(message, xml_response: ElementTree):
        result_list = []
        for error in xml_response.iter('error'):
            result_list.append(PrestashopErrorElement(error.find('code').text, error.find('message').text))
        if len(result_list) > 0:
            raise PrestashopOperationException(message, result_list)

    @staticmethod
    def encode_multipart_formdata(file=None, url=None):
        image = file

        BOUNDARY = '----------ThIs_Is_tHe_bouNdaRY_$'
        CRLF = '\r\n'.encode('ascii')
        L = []
        L.append('--'.encode('ascii') + BOUNDARY.encode('ascii'))
        L.append(
            ('Content-Disposition: form-data; name="%s"; filename="%s"' % ('image', image.get('name'))).encode('ascii'))
        L.append(('Content-Type: %s' % mimetypes.guess_type(image.get('name'))[0]).encode('ascii'))
        L.append(''.encode('ascii'))
        L.append(image.get('bytes'))
        L.append('--'.encode('ascii') + BOUNDARY.encode('ascii') + '--'.encode('ascii'))
        L.append(''.encode('ascii'))
        body = CRLF.join(L)
        headers = {'Content-Type': 'multipart/form-data; boundary=%s' % BOUNDARY}
        return headers, body

    @staticmethod
    def find_id(xml: ElementTree):
        return xml[0].find('id').text


    @staticmethod
    def find_type(xml: ElementTree):
        return xml[0].tag

    def build_search_element(self, xml: ElementTree, resource: str):
        return PrestashopSearchElement(self.find_id(xml), '%s%s/%s' % (self._api_url, resource, self.find_id(xml)))

api = None

def init():
    global api
    api = Prestashop(config.get_value('prestashop.apiUrl'),config.get_value('prestashop.apiKey'))