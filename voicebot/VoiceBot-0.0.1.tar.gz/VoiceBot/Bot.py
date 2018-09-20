#coding:utf-8

import ESL
import json
import datetime
import time
import sys,urllib3,urllib
import socketserver
from urllib3.exceptions import InsecureRequestWarning
import ssl
import  threading
import xml.dom.minidom as mdom
import queue
import  gc
from MyDialog.d_payback import *

urllib3.disable_warnings(InsecureRequestWarning)

recordContextPath=sys.path[0]

class BotTcpHandler(socketserver.BaseRequestHandler):
    access_token = '24.8a901b663eff65bbf4703ab27e156861.2592000.1538309173.282335-11126101'
    rcontextUploadType="url"
    uint_version = 2
    asr_mader="ali"   #ali 阿里巴巴,bd 百度,kd 科大讯飞
    asr_resutlType= "json"#'plain'#'xml'#
    def InitHandle(self):
        self.scence = '9720'#'2490'#'3400'
        self.switch = {"CHANNEL_ANSWER": self.EventAnswer, "CHANNEL_HANGUP": self.EventHangup,
                       "PLAYBACK_START": self.EventPlayStart, "PLAYBACK_STOP": self.EventPlayStop,
                       "DETECTED_SPEECH": self.EventDetectedSpeech,"CHANNEL_HANGUP_COMPLETE":self.EventHangupComplete,
                       "CHANNEL_DESTROY":self.distroy
                       }
        self.unit_log_id = 0
        self.silenceTimeout = 5
        self.silenceTimes = 0
        self.isAnswer = False  # 是否应答
        self.isPlaying = False  # 机器是否正在说话
        self.asrIdlStartTime = None  # 语音识别，静音计时开始时间
        self.bot_session = ''
        #self.playQueue = None#queue.Queue()
        self.sentence_id=None
        self.isBreak = False
        self.temp=0
        self.suffix = '.mp3'
        #self.sayThread=None

    def GetEventInfo(self,event):
        ename = event.getHeader ("Event-Name")
        e_sequence = event.getHeader ("Event-Sequence")
        euid= event.getHeader ('unique-id')
        #print( event.serialize ('json'))
        return  ename,euid

    def GetChannelInfo(self,con):
        info = con.getInfo ()
        #print (info.serialize ('json'))
        self.uuid = info.getHeader ('unique-id')
        self.cname = info.getHeader ('Channel-Channel-Name')
        self.recordDir=info.getHeader('variable_RecordDir')
        self.scence =info.getHeader('variable_Scence_id')
        self.case=info.getHeader("variable_case_number")
        self.money = info.getHeader("variable_money")
        self.c_name = info.getHeader("variable_c_name")
        self.scenceName = info.getHeader ('variable_Scence_name')
        self.userInfo={"name":"ldd","sex":"male","alias":"li_m","money":2320.,"over_time":5}
        print("scenece:",self.scence,self.scenceName)

    def SetChannelVariable(self,con):
        con.execute ('set', 'fire_asr_events=true', self.uuid)  #当无法接收到语音识别事件detected-speech时候可以将此行取消注释
        con.execute ('set', "rtp_enable_vad_out=true", self.uuid)
        #con.execute ("set", 'record_sample_rate=16000', self.uuid)
        con.execute ("set", 'variable_builder=mifeng', self.uuid)
        con.execute("set","playback_delimiter=@",self.uuid)
        con.execute("set", "playback_sleep_val=50", self.uuid)

    def uploadContext(self,con):
        print ("已经挂断,保存对话内容")
        contextfile = self.saveDailogContext ()
        print ('保存完成，上传对话记录')
        apisrt = "http://116.236.220.214:22286/etc-web/v1/api/dialog/updateDialog?uuid="+self.uuid
        #apisrt = "http://114.116.39.230:8500/VoiceBotService/v1/botManager/dialogRecord?uuid=" + self.uuid
        if BotTcpHandler.rcontextUploadType=='fs':
            self.fsUpload(con,contextfile,apisrt)
        else:
            self.urlUpload(apisrt,contextfile)
        print ('上传对话记录完成，')

    def fsUpload(self,con,file,url):
        rcf = " RecordContextFile="+file
        uplaodstr = url+rcf+' %s nopost event'
        evt = con.api ('curl_sendfile ' + uplaodstr)
        print (uplaodstr)
        #print (evt.serialize ('json'))

    def urlUpload(self,url,file):
        try:
            with open(file) as cjson:
                file_data=cjson.read()
                print(file," file length：",len(file_data))
        except FileNotFoundError as fnfe:
            print(datetime.datetime.now(),'文件：',file,'无法找到' )
            return None

        for i in  range(3):
            response = urllib3.PoolManager().request("Patch", url,
                                                     fields={'recordcontextfile': (file, file_data),
                                                                 "score": self.payback.context.score,
                                                                 "case_number":self.case,
                                                                "attitude": self.payback.context.attitude[0]})
            #response = urllib3.PoolManager ().request ("Patch", url,fields={'RecordContextFile': (file, file_data),"Score":self.payback.context.score,"Remark":self.payback.context.attitude})
            rd= json.loads (response.data)
            if response.status==200:
                break
            time.sleep(5)
        return rd

    def urlUploadRecord(self,url,file):
        try:
            with open(file,"rb") as cjson:
                file_data=cjson.read()
                print(file, " file length：", len(file_data))
        except FileNotFoundError as fnfe:
            print(datetime.datetime.now(),'文件：',file,'无法找到' )
            return  None

        for i in  range(3):
            response = urllib3.PoolManager().request("Patch", url, fields={'recordfile': (file, file_data)})
            #response = urllib3.PoolManager ().request ("Patch", url,fields={'RecordFile': (file, file_data)})
            rd= json.loads (response.data)
            if response.status==200:
                break
            time.sleep(5)
        print(rd)
        return rd

    def uploadRecord(self,con):
        print (datetime.datetime.now(),'保存完成，上传对话录音')

        if BotTcpHandler.rcontextUploadType == 'fs':
            # apisrt = "http://114.116.39.230:8500/VoiceBotService/v1/botManager/dialogRecord?uuid=%s %s nopost event"
            apisrt = "http://116.236.220.214:22286/etc-web/v1/api/dialog/updateDialog?uuid=%s %s nopost event"
            rf = " RecordFile=" + self.recordDir + "/%s" + self.suffix
            uplaodstr = apisrt % (self.uuid, (rf % self.uuid))
            evt = con.api('curl_sendfile ' + uplaodstr)
            bd = evt.getHeader('_body')
            if  bd and '200' in bd or 'Ok' in bd or bd['retMsg']=='ok':
                print(datetime.datetime.now(),'上传对话记录录音完成')
            else:
                print(datetime.datetime.now(),'录音完成上传失败')
            print(uplaodstr)
        else:
            f= self.recordDir+"/"+self.uuid+self.suffix
            urlr="http://116.236.220.214:22286/etc-web/v1/api/dialog/updateDialog?uuid="+self.uuid
            urlrd=self.urlUploadRecord(urlr,f)
            print(datetime.datetime.now(),"上传返回:",urlrd)
            if  urlrd and ('200' in urlrd or 'Ok' in urlrd or urlrd['retMsg']=='ok'):
                print(datetime.datetime.now(),'上传对话记录录音完成')
            else:
                print(datetime.datetime.now(),'录音完成上传失败')
            print(urlr)

        return  False

    def EventHangupComplete(self,con,event):
        print('挂断后续工作处理完成，开始上传通话记录与录音')
        self.uploadContext(con)
        self.uploadRecord(con)
        return  True

    def distroy(self,con):
        print("通道销毁")
        return  True

    def handle(self):
        self.InitHandle()
        reqInfo = self.request.fileno()
        con = ESL.ESLconnection (reqInfo)
        self.sentence_id=None;
        self.GetChannelInfo (con)
        self.payback = payback (recordContextPath+'/dialogflow/'+self.scenceName+'.json')
        con.events ("json", "all")
        con.sendRecv ('myevents')
        con.sendRecv('divert_events')
        con.sendRecv('linger')
        if con.connected():
            print ("已经连接成功")
            #self.sayThread=threading.Thread (target=self.threadSay,args=(con,))
            #self.sayThread.start ()
            #print("说话线程已启动")
            self.SetChannelVariable(con)
            self.EventHandle(con)
            #self.myAsrModEvnetHandle(con)
        #self.sayThread.join()
        con.disconnect ()

    def saveDailogContext(self):
        filename = recordContextPath+'/dialogRecord/'+self.uuid+'.json'
        dcontexts=self.payback.context.getDialogContexts()
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

    def myAsrModEvnetHandle(self,con):
        print("我的asr测试开始")
        con.execute("answer","",self.uuid)
        con.execute('detect_speech','zw_asr {start-input-timers=false,no-input-timeout=1000}yes_no yes_no', self.uuid)
        #con.execute ("playback", "/root/workspace/zw_project/VoiceBot/record/beieronline/FAQ11.mp3", self.uuid)
        while 1:
            event =con.recvEvent()
            if event:
                ename=event.getHeader ("Event-Name")
                #print(event.serialize())
                if ename=='DETECTED_SPEECH':
                    statu = event.getHeader ("Speech-Statu")
                    body = event.getHeader ("_body")
                    print("statu:",statu,"  r:",body)
                    if statu=='13' or statu=='8' or statu=='16' or statu=='5':
                        print('resume')
                if ename=="SERVER_DISCONNECTED":
                    break

    def aliDetectedSpeech(self,con,event):
        statu = event.getHeader ("Speech-Statu")
        body = event.getHeader ("_body")
        #print("ali return:",body," statu:",statu)
        if statu == '5'   :
            uSay,s_id=self.parseJson(body)
            print("ali detected(", datetime.datetime.now(), ")", uSay,s_id)
            if  self.sentence_id!=s_id and uSay:
                self.sentence_id=s_id
                #print('is playing ',self.isPlaying)
                if self.isPlaying == False:
                    aiSay = self.fetchSayTxt (con, uSay)
                    #print ("uSay:", uSay)
                    if aiSay :
                        self.sayTo(con,aiSay,uSay)
                        self.isBreak = False
                elif self.isPlaying == True and  self.isBreak==False:
                    print('打断下：')
                    self.isBreak = True
                    con.api('uuid_fileman '+self.uuid+' pause')
                    aiSay = self.fetchSayTxt (con, uSay)
                    if aiSay :
                        print('停止说话')
                        con.api('uuid_fileman '+ self.uuid+' stop' )
                        self.sayTo(con,aiSay,uSay)
                    else:
                        con.api('uuid_fileman '+self.uuid+' pause')

        return  False

    def kdDetectedSpeech(self,con,event):
        con.execute ('detect_speech', 'pause', self.uuid)
        statu = event.getHeader ("Speech-Statu")
        body = event.getHeader ("_body")
        print ("kd Detected time:", datetime.datetime.now ())
        if statu == '5':
            uSay=self.kd_parseJson(body)
            if uSay and self.isPlaying == False:
                aiSay = self.fetchSayTxt (con, uSay)
                #print ("对话处理完 time:", datetime.datetime.now ())
                if  aiSay:
                    self.sayTo (con, aiSay, uSay);

    def kd_parseJson(self,jsonStr):
        strRet = '';
        if self.asr_resutlType=="json":
            ret = json.loads (jsonStr)
            for word in ret['ws']:
                for cword in word['cw']:
                    strRet+=cword['w']
                    break
        else:
            strRet =jsonStr
        print ("source:",jsonStr)
        print ("target:",strRet)
        return  strRet,None

    def parseJson(self,jsonStr):
        retStr=''
        sentence_id=None
        #print(jsonStr)
        if self.asr_resutlType=="json":
            ret = json.loads (jsonStr)
            if 'result' in ret:
                retStr=  ret["result"]["text"]
                sentence_id=ret["result"]["sentence_id"]
        else:
            retStr =jsonStr
        return retStr,sentence_id

    def EventHandle(self,con):
        print (self.uuid,"应答，开始对话")
        #self.EventAnswer(con,None)
        #con.execute ("playback", "/root/workspace/zw_project/VoiceBot/record/beieronline/FAQ11.mp3", self.uuid)
        while 1:
            event=con.recvEvent()
            if event:
                ename,euuid=self.GetEventInfo(event)
                #print("event:",ename)

                if (ename in self.switch) and self.switch[ename](con,event) == True:
                    break
                if ename=='SERVER_DISCONNECTED':
                    break
            self.SilenceTimeout(con)
        print('通话结束，事件监退出')

    def EventDetectedSpeech(self, con, event):
        self.unit_log_id += 1
        #self.asrIdlStartTime=None
        if self.asr_mader=="ali":
            return  self.aliDetectedSpeech(con,event)
        elif self.asr_mader=='bd':
            return  self.bdDetectedSpeech(con,event)
        elif self.asr_mader=="kd":
            return self.kdDetectedSpeech(con,event)
        return  False

    def bdDetectedSpeech(self,con,event):
        speechType = event.getHeader ("Speech-Type")

        if speechType == 'begin-speaking':
            print ('我听到有人在说话:')
        elif speechType == 'detected-speech':
            self.asrIdlStartTime=None
            asrResult=event.getHeader('_body')
            if asrResult and (not (asrResult == 'Completion-Cause: 002')):
                if self.isPlaying:
                    con.api('uuid_break ' + self.uuid)
                    self.isPlaying=False
                userSay=self.parseXml(asrResult)
                con.execute ("detect_speech", 'pause', self.uuid)
                aiSay=self.fetchSayTxt(con,userSay)
                if aiSay:
                    self.say (con,userSay)
                else:
                    con.execute ('detect_speech', 'resume', self.uuid)
        return False

    def EventHangup(self,con,event):
        print("挂断")
        return False

    def SilenceTimeout(self,con):
        isTimeOut= False if not self.asrIdlStartTime else (datetime.datetime.now() - self.asrIdlStartTime).seconds > self.silenceTimeout
        newSay=None
        if self.isAnswer==True and (not self.isPlaying)  and isTimeOut==True:
            if self.silenceTimes==0:
                #self.silenceTimeout=3
                newSay= self.payback.fetchQA ('GREET1')
            elif self.silenceTimes==1:
                #self.silenceTimeout = 2
                newSay = self.payback.fetchQA ('GREET2')
            elif self.silenceTimes==2:
                newSay = self.payback.fetchQA ('GREET3')
            else:
                text = self.fetchSayTxt (con)
                if text:
                    newSay=text
            if newSay and self.isPlaying == False:
                #self.inQueue(newSay)
            #if self.isPlaying == False:
                self.sayTo (con,newSay,"")
            self.silenceTimes+=1

    def EventAnswer(self,con,event):
        print("answered")
        if self.asr_mader=='ali':
            con.execute ('detect_speech', 'zw_asr {start-input-timers=false,no-input-timeout=1000}yes_no yes_no',  self.uuid)
        else :
            con.execute ('detect_speech','unimrcp {start-input-timers=false,no-input-timeout=1000}yes_no yes_no', self.uuid)
        #self.inQueue(self.payback.context.current_dn)
        #if self.isPlaying == False:
        self.sayTo (con,self.payback.context.current_dn,"")
        self.isAnswer=True
        return False

    def EventPlayStart(self,con,event):
        #print ("play start")
        #print(event.serialize('json'))
        self.isPlaying = True
        self.asrIdlStartTime =None
        #print ("play start time:", datetime.datetime.now (),self.isPlaying)
        #print (('PlayStart new', datetime.datetime.now()))
        return False

    def EventPlayStop(self,con,event):
        #print ("play end time:", datetime.datetime.now ())
        #print(event.serialize('json'))
        self.asrIdlStartTime = datetime.datetime.now ()
        if self.asr_mader=="ali":
            # last_offset= event.getHeader("variable_playback_last_offset_pos")
            # samples=event.getHeader("variable_playback_samples")
            # print("last_offset:",last_offset,"samples:",samples)
            # if samples!=last_offset:
            #     self.isBreak=True
            # else:
            #     self.isBreak=False
            pass
        elif self.asr_mader=="kd":
            con.execute ('detect_speech', 'resume', self.uuid)
        else:
            con.execute ('detect_speech', 'resume', self.uuid)
        self.isPlaying = False
        if self.payback.context.end == True:
            con.execute("hangup","",self.uuid)
        return False

    def parseXml(self,xmlStr):
        '''
        解析语音识别结果，获取说话内容
        :param xmlStr: 语言识别的ｘｍｌ内容
        :return: 说话内容
        '''
        if xmlStr:
            xdom=mdom.parseString (xmlStr)
            nod= xdom.documentElement.getElementsByTagName('input')
            #print (nod[0].childNodes[0].nodeValue)
            if nod[0] and nod[0].childNodes[0] and nod[0].childNodes[0].nodeValue:
                strtext= nod[0].childNodes[0].nodeValue
                return strtext[0:-1]
        return None

    def fetchSayTxt(self, con, txtFrom = "next"):
        if BotTcpHandler.uint_version==2:
            toTxt="AN1"
            method = ""
            toTxt, method = self.interop2(txtFrom)
            #print("unit return,txt:",toTxt,'method:',method)
            if method:
                toTxt = self.payback.fetchNext (method)
            elif toTxt :
                if toTxt=="AN1":
                    toTxt =self.payback.fetchNext('next')
                else:
                    toTxt =self.payback.fetchQA(toTxt)
            else:
                toTxt=None
        return toTxt

    '''
    def inQueue(self,aiSay):
        print("in queue:",aiSay)
        self.playQueue.put_nowait (aiSay)
    
    def threadSay(self,con):
        while 1:
            if not self.playQueue.empty():
                aiSay=self.playQueue.get_nowait();
                print ('out queue:',aiSay)
                self.sayTo(con,aiSay,'')
            else:
                time.sleep(1)
        return

    def say(self,con,utext=""):
        while  not self.playQueue.empty():
            aiSay=self.playQueue.get_nowait();
            print ('out queue:',aiSay)
            self.sayTo(con,aiSay,utext)
            print ('palying:')
        print("return :")
        return
    '''

    def sayTo(self,con,text,utext=""):
        if not text: #将无法获取unit结果的对话做不理会处理。
            return ;
        self.isPlaying=True
        print ('@人说:','(',datetime.datetime.now(),')', utext,self.payback.context.score)
        print ('                        @机器说:','(',datetime.datetime.now(),')', text['text'])
        self.payback.context.appendDialogContext (text, utext)
        if text["type"]=="tts":
            tts ='%s%s%s' % ("shout://tsn.baidu.com/text2audio?lan=zh&ctp=1&cuid=abcdxxx&tok="+BotTcpHandler.access_token+"&tex=" , text['text'].replace(" ",""), "&vol=9&per=0&spd=6&pit=3")
            con.execute ("playback", tts, self.uuid)
        elif text["type"]=="record":
            pb_str=self.get_playback_str(sys.path[0]+'/record/'+self.scenceName+"/",text["recordNumber"])
            if pb_str:
                con.execute ("playback", pb_str, self.uuid)
        else:
            print(text["type"],"is unknow play type,required tts or record(mp3,wav)")

    def interop2(self,text,userid='mifeng'):
        if text == "next":return '', text
        url='https://aip.baidubce.com/rpc/2.0/unit/bot/chat?access_token=' + self.access_token
        client_session={ "client_results":"", "candidate_options":[]}
        request={ "bernard_level":0,"query":text,"updates":"", "user_id":userid,
                  "query_info":{"asr_candidates":[],"source":"KEYBOARD","type":"TEXT"},
                  "client_session":json.dumps(client_session)}
        pd={'bot_session':self.bot_session,'log_id':self.unit_log_id,'request':request,"bot_id":self.scence,"version":"2.0"}
        content =self.urlRequest(url,pd)
        aistr = ''
        aimeth = ''
        if (content):
            if 'error_code' in  content and content['error_code']==0:
                self.bot_session='' #self.bot_session = content['result']['bot_session']
                aisay=content['result']['response']['action_list'][0]['say']
                aimethod=content['result']['response']['action_list'][0]['custom_reply']
                #if 'func' in aimethod :
                    #mdist = json.loads(aimethod)
                    #aimethod =mdist['func']
                if aisay:
                    aistr = aisay #s_str = s_ucode.encode ("utf-8")
                if aimethod:
                    aimeth=aimethod
                    if aimeth.index('func'):
                        aimethobj= json.loads(aimeth)
                        if 'func' in aimeth:
                            #print("ai method:",aimethobj)
                            aimeth=aimethobj["func"]
            elif content['error_code']!=0:
               print(( '错误玛: ' , content['error_code']))
               print(( '错误：',content['error_msg'].encode ("utf-8")))
        return aistr, aimeth

    def urlRequest(self,url,paramData):
        pjd = json.dumps (paramData)
        response = urllib3.PoolManager ().request ("POST", url, body=pjd.encode (), headers={'Content-Type': 'application/json'})
        return json.loads (response.data)

    def acd(self, con):
        print ("join acd function")
        # con.execute('answer', '', self.uuid)
        con.execute ('set', 'tts_engine=tts_commandline', self.uuid)
        con.execute ('set', 'tts_voice=Ting-Ting', self.uuid)
        # con.execute('set', 'continue_on_fail=true', self.uuid)  # 设置这个变量的意义在于,用于在呼叫坐席失败时,不挂断电话
        con.execute ('set', 'hangup_after_bridge=true', self.uuid)  # 设置这个变量的意义在于,在于成功bridge后(即成功接通之后)坐席首先挂机,则挂断电话
        # con.execute('speak', '您好,欢迎致电,电话接通中,请稍候', self.uuid)  # 在播放完欢迎的声音之后,继续播放音乐,直到转到坐席

        con.execute ('playback', '/workspace/BeierVoice/record/beieronline/music.mp3', self.uuid)  # 播放一段音频直到电话接通
        time.sleep (50)  # 延时2s
        dial = 'user/' + '1001'  # self.FindAvailableAgent()
        print ("dial:", dial)
        con.execute ('bridge', dial, self.uuid)  # 桥接到找到的坐席

    def  get_playback_str(self,path,records):
        r_str=None
        for  record in records:
            if r_str:
                if record in 'money':
                    tts = '%s%s%s' % (
                    "shout://tsn.baidu.com/text2audio?lan=zh&ctp=1&cuid=abcdxxx&tok=" + BotTcpHandler.access_token + "&tex=",
                    self.money+"元", "&vol=9&per=0&spd=6&pit=3")
                    r_str += "@" + tts
                elif record == 'name':
                    tts = '%s%s%s' % (
                    "shout://tsn.baidu.com/text2audio?lan=zh&ctp=1&cuid=abcdxxx&tok=" + BotTcpHandler.access_token + "&tex=",
                    self.c_name+'吗？', "&vol=9&per=0&spd=6&pit=3")
                    r_str+="@"+tts
                else:
                    r_str+="@"+path+record+".mp3"
            else:
                r_str = path+record+".mp3"
        return  r_str


    def combine_record(self,record):
        if record =="money":
            pass
        elif  record=='alias':
            pass
        elif  record=='over_time':
            pass


