#coding:utf-8

import ESL
import  socketserver
import json
import aip
import  xml.dom.minidom as mdom
import datetime
import time
import uuid
import urllib, urllib3, sys,urllib3
import ssl
from MyDialog.d_payback import *

class MyTCPHandler(socketserver.BaseRequestHandler):
    session_id = ''
    bot_session = ''
    # access_token = '24.11cf4eba845cde3fdea8d4c1930650f9.2592000.1526029091.282335-10938323'
    access_token = '24.3cc7f347e9ca4740cabf1164905d6d15.2592000.1529578415.282335-11126101'
    # scene_id='19157'
    scene_id ='2490' #'1821'  # '1698'#'1493'#'20775'#'20159'#
    log_id = 1;
    unit_v = 2
    count = 0   #创建一个类变量

    def __init__(self, request, client_address, server):
        super().__init__(request,client_address,server)


    def handle(self):
        print(( self.client_address,'connected!'))
        self.payback = payback ('beieronlinebak.json')
        fd= self.request.fileno()
        print (fd)
        con=ESL.ESLconnection(fd)
        con.events("json","ALL")
        #con.sendRecv('events json ALL')
        #con.sendRecv ('myevents')
        #con.sendRecv('linger')
        #con.sendRecv ('divert_event')
        self .hello="我是"

        print (( 'accept:',con.connected()))
        if con.connected():
            info = con.getInfo ()
            uuid = info.getHeader ('unique-id')
            cname = info.getHeader ('Channel-Channel-Name')
            con.execute ('set', 'fire_asr_events=true', uuid)
            con.execute ('set', "rtp_enable_vad_out=true", uuid)
            con.execute ("set", 'record_sample_rate=16000', uuid)
            self.playAndDetectSpeech(con,uuid)
            print( '准备退出')
            if  con.connected():
                #con.execute ("hangup", '', uuid)
                con.disconnect ()
                pass
            print ((cname, '已经退出'))

    def playAndDetectSpeech(self,con,uuid):

        le_sequence=0
        count=1

        isanswer=False
        canstop=False
        idlstart=None
        secondtemp = 15
        con.execute ("answer", "", uuid)
        while 1:
            e_info = con.recvEventTimed(10)
            if (not canstop) and idlstart and isanswer == True and (datetime.datetime.now() - datetime.timedelta(seconds=secondtemp) > idlstart):
                print (( '静音时段: start :',idlstart,'end:',datetime.datetime.now (),'静音连续次数：',count))
                if count==1:
                    secondtemp = 5
                    self.say (con, uuid, self.payback.fetchQA('GREET1'))
                elif count==2:
                    secondtemp = 2
                    self.say (con, uuid, self.payback.fetchQA('GREET2'))
                elif count==3:
                    secondtemp = 2
                    self.say (con, uuid, self.payback.fetchQA('GREET3'))
                elif count >= 4:
                    text = self.fetchSayTxt(con, uuid)
                    secondtemp = 2
                    if  text:
                        self.say(con, uuid, text)
                    else:
                        pass
                    #count=2
                    #secondtemp = 15
                count+=1
                idlstart=datetime.datetime.now ()
                #print  'idlestart in begin:', idlstart
            if e_info:
                ename=e_info.getHeader("Event-Name")
                e_sequence =e_info.getHeader("Event-Sequence")
                #print(ename)
                if ename=="CHANNEL_ANSWER":
                    con.execute ('detect_speech',
                                 'unimrcp {start-input-timers=false,no-input-timeout=1000}yes_no yes_no', uuid)
                    #con.execute ("playback", "/root/workspace/zw_project/VoiceBot/record/beieronline/f0lll1.mp3", uuid)
                    self.say (con, uuid, self.payback.context.current_dn)
                    isanswer = True
                if  ename== 'PLAYBACK_STOP':
                    print("p stop")
                    canstop=False
                    con.execute ('detect_speech', 'resume', uuid)
                    if self.payback.context.end:
                        break
                if ename=='PLAYBACK_START':
                    print ("p start")
                    canstop=True
                    idlstart=None
                if ename=='PRIVATE_COMMAND':
                    if isanswer:
                        print(('PRIVATE_COMMAND',idlstart))
                        if not canstop:
                            idlstart = datetime.datetime.now ()
                        else :
                            idlstart =None
                        print (('PRIVATE_COMMAND new', idlstart))
                    print("secondtemp:",secondtemp)
                if ename=='DETECTED_SPEECH' and le_sequence!=e_sequence:
                    le_sequence=e_sequence
                    speechType = e_info.getHeader ("Speech-Type")
                    self.log_id+=1
                    if speechType=='begin-speaking':
                        print( '我听到有人在说话:')
                        #con.execute ('uuid_break', uuid, uuid)
                    elif speechType == 'detected-speech':
                        idlstart = None
                        count=4
                        recogResults=e_info.getHeader('_body')
                        if recogResults == 'Completion-Cause: 002':
                            pass
                        else:
                            if canstop:
                                con.api('uuid_break '+uuid)
                                canstop=False
                            ttext = self.parseXml (recogResults)
                            con.execute ("detect_speech", 'pause', uuid)
                            text = self.fetchSayTxt(con, uuid, ttext)
                            print(("静音",secondtemp,idlstart))
                            if (not self.payback.context.end) and text :
                                print (('你说:', ttext))
                                secondtemp = len (text['text']) / 7  # 识别到正常语音，询问间隔又设置为10s
                                if secondtemp < 5: secondtemp = 5
                                self.say (con, uuid, text,ttext)
                            elif text:
                                secondtemp = len (text['text']) / 7  # 识别到正常语音，询问间隔又设置为10s
                                if secondtemp < 5:
                                    secondtemp = 5
                                    self.say(con, uuid, text,ttext)
                            else:
                                    break
                    elif speechType == 'closed':
                        #print '语音识别被closed.'
                        break
                    else:
                        pass
                if ename=='CHANNEL_HANGUP':
                    break

    def parseXml(self,xmlStr):
        if xmlStr:
            xdom=mdom.parseString (xmlStr)
            nod= xdom.documentElement.getElementsByTagName('input')
            print (nod[0].childNodes[0].nodeValue)
            if nod[0] and nod[0].childNodes[0] and nod[0].childNodes[0].nodeValue:
                strtext= nod[0].childNodes[0].nodeValue
            else:
                strtext='你说什么,我没有听清!'
            return strtext[0:-1]
        return "中华人民共和国"

    def fetchSayTxt(self, con, uuid, txtFrom = "next"):
        if self.unit_v==1:
            toTxt, sid = self.interop(txtFrom, self.session_id)
            self.session_id = sid
        if self.unit_v==2:
            #print  "unit调用:",
            toTxt, method = self.interop2(txtFrom,self.bot_session)
            print(("unit 返回结果:（对话内容）", toTxt,"|（内部方法）",method))
            if toTxt == '您要问的是以下哪个问题？' :
                toTxt = self.payback.fetchNext ("WHAT")
            elif method:
                toTxt = self.payback.fetchNext (method)
            elif toTxt :
                if toTxt=="AN1":
                    toTxt =self.payback.fetchQA('next')
                else:
                    toTxt =self.payback.fetchQA(toTxt)
            else:
                toTxt=None
        return toTxt

    def recordVoice(self,con,uuid,voiceNumber):
        #print  '开始录音'
        con.execute("record", '/usr/local/freeswitch/recordings/archive/' + str(voiceNumber) + '.wav 20 2000 2', uuid)
        # con.execute ("record_session", '/usr/local/freeswitch/recordings/archive/' + uuid + '.wav', uuid)

    def setChannelVerb(self,con,uuid):
        con.execute ("set", 'record_sample_rate=44100', uuid)
        # con.execute ("set", 'vad=out', uuid)

    def say(self,con,uuid,text,utext=""):
        print((  '机器说:', text['text']))
        if text["type"]=="tts":
            self.payback.context.appendDialogContext(utext,text)
            #tts_str_bd ='%s%s%s' % ("shout://tsn.baidu.com/text2audio?lan=zh&ctp=1&cuid=abcdxxx&tok=24.11cf4eba845cde3fdea8d4c1930650f9.2592000.1526029091.282335-10938323&tex=" , text, "&vol=9&per=0&spd=5&pit=5")
            playstr ='%s%s%s' % ("shout://tsn.baidu.com/text2audio?lan=zh&ctp=1&cuid=abcdxxx&tok="+self.access_token+"&tex=" , text['text'].replace(" ",""), "&vol=9&per=0&spd=6&pit=3")
            con.execute ("playback", playstr, uuid)
            #print "tts:",tts_str_bd
        elif text["type"]=="record":
            playstr="/root/workspace/zw_project/VoiceBot/record/beieronline/"+text["recordNumber"]+".mp3"
            print(playstr)
            con.execute ("playback", playstr, uuid)

    def interop2(self,text,bot_session,userid='mifeng'):
        if text == "next":
            return '', text
        url='https://aip.baidubce.com/rpc/2.0/unit/bot/chat?access_token=' + self.access_token
        client_session={ "client_results":"", "candidate_options":[]}
        request={
            "bernard_level":0,
            "query":text,
            "updates":"",
            "user_id":userid,
            "query_info":{"asr_candidates":[],"source":"KEYBOARD","type":"TEXT"},
            "client_session":json.dumps(client_session)
        }
        pd={'bot_session':self.bot_session,'log_id':self.log_id,'request':request,"bot_id":self.scene_id,"version":"2.0"}
        print ('bot s:',pd)
        content =self.urlRequest(url,pd)
        #print  content
        if (content):
            if 'error_code' in  content and content['error_code']==0:
                #self.bot_session = content['result']['bot_session']
                self.bot_session='';
                s_ucode=content['result']['response']['action_list'][0]['say']
                method=content['result']['response']['action_list'][0]['custom_reply']
                if s_ucode:
                    s_str = s_ucode
                    #s_str = s_ucode.encode ("utf-8")
                else:
                    s_str=''
                if method:
                   s_m_str=method
                else:
                    s_m_str=""
                return s_str,s_m_str
            elif content['error_code']!=0:
               print(( '错误玛: ' , content['error_code']))
               print(( '错误：',content['error_msg'].encode ("utf-8")))
        return '您说什么,没听清?', ''

    def interop(self,text,session_id):
        #host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=abcdexxx&client_id=s4eB21vTQssWoYlBd8jTAHVQ&client_secret=HOcBpqXuHeoGe16Gt13TQ0eUUGR8MsOs '
        url = 'https://aip.baidubce.com/rpc/2.0/solution/v1/unit_utterance?access_token=' + self.access_token
        pd={'scene_id':self.scene_id,'query':text,'session_id':session_id}
        #print '对话', pd
        content =self.urlRequest(url,pd)
        #print 'unit 返回结果：',content
        if (content):
            if 'result' in content and content['result'] and content['result']['qu_res']:
               # print  content['result']['action_list']
                s_ucode = content['result']['action_list'][0]['say']
                s_str=s_ucode.encode("utf-8")
                self.session_id = content['result']['session_id']
                #print  s_str,s_ucode
                return  s_str,self.session_id
        return  '您说什么,没听清?',''

    def urlRequest(self,url,paramData):
        pjd = json.dumps (paramData)
       # print (pjd)
        response = urllib3.PoolManager ().request ("POST", url, body=pjd.encode (), headers={'Content-Type': 'application/json'})
        #print (response.data)
        return json.loads (response.data)

server=socketserver.ThreadingTCPServer(("",8040),MyTCPHandler)
server.serve_forever()

