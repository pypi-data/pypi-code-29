from kpc_connector_utils.common.singleton import singleton

import json
import base64
import logging


@singleton
class ContextWrapper:

    def __init__(self):
        self._logger = logging.getLogger()
        self._logger.setLevel(logging.INFO)
        self._context = None

    def get_context(self):
        return self._context

    def set_context(self, context):
        self._context = context

    def is_context_set(self):
        return self._context is not None

    def create_custom_client_context(self):
        custom_client_ct = self._get_custom_client_context()

        custom = custom_client_ct.get('custom')
        req_ct = custom.get('request_context')
        if custom and req_ct:
            self._logger.info('request_context_info: {}'.format(json.dumps(req_ct)))

        prior_ct = custom.get('prior_request_context')
        if custom and prior_ct:
            self._logger.info('prior_request_context: {}'.format(json.dumps(prior_ct)))

        return ContextWrapper.encode_req(custom_client_ct)

    def _get_custom_client_context(self):
        custom_client_ct = {'custom': {}}
        if not self._context:
            return custom_client_ct

        custom_client_ct['custom']['request_context'] = self._extract_context_info()

        prior = self._extract_prior_context_info()
        if prior:
            custom_client_ct['custom']['prior_request_context'] = prior

        return custom_client_ct

    def _extract_context_info(self):
        return {
            'function_name': self._context.function_name,
            'function_version': self._context.function_version,
            'invoked_function_arn': self._context.invoked_function_arn,
            'aws_request_id': self._context.aws_request_id,
            'log_group_name': self._context.log_group_name,
            'log_stream_name': self._context.log_stream_name
        }

    def _extract_prior_context_info(self):
        if not self._context:
            return None

        if not self._context.client_context:
            return None

        custom_ct = self._context.client_context.custom
        if not custom_ct:
            return None

        if not custom_ct.get('request_context'):
            return None

        return custom_ct.get('request_context')

    @staticmethod
    def encode_req(enc_str):
        return base64.b64encode(json.dumps(enc_str).encode()).decode('utf-8')
