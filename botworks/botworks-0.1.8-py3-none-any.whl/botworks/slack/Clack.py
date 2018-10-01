import logging
import time

from slackclient import SlackClient

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

BOT_NAME = "autodesktest"


class Clack:
    def __init__(self, bot_token, bot_name, config=None):
        if config is None:
            config = {}
        obfuscated_token = bot_token[:5] + "*********************************" + bot_token[-4:]
        log.error("Got token " + obfuscated_token)
        self.__slack_client = SlackClient(bot_token)
        self.__bot_token = bot_token
        self.__admin_channel = None
        if not self.__slack_client.rtm_connect():
            log.error("Failed to initialize")
            exit(1)

        self.__user_list_refresh_time = 0
        self.__channel_list_refresh_time = 0
        self.__deleted_user_list = []
        self.__complete_user_list = None
        self.__complete_channel_list = None
        self.__active_human_user_list = []

        self.__complete_user_list = self.all_users()
        self.__complete_channel_list = self.all_channels()
        log.info("User list size: " + str(len(self.__complete_user_list)))
        log.info("DeletedUserList : " + str(len(self.__deleted_user_list)))
        log.info("channel list size: " + str(len(self.__complete_channel_list)))
        bot = self.find_user_by_name(bot_name)
        self.__myId = bot['id']
        if config and 'log_level' in config:
            log.setLevel(config['log_level'])

    def get_bot_info(self):
        return {"id": self.__myId, "token": self.__bot_token}

    def read(self):
        return self.__slack_client.rtm_read()

    def get_channel_member_count(self, channel_id):
        try:
            channel_members = self.__slack_client.api_call("channels.info",
                                                           channel=channel_id).get('channel').get('members')
            cleaned_list = list(set(channel_members) - set(self.__active_human_user_list))
            return len(cleaned_list)
        except Exception as e:
            log.error(e)
            log.error(e.__traceback__)
            log.warning(self.__slack_client.api_call("channels.info", channel=channel_id))
            return "1"

    def post_message(self, channel, message, send_delete_message=True):
        x = self.__slack_client.api_call("chat.postMessage", channel=channel,
                                         text=message, as_user=True)
        if send_delete_message and self.__admin_channel:
            self.post_message(self.__admin_channel, message + "\n!delete " + str(x['channel']) + " " + str(x['ts']),
                              send_delete_message=False)

    def react(self, payload, reaction: str):
        log.info("reaction: " + str(
            self.__slack_client.api_call("reactions.add",
                                         name=reaction, channel=payload.channel,
                                         timestamp=payload.timestamp)
        ))

    def ephemeral_message(self, payload, message: str):
        log.info(
            self.__slack_client.api_call("chat.postEphemeral",
                                         channel=payload.channel, user=payload.user,
                                         text=message, as_user=True)
        )

    def thread_reply(self, payload, message: str, send_delete_message=True):
        ts = payload.timestamp
        if 'thread_ts' in payload.raw:
            ts = payload.raw['thread_ts']
        x = self.__slack_client.api_call("chat.postMessage", channel=payload.channel,
                                         text=message, thread_ts=ts, as_user=True)
        if send_delete_message and self.__admin_channel:
            self.post_message(self.__admin_channel, message + "\n!delete " + str(x['channel']) + " " + str(x['ts']),
                              send_delete_message=False)

    def all_users(self):
        if self.__user_list_refresh_time > time.time():
            return self.__complete_user_list
        api_call = self.__slack_client.api_call("users.list")
        if api_call.get('ok'):
            self.__user_list_refresh_time = int(time.time() + 6000)
            deleted_users = filter(lambda m: 'deleted' in m and m['deleted'] and 'id' in m, api_call.get('members'))
            self.__deleted_user_list = list(deleted_users)
            self.__active_human_user_list = [user['id'] for user in api_call.get('members')
                                             if not user['deleted'] and not user['is_bot']]
            return api_call.get('members')
        return self.__complete_user_list

    def all_channels(self):
        if self.__channel_list_refresh_time > time.time():
            return self.__complete_channel_list
        api_call = self.__slack_client.api_call("channels.list")
        if api_call.get('ok'):
            self.__channel_list_refresh_time = int(time.time() + 6000)
            return api_call.get('channels')
        return self.__complete_channel_list

    def find_user_by_name(self, search_term: str):
        all_users = self.all_users()
        name = search_term.lower()
        if not all_users:
            return None
        for u in all_users:
            if ('real_name' in u and u['real_name'].lower() == name) \
                    or ('name' in u and u['name'].lower() == name) \
                    or ('id' in u and u['id'].lower == name)\
                    or ('profile' in u and (
                            ('display_name_normalize' in u['profile'] and u['profile']['display_name_normalize'] == name) or
                            ('display_name' in u['profile'] and u['profile']['display_name'] == name))):
                return u
        return None

    def get_user_by_id(self, user_id: str):
        return self.__slack_client.api_call("users.info", user=user_id)

    def find_channel_info(self, channel_name: str):
        lower_channel = channel_name.lower()
        channels = self.all_channels()
        for c in channels:
            if ('name' in c and c['name'].lower() == lower_channel) or ('id' in c and c['id'].lower() == lower_channel):
                return c
        return None

    def list_im(self):
        return self.__slack_client.api_call("im.list")

    def delete_message(self, channel, ts):
        channel = channel.upper()
        log.debug("deleting " + channel + " " + ts)
        log.debug(self.__slack_client.api_call("chat.delete", ts=ts, channel=channel))

    # def leave(channel):  # bots can't do this.
    #     print(slack_client.api_call("channels.leave", channel=channel))
