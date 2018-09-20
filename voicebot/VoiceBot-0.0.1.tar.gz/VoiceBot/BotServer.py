
import sys
import json
import time
import threading
import socketserver
from Bot import BotTcpHandler


class ServerThread(threading.Thread):
    def __init__(self,arg):
        super(ServerThread, self).__init__()#注意：一定要显式的调用父类的初始化函数。
        self.arg=arg
    def run(self):#定义每个线程要运行的函数
        time.sleep(1)
        print (self.arg['ip'],":",self.arg['port'], " started.")
        self.arg["fun"](self.arg['ip'],self.arg['port'])



def loadConfig():
    ip='0.0.0.0'
    port=8180
    path=sys.path[0]
    with open(path+"/botConfig.json",'r') as jf:
        jstr=json.loads(jf.read())
    return jstr

def startOneServer(ip,port):
    try:
        server = socketserver.ThreadingTCPServer ((ip, port), BotTcpHandler)
        server.serve_forever()
    except  KeyboardInterrupt :
        print('i get en error')
        server.shutdown()
    except  OSError  as  ex:
        print(ex)

if __name__ == '__main__':
    confList= loadConfig()
    #print(confList)
    try:
        for k,v in confList.items():
            for bot in v["bot"]:
                arg={'fun':startOneServer,"ip":bot["ip"],"port":bot["port"]}
                st=ServerThread(arg);
                st.start()
    except Exception as e:
        print('aaaaaa',e)



