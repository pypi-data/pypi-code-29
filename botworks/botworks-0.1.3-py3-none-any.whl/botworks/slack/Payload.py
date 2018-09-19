import requests
import logging
import pytesseract

from io import BytesIO

from PIL import Image

from botworks.chat.EventTypes import user_typing_ignored

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class Payload:
    def __init__(self):
        self.user = None
        self.raw = None
        self.lower_message = None
        self.event_type = None
        self.channel = None
        self.timestamp = None
        self.is_direct_message = None
        self.isTargetedMessage = None
        self.imageText = None
        self.sharedMessage = None

    def finalize(self, rtm_message, bot_id: str, bot_token: str):
        self.raw = rtm_message
        self.user = rtm_message['user']
        self.lower_message = rtm_message['text'].lower() if 'text' in rtm_message else ""
        self.event_type = rtm_message['type'].lower() if 'type' in rtm_message else ""

        channel_field = "channel"
        if 'channel_id' in rtm_message:
            channel_field = 'channel_id'
        log.debug("Using " + channel_field + " as " + rtm_message[channel_field])
        self.channel = rtm_message[channel_field]
        self.timestamp = rtm_message['ts']
        self.is_direct_message = str(rtm_message['channel']).startswith("D")
        self.isTargetedMessage = self.is_direct_message
        if str(self.lower_message).startswith("<@" + str(bot_id) + ">"):
            self.isTargetedMessage = True
            self.lower_message = str(self.lower_message).replace("<@" + str(bot_id) + ">", "", 1).strip()

        if 'file' in rtm_message and bot_token:
            try:
                url = rtm_message['file']['url_private_download']
                log.info("Fetching image url: " + url)
                auth_header = {"Authorization": "Bearer " + bot_token}
                string = BytesIO(requests.get(url, headers=auth_header).content)
                img = Image.open(string)
                decoded_text = pytesseract.image_to_string(img)
                self.imageText = decoded_text

            except Exception as e:
                log.error("Error parsing image text: " + str(e))
                self.imageText = None
        else:
            self.imageText = None

        if 'attachments' in rtm_message and len(rtm_message['attachments']) > 0:
            self.sharedMessage = rtm_message['attachments'][0]
        else:
            self.sharedMessage = None


class PayloadFactory:
    def __init__(self, bot_id: str, bot_token: str, config=None):
        if config is None:
            config = {}
        self.__config = config
        self.__botId = bot_id
        self.__botToken = bot_token
        if 'log_level' in config:
            log.setLevel(config['log_level'])

    def parse_payload(self, message):
        if self.valid_message(message):
            log.debug(message)
            return Payload().finalize(message, self.__botId, self.__botToken)
        return None

    @staticmethod
    def valid_message(message):
        return message and ('bot_id' not in message or not message['bot_id'])\
               and ('is_ephemeral' not in message or not message['is_ephemeral'])  \
               and (('text' in message or 'type' in message and not message['type'] == user_typing_ignored)
                    and 'user' in message and 'channel' in message)

