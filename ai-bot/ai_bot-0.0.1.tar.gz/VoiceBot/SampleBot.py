#coding:utf-8

import ESL
import json
import time
import datetime
import socketserver
import sys,urllib3,urllib
from MyDialog.d_payback import *
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)
currentPath=sys.path[0]

'''
    web post请求
    url：请求地址，包括请求的参数由？和地址相连的参数，参数之间由&连接
    jsonBodyData：请求体，jsonstring
 '''
def webPostRequest(url, jsonBodyData):
    response = urllib3.PoolManager ().request ("POST", url, body=jsonBodyData.encode (),
                                               headers={'Content-Type': 'application/json'})
    return json.loads (response.data)

def webGetRequest(url):
    response = urllib3.PoolManager ().request("GET", url,headers={'Content-Type': 'application/json'})
    return json.loads (response.data)

def readJsonFile(filename):
    with open (filename, 'r') as load_f:
        return json.load (load_f)

class VoiceBase(object):
    def __init__(self,voice_param,*asrgs,**kwargs):
        self._voice_param=voice_param

    def initParam(self,con_str, **kwargs):
        p = ''
        for k, v in kwargs.items ():
            p += k + "=" + v + con_str
        return p

    @property
    def mader(self):
        if self._voice_param and "mader" in self._voice_param:
            return self._voice_param["mader"]
        return None

    @property
    def request_type(self):
        if self._voice_param and "request_type" in self._voice_param:
            return self._voice_param["request_type"]
        return None

    @property
    def param(self):
        if self._voice_param and "param" in self._voice_param:
            return  self.initParam("&",**self._voice_param["param"])+'auth=mifeng'
        return None

    @property
    def sdk_param(self):
        if self._voice_param and "param" in self._voice_param:
            return  self.initParam(",",**self._voice_param["param"])
        return None

    @property
    def url(self):
        if self._voice_param and "url" in self._voice_param:
            return self._voice_param["url"]
        return ""

    @property
    def body(self):
        if self._voice_param and "body" in self._voice_param:
            return self._voice_param["body"]
        return ""

class AsrHandle (VoiceBase):
    def __init__(self, voice_param,*args, **kwargs):
        super(AsrHandle,self).__init__(voice_param)

    @property
    def result_type(self):
        if self._voice_param and "result_type" in self._voice_param:
            return  self._voice_param["result_type"]
        return ""

    @property
    def sdk_param(self):
        tp=super (AsrHandle, self).sdk_param
        return  tp+ "start-input-timers=false,no-input-timeout=1000"

    def start(self, con, uuid, **kwargs):
        return con.execute ('detect_speech', 'zw_asr {' + self.sdk_param + '}yes_no yes_no', uuid)

    def pause(self, con, uuid):
        return con.execute ('detect_speech', 'pause', uuid)

    def resume(self, con, uuid):
        return con.execute ('detect_speech', 'resume', uuid)

    def detected(self, event):
        statu = event.getHeader ("Speech-Statu")
        body = event.getHeader ("_body")
        if statu == '5':
            if self.mader == "ali":
                return self.aliParse (body),True
            elif self.mader == "kd":
                return self.kdParse (body),True
            elif self.mader == 'bd':
                return self.bdParse (body),True
            else:
                print ("unknow asr type:" + self.mader)
        return None,False

    def bdParse(self, jsonTxt):
        print(' unimplement the method bd parse in asrhandle.')
        return None,None

    def kdParse(self, json_str):
        retStr = None
        if self.result_type == "json":
            ret = json.loads (json_str)
            for word in ret['ws']:
                for cword in word['cw']:
                    retStr += cword['w']
                    break
        else:
            retStr = json_str
        #print ("source:", json_str)
        #print ("target:", retStr)
        return None,None

    def aliParse(self, json_str):
        retStr = None
        if self.result_type == "json":
            ret = json.loads (json_str)
            if 'result' in ret:
                retStr = ret["result"]["text"]  # ,ret["result"]["sentence_id"]
        else:
            retStr = json_str
        return retStr

