import itchat
import base64
import json
from .qrlogin import send_ding_img
from Reserver.model import Msg, Token
import requests
from qlib.data import Cache
import sys
import os
from argparse import ArgumentParser

MSG_DB = os.path.expanduser("~/.qqbot-tmp/msg-db.sql")

@itchat.msg_register(itchat.content.TEXT, isGroupChat=False)
def search(msg):
    # if msg.FromUserName == 'fil'
    if msg['ToUserName'] != 'filehelper': return
    if msg.text.startswith("/"):
        key,val = msg.text[1:].split(maxsplit=1)
        d = {key:val}
        print(d)
        res = requests.post("http://localhost:14144/setting", data={
            'setting': json.dumps(d)
        }).json()
        itchat.send(res['res'], toUserName='filehelper')
    else:
        res = requests.post("http://localhost:14144/search", data={
            'key': msg.text
            }).json()
        if isinstance(res, list):
            for m in res:
                im = Msg(**m)
                mm = "%s nick:%s[%s] in (%s) said:\n%s" %(im.sendUser, im.sendNick, im.sendQq, im.name, im.sendContent)
                itchat.send(mm, toUserName='filehelper')
        else:
            itchat.send('Not found', toUserName='filehelper')



class Loginer:

    def __init__(self, token):
        self.token = token

    def __call__(self, uuid=None, status=None, qrcode=None):
        send_ding_img(self.token, "login ...", img=base64.b64encode(qrcode).decode('utf-8'))

    def __del__(self):
        itchat.logout()


def StartWeRobot():
    parser = ArgumentParser()
    parser.add_argument("-s", "--start", action="store_true",default=False, help="start server")
    parser.add_argument("-a", "--add-token",default=None,help="setting token")
    parser.add_argument("-I", "--initialization",action="store_true",default=False, help="initialization config")
    args = parser.parse_args()
    c = Cache(MSG_DB)
    if args.start:
        t = list(c.query(Token, tp='ding'))[-1]
        l= Loginer(t.text)
        itchat.auto_login(qrCallback=l,hotReload=True)
        itchat.run()
    
    elif args.add_token:
        t = Token(text=args.add_token, tp='ding')
        t.save(c)

    elif args.initialization:
        text = """[program:x-wechat]
command=/usr/local/bin/Qwechat -s
stdout_logfile= /var/log/x-wechat.log 
stderr_logfile= /var/log/x-wechat.err.log
        """
        text3 = """[program:x-replayer]
command=/usr/local/bin/Qserver -p 14144
stdout_logfile= /var/log/x-relayer.log 
stderr_logfile= /var/log/x-relayer.err.log
        """
        text2 = """[unix_http_server]
file=/tmp/supervisor.sock                       ; path to your socket file

[supervisord]
logfile=/var/log/supervisord/supervisord.log    ; supervisord log file
logfile_maxbytes=50MB                           ; maximum size of logfile before rotation
logfile_backups=10                              ; number of backed up logfiles
loglevel=error                                  ; info, debug, warn, trace
pidfile=/var/run/supervisord.pid                ; pidfile location
nodaemon=false                                  ; run supervisord as a daemon
minfds=1024                                     ; number of startup file descriptors
minprocs=200                                    ; number of process descriptors
user=root                                       ; default user
childlogdir=/var/log/supervisord/               ; where child log files will live

[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

[supervisorctl]

[inet_http_server]
port = 127.0.0.1:9001


[include]

files = /root/.config/services/*.conf
        """
        if not os.path.exists(os.path.expanduser("~/.config/services")):
            os.mkdir(os.path.expanduser("~/.config/services"))

        with open(os.path.expanduser("~/.config/services/x-wechat.conf"), 'w') as fp:
            fp.write(text)

        with open(os.path.expanduser("~/.config/services/x-relayer.conf"), 'w') as fp:
            fp.write(text3)

        with open(os.path.expanduser("~/.config/supervisor.conf"),'w') as fp:
            fp.write(text2)
        print("-- init --- install ok")
        os.popen("pip3 install -U git+https://github.com/Supervisor/supervisor.git 1>/dev/null 2>/dev/null;").read()
        os.popen("mkdir /var/log/supervisord/ ").read()
        os.popen("supervisord -c ~/.config/supervisor.conf").read()
        print("-- init --- start supervisor ok")
        os.popen("supervisorctl reread;supervisorctl update;").read()
        print("-- init --- start load procecers ok")
