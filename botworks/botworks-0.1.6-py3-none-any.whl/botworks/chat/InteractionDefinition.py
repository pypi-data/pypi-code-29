import logging
import time
from typing import List

from botworks.chat.Response import IResponse
from botworks.chat.Trigger import Trigger
from botworks.config_constants import LOG_LEVEL
from botworks.slack.Payload import Payload

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class InteractionDefinition:
    def __init__(self, trigger: Trigger, response: IResponse, cooldown_duration=600, mod_exempt=True):
        self.response = response
        self.trigger = trigger
        self.cooldown_duration = cooldown_duration
        self.cooldown_end = 0
        self.modExempt = mod_exempt
        self.conf = {}

    def finalize(self, config):
        self.conf = config
        log.setLevel(config[LOG_LEVEL])

    def check(self, payload: Payload, mod_ids: List[str]) -> bool:
        log.info("Checking for response " + str(self.response))
        if self.modExempt and payload.user in mod_ids:
            return False
        return self.trigger.check(payload)

    def respond(self, clacker, payload: Payload):
        if time.time() < self.cooldown_end:
            return
        self.cooldown_end = time.time() + self.cooldown_duration
        self.response.respond(clacker, payload)