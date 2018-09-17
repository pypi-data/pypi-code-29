from dataflows import Flow, PackageWrapper
from datapackage import Package
from datapackage_pipelines_ckanext import helpers as ckanext_helpers
import shutil
from os import path
import json
from oauth2client.client import OAuth2Credentials
from googleapiclient.discovery import build
from httplib2 import Http
from email.mime.text import MIMEText
from os import environ
import base64
from collections import defaultdict, deque
from utils import temp_loglevel


def flow(parameters, datapackage, resources, source_stats):
    config = ckanext_helpers.get_plugin_configuration('upload_via_email')
    data_path = config['data_path']
    credentials = OAuth2Credentials.from_json(config['gmail_token'])
    assert credentials and not credentials.invalid
    service = build('gmail', 'v1', http=credentials.authorize(Http()), cache_discovery=False)

    def get_ckan_log(datasets_messages, ckan_log_resource):
        last_created_datasets = deque(maxlen=10)
        stats = defaultdict(int)
        ckan_log_path = path.join(data_path, 'ckan_log', 'datapackage.json')
        if path.exists(ckan_log_path):
            yield from Package(ckan_log_path).get_resource('ckan-log').iter(keyed=True)
        successful_message_ids = set()
        for row in ckan_log_resource:
            if not row['dataset_name'] or row['dataset_name'] == '_':
                continue
            message_id = datasets_messages.get(row['dataset_name'])
            row['message_id'] = message_id
            if not row['error'] and message_id not in successful_message_ids:
                successful_message_ids.add(message_id)
                with open(path.join(data_path, 'attachments', message_id, 'message.json')) as f:
                    message = json.load(f)
                from_email = [header['value'] for header in message['payload']['headers'] if header['name'] == 'From'][0]
                row['from_email'] = from_email
                dataset_url = '{}/dataset/{}'.format(environ['CKAN_URL'], row['dataset_name'])
                last_created_datasets.append(dataset_url)
                message = MIMEText(config['success_message'].format(dataset_url=dataset_url))
                message['to'] = from_email
                message['from'] = config['success_message_from_email']
                message['subject'] = config['success_message_subject']
                message = {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode('utf-8')}
                with temp_loglevel():
                    service.users().messages().send(userId='me', body=message).execute()
                stats['update_created_datasets: sent emails'] += 1
            yield row
        shutil.rmtree(path.join(data_path, 'attachments'), ignore_errors=True)
        source_stats.update(**stats)
        source_stats['last created datasets'] = list(last_created_datasets)

    def update_created_datasets(package: PackageWrapper):
        for descriptor in datapackage['resources']:
            if descriptor.get('dpp:streaming'):
                resource = next(resources)
                if descriptor['name'] == 'messages-datasets':
                    datasets_messages = {row['dataset_name']: row['message_id'] for row in resource}
                elif descriptor['name'] == 'ckan-log':
                    ckan_log_resource = resource
                    ckan_log_descriptor = descriptor
        for resource in resources:
            for row in resource:
                pass
        ckan_log_descriptor['schema']['fields'] += [{'name': 'message_id', 'type': 'string'},
                                                    {'name': 'from_email', 'type': 'string'}]
        yield Package({'name': '_', 'resources': [ckan_log_descriptor]})
        yield get_ckan_log(datasets_messages, ckan_log_resource)


    return Flow(update_created_datasets)
