# -*- coding: utf-8 -*-

'''
Created on 2018. 9. 12.
@author: jason96
'''
from base import SplunkBase, SPINDEX
from splunklib import results
import requests
import json
import uuid


class SPException(Exception):

    def __init__(self, message):
        super(SPException, self).__init__(message)


class Indexer(SplunkBase):

    def __init__(self):
        super(Indexer, self).__init__()
        if SPINDEX not in self.service.indexes:
            self.service.indexes.create(SPINDEX)

    def index(self, index, doc, sourcetype='json', host='local'):
        if index in self.service.indexes:
            target = self.service.indexes[index]
            return target.submit(doc, sourcetype=sourcetype, host=host)
        else:
            raise SPException('No index specified.')


class Searcher(SplunkBase):

    def __init__(self):
        super(Searcher, self).__init__()

    def search_results_list(self, response):
        results_list = []
        reader = results.ResultsReader(response)
        for result in reader:
            if isinstance(result, dict):
                results_list.append(result)
        return results_list

    def search(self, spl):
        kwargs = {"count": 0}
        oneshotsearch_results = self.service.jobs.oneshot(spl, **kwargs)
        return self.search_results_list(oneshotsearch_results)


class ITSIManager(SplunkBase):
    '''
    This class is based on version 3.1.0(ITSI)
    http://docs.splunk.com/Documentation/ITSI/3.1.0/RESTAPI/ITSIRESTAPIreference
    http://docs.splunk.com/Documentation/ITSI/3.1.0/RESTAPI/ITSIRESTAPIschema
    '''

    def __init__(self):
        super(ITSIManager, self).__init__()
        base_uri = 'https://%s:8089/servicesNS/nobody/SA-ITOA/itoa_interface'
        self.base_uri = base_uri % (self.config['splunk_ip'],)

    def get_uuid(self,):
        return str(uuid.uuid1()).replace('-', '')[:24]

    def add_kpi_base_search_metrics(self, title, metrics):
        kpi_base = None
        for kpi_base_search in self.get_kpi_base_searches():
            if kpi_base_search['title'] == title:
                kpi_base = kpi_base_search
        if kpi_base is not None:
            kpi_base['metrics'] = metrics
            self.itsi_uri = ('%s/%s/%s') % (self.base_uri,
                                            'kpi_base_search',
                                            kpi_base['_key'])
            req = requests.put(self.itsi_uri,
                               auth=('admin', 'changepassword'),
                               data=json.dumps(kpi_base),
                               verify=False)
            return json.loads(req.content)
        else:
            return None

    def get_kpi_base_searches(self):
        self.itsi_uri = ('%s/%s') % (self.base_uri, 'kpi_base_search',)
        req = requests.get(self.itsi_uri, auth=('admin', 'changepassword'),
                           verify=False)
        return json.loads(req.content)

    def del_kpi_base_search(self, title):
        # fields='title''&'filter='\{"title":"bar"\}' -X DELETE
        self.itsi_uri = ('%s/%s') % (self.base_uri, 'kpi_base_search',)
        post_data = {}
        post_data['fields'] = 'title'
        post_data['filter'] = {"title": title}
        requests.delete(self.itsi_uri, auth=('admin', 'changepassword'),
                        data=json.dumps(post_data),
                        verify=False)

    def add_kpi_base_search(self, title, desc=''):
        self.itsi_uri = ('%s/%s') % (self.base_uri, 'kpi_base_search',)
        post_data = {}
        post_data['title'] = title
        post_data['description'] = desc
        req = requests.post(self.itsi_uri, auth=('admin', 'changepassword'),
                            data=json.dumps(post_data),
                            verify=False)
        return json.loads(req.content)
