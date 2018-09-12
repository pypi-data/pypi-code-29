# coding=utf-8
"""
The Template Folders API endpoint

Documentation: http://developer.mailchimp.com/documentation/mailchimp/reference/template-folders/
Schema: https://api.mailchimp.com/schema/3.0/TemplateFolders/Instance.json
"""
from __future__ import unicode_literals

from mailchimp3.baseapi import BaseApi


class TemplateFolders(BaseApi):
    """
    Organize your templates using folders.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(TemplateFolders, self).__init__(*args, **kwargs)
        self.endpoint = 'template-folders'
        self.folder_id = None


    def create(self, data):
        """
        Create a new template folder.

        :param data: The request body parameters
        :type data: :py:class:`dict`
        data = {
            "name": string*
        }
        """
        if 'name' not in data:
            raise KeyError('The template folder must have a name')
        response = self._mc_client._post(url=self._build_path(), data=data)
        if response is not None:
            self.folder_id = response['id']
        else:
            self.folder_id = None
        return response


    def all(self, get_all=False, **queryparams):
        """
        Get all folders used to organize templates.

        :param get_all: Should the query get all results
        :type get_all: :py:class:`bool`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        queryparams['count'] = integer
        queryparams['offset'] = integer
        """
        self.folder_id = None
        if get_all:
            return self._iterate(url=self._build_path(), **queryparams)
        else:
            return self._mc_client._get(url=self._build_path(), **queryparams)


    def get(self, folder_id, **queryparams):
        """
        Get information about a specific folder used to organize templates.

        :param folder_id: The unique id for the File Manager folder.
        :type folder_id: :py:class:`str`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        """
        self.folder_id = folder_id
        return self._mc_client._get(url=self._build_path(folder_id), **queryparams)


    def update(self, folder_id, data):
        """
        Update a specific folder used to organize templates.

        :param folder_id: The unique id for the File Manager folder.
        :type folder_id: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:class:`dict`
        data = {
            "name": string*
        }
        """
        if 'name' not in data:
            raise KeyError('The template folder must have a name')
        self.folder_id = folder_id
        return self._mc_client._patch(url=self._build_path(folder_id), data=data)


    def delete(self, folder_id):
        """
        Delete a specific template folder, and mark all the templates in the
        folder as ‘unfiled’.

        :param folder_id: The unique id for the File Manager folder.
        :type folder_id: :py:class:`str`
        """
        self.folder_id = folder_id
        return self._mc_client._delete(url=self._build_path(folder_id))


