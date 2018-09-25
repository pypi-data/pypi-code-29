from django.test import TransactionTestCase
from concierge_paas_plugin.api import create_profile, queryprofile
from concierge_paas_plugin.models import Configuration


class CreateProfileTest(TransactionTestCase):
    def setUp(self):
        self.configuration = Configuration(token='045d5617bbbd13c523be1fa6b86486e3c8a57b00', end_point="http://localhost:8001/protected", default=True, trigger=True)
        self.configuration.save()

        self.userId = 123456

    def tearDown(self):
        # rollback user
        pass

    def test_createBasicProfile(self):
        username = "custom_username"
        email = username + '@sometest.com'
        create_profile(self.userId, username, email)

        response = queryprofile(self.userId)
        self.assertTrue(username in str(response))

    def test_userAlreadyExist(selfs):
        pass