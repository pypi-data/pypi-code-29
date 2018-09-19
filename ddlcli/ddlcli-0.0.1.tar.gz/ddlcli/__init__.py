import json
from os.path import basename
from os.path import splitext

import yaml

from ddlcli.job_util import submit_task, login_user


def submit_job(task_path, master_endpoint="http://dtf-masterserver-dev.us-west-1.elasticbeanstalk.com"):
    with open(task_path) as f:
        config = None
        filename, file_extension = splitext(basename(task_path))
        if file_extension == ".json":
            config = json.load(f)
        elif file_extension == ".yaml":
            config = yaml.load(f)
        else:
            raise ValueError("{} is not a valid config".format(str(f)))

    data = {
        'email': config["email"],
        'password': config["password"]
    }

    print("===========================================")
    print("Step 1: User login")
    print("===========================================")
    auth = login_user(data, master_endpoint)

    print("===========================================")
    print("Step 2: Submit task")
    print("===========================================")

    job_data = config["job_data"]
    s3_data = config['s3_data']

    submit_task(job_data, s3_data, auth, master_endpoint)
