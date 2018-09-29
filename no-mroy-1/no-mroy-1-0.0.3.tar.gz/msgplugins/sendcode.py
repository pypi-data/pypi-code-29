from Reserver.utils import package
from Reserver.utils import MsgMan
from msgplugins.qrlogin import send_ding_img
from termcolor import colored
from qlib.data import dbobj, Cache
import pdb
import os
from concurrent.futures.thread import ThreadPoolExecutor


DEBUG = os.getenv("DEBUG")
MSG_DB = os.path.expanduser("~/.qqbot-tmp/msg-db.sql")

class Msg(dbobj):pass
class Token(dbobj):pass
class Key(dbobj):pass

def send_notification(im, ding_token):
    mm = "%s nick:%s[%s] in (%s) said:\n%s" %(im.sendUser, im.sendNick, im.sendQq, im.name, im.sendContent)
    send_ding_img(ding_token, mm, title='')

def onQQMessage(bot, contact, member, content):
    # print(f"{contact} | {member.name} : {content}")

    m =  MsgMan()
    print(colored(contact.name + "|" + member.name, 'green'),end='\r')
    msg_d = contact.__dict__
    msg_d['sendUser'] = member.name
    msg_d['sendQq'] = member.uin
    msg_d['sendNick'] = member.nick
    msg_d['sendType'] = contact.ctype
    msg_d['sendContent'] = content
    msg = Msg(**msg_d)
    m.syncs_msg(msg)

    c = Cache(MSG_DB)
    ding_tk = list(c.query(Token, tp='ding'))[-1]
    if_send = False
    for k in c.query(Key):
        if k.text in content:
            if_send= True
            break
    if if_send:
        send_notification(msg, ding_tk.text)
            


def onPlug(bot):
    print(" -- start plugin  version: 0.0 -- ")
    m =  MsgMan()
    if m.test():
        print("--- server ok ----- ")
    else:
        print(colored("Error Server: "+ m.api, 'red'))
    # m.syncs_msgs(msgs)