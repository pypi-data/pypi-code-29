"""Contains constants for the program."""

# How many seconds to wait for a request response
DEFAULT_TIMEOUT_SECONDS = 90


# Useful HTTP status codes (nice and verbose :D)
HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_202_ACCEPTED = 202


# Options for the task instance's state field
CREATED = 'created'
PUBLISHED = 'published'
RUNNING = 'running'
SUCCESSFUL = 'successful'
FAILED = 'failed'
TERMINATED = 'terminated'
