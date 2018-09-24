from django.test import TestCase
from concierge_paas_plugin.api import create_profile, queryprofile
from concierge_paas_plugin.models import Configuration


class CreateProfileTest(TestCase):
    def setUp(self):
        self.configuration = Configuration(token='045d5617bbbd13c523be1fa6b86486e3c8a57b00', end_point="http://localhost:8001/protected", default=True, trigger=True)
        self.configuration.save()

    def test_createBasicProfile(self):
        userid = 123

        create_profile(userid, "username", "user@user.com")

        response = queryprofile(123)
        print(response)
        # self.assertEqual(response, "12564")