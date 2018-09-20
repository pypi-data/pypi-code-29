#coding:utf-8
import time
import json
import base64
import threading
import websocket
import sys,urllib3,urllib

import AutoCall.Dialer

import  queue
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)

def webRequest(method,url,body="",auth="Basic"):
    print ("task", url, body)
    try:
        if  body:
            response = urllib3.PoolManager ().request (method, url,body = body.encode (),headers={'Content-Type': 'application/json','Authorization':auth})
        else:
            response = urllib3.PoolManager ().request(method, url,headers={'Content-Type': 'application/json','Authorization':auth })
        if response.status==200:
            return json.loads (response.data)
    except ConnectionRefusedError:
        print ('服务器拒绝连接:', url)
    return None

'''
获取拨打列表
'''
def scan(isReady,**kwargs):
    if  kwargs["rest_type"] =="java":
        url = kwargs["tasks_url"] + "ready" if isReady else "excuting"
        data = webRequest ("GET", url, auth=getAuthStr (**kwargs))
        if data:
            return json.loads(json.dumps(data).lower())
    else:
        url=kwargs["tasks_url"]+  "?search=ready" if  isReady else   "?search=excuting"
        data = webRequest ("GET", url, auth=getAuthStr (**kwargs))
        if data:
            return  json.loads(json.dumps(data["results"]).lower())
    return None

def getAuthStr(**kwargs):
    upwd = kwargs['username'] + ":" + kwargs['password']
    return  "Basic "+ base64.standard_b64encode(upwd.encode()).decode()

def getDefualtLine(task):
    if task['bot']:
        pass
    if task['line']:
        line=task["line"]
        return  {'linename':line['name'], 'aiPhoneNum': '6666', 'aiDialPlanName': 'default', 'serverIp': '114.116.39.18', 'serverPort': '8021', 'clientName': 'ClueCon', 'scencenumber': '9720', 'scencename': 'IOU2345'}
    if task['scence']:
        pass
    return  {'linename':'yuneasy0794','aiPhoneNum':'6666','aiDialPlanName':'default','serverIp':'114.116.39.18','serverPort':'8021','clientName':'ClueCon','scencenumber':'9720','scencename':'IOU2345'}

def calling(**kwargs):
     task_number=0
     isReady=True
     while True:
         try:
             task_number += 1
             tasks = scan (isReady, **kwargs)
             if tasks and  len(tasks)>0:
                 for task in tasks:
                     dialer = AutoCall.Dialer.PhoneDialer (task, getDefualtLine (task), None, **kwargs)
                     tThread = threading.Thread (target=dialer.dials)
                     tThread.start ()
                     print (task['name'], 'started. index is :', task_number)
         except Exception as e:
             print ('Exception in calling:', e)
         time.sleep(120)

def config(conf_profile):
    print ('load cc config')
    with open(conf_profile,'r') as conff:
        return  json.loads(conff.read())

def run(conf_profile):
    conf = config (conf_profile)
    print ('----------------------------------------begin calling loop-------------------------------------------')
    calling(**conf)
    print('---------------------------------------------main exit!-------------------------------------------------')


#队列字典
queue_dict={}


class QueueThread(object):
    def __init__(self,tqueue,**kwargs):
        self._queue=tqueue
        self.conf=kwargs
        self.task_thread=None
        self.wait_tasks =[]

    def  run_task(self,task):
        if task["id"] not in self.wait_tasks:
            self._queue.put_nowait (task)
            self.wait_tasks.append(task["id"])
        #self.run()

    def run(self):
            if  not  (self.task_thread and  self.task_thread.is_alive()):
                if  self._queue and not self._queue.empty():
                    self.task_thread=threading.Thread(target=self.worker)
                    print('queue begin')
                    self.task_thread.start()

    def  worker(self):
        while  not self._queue.empty():
            task=self._queue.get_nowait()
            dialer = AutoCall.Dialer.PhoneDialer (task, getDefualtLine (task), None, **self.conf)
            print("task ",task['name'],"is runing")
            dialer.dials()
            print ("task ", task['name'], "is end")
        print("queue end")

def runTask(**kwargs):
    task_number = 0
    isReady = True
    scan_number = 0
    while True:
        scan_number+=1
        try:
            tasks = scan (isReady, **kwargs)
            if tasks and len (tasks) > 0:
                for task in tasks:
                    task_number += 1
                    print ("task ",task_number,':', task)
                    line_id=task["line"]["id"]
                    if line_id not in queue_dict:
                        queue_dict[line_id]=QueueThread(queue.Queue(),**kwargs)
                    queue_dict[line_id].run_task(task)
                    print (task['name'], 'started. index is :', task_number)

            if  queue_dict and len(queue_dict)>0:
                for k,v in queue_dict.items():
                    v.run()
            print("loop",scan_number)
        except Exception as e:
            print ('Exception in fetchTask:', e)
        time.sleep (60)

def  run_with_queue(conf_profile):
    conf =  config (conf_profile)
    print ('---------------------------------------------排队呼叫开启-------------------------------------------------')
    runTask (**conf)
    print ('---------------------------------------------排队呼叫结束!-------------------------------------------------')



