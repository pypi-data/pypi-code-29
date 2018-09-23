DEFAULT_IMAGE = 'orihoch/dataflows-serverless:9'

WAIT_FOR_SECONDARIES_DELAY_SECONDS = .1
WAIT_FOR_PRIMARY_STEP_COMPLETE_DELAY_SECONDS = .1
WAIT_FOR_PRIMARY_JOB_COMPLETE_DELAY_SECONDS = .1
K8S_GET_POD_NAME_DELAY_SECONDS = .1

PRIMARY_STEP_COMPLETE_FILE_TEMPLATE = '{workdir}/primary/{step_idx}/primary-step-complete.json'
SECONDARY_OUTPUT_DATAPACKAGE_PATH_TEMPLATE = '{workdir}/secondaries/{step_idx}/secondary-{secondary}'
SECONDARY_OUTPUT_DATAPACKAGE_FILE_TEMPLATE = (SECONDARY_OUTPUT_DATAPACKAGE_PATH_TEMPLATE
                                              + '/datapackage.json')
SECONDARY_STATS_FILE_TEMPLATE = '{workdir}/secondaries/{step_idx}/secondary-{secondary}/stats.json'
PRIMARY_INPUT_DATAPACKAGE_PATH_TEMPLATE = '{workdir}/primary/{step_idx}/input'
PRIMARY_INPUT_DATAPACKAGE_FILE_TEMPLATE = (PRIMARY_INPUT_DATAPACKAGE_PATH_TEMPLATE
                                           + '/datapackage.json')

DEFAULT_SERVERLESS_WORKDIR = '/var/dataflows-serverless'

NFS_CODE_DIRECTORY = '/exports/code'
PRIMARY_POD_OUTPUT_DATA_DIR = '/var/dataflows-serverless'
