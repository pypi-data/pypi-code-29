import logging
from typing import List

from botworks.channel.Channel import Channel
from botworks.slack import Payload
from botworks.slack.Payload import PayloadFactory

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class MessageHandler:
    def __init__(self, clacker, channels: List[Channel], config=None):
        if config is None:
            config = {}
        self.__conf = config
        if 'log_level' in config:
            log.setLevel(config['log_level'])

        self.__clacker = clacker
        bot = clacker.get_bot_info()
        self.__payload_factory = PayloadFactory(bot["id"], bot["token"], config=self.__conf)
        self.__channels = channels

    def parse_slack_output(self, slack_rtm_output):
        output_list = slack_rtm_output
        try:
            if output_list and len(output_list) > 0:
                for output in output_list:
                    log.debug(output)
                    try:
                        self.process_payload(self.__payload_factory.parse_payload(output))
                    except Exception as e:
                        log.warning("Error processing payload\n\t" + str(e))
        except Exception as e:
            log.error("Bad error processing payload.\n\t\t" + str(e))

    def process_payload(self, payload: Payload):
        if payload:
            try:
                message_channel = self.__get_channel_for_message(payload.channel)
                if message_channel:
                    log.debug("checking responses in " + str(message_channel))
                    for m in message_channel.responses:
                        if m.check(payload, message_channel.mod_ids):
                            m.respond(self.__clacker, payload)
                            break
            except Exception as e:
                log.error("Crashed handling " + payload.lower_message)
                log.error(e)

    def __get_channel_for_message(self, channel):
        for c in self.__channels:
            if c.channelId == channel:
                return c
        return None
