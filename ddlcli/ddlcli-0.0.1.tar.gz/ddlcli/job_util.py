import json
import uuid
from os.path import isfile, isdir

import requests

from ddlcli.constants import CODE_DIR_NAME
from ddlcli.s3_util import create_s3_client, upload_dir_to_s3, upload_file_to_s3


class TokenAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = 'Token ' + self.token
        return r


def submit_task(job_data, s3_data, auth, master_endpoint):
    validate_tf_param(job_data)

    # upload binary to s3
    job_s3_uuid = str(uuid.uuid4())
    code_location_s3, dataset_location_s3 = upload_to_s3(
        job_data["model_location"], job_data["dataset"]["dataset_location"], job_s3_uuid, s3_data)

    print("job uuid on s3 is: {}".format(job_s3_uuid))
    job_data["model_location"] = code_location_s3
    job_data["dataset"]["dataset_location"] = dataset_location_s3

    print("model_location: {0}, dataset_location: {1}".format(job_data["model_location"], job_data["dataset"]["dataset_location"]))

    request_body = {
        'parameters': json.dumps(job_data)
    }

    create_task_request = requests.post("{}/api/v1/user/tf/job/".format(master_endpoint), data=request_body, auth=auth)
    create_task_resp = json.loads(create_task_request.text)
    print("Status: {}".format(create_task_request.status_code))
    if not create_task_request.ok:
        print("Error: {}".format(create_task_resp.get("error")))
        print("Message: {}".format(create_task_resp.get("message")))
        exit(-1)

    print("job_uuid: {}".format(create_task_resp.get("job_uuid")))
    print("job_type: {}".format(create_task_resp.get("job_type")))

def login_user(data, master_endpoint):
    login_request = requests.post("{}/api/v1/user/login/".format(master_endpoint), data=data)
    login_response = json.loads(login_request.text)

    if not login_request.ok:
        print("Error: {}".format(login_response.get("error")))
        if login_request.status_code == 401:
            r = requests.post("{}/api/v1/user/register/".format(master_endpoint), data=data)
            print("Status: {}".format(r.status_code))
            resp = json.loads(r.text)
            if r.ok == False:
                print("Error: {}".format(resp.get("error")))
                exit(-1)

        login_request = requests.post("{}/api/v1/user/login/".format(master_endpoint), data=data)
        login_response = json.loads(login_request.text)

    auth_token = login_response.get('auth_token', None)
    return TokenAuth(auth_token)

def validate_tf_param(tf_param):
    model_location = tf_param["model_location"]
    if not isdir(model_location) and not isfile(model_location):
        raise ValueError("cannot find model path {}".format(model_location))
    else:
        with open("./.model", "w") as f:
            f.write(model_location)

    dataset_location = tf_param["dataset"]["dataset_location"]
    if not isdir(dataset_location) and not isfile(dataset_location):
        raise ValueError("cannot find dataset path {}".format(dataset_location))

    if tf_param["worker_required"] <= 0:
        raise ValueError("number of workers cannot be less than or equal to 0")

def upload_to_s3(code_location, dataset_location, uuid, s3_data):
    client = create_s3_client(s3_data["region_name"], s3_data["aws_access_key_id"], s3_data["aws_secret_access_key"])
    code_location_s3 = upload_dir_to_s3(code_location, s3_data["bucket_name"], CODE_DIR_NAME, uuid, client)
    if isfile(dataset_location):
        file_name = "{0}/{1}".format(uuid, "dataset")
        dataset_location_s3 = upload_file_to_s3(dataset_location, s3_data["bucket_name"], file_name, client)
    else:
        dataset_location_s3 = upload_dir_to_s3(dataset_location, s3_data["bucket_name"], "dataset", uuid, client)

    return code_location_s3, dataset_location_s3