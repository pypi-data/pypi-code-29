import json
from os.path import abspath, join
from tempfile import mkdtemp
import falcon
from sge.submit import JobRequest
from sge.status import get_job_detail, get_job_status
import sge_client.io.jobarchive
import sge_server

class JobCollection(object):
    def __init__(self, config):
        self.config = config

    def on_post(self, req, resp):
        request_body = json.load(req.bounded_stream)
        environment = request_body.pop('environment', {})
        environment['SCRIPT'] = "./" + request_body.pop('command')
        environment['ARCHIVE_DIR'] = self.config.completed_files_root
        environment.update(self.config.script_env.dict())
        package = request_body.pop('package')
        working_dir = mkdtemp(dir=self.config.work_root)
        qsub = self.config.qsub_settings.copy()
        output_dir = qsub.pop('output_dir', working_dir)
        sge_client.io.jobarchive.extract_job(package, working_dir)
        job_request = JobRequest(command=self.config.script_wrapper,
                                 environment=environment,
                                 output_dir=output_dir,
                                 working_directory=working_dir, **request_body, **qsub)
        job_id = job_request.submit()
        resp.body = json.dumps(dict(job_id=job_id))
        resp.status = falcon.HTTP_CREATED

class JobItem(object):
    def __init__(self, config):
        self.config = config

    def on_get(self, req, resp, job_id):
        detail = get_job_detail(job_id)
        if detail:
            detail = detail.to_dict()
            detail['status'] = get_job_status(job_id)
            resp.content_type = 'application/json'
            resp.body = json.dumps(detail)
            resp.status = falcon.HTTP_OK
        else:
            resp.body = json.dumps(dict(job_id=job_id, status='not_found'))
            resp.status = falcon.HTTP_NOT_FOUND

class DefaultRoute(object):
    def on_get(self, req, resp):
        resp.body = json.dumps({
            'status': 200,
            'application': "Remote SGE",
            'message' : "Unauthorized use is forbiddden."
        })
        resp.status = falcon.HTTP_200
