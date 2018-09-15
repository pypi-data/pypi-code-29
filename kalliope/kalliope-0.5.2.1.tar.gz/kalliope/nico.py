# coding: utf8
import logging
import uuid
from threading import Thread

import requests

from kalliope.neurons.ansible_playbook import Ansible_playbook

logging.basicConfig()
logger = logging.getLogger("kalliope")
logger.setLevel(logging.DEBUG)
# from kalliope import BrainLoader, SettingLoader, SynapseLauncher
#
# brain = BrainLoader().brain
# settings = SettingLoader().settings
# #
# order = "say one example"
# # order = "remind me to call mom in three seconds"
# SynapseLauncher.run_matching_synapse_from_order(order_to_process=order,
#                                                 brain=brain,
#                                                 settings=settings)


# parameters = {
#     "task_file": "test.yml",
#     "sudo": True,
#     "sudo_user": "root",
#     "sudo_password": "azerty"
# }
#
# Ansible_playbook(**parameters)

GA_TRACKING_ID = "UA-124800612-1"


class GoogleTracking(Thread):
    """
    send hit to Google Analytics
    allow to anonymously evaluate the global usage of Kalliope app by users
    """

    def __init__(self, **kwargs):
        super(GoogleTracking, self).__init__()
        self.category = kwargs.get("category")
        self.action = kwargs.get("action")
        self.label = kwargs.get("label", None)
        self.value = kwargs.get("value", 0)
        self.kalliope_version = kwargs.get("kalliope_version", 0)

    def run(self):
        self.track_event(self.kalliope_version, self.category, self.action, self.label, self.value)

    @staticmethod
    def track_event(cid, kalliope_version, category, action, label=None, value=0):
        # allowed parameters: https://developers.google.com/analytics/devguides/collection/protocol/v1/parameters
        data = {
            'v': '1',  # API Version.
            'tid': GA_TRACKING_ID,  # Tracking ID / Property ID.
            'cid': cid,  # unique user id
            'an': "kalliope",
            'av': kalliope_version,
            'ds': 'api',
            't': 'event',  # Event hit type.
            'ec': category,  # Event category.
            'ea': action,  # Event action.
            'el': label,  # Event label.
            'ev': value,  # Event value, must be an integer
        }
        try:
            response = requests.post(
                'http://www.google-analytics.com/collect', data=data)

        # If the request fails, this will raise a RequestException.
            response.raise_for_status()
        except Exception as e:
            logger.debug("[GoogleTracking] fail to send data: %s" % e)


my_cid = uuid.uuid4().hex

gt = GoogleTracking(cid=my_cid, kalliope_version="0.5.2", category='STT', action='STT call')
gt.start()


print("hello")
