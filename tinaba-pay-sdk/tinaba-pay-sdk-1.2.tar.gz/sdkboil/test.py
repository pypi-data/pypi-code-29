import json

from sdkboil.apicontext import ApiContext
from unittest.mock import patch
from unittest import TestCase

"""
test_api_*_objects = {
    ACTION_NAMESPACE : {
        'body_params': {},
        'url_params': {},
        'exceptions': {},
        'receive_object': {},
        'query_params': {}
    }
}
"""


class MockResponse(object):
    def __init__(self, status, body):
        self.status_code = status
        self.body = body
        self.text = str(self.body)
        self.content = json.dumps(self.body).encode()

    def json(self):
        return self.body


class TestSDK(TestCase):
    factory = None
    test_api_post_objects = None
    test_api_get_objects = None
    test_api_update_objects = None
    test_api_delete_objects = None
    test_api_nonRESTful_objects = None

    def setUp(self):
        self.patch1 = patch('ch_sdk.actions.AuthenticatedAction.needs_auth', return_value=False)
        self.patch2 = patch('ch_sdk.actions.EventSendingAction.get_failure_hooks', return_value=[])
        self.patch3 = patch('ch_sdk.actions.EventSendingAction.get_presend_hooks', return_value=[])
        self.patch4 = patch('ch_sdk.actions.EventSendingAction.get_success_hooks', return_value=[])
        self.patch1.start()
        self.patch2.start()
        self.patch3.start()
        self.patch4.start()
        self.context = ApiContext({'mode': lambda: 'live',
                                   'version': 'v1',
                                   'url_template': '{hostname}{base_url}{route}',
                                   'live': {'timeout': 10,
                                            'credentials': {'client_id': 'mock_id', 'secret': 'mock_secret'},
                                            'cache_driver': 'redis',
                                            'redis': {
                                                'host': 'host',
                                                'port': 6379,
                                                'pwd': 'pwd',
                                                'token_key': 'key'},
                                            'hostname': 'https://localhost',
                                            'port': 80,
                                            'base_url': ''},

                                   })
        self.factory = TestSDK.factory(self.context)
        self.test_api_nonRESTful_objects = TestSDK.test_api_nonRESTful_objects
        self.test_api_get_objects = TestSDK.test_api_get_objects
        self.test_api_delete_objects = TestSDK.test_api_delete_objects
        self.test_api_update_objects = TestSDK.test_api_update_objects
        self.test_api_post_objects = TestSDK.test_api_post_objects
        self.to_patch = 'sdkboil.action.Request.send'

    def tearDown(self):
        self.patch1.stop()
        self.patch2.stop()
        self.patch3.stop()
        self.patch4.stop()

    def test_sdk_get_actions(self):
        for action_namespace in self.test_api_get_objects:
            print('Running Test for {}'.format(action_namespace))
            action = self.factory.make(action_namespace)
            action.url_params = self.test_api_get_objects[action_namespace]['url_params']
            action.query_params = self.test_api_get_objects[action_namespace]['query_params']
            with patch(self.to_patch,
                       return_value=MockResponse(200,
                                                 self.test_api_get_objects[action_namespace][
                                                     'receive_object'])) as mock_get:
                action.run()
                mock_get.assert_called_with()

    def test_sdk_post_actions(self):
        for action_namespace in self.test_api_post_objects:
            print('Running Test for {}'.format(action_namespace))
            action = self.factory.make(action_namespace)
            action.url_params = self.test_api_post_objects[action_namespace]['url_params']
            action.body_params = self.test_api_post_objects[action_namespace]['body_params']
            with patch(self.to_patch,
                       return_value=MockResponse(201, self.test_api_post_objects[action_namespace][
                           'receive_object'])) as mock_post:
                action.run()
                mock_post.assert_called_with()

    def test_sdk_delete_actions(self):
        for action_namespace in self.test_api_delete_objects:
            print('Running Test for {}'.format(action_namespace))
            action = self.factory.make(action_namespace)
            action.url_params = self.test_api_delete_objects[action_namespace]['url_params']
            action.query_params = self.test_api_delete_objects[action_namespace]['query_params']
            with patch(self.to_patch,
                       return_value=MockResponse(204, self.test_api_delete_objects[action_namespace][
                           'receive_object'])) as mock_delete:
                action.run()
                mock_delete.assert_called_with()

    def test_sdk_update_actions(self):
        for action_namespace in self.test_api_update_objects:
            print('Running Test for {}'.format(action_namespace))
            action = self.factory.make(action_namespace)
            action.url_params = self.test_api_update_objects[action_namespace]['url_params']
            action.query_params = self.test_api_update_objects[action_namespace]['query_params']
            action.body_params = self.test_api_update_objects[action_namespace]['body_params']
            with patch(self.to_patch,
                       return_value=MockResponse(200, self.test_api_update_objects[action_namespace][
                           'receive_object'])) as mock_update:
                action.run()
                mock_update.assert_called_with()

    def test_sdk_nonRESTful_actions(self):
        for action_namespace in self.test_api_nonRESTful_objects:
            print('Running Test for {}'.format(action_namespace))
            action = self.factory.make(action_namespace)
            action.url_params = self.test_api_nonRESTful_objects[action_namespace]['url_params']
            action.body_params = self.test_api_nonRESTful_objects[action_namespace]['body_params']
            action.query_params = self.test_api_nonRESTful_objects[action_namespace]['query_params']
            with patch(self.to_patch,
                       return_value=MockResponse(200, self.test_api_nonRESTful_objects[action_namespace][
                           'receive_object'])) as mock_action:
                action.run()
                mock_action.assert_called_with()

    def test_sdk_exceptions(self):
        global_objects = {**self.test_api_update_objects,
                          **self.test_api_get_objects,
                          **self.test_api_post_objects,
                          **self.test_api_delete_objects,
                          **self.test_api_nonRESTful_objects}
        for action_namespace in global_objects:
            print("Running Test exceptions for {}".format(action_namespace))
            action = self.factory.make(action_namespace)
            action.url_params = global_objects[action_namespace]['url_params']
            try:
                action.body_params = global_objects[action_namespace]['body_params']
            except KeyError:
                pass
            try:
                action.query_params = global_objects[action_namespace]['query_params']
            except KeyError:
                pass
            for key, value in global_objects[action_namespace]['exceptions'].items():
                with patch(self.to_patch,
                           return_value=MockResponse(key, {})) as mock_action:
                    with self.assertRaises(value):
                        action.compiled = False
                        action.run()
                        mock_action.assert_called_with()