class TtsHandle (VoiceBase):
    @property
    def speak_type(self):
        if self._voice_param and "speak_type" in self._voice_param:
            return  self._voice_param["speak_type"]
        return None

    def say(self,con,uuid,ai):
        self.isPlaying = True
        if  self.speak_type=='tts':
            if self.request_type=='web':
                requestUrl=(self.url+'?'+self.param) % ai['text']
                con.execute ("playback", "shout:"+requestUrl, uuid)
            else:
                # con.execute ("speak", 'hello,boy', self.uuid)
                pass
        elif self.speak_type=='record':
            recordUrl=self.url+ai["recordNumber"]+".mp3"
            con.execute ("playback", recordUrl, uuid)
        else:
            print (self.speak_type, "is unknow play type,required tts or record(mp3,wav)")

class NlsHandle(VoiceBase):

    def __init__(self,voice_param,*asrgs,**kwargs):
        self.log_id=0
        self._end = False
        self._dialog=None
        super(NlsHandle,self).__init__(voice_param,*asrgs,**kwargs)

    @property
    def dialog_type(self):
        if  self._voice_param:
            return  self._voice_param["dialog"]["type"]
        return None

    @property
    def dialog(self):
        if   self._voice_param and not self._dialog:
            dialog_content=""
            dialog_p=self._voice_param["dialog"]
            if dialog_p["type"]=='buildin':
                fname=sys.path[0]+dialog_p["name"]
                dialog_content=readJsonFile(fname)
            else:
                dialog_content=webGetRequest(dialog_p["url"]+"?"+self.initParam("&",dialog_p["param"]))
            self._dialog=payback("",**dialog_content)
        return self._dialog



    '''
    对话交互
        如果结果是对话内容，此处则返回对话文本（tts）,录音文件名（record）
    '''
    def interop(self,userTxt='begin'):
        requestUrl=''
        if self.request_type=='web' and self.param:
            if self.dialog_type=="buildin":
                if userTxt == 'begin':
                    txt = self.dialog.context.current_dn
                    self._end = False
                else:
                    if userTxt != 'next' and userTxt != "GREET1" and userTxt != "GREET2" and userTxt != "GREET3":
                        requestUrl = (self.url + '?' + self.param)
                        if self.mader == "bd":
                            self.log_id += 1
                            self.body["log_id"] = self.log_id
                        jStr = json.dumps (self.body) % userTxt
                        jsonResponse = webPostRequest (requestUrl, jStr)
                        method, txt = self.parse (jsonResponse)
                    else:
                        if userTxt == 'next':
                            method = userTxt
                        else:
                            txt = userTxt
                    if method == 'end' or method == 'bye':
                        self._end = True
                    else:
                        if method:
                            txt= self.dialog.fetchNext(method)
                        elif txt:
                            txt= self.dialog.fetchQA(txt)
                        self._end=self.dialog.context.end
            else:
                print ("unimplement dialog")
        else:
            print("unimplement interop")
        return txt

    def parse(self,jsonTxt):
        if self.mader=='bd':
            return self.bdParse(jsonTxt)
        elif self.mader=='kd':
            return self.kdParse (jsonTxt)
        elif self.mader=='ali':
            return self.aliParse (jsonTxt)
        else:
            print (self.mader, "is unknow nls mader")

    def bdParse(self,jsonTxt):
        txt=None
        method=None
        if jsonTxt:
            if 'error_code' in jsonTxt  and jsonTxt['error_code']==0:
                txt=jsonTxt['result']['response']['action_list'][0]['say']# 1.0 需要编码解码s_str = s_ucode.encode ("utf-8")
                method=jsonTxt['result']['response']['action_list'][0]['custom_reply']
                if method and method.index('func'):
                        if 'func' in method:
                            method=json.loads(method)["func"]
                        else:
                            print (method)
                            method=None
            elif jsonTxt['error_code']!=0:
               print('error: ' , jsonTxt['error_code'],'error-code:',jsonTxt['error_msg'].encode ("utf-8"))
        return  method,txt

    def kdParse(self, jsonTxt):
        print(' unimplement the method kd parse in nlphandle.')
        return None,None

    def aliParse(self, jsonTxt):
        print (' unimplement the method ali parse in nlphandle.')
        return None,None

    @property
    def end(self):
        return self._end

