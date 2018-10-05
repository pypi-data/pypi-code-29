"""Streamr infrastructure Pull Request Laundry Mat.

Usage:
  laundromat (-c FILE | -a AGE -d DOCKER -i INTERVAL -b BUCKET_PREFIX)
  laundromat (-h | --help)
  laundromat --version

Options:
  -h --help                                         # Show this screen.
  -c FILE --config=FILE                             # Path to file
  -d DOCKER --docker=DOCKER                         # Docker image
  -a AGE --max_age=AGE                              # Max age in days of a PR infrastructure [default: 5].
  -i INTERVAl --interval=INTERVAL                   # Interval in hours to check age of infrastructure  [default: 10]
  -b BUCKET_PREFIX --bucket_prefix=BUCKET_PREFIX    # Prefix of buckets to check

"""

import logging
import os
import traceback
from time import sleep
import datetime
import boto3
from botocore.exceptions import ClientError
from docopt import docopt
import docker
from laundromat.configuration import Config, load_config

__version__ = "0.0.9"
logger = logging.getLogger()

s3_resource = None
s3_client = None
cw_client = None
client = None


def get_buckets(prefix: str) -> list:
    """
    Gets buckets filtered by prefix
    :param prefix:
    :return:
    """
    buckets = []
    for bucket in s3_resource.buckets.all():
        if bucket.name.startswith(prefix):
            buckets.append(bucket.name)
    logger.info("Pull request Marketplace infrastructures: %d", len(buckets))
    return buckets


def is_valid(bucket_name: str, max_age: int) -> bool:
    """
    Get creation dat of index.html and compare to max_age
    :param bucket_name:
    :param max_age:
    :return:
    """
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)

    for content in bucket.objects.all():
        if content.key == "index.html":
            present = datetime.datetime.now()
            max_date = content.last_modified + datetime.timedelta(days=max_age)
            return present < max_date.replace(tzinfo=None)
    # if there is no index.html file then the bucket is not valid
    return False


def destroy_infra(docker_image: str, bucket_name: str):
    client.login(username=os.environ.get("DOCKER_USER", None), password=os.environ.get("DOCKER_PASSWORD", None),
                 email=os.environ.get("DOCKER_EMAIL", None))
    cmd = ["~/.local/bin/aws s3 cp --region eu-west-1 s3://" + bucket_name + "/terraform.tfstate .",
           "~/.local/bin/aws s3 rm --region eu-west-1 s3://" + bucket_name + " --recursive", "terraform init",
           "terraform destroy -auto-approve -var bucket_name=" + bucket_name + " -var waf_acl_id=0"]

    full_command = "'(" + ";".join(cmd) + ")'"
    logger.info("Start Destroying %s", bucket_name)
    container = client.containers.create(docker_image,
                                         environment=[
                                             "AWS_ACCESS_KEY_ID=" + os.environ.get("TERRA_AWS_ACCESS_KEY_ID", None),
                                             "AWS_SECRET_ACCESS_KEY=" + os.environ.get("TERRA_AWS_SECRET_ACCESS_KEY",
                                                                                       None),
                                             "AWS_DEFAULT_REGION=" + os.environ.get("TERRA_AWS_DEFAULT_REGION",
                                                                                    None)],
                                         command=full_command)
    container.start()
    result = container.wait()
    logger.info("Destruction of %s complete!", bucket_name)
    logger.debug(result)
    try:
        # check if bucket was removed
        objs = s3_client.list_objects_v2(Bucket=bucket_name)
    except ClientError:
        if result["StatusCode"] == 0:
            return True

    return False


def start(config: tuple):
    """
    Start the execturion of the service
    :param config:
    :return:
    """
    while True:
        old_infra = 0
        destroyed_infra = 0
        unsucessfull_destroyed_infra_meta = []

        for bucket in get_buckets(config.bucket_prefix):
            try:
                if not is_valid(bucket, config.max_age):
                    old_infra += 1
                    if destroy_infra(config.docker, bucket):
                        destroyed_infra += 1
                    else:
                        unsucessfull_destroyed_infra_meta.append(bucket)
            except [KeyError, ClientError]:
                old_infra += 1
                unsucessfull_destroyed_infra_meta.append(bucket)
                traceback.print_exc()

        logger.info("Expired pull request marketplace infrastructure: %d", old_infra)
        logger.info("Successfully destroyed pull request marketplace infrastructure: %d",
                    old_infra - len(unsucessfull_destroyed_infra_meta))
        if len(unsucessfull_destroyed_infra_meta) != 0:
            logger.warning("Failed destroyed pull request marketplace infrastructure: %s",
                           unsucessfull_destroyed_infra_meta)
        if config.metrics:
            cw_client.put_metric_data(
                Namespace='devops',
                MetricData=[
                    {
                        'MetricName': 'laundromat',
                        'Dimensions': [
                            {
                                'Name': 'Infrastructure',
                                'Value': 'expired_infra'
                            }
                        ],
                        'Value': old_infra,
                        'Counts': [
                            1
                        ],
                        'Unit': 'Count'
                    },
                    {
                        'MetricName': 'laundromat',
                        'Dimensions': [
                            {
                                'Name': 'Infrastructure',
                                'Value': 'suc_destroy'
                            }
                        ],
                        'Value': old_infra - len(unsucessfull_destroyed_infra_meta),
                        'Counts': [
                            1
                        ],
                        'Unit': 'Count'
                    },
                    {
                        'MetricName': 'laundromat',
                        'Dimensions': [
                            {
                                'Name': 'Infrastructure',
                                'Value': 'fail_destroy'
                            },
                        ],
                        'Value': len(unsucessfull_destroyed_infra_meta),
                        'Counts': [
                            1
                        ],
                        'Unit': 'Count'
                    }
                ]
            )
        sleep(config.interval)


def main():
    global s3_resource
    global s3_client
    global cw_client
    global client

    arguments = docopt(__doc__, version='Marketplace PR Laundromat' + __version__)
    if arguments["--config"]:
        config = load_config(arguments["--config"])
    else:
        config = Config(docker=arguments["--docker"], max_age=int(arguments["--max_age"]),
                        interval=int(arguments["--interval"]),
                        bucket_prefix=arguments["--bucket_prefix"])

    logging.basicConfig(filename="/var/log/laundromat/laundromat.log",
                        filemode='a',
                        format='%(asctime)s-%(name)s-%(levelname)s: %(message)s',
                        level=config.log_level)

    s3_resource = boto3.resource('s3')
    s3_client = boto3.client('s3')
    cw_client = boto3.client('cloudwatch', region_name="eu-west-1")
    client = docker.from_env()

    logger.info("Starting Laundromat")
    logger.debug("Config:")
    logger.debug(config)

    start(config)


if __name__ == '__main__':
    main()
