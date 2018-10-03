#!/usr/bin/env python

import os
import json
import logging
import requests


class XNATException(Exception):
    '''
    XNAT-specific Exception class for handling library-related errors
    '''
    pass


class Connection(object):
    '''
    Class with set of functionalities for interfacing/communicating with XNAT using REST API
    To instantiate properly, provide: XNAT hostname (URL), credentials (either sessionID token or basic auth. credentials)
    Note I: that a valid XNAT account is required to interface with the XNAT
    Note II: Support for self-signed SSL certificates provided (unverified_context)
    Note III: Support for offline-mode class instantiation
    '''
    def __init__(self, hostname, credentials=None, verify=True, verbose=False):

        self.host = self._normalize_URI(hostname)
        # logging handling
        self.log = logging.getLogger('bxl')
        if verbose :
            self.log.setLevel(logging.DEBUG)
        # SSL context verification handling
        self.verified_SSL_context = verify
        if not verify :
            # Suppress warning messages which may get quite annoying
            import urllib3
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        # credentials handling
        if isinstance(credentials, tuple) and len(credentials) == 2:
            # Basic HTTP auth. method
            self.jsession_id = {"JSESSIONID": self._open_jsession(credentials)}
        elif isinstance(credentials, basestring) :
            # sessionID token auth. method
            self.jsession_id = {"JSESSIONID": credentials}
        else :
            # offline mode
            self.jsession_id = None

        if self.jsession_id :
            if self.resource_exist(self.host) :
                self.log.info('Connected to %s' % self.host)
            else :
                self.log.error('Unable to connect to server %s, check credentials and/or server availability. Offline connection.'
                              % self.host)
                self.jsession_id = None
        else :
            self.log.warning('No credentials provided. Offline connection')

    def __enter__(self):

        return self

    def __exit__(self, type, value, traceback):

        if self.jsession_id :
            self.close_jsession()


    def _normalize_URI(self, URI):
        '''
        Helper to harmonize any given URI by removing existing ending slash ('/') chars
        :param URI: URI string to normalize
        :return: A normalized URI string
        '''

        return URI.strip('/')


    def _open_jsession(self, credentials):
        '''
        Authenticates and returns a jsessionID token
        :param credentials: tuple with credentials
        :return: An HTTP response object
        '''

        URI = self.host + '/data/JSESSION'

        response = requests.post(URI,
                                 auth=(credentials[0], credentials[1]),
                                 verify=self.verified_SSL_context,
                                 timeout=10
                                 )

        if response.status_code != requests.codes.ok:
            raise XNATException('HTTP response: #%s%s%s' %(response.status_code,os.linesep,response.content))

        return response.content


    def close_jsession(self):
        '''
        Closes the session with XNAT server and consumes the JSESSIONID token
        '''

        URI = self.host + '/data/JSESSION'

        response = requests.delete(URI,
                                   cookies=self.jsession_id,
                                   verify=self.verified_SSL_context,
                                   timeout=10
                                   )

        if response.status_code != requests.codes.ok:
            raise XNATException('HTTP response: #%s%s%s' % (response.status_code, os.linesep, response.content))

        self.jsession_id = None
        self.log.info('Disconnected from %s' % self.host)


    def resource_exist(self,URI):
        '''
        HTTP query to check if a given URI already exists
        :param URI: XNAT resource URI
        :returns: True if resource exists in the XNAT server; false otherwise
        '''

        response = requests.head(URI,
                                 cookies=self.jsession_id,
                                 verify=self.verified_SSL_context,
                                 timeout=10
                                 )

        return bool(response.status_code == requests.codes.ok)


    def _get_raw_data(self, URI, options=None):
        '''
        Retrieves unformatted data from XNAT (GET action)
        :param URI: XNAT resource URI
        :param options: dictionary with query options and flags
        :return: Raw data structure object (string formatted data chunk)
        '''

        response = requests.get(URI,
                                params=options,
                                cookies=self.jsession_id,
                                verify=self.verified_SSL_context,
                                timeout=100
                                )

        if response.status_code != requests.codes.ok:
            raise XNATException('HTTP response: #%s%s%s' % (response.status_code, os.linesep, response.content))

        return response.content


    def _query_data(self, URI, options=None):
        '''
        Queries for a (filtered,sorted) list of data entities in XNAT (GET action)
        :param URI: XNAT resource URI
        :param options: dictionary with query options and flags
        :return: Manipulable data structure parsed as a JSON object
        '''

        # force output data format to JSON
        if not options :
            options = {}
        options['format'] = 'json'

        data = self._get_raw_data(URI, options)

        json_data = json.loads(data)
        result_set = json_data['ResultSet']['Result']

        return result_set


    #def post_uri(self, URI, options=None):
    #    '''
    #    Updates an XNAT resource or entity (POST action)
    #    :param URI: XNAT resource URI
    #    :param options: dictionary with post options and flags
    #    :return: An HTTP response object
    #    '''

    #    response = requests.post(URI,
    #                             params=options,
    #                             cookies=self.jsession_id,
    #                             verify=self.verified_SSL_context,
    #                             timeout=100
    #                             )
    #    if response.status_code != requests.codes.ok:
    #        raise XNATException('HTTP response: #%s%s%s' % (response.status_code, os.linesep, response.content))

    #    return response


    def _put_resource(self, URI, options=None):
        '''
        Creates an XNAT entity with no data (PUT action)
        :param URI: XNAT resource URI
        :param options: dictionary with put options and flags
        :return: An HTTP response object
        '''

        return self._put_data(URI, data="", options=options)


    def _put_data(self, URI, data, options=None):
        '''
        Creates or updates an XNAT entity with HTTP body data (i.e. XML object)
        :param URI: XNAT resource URI
        :param data: data content to create/update
        :param options: dictionary with options and flags
        :return: An HTTP response object
        '''

        response = requests.put(URI,
                                data=data,
                                params=options,
                                cookies=self.jsession_id,
                                verify=self.verified_SSL_context,
                                timeout=100
                                )
        if response.status_code not in [200, 201]:
            raise XNATException('HTTP response: #%s%s%s' % (response.status_code, os.linesep, response.content))

        return response


    def _put_file(self, URI, filename, options=None):
        '''
        Creates or updates an XNAT resource with file data (XML)
        :param URI: XNAT resource URI
        :param filename: file name to upload
        :param options: dictionary with options and flags
        :return: An HTTP response object
        '''

        with open(filename, 'rb') as f:
            response = requests.put(URI,
                                    params=options,
                                    cookies=self.jsession_id,
                                    verify=self.verified_SSL_context,
                                    timeout=100,
                                    files={os.path.basename(filename): f})

        if response.status_code != requests.codes.ok:
            raise XNATException('HTTP response: #%s%s%s' % (response.status_code, os.linesep, response.content))
        #else:
        #    self.log.info('Resource file (%s) created' %response.request.url)
        return response


    def delete_resource(self, URI, options=None):
        '''
        Deletes an XNAT entity (DELETE action)
        :param URI: XNAT resource URI
        :return: An HTTP response object
        '''

        response = requests.delete(URI,
                                   params=options,
                                   cookies=self.jsession_id,
                                   verify=self.verified_SSL_context,
                                   timeout=100
                                   )
        if response.status_code != requests.codes.ok:
            raise XNATException('HTTP response: #%s%s%s' % (response.status_code, os.linesep, response.content))

        self.log.info('Resource (%s) deleted' % self.host)

        return response


    def get_projects(self):
        '''Query XNAT for a list of available projects
        :return: A projectID-keyed dictionary containing project IDs, names and URIs
        '''

        URI = self.host + '/data/projects'
        options = {'columns' : 'ID,name,URI' }
        plist = self._query_data(URI, options)

        # parse the results
        projects = {}
        for project in plist :
            projects[project['ID']] = project

        return projects


    def get_project_users(self, projectID):
        '''Query XNAT for a list of users belonging to a given project
        :param projectID: XNAT identifier of the project
        :return: A loginID-keyed dictionary containing project users information fields
        '''

        URI = self.host + '/data/projects/%s/users'%projectID
        ulist = self._query_data(URI)

        # parse the results
        users = {}
        for user in ulist :
            users[user['login']] = user

        return users


    def get_project_pipelines(self, projectID):
        '''Query XNAT for a list of enabled pipelines from a given project
        :param projectID: XNAT identifier of the project
        :return: A pipelineID-keyed dictionary containing project pipelines information fields
        '''

        URI = self.host + '/data/projects/%s/pipelines'%projectID
        plist = self._query_data(URI)

        # parse the results
        pipelines = {}
        for pipeline in plist :
            pipelines[pipeline['Name']] = pipeline

        return pipelines


    def get_project_aliases(self, projectID):
        '''Query XNAT for a list of alias names for a project
        :param projectID: XNAT identifier of the project
        :return: A list of alias name-strings for the given project
        '''

        URI = self.host + '/data/projects'
        data = self._query_data(URI, {'ID':projectID, 'columns':'alias'})

        # parse the results
        return [item['alias'] for item in data if item['alias'] ]


    def get_subjects(self, projectID=None, options=None):
        '''Query XNAT for a list of subjects
        :param projectID: XNAT ID of the project to filter subjects by (optional)
        :param options: dictionary with options
        :return: A subjectID-keyed dictionary containing subject IDs, labels, URI and stuff
        '''

        if projectID :
            URI = self.host + '/data/projects/%s/subjects'%projectID
        else :
            URI = self.host + '/data/subjects'

        if not options :
            options = {}

        slist = self._query_data(URI, options)

        # parse the results
        subjects = {}
        for subject in slist :
            subjects[subject['ID']] = subject

        return subjects


    def get_experiments(self, projectID=None, options=None):
        '''Query XNAT for a list of experiments
        :param projectID: XNAT ID of the project to filter experiments by (optional)
        :param options: dictionary with options
        :return: A experimentID-keyed dictionary containing sessions info
        '''

        root_uri = self.host + '/data'
        if projectID :
            root_uri = root_uri + '/projects/%s' % projectID
        URI = root_uri + '/experiments'

        if not options :
            options = {}

        if options.get('columns') :
            if 'ID' not in options['columns'].split(',') :
                options['columns'] += ',ID'
        else:
            options['columns'] = 'ID'

        elist = self._query_data(URI, options)

        # parse the results
        experiments = {}
        for exp in elist :
            experiments[exp['ID']] = exp

        return experiments


    def get_subject_experiments(self, projectID, subject, options=None):
        '''Query XNAT for experiments from a given Project and Subject
        :param projectID: XNAT ID of the project to filter experiments by (optional)
        :param subject: XNAT ID (or its label within the project!) of the subject to filter experiments by (optional)
        :param options: dictionary with options
        :return: A experimentID-keyed dictionary containing sessions info
        '''

        URI = self.host + '/data/projects/%s/subjects/%s/experiments'%(projectID,subject)

        if not options :
            options = {}

        if options.get('columns') :
            if 'ID' not in options['columns'].split(',') :
                options['columns'] += ',ID'
        else:
            options['columns'] = 'ID'

        elist = self._query_data(URI, options)

        # parse the results
        experiments = {}
        for exp in elist :
            experiments[exp['ID']] = exp

        return experiments


    def get_mrsessions(self, projectID=None, options=None):
        '''Query XNAT for a list of MRI imaging sessions
        :param projectID: XNAT ID of the project to filter experiments by (optional)
        :param options: dictionary with options
        :return: A experimentID-keyed dictionary containing sessions info
        '''

        if not options :
            options = {}
        options['xsiType'] = 'xnat:mrSessionData'

        return self.get_experiments(projectID,options=options)


    def get_petsessions(self, projectID=None, options=None):
        '''Query XNAT for a list of PET imaging sessions
        :param projectID: XNAT ID of the project to filter experiments by (optional)
        :param options: dictionary with query options (optional)
        :return: A experimentID-keyed dictionary containing sessions info
        '''

        if not options:
            options = {}
        options['xsiType'] = 'xnat:petSessionData'

        return self.get_experiments(projectID, options=options)


    def get_scans(self, experimentID, options=None):
        '''Query XNAT for a list of scans on an Image Session experiment
        :param experimentID: XNAT ID of the experiment to get scans from
        :param options: dictionary with query options (optional)
        :return: A scanID-keyed dictionary containing scans info
        '''

        URI = self.host + '/data/experiments/%s/scans' %experimentID

        if not options:
            options = {}

        #options['xsiType'] = 'xnat:mrScanData'

        if options.get('columns') :
            if 'ID' not in options['columns'].split(',') :
                options['columns'] += ',ID'
        else:
            options['columns'] = 'ID'

        slist = self._query_data(URI, options)

        # parse the results
        scans = {}
        for scan in slist :
            scans[scan['ID']] = scan

        return scans


    def get_mrscans(self, experimentID, options=None):
        '''Query XNAT for a list of MR-only scans on an Image Session experiment
        :param experimentID: XNAT ID of the experiment to get scans from
        :param options: dictionary with query options (optional)
        :return: A scanID-keyed dictionary containing scans info
        '''

        if not options:
            options = {}
        options['xsiType'] = 'xnat:mrScanData'

        return self.get_scans(experimentID,options)


    def get_petscans(self, experimentID, options=None):
        '''Query XNAT for a list of PET-only scans on an Image Session experiment
        :param experimentID: XNAT ID of the experiment to get scans from
        :param options: dictionary with query options (optional)
        :return: A scanID-keyed dictionary containing scans info
        '''

        if not options:
            options = {}
        options['xsiType'] = 'xnat:petScanData'

        return self.get_scans(experimentID,options)


    def get_scan_resources(self, experimentID, scanID='ALL', options=None):
        '''Query XNAT for a list of Scan(s) Resources of a given ImageSession
        :param experimentID: XNAT ID of the experiment to list data from
        :param scanID: Specific scan to list resources from
        :param options: dictionary with options
        :return: A resourceID-keyed dictionary containing scan resources info
        '''

        URI = self.host + '/data/experiments/%s/scans/%s/resources' %(experimentID,scanID)

        if not options:
            options = {}

        rlist = self._query_data(URI, options)

        # parse the results
        scan_resources = {}
        for resource in rlist:
            #scan_resources[(resource['cat_id'],resource['label'])] = resource
            scan_resources[resource['xnat_abstractresource_id']] = resource

        return scan_resources


    def get_experiment_resources(self, experimentID, options=None):
        '''Query XNAT for a list of Resources of a given Experiment
        :param experimentID: XNAT ID of the experiment to list resources from
        :param options: dictionary with options
        :return: A resourceID-keyed dictionary containing scan resources info
        '''

        URI = self.host + '/data/experiments/%s/resources' %(experimentID)

        if not options:
            options = {}

        rlist = self._query_data(URI, options)

        # parse the results
        resources = {}
        for resource in rlist:
            resources[resource['xnat_abstractresource_id']] = resource

        return resources


    def get_experiment_labels(self, experimentID):
        '''Query XNAT for a list of labels and IDs for a given Experiment
        :param experimentID: XNAT ID of the experiment to list labels/IDs from
        :return: A dictionary with the Project, Subject and Experiment labels and IDs
        '''

        e_URI = self.host + '/data/experiments'
        e_options = {'ID': experimentID,
                   'columns': 'ID,label,project,subject_ID',
                   'format': 'json'}
        e_list = self._query_data(e_URI, e_options)

        # Perform an extra query to fetch the Subject label (not available at Experiment level!)
        s_URI = self.host + '/data/subjects'
        s_options = {'ID': e_list[0]['subject_ID'],
                   'columns': 'label',
                   'format': 'json'}
        s_list = self._query_data(s_URI, s_options)

        # populate the output dict structure
        labels = {}
        labels['project'] = e_list[0]['project']
        labels['session'] = e_list[0]['label']
        labels['sessionID'] = e_list[0]['ID']
        labels['subjectID'] = e_list[0]['subject_ID']
        labels['subject'] = s_list[0]['label']

        return labels


    def get_scan_resource_files(self, experimentID, scanID, resourceID=None, options=None):
        '''Query XNAT for a list of Scan resource files of a given ImageSession
        :param experimentID: XNAT ID of the experiment to list resource files from
        :param scanID: Specific scan(s) to list files from (multiple scanIDs as comma-seppareted values accepted)
        :param resourceID: Specific resource collection to list files from (optional)
        :param options: dictionary with options
        :return: A URI-keyed dictionary containing scan resources info
        '''

        if resourceID :
            URI = self.host + '/data/experiments/%s/scans/%s/resources/%s/files' % (experimentID, scanID, resourceID)
        else :
            URI = self.host + '/data/experiments/%s/scans/%s/files' % (experimentID, scanID)

        if not options:
            options = {}

        flist = self._query_data(URI, options)

        # parse the results
        resource_files = {}
        for f in flist:
            resource_files[f['URI']] = f

        return resource_files


    def get_experiment_resource_files(self, experimentID, resourceID=None, options=None):
        '''Query XNAT for a list of Experiment resource files
        :param experimentID: XNAT ID of the experiment to list resource files from
        :param options: dictionary with options
        :param resourceID: Specific resource collection to list files from (optional)
        :return: A URI-keyed dictionary containing scan resources info
        '''

        if resourceID :
            URI = self.host + '/data/experiments/%s/resources/%s/files' % (experimentID, resourceID)
        else :
            URI = self.host + '/data/experiments/%s/files' % (experimentID)

        if not options:
            options = {}

        flist = self._query_data(URI, options)

        # parse the results
        resource_files = {}
        for f in flist:
            resource_files[f['URI']] = f

        return resource_files


    def download_resource(self, URI, options=None):
        '''
        Retrieves resource from XNAT (GET action) as stream
        :param URI: XNAT resource URI
        :param options: dictionary with query options and flags
        :return: Raw data structure object (string formatted data chunk)
        '''

        response = requests.get(URI,
                                stream=True,
                                params=options,
                                cookies=self.jsession_id,
                                verify=self.verified_SSL_context,
                                timeout=100
                                )

        if response.status_code != requests.codes.ok:
            raise XNATException('HTTP response: #%s%s%s' % (response.status_code, os.linesep, response.content))

        return response.content


    def get_dicom_dump(self, projectID, experimentID, scanID=None, tags_list=None):
        '''
        Parses the header of a random DICOM file and returns back its content
        :param projectID: XNAT project where DICOMs belong to
        :param experimentID: XNAT experiment where DICOMs belong to
        :param scanID: XNAT scan where DICOMs belong to (optional)
        :param tag_list: list of DICOM tag codes to parse and dump
        :return: List of dictionaries representing DICOM header attributes (tags) and its values
        '''

        source = '/archive/projects/%s/experiments/%s' % (projectID, experimentID)
        if scanID :
            source += '/scans/%s' %scanID

        URI = self.host + '/REST/services/dicomdump'
        options = { 'format' : 'json', 'src' : source }
        if tags_list and isinstance(tags_list, list):
            options['field'] = tags_list

        dump = self._query_data(URI, options)

        return dump
