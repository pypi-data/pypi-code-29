"""
Plumbing for sending the local job to the remote.

Ultimately, a request needs to be sent to the server, with:

* name
* arguments
* job_files

"""

from os.path import basename
import re
import json
import requests
import falcon
import sge_client.io
import sge_client.io.database
from sge_client.io.jobarchive import package_job, extract_unencoded
from sge_client.util.string_to_int_list import string_to_int_list
import sge_client.client_config
from sge.io.config import load_config
import sge.status
import sge.control
# from sge.status import get_job_detail, get_job_status, SgeJobStateCode
# from sge.control import user_hold, suspend, terminate
from argparse import RawTextHelpFormatter
from sge.util.arg_parser import ArgParser
DEFAULT_ENDPOINT = "default"
parser = ArgParser(prog="remote_sge shuttle", formatter_class=RawTextHelpFormatter)

def parse_args():
    parser.add_argument('shuttle', help='The command being run.  Holds or suspends a job and' +
                        'submits it to the remote.')
    parser.add_argument('subcommand', help='Which action for the shuttle to perform. ' +
                        'Valid values are collect or submit.')
    parser.add_argument('job_ids', help='List of jobs to submit, in the form of 1-6,10,1000-2000.' +
                        ' Must be provided if subcommand is submit.', default='', nargs='?')
    parser.add_argument('-e', '--endpoint', help="Preconfigured named host to interact with",
                        default=DEFAULT_ENDPOINT)
    args = parser.parse_args()
    if args.subcommand not in ['collect', 'submit']:
        parser.error("subcommand must be either collect or submit.")
    if not args.job_ids and args.subcommand == "submit":
        parser.error("job_ids must be provided if subcommand is submit.")
    return args

def main():
    args = parse_args()
    if args.subcommand == "submit":
        submit(string_to_int_list(args.job_ids), endpoint=args.endpoint)
    else:
        collect(endpoint=args.endpoint)

class JobNotFound(dict):
    def __init__(self, job_id):
        super().__init__(status='not_found', job_id=job_id)

def get_remote_detail(job_id, endpoint=DEFAULT_ENDPOINT):
    config = sge_client.client_config.ClientConfig(load_config(), endpoint)
    url = '%s://%s:%s/jobs/%s' % (
        config.request_schema, config.host, config.port, job_id)
    response = requests.get(url, **config.ssl_config)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return JobNotFound(job_id)
    else:
        raise Exception("Error getting job detail.  HTTP Status: %s.\n\nBody: %s" %
                        (response.status_code, response.text))

def submit(job_ids, endpoint=DEFAULT_ENDPOINT):
    config = sge_client.client_config.ClientConfig(load_config(), endpoint)
    remote_job_id = None
    with requests.Session() as session:
        with sge_client.io.database.Db() as database:
            session.verify = config.ca_certificate
            session.cert = config.client_key_config
            url = '%s://%s:%s/jobs' % (
                config.request_schema, config.host, config.port)
            request = requests.Request('POST', '%s://%s:%s/jobs' % (
                config.request_schema, config.host, config.port))
            prepared = session.prepare_request(request)

            for job_id in job_ids:
                status = sge.status.get_job_status(job_id)
                print("Status %s, fool!" % status)
                if status in [sge.status.SgeJobStateCode.RUNNING,
                              sge.status.SgeJobStateCode.QUEUED_HELD]:
                    sge.control.suspend(job_id)
                elif status in [sge.status.SgeJobStateCode.QUEUED_ACTIVE,
                                sge.status.SgeJobStateCode.QUEUED_HELD]:
                    sge.control.user_hold(job_id)
                else:
                    print("Not shuttling job %s because it could not be found or is in an unknown state." % job_id)
                    continue

                job_detail = sge.status.get_job_detail(job_id)
                prepared.prepare_body(None, None, {
                    'name' : job_detail.name,
                    'command' : basename(job_detail.command_path),
                    'arguments' : job_detail.arguments,
                    'environment' : job_detail.environment,
                    'package' : package_job(job_detail.command_path,
                                            working_dir=job_detail.working_dir,
                                            mask=job_detail.name + "*",
                                            filespec=job_detail.environment.get('FILESPEC', None))
                })
                response = session.send(prepared)
                if response.status_code != 201:
                    print("Job %s unsuccessful.  Expected http %s, received %s.  Server's response was %s." %
                        (job_id, falcon.HTTP_201, response.status_code, response.text))
                    continue
                else:
                    database.insert(job_id, response.json()['job_id'], job_detail.working_dir)
                    # We're mostly just returning the remote job id for debugging purposes.
                    remote_job_id = response.json()['job_id']
    return remote_job_id

JOB_ID_RE = re.compile(r"\d+")

def job_complete(job_id, endpoint=DEFAULT_ENDPOINT):
    config = sge_client.client_config.ClientConfig(load_config(), endpoint)
    url = ('%s://%s:%s/jobs/complete/%s.tgz' %
           (config.request_schema, config.host, config.port, job_id))
    response = requests.head(url, **config.ssl_config)
    return response.status_code == 200

def collect_one(database, remote_id=None, local_id=None, endpoint=DEFAULT_ENDPOINT):
    config = sge_client.client_config.ClientConfig(load_config(), endpoint)
    if remote_id:
        job_info = database.find_by_remote_job_id(remote_id)
        if job_info == None:
            print('Job %s not found locally.  Moving on.' % remote_id)
            return
    else:
        job_info = database.find_by_local_job_id(local_id)

    url = ('%s://%s:%s/jobs/complete/%s.tgz' %
           (config.request_schema, config.host, config.port, job_info['remote_id']))
    response = requests.get(url, stream=True, **config.ssl_config)

    if response.status_code == 200:
        print(response.headers)

        extract_unencoded(response.raw, job_info['local_wd'])
        requests.delete(url, **config.ssl_config)
        sge.control.terminate(job_info['local_id'])
        database.delete(job_info)
        print("Retrieved data for local job id %s" % job_info['local_id'])
    else:
        print("Server responded with %s" % response.status_code)
        print(response.text)


def collect(endpoint=DEFAULT_ENDPOINT):
    config = sge_client.client_config.ClientConfig(load_config(), endpoint)

    with requests.Session() as session:
        with sge_client.io.database.Db() as database:
            session.verify = config.ca_certificate
            session.cert = config.client_key_config
            response = session.get('%s://%s:%s/jobs/complete/' %
                                   (config.request_schema, config.host, config.port))
            print(response.content)
            for job_id in {JOB_ID_RE.match(j['name'])[0] for j in response.json()}:
                collect_one(database, remote_id=job_id)
