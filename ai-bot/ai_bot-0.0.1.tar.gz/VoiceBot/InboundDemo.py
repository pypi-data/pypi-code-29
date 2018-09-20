#coding:utf-8

import ESL
import socketserver



def dail(con,number):
    #9720    2490
    #dail_str='originate user/'+number+' &echo'
    #dail_str='originate sofia/gateway/yuneasy0794/15062405910 &playback /usr/local/freeswitch/recordings/archive/test.wav'
    #dail_str = 'originate user/1005 ai01 xml default'
    #dail_str = 'originate 8888 &bridge(user/1000)'
    # 13772491757  祝  13916483739 张 15062405910,17321307255  李 18209288679
    dail_str='originate {originattion_caller_id_number=7777,Scence_id=9720,Scence_name=yundaozichan,callee_id_number='+number+',config_name=testbot}sofia/gateway/yuneasy0794/'+number+' 7777 xml default'
    #dail_str = 'originate  sofia/gateway/yuneasy0794/' + number+' &socket(127.0.0.1:8040 async full)'
    #dail_str='originate sofia/gateway/yuneasy0794/'+number+' socket:192.168.3.146:8040 async  full'zhongzilian

    #dail_str = 'originate user/1000 8888 xml default'
    print(dail_str)
    return con.api(dail_str)

def autoDail():
    con =ESL.ESLconnection('114.116.39.18','8021','ClueCon')
    if con.connected():
        print ( '已链接上')
        con.events('json','all')
        evt = dail (con, '13772491757')
        while 1:
            evt =con.recvEvent()
            if evt :
                evt_name=evt.getHeader("Event-Name")
                print (("event :", evt_name))
                print(evt.serialize ('json'))
                if evt_name=="SERVER_DISCONNECTED" or evt_name=="CHANNEL_DESTROY":
                    break
                if evt_name=='CHANNEL_ANSWER':
                    pass
                if  evt_name=='CHANNEL_HANGUP':
                    print ()
                    break
                if  evt_name=='CHANNEL_STATE'  or evt_name=='CHANNEL_CALLSTATE':
                    pass
                 #print (evt.serialize ('json'))


    con.disconnect()
    #print '已断开链接'

if __name__ == '__main__':
    autoDail()
    print('结束拨号过程')
