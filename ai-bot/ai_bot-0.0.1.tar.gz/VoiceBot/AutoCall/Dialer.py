#coding:utf-8

import ESL
import  json
import time
import  base64
import  datetime
import threading
import socketserver
import sys,urllib3,urllib
from urllib3.exceptions import InsecureRequestWarning

# 13772491757  祝  13916483739 张 15062405910  李 18209288679
class PhoneDialer(object):
    '''
    外呼拨号器
    '''
    def __init__(self,task,line,bot,**kwargs):
        '''
        初始化拨号器
        :param task:
        :param line: 外线配置对象
        '''
        self.line=line;
        self.bot=bot
        self.task=task  # 呼叫号码
        self.t_conf=kwargs
        self.dail_str = 'originate {param}sofia/gateway/{linename}/{dest} {bot} xml {dialplan}' #拨叫字符串
        self.isEslConnected = False #esl连接状态

    def getEsl(self):
        '''
        获取esl连接对象
        :return: 返回连接成功的esl对象
        '''
        con=ESL.ESLconnection(self.line['serverIp'],self.line['serverPort'],self.line['clientName'])
        if con.connected():
            con.events('json','all')
            self.isEslConnected=True
        else:
            #此处需要引发连接连接服务器异常
            pass
        return  con

    def stopEsl(self,con):
        '''
        断开esl连接
        :param con: esl连接对象
        :return: 无返回
        '''
        if  self.isEslConnected==True:
            con.disconnect()
            self.isEslConnected=False

    def dial(self,number,is_supervision=False,websock=None):
        '''
        拨号，websock不空的话就会监视拨打状态，否则不监视
        :param websock: websock对象
        :return:  无返
        '''
        con=self.getEsl()
        #param ="{originattion_caller_id_number="+self.line['aiPhoneNum']+",config_name=testbot,callee_id_number="+number["Phone"]+",Scence_id="+self.task['scencenumber']+",Scence_name="+self.task['scencename']+"}"
        if self.t_conf['rest_type']=='java':

            if 'companycode' in self.task:
                owner=str(self.task['companycode'])
            else:
                owner=str(number['companycode'])
            case=number['casenumber'] if number['casenumber'] else ''
            mone=number['overdueamount'] if number['overdueamount'] else 0
            param = "{companycode="+owner+\
                    ",originattion_caller_id_number=" + self.task['bot']['number'] + \
                    ",config_name=testbot,callee_id_number=" +  number["phone"] + \
                    ",Scence_id=" + self.task['scence']['code'] +\
                    ",Scence_name=" + self.task['scence']['name'].upper() +\
                    ",scence_obj_id="+ self.task['scence']['id']+\
                    ",bot_obj_id="+self.task['bot']['id']+\
                    ",line_obj_id="+self.task['line']['id']+ \
                    ",creater_id="+self.task["createrid"]+\
                    ",customer_obj_id="+number["id"]+\
                    ",money="+str(mone)+\
                    ",c_name="+number['name']+\
                    ",case_number="+case+"}"
        else:
            param = "{owner_id="+str(self.task['creater']['id'])+\
                    ",originattion_caller_id_number=" + self.task['bot']['number'] + \
                    ",config_name=testbot,callee_id_number=" +  number["phone"] + \
                    ",Scence_id=" + self.task['scence']['code'] + \
                    ",Scence_name=" + self.task['scence']['name'] .upper()+ \
                     ",scence_obj_id="+ self.task['scence']['id']+\
                    ",bot_obj_id="+self.task['bot']['id']+\
                    ",line_obj_id="+self.task['line']['id']+\
                    ",customer_obj_id="+number["id"]+"}"

        ds=self.dail_str.format(param=param,linename=self.line['linename'],dest=number["phone"],bot=self.task['bot']['number'],dialplan=' default')
        print("dial:",ds)
        con.api(ds)
        if  is_supervision == True:
            self.supervision(con,number,websock)
        self.stopEsl (con)

    def supervision(self,con,number,webock):

        print('supervision', number )
        '''
        监视通话事件
        :param con:esl连接对象
        :param webock: websocket 对象
        :return: 无返回
        '''
        while 1:
            evt = con.recvEvent ()
            if evt:
                evt_name=evt.getHeader ("Event-Name")
                if evt_name == "SERVER_DISCONNECTED":
                    print('号码:', number['phone'], 'disconnected')
                    break
                if   evt_name=='CHANNEL_HANGUP_COMPLETE':
                    print('号码:', number['phone'], 'hangup complete')
                if evt_name == "CHANNEL_DESTROY" :
                    print('号码:',number['phone'],'destroy')
                    break
                if evt_name == 'CHANNEL_ANSWER':
                    print("号码:",number['phone'],'answered')
                    self.sendMessagToClient (evt_name,number, webock, evt)
                if evt_name == 'CHANNEL_HANGUP':
                    print('号码:',number['phone'],'hangup')
                    self.sendMessagToClient(evt_name,number,webock,evt)

    def setDest(self,dest):
        pass

    def sendMessagToClient(self,evt_name,number,websock,fsevent):
        '''
        往客户端会送电话状态，通过websocket
        :param evt_name: 事件名称
        :param websock: websock实例
        :param fsevent: fs socket event
        :return: 无返回
        '''
        act = fsevent.getHeader ('Answer-State')
        target = fsevent.getHeader ('Caller-Caller-ID-Number')
        cs = fsevent.getHeader ('Channel - State')
        ccs = fsevent.getHeader ('Channel-Call-State')
        cause = fsevent.getHeader ('Hangup-Cause')
        if  websock:
            msg=json.dumps (
                {'phone-number': target,
                 'action': evt_name,
                 'answer-state': act if act else "",
                 'channel-state': cs if cs else "",
                 'channel-callstate': ccs if ccs else "",
                 'hangup-hause': cause if cause else ""})
            websock.send(msg.encode('utf-8'))
        else:
            self.updateNumber3Times(number['id'],act if act else "finish")

    def webRequest(self,method, url, body="", auth="Basic"):
        print("webRequest",url,body)
        try:
            if body:
                response = urllib3.PoolManager ().request (method, url, body=body.encode (),
                                                           headers={'Content-Type': 'application/json',
                                                                    'Authorization': auth})
            else:
                response = urllib3.PoolManager ().request (method, url, headers={'Content-Type': 'application/json',
                                                                                 'Authorization': auth})
            if response.status == 200 :
                #print(response.data)
                return json.loads (response.data)
        except ConnectionRefusedError:
            print('服务器拒绝连接:',url)
        return None

    def getAuthStr(self):
        upwd = self.t_conf['username'] + ":" + self.t_conf['password']
        return "Basic " + base64.standard_b64encode (upwd.encode ()).decode ()

    def updateTask(self,taskId, statu):
        newtask={}
        if statu=='excuting':
            start_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            newtask['Status']=statu
            newtask['StartTime']=start_time
        elif statu=='finish':
            end_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            newtask['Status']= statu
            newtask['EndTime']=end_time
        else:
            newtask={"Status": statu}

        if self.t_conf['rest_type'] == 'java':
            url = self.t_conf['tasks_update_url']
            newtask['id'] = taskId
            jsstr = json.dumps (newtask).lower()
        else:
            url = self.t_conf['tasks_update_url'] + "%s/" % taskId
            jsstr = json.dumps (newtask)

        return self.webRequest ("patch", url, jsstr, self.getAuthStr ())

    def updateNumber(self,number,statu):
        if   self.t_conf['rest_type']=='java':
            url = self.t_conf["customer_update_url"]
            bd = json.dumps ({"id":number,"dialstatu": statu}).lower()
        else:
            url = self.t_conf["customer_update_url"] + "%s/" % number
            bd = json.dumps ({"DialStatu": statu})
        return self.webRequest("patch",url,bd,self.getAuthStr())

    def updateNumber3Times(self,number,statu):
        update_count = 0
        while not  self.updateNumber(number,statu):
            if  update_count<3:
                time.sleep(30)
                update_count+=1
            else:
                return  False
        return  True


    def updateTask3Times(self,taskId,statu):
        update_count = 0
        while  not self.updateTask (taskId,statu):  # 更新任务的状态为开始执行
            if update_count<3:
                time.sleep (30)
                update_count += 1
            else:
                return False
        return True

    def dials(self):
        if self.updateTask3Times(self.task["id"], 'excuting')==True:
            for number in self.task["numbers"]:
                    try :
                        if number["dialstatu"] == "ready" or number["dialstatu"] == "new" :
                            if  self.updateNumber3Times(number['id'],"calling") :#更新号码状态
                                self.dial(number,True)
                            else:
                                print('号码状态失败:',number['phone'])
                    except  Exception as exp:
                         print("Exception in dials metohed of  dialer",number['phone'],"exp:",exp.args)
                #self.updateNumber (number['Id'], "")  # 更新号码状态
            # 更新任务的状态
            self.updateTask3Times(self.task["id"], "finish")


