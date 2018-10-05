import re


BUNDLE_ITEM_KINDS = (
    'array',
    'boolean',
    'media',
    'null',
    'number',
    'object',
    'string'
)

MESSAGE_KINDS = (
    'confirm',
    'success',
    'error'
)

OPERATION_SCHEDULES = (
    'auto',
    'manual',
)

OPERATION_STATUSES = (
    'pending',
    'scheduling',
    'scheduled',
    'running',
    'failed',
    'cancelled',
    'successful'
)

WORK_REQUEST_STATUSES = (
    'pending',
    'accepted',
    'rejected',
    'failed'
)

CODENAME_RE = re.compile(r'^([a-z][a-z0-9_]*)\.([a-z][a-z0-9_]*)$')