'''
    如果nls返回的结果是语音流,则直接跳过nls过程,而将nls的相关参数配置到tts上
    tts可以直接把数据shout到fs中,播放出去
'''
class SampleBotTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        if self.con.connected():
            self.setChannelVariable()
            while 1:
                event = self.con.recvEventTimed (100)
                self.SilenceTimeout()
                if event:
                    ename, euuid = self.getEventInfo (event)
                    print (ename)
                    if  euuid == self.uuid and ename in self.switch and self.switch[ename](event)==True:
                        break

        return

    def setup(self):
        self.rcontextUploadType='url'
        self.idleTime=None
        self.silenceTimes = 0
        self.silenceTimeout=10
        self._conf=None
        self.is_tnls=False
        reqInfo = self.request.fileno ()
        self.con = ESL.ESLconnection (reqInfo)
        self.getRequestInfo()
        self.subscriptionEvents()
        self.initSwitch()
        self.isAnswer=False
        self.isPlaying = False

    @property
    def config(self):
        if not self._conf:
            with open (sys.path[0] + "/botConfig.json", 'r') as jf:
               self._conf = json.loads (jf.read ())
        return  self._conf

    def finish(self):
        return

    def initSwitch(self):
        self.switch = {
                        "CHANNEL_ANSWER": self.evtAnswer, "CHANNEL_HANGUP": self.evtHangup,
                       "PLAYBACK_START": self.evtPlayStart, "PLAYBACK_STOP": self.evtPlayStop,
                       "DETECTED_SPEECH":self.evtDetectedSpeech, "CHANNEL_HANGUP_COMPLETE": self.evtHangupComplete,
                       "SERVER_DISCONNECTED":self.evtServerDisconnected
                       }

    def subscriptionEvents(self):
        self.con.events ("json", "all")
        self.con.sendRecv ('myevents')
        self.con.sendRecv ('divert_events')
        self.con.sendRecv ('linger')

    def getRequestInfo(self):
        info = self.con.getInfo ()
        self.uuid = info.getHeader ('unique-id')
        self.cname = info.getHeader ('Channel-Channel-Name')
        self.record_dir = info.getHeader ('variable_RecordDir')
        self.configName = info.getHeader ('variable_config_name')
        if self.config[self.configName]["config"]["isParamFrom"]!="config":
            #读取所有通道参数但前不支持
            self.asr = AsrHandle(json.loads(info.getHeader ('variable_asr_param')))
            self.tts = TtsHandle(json.loads (info.getHeader ('variable_tts_param')))
            self.nls = NlsHandle (json.loads (info.getHeader ('variable_nls_param')))
        else:
            cfg=self.config[self.configName]["config"]
            self.asr=AsrHandle(cfg["asr"])
            self.tts=TtsHandle(cfg["tts"])
            self.nls = NlsHandle (cfg["nls"])

    def setChannelVariable(self):
        #self.con.execute ('set', 'fire_asr_events=true', self.uuid)  #当无法接收到语音识别事件detected-speech时候可以将此行取消注释
        self.con.execute ('set', "rtp_enable_vad_out=true", self.uuid)
        #con.execute ("set", 'record_sample_rate=16000', self.uuid)
        self.con.execute ("set", 'variable_builder=mifeng', self.uuid)

    def getEventInfo(self,event):
        ename = event.getHeader ("Event-Name")
        euid= event.getHeader ('unique-id')
        #print( event.serialize ('json'))
        return  ename,euid

    def evtAnswer(self,event):
        self.isAnswer =True
        beginT=self.nls.interop('begin')
        self.asr.start (self.con, self.uuid)
        self.tts.say(self.con,self.uuid,beginT)
        self.nls.dialog.context.appendDialogContext (beginT, '')
        return False

    def evtDetectedSpeech(self,event):
        print("detected......",self.isPlaying)
        if self.asr and self.isPlaying == False:
            if self.asr.mader=='kd':
                #stop detected
                self.con.execute ('detect_speech', 'pause', self.uuid)
            asr_txt,isValid= self.asr.detected(event)
            if asr_txt and isValid==True:
                if self.nls:
                    txt = self.nls.interop(asr_txt)
                    self.nls.dialog.context.appendDialogContext(txt,asr_txt)
                    print ("人:",asr_txt)
                    print("                             机器:",txt["text"])
                else:
                    txt =asr_txt

                if self.tts :
                    #如果nls返回的结果为语音流,则在tts中直接调用,就可以把nls的相关信息直接配置到tts上
                    self.tts.say(self.con,self.uuid,txt)
        return self.nls.end #nls 返回结果为语音流暂未处理

    def evtPlayStart(self,event):
        self.isPlaying = True
        print("p start")
        self.idleTime = None
        return False

    def evtPlayStop(self,event):
        self.idleTime = datetime.datetime.now ()
        self.isPlaying = False
        print ("p end")
        if self.nls.end == True:
            self.con.execute ("hangup", "", self.uuid)
        if self.asr.mader == "ali":
            pass
        elif self.asr.mader == "kd":
            self.con.execute ('detect_speech', 'resume', self.uuid)
        else:
            self.con.execute ('detect_speech', 'resume', self.uuid)

        return False

    def evtHangup(self,event):
        return False

    def evtHangupComplete(self,event):
        self.uploadContext (self.con)
        self.uploadRecord (self.con)
        return True

    def evtServerDisconnected(self,event):
        return  True

    def SilenceTimeout(self):
        isTimeOut= False if not self.idleTime else (datetime.datetime.now() - self.idleTime).seconds > self.silenceTimeout
        newSay=None
        if self.isAnswer==True and (not self.isPlaying)  and isTimeOut==True:
            if self.silenceTimes==0:
                newSay= self.nls.interop('GREET1')
            elif self.silenceTimes==1:
                newSay = self.nls.interop ('GREET2')
            elif self.silenceTimes==2:
                newSay = self.nls.interop ('GREET3')
            else:
                text = self.nls.interop ('next')
                if text:
                    newSay=text
            if newSay and self.isPlaying == False:
                self.tts.say (self.con,self.uuid,newSay)
                self.nls.dialog.context.appendDialogContext (newSay, '')
            self.silenceTimes+=1

    def saveDailogContext(self):
        filename = sys.path[0]+'/dialogRecord/'+self.uuid+'.json'
        dcontexts=self.nls.dialog.context.getDialogContexts()
        rDcontext=[]
        for text in dcontexts:
            if text['man'] and text['man']!='':
               man=text['man']
            else :
                man=""
            if text['ai']:
                ai=text['ai']['text']
            else:ai=""
            if man or ai:
                rDcontext.append({"man":man,'ai':ai})
        with open (filename, 'w') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write (json.dumps(rDcontext).encode('utf-8').decode('unicode_escape'))
        return filename

    def uploadContext(self, con):
        print ("已经挂断,保存对话内容")
        contextfile = self.saveDailogContext ()
        print ('保存完成，上传对话内容')
        apisrt =self.config[self.configName]["dialogrecord_url"]+"" + self.uuid
        if self.rcontextUploadType == 'fs':
            self.fsUpload (con, contextfile, apisrt)
        else:
            self.urlUpload (apisrt, contextfile)
        print ('上传对话内容完成，')

    def fsUpload(self, con, file, url):
        rcf = " RecordContextFile=" + file
        uplaodstr = url + rcf + ' %s nopost event'
        evt = con.api ('curl_sendfile ' + uplaodstr)
        print (evt.serialize ('json'))

    def urlUpload(self, url, file):
        with open (file) as cjson:
            file_data = cjson.read ()
        for i in range (3):
            response = urllib3.PoolManager ().request ("POST", url, fields={'RecordContextFile': (file, file_data)})
            rd = json.loads (response.data)
            if response.status == 200:
                break
            time.sleep (5)
        return rd

    def uploadRecord(self, con):
        print ('保存完成，上传对话录音')
        apisrt = self.config[self.configName]["dialogrecord_url"]+"%s %s nopost event"
        rf = "RecordFile=" + self.record_dir + "/%s.wav"
        uplaodstr = apisrt % (self.uuid, (rf % self.uuid))
        evt = con.api ('curl_sendfile ' + uplaodstr)
        print (evt.serialize ('json'))
        print ('上传对话录音完成')
        #print (uplaodstr)
        return False

server = socketserver.ThreadingTCPServer (('0.0.0.0', 8240), SampleBotTcpHandler)
server.serve_forever()