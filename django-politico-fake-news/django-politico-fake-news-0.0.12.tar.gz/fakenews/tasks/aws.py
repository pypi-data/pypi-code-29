import logging
import json

from fakenews.utils.aws import defaults, get_bucket
from celery import shared_task

logger = logging.getLogger('tasks')

CACHE_HEADER = str('max-age=300')


@shared_task(acks_late=True)
def publish_to_aws(filepath, data):
    bucket = get_bucket()

    bucket.put_object(
        Key=filepath,
        ACL=defaults.ACL,
        Body=json.dumps(data),
        CacheControl=CACHE_HEADER,
        ContentType='application/json'
    )

    logger.info('{} published to AWS.'.format(filepath))


@shared_task(acks_late=True)
def remove_from_aws(filepath):
    bucket = get_bucket()

    bucket.delete_objects(Delete={
        'Objects': [{
            'Key': filepath
        }]
    })

    logger.info('{} removed from AWS.'.format(filepath))
