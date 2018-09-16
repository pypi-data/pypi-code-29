import requests

class GabAPI:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        login_url = 'https://gab.ai/auth/login'
        self.client = requests.session()
        self.client.get(login_url)
        c = self.client.cookies

        login_data = {
            'username': self.username,
            'password': self.password,
            '_token': c['XSRF-TOKEN']
        }
        r = self.client.post(login_url, data=login_data)
        r = self.client.get('https://gab.ai/api/topics')

        token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjU4NjIyOCwiaXNzIjoiaHR0cHM6Ly9nYWIuYWkvaG9tZSIsImlhdCI6MTUzNzA5MDM5NSwiZXhwIjoxNTM3NDUwMzk1LCJuYmYiOjE1MzcwOTAzOTUsImp0aSI6IjZOemRUclhIVHlYVWhtbW4ifQ.bhMDQAzWicE4E6JHfmiMBagHjX0bQT8R7NePu3OXJ1E'
        self.client.headers = {
            'authorization': 'Bearer '+token,
            'x-xsrf-token': c['XSRF-TOKEN']
        }

    def post_comment(self, body='', filename=None):
        post = {
          "body": "<p>"+ body +"</p>",
          "reply_to": "",
          "is_quote": "0",
          "is_html": "1",
          "nsfw": "0",
          "is_premium": "0",
          "_method": "post",
          "gif": "",
          "topic": None,
          "group": None,
          "share_facebook": None,
          "share_twitter": None,
          "media_attachments": [],
          "premium_min_tier": 0
        }
        if filename != None:
            post['media_attachments'] = [self.post_media(filename)]

        return self.client.post('https://gab.ai/posts', data=post)

    def post_media(self, filename):
        image = open(filename, 'rb')
        type = 'image/png'
        files = { 'file': ('file', image, type) }
        params = { 'token': self.client.cookies['XSRF-TOKEN'] }
        r =  self.client.post('https://gab.ai/api/media-attachments/images', files = files)
        return r.json()['id']
