import vk #for vk features
from datetime import datetime #for time comparison
import json #for json parsing


class VkLibrary:
    def __init__(self, login, password, app_id, id ):
        self.login = login
        self.password = password
        self.app_id = app_id
        self.api = None
        self.my_id = id
        self.friends_dict = dict()
        self.count = 0

    def hello_world(self):
        print("this is fine.")

    def login(self):
        vk_auth_session = vk.AuthSession(self.app_id, self.login, self.password, scope='wall, messages')
        self.api = vk.API(vk_auth_session, v='5.69')

    def send_message(self, user_id, text_msg):
        self.api.messages.send(user_id=user_id, message=text_msg)

    def __parse_json(self, json_string, field1, field2):
        try:
            parsed_string = json.loads(json_string)
            substring = str(parsed_string[field1]).replace('[', '')
            substring = substring.replace(']', '')
            substring = substring.replace("'", '"')
            json_dict = json.loads(substring)
            return str(json_dict[field2])
        except (json.JSONDecodeError, TypeError):
            print('Error occurred while parsing JSON')

    def get_friends(self):
        resp3 = self.api.friends.get(user_id=self.my_id, order='name', count='1000', offset='0', fields='name', name_case='nom')
        users_json_list = resp3['items']
        self.count = 0
        for item in users_json_list:
            name = str(item['first_name']) + ' ' + str(item['last_name'])
            user_id = str(item['id'])
            self.count += 1
            self.friends_dict.update({name: user_id})
        return self.friends_dict

    def get_users(self, user_id):
        return self.api.users.get(user_ids=user_id)

    def get_last_message(self, count_):
        resp = self.api.messages.get(count=str(count_))
        resp = str(resp).replace("'", '"')
        us_id = self.__parse_json(resp, 'items', 'user_id')
        resp2 = self.get_users(us_id)
        resp2 = str(resp2).replace("'", '"')
        resp2 = resp2.replace('[', '')
        resp2 = resp2.replace(']', '')
        resp2 = json.loads(resp2)
        message = self.__parse_json(resp, 'items', 'body')
        first_name = resp2['first_name']
        last_name = resp2['last_name']
        return [message, first_name, last_name]


    def auto_post_on_time(self,time, message, id,  group ):
    # use only in loop or in handler
    #time should be presented like this: '2018-12-31 22:30'
    # or define a simple loop inside
    #while 1:
        # compare current and specified time
        if datetime.now().strftime('%Y-%m-%d %H:%M') == time:
            # send messages
            if group is True:
                self.api.messages.send(peer_id=id, message='test message for a group chat') # send to a group chat
            else:
                self.api.messages.send(user_id=id, message='test message')  # send to a user
            # break infinite loop
            # break