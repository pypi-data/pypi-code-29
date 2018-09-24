import json
import os

import lxml.html
import requests
import requests.cookies


class CanvasSession:
    session = None

    login_url = "https://federation.ku.dk/CookieAuth.dll?Logon"
    login_start = "https://absalon.ku.dk/login"
    api_url = "https://absalon.ku.dk/api/v1/"

    def __init__(self, username=None, password=None, token=None):
        self.username = username
        self.password = password
        self.token = token

    def get_session(self):
        if not self.session:
            self.create_session()
        return self.session

    def create_session(self):
        self.session = requests.session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 ('
                          'KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})

        if self.token:
            cookie = requests.cookies.create_cookie('canvas_session', self.token)
            self.session.cookies.set_cookie(cookie)
            return

        login = self.session.get(self.login_start)

        login_html = lxml.html.fromstring(login.text)
        hidden_elements = login_html.xpath('//input[@type="hidden"]')
        form = {x.attrib['name']: x.attrib['value'] for x in hidden_elements}

        form['username'] = self.username
        form['password'] = self.password
        form['trusted'] = "4"

        self.session.headers.update({'referer': login.url})
        response = self.session.post(self.login_url, data=form)

        saml_html = lxml.html.fromstring(response.text)
        hidden_elements = saml_html.xpath('//input[@type="hidden"]')
        form_element = saml_html.xpath('//form')
        form = {x.attrib['name']: x.attrib['value'] for x in hidden_elements}

        self.session.post(form_element[0].attrib["action"], data=form)

    def api_call(self, call):
        session = self.get_session()
        data = session.get(self.api_url + call)
        data = data.text.replace('while(1);', '')
        return json.loads(data)

    def download_file(self, path, url):
        if not url or os.path.isfile(path):
            return

        session = self.get_session()
        r = session.get(url, stream=True)
        with open(path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
