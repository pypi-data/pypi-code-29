class vk:
    def __init__(self, login, password):
        self.__check_module()
        import vk_api
        self.__vk = vk_api.VkApi(login=login, password=password)
        self.__vk.auth()
        self.__name = self.name
        self.__id = self.user_id
        print('[{}]'.format(self.__name))
        print('\033[;1mAuthorization successful\033[0;0m')

    @staticmethod
    def __check_module():
        try:
            import vk_api
        except ImportError:
            import sys
            print('\33[31m'
                  'Error, module vk_api is required\nYou can install it using command\n'
                  '"pip install vk_api"\033[0;0m')
            sys.exit()

    @property
    def name(self) -> str:
        return str(self.__vk.method('account.getProfileInfo').get('first_name', None)
                   + ' ' +
                   self.__vk.method('account.getProfileInfo').get('last_name', None))

    @property
    def user_id(self):
        return self.__vk.method('users.get',
                                {'user_ids': self.__vk.method('account.getProfileInfo')['screen_name']})[0]['id']

    @property
    def info(self):
        print(
            self.__name + '\n' + str(self.__id)
        )
        return self.__name + '\n' + str(self.__id)

    def write(self, user_id, message):
        self.__vk.method('messages.send', {'user_id': user_id, 'message': message})

    def write_chat(self, chat_id, message):
        self.__vk.method('messages.send', {'chat_id': chat_id, 'message': message})

    def chat_name(self, chat_id) -> str:
        return self.__vk.method('messages.getChat', {'chat_id': chat_id}).get('title')

    def change_chat_name(self, chat_id, name):
        self.__vk.method('messages.editChat', {'chat_id': chat_id, 'title': name})

    def add_chat_member(self, chat_id, user_id):
        self.__vk.method('messages.addChatUser', {'chat_id': chat_id, 'user_id': user_id})

    def remove_chat_member(self, chat_id, user_id):
        self.__vk.method('messages.removeChatUser', {'chat_id': chat_id, 'user_id': user_id})

    def chat_users(self, chat_id):
        return self.__vk.method('messages.getChatUsers', {'chat_id': chat_id})

    @staticmethod
    def help():
        print('\033[92mfrom vbx_vk import *\n'
              'object = vk(login, password) - authorizes object\'s vk account\n'
              'object.name - returns object\'s name\n'
              'object.user_id - returns object\s id\n'
              'object.info - returns both name and user\'s id\n'
              'object.write(user_id, message) - sends a message to private messages\n'
              'object.write_chat(chat_id, message) - sends a message to the chat\n'
              'object.chat_name(chat_id) - returns chat id\n'
              'object.change_chat_name(chat_id, name) - changes chat\'s name\n'
              'object.add_chat_member(chat_id, user_id) - adds specified user to the chat\n'
              'object.remove_chat_member(chat_id, user_id) - removes specified user from the chat\n'
              'object.chat_users(chat_id) - returns a list of chat members\n'
              '\033[0;0m')


if __name__ == '__main__':
    vk.help()
