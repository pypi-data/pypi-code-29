from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os
# import pandas   写csv文件
import json
import requests
from pyaudio import PyAudio,paInt16
import wave
import numpy as np
import pygame
import time
from aip import AipSpeech
import soundfile as sf
import matplotlib.pyplot as plt
import urllib
import http.client
import random
import hashlib

role ='女孩'#line:2
global parwidth #line:3
parwidth =600 #line:4
APP_ID ='10698474'#line:6
API_KEY ='hxGbVfeU15rnpw8s9SBWkixq'#line:7
SECRET_KEY ='48O289dZ81bALiWBGNySH6P91dtQ5zn5'#line:8
client =AipSpeech (APP_ID ,API_KEY ,SECRET_KEY )#line:9
modelflog ='唤醒'#line:12
ipStr ='http://jiaoxue.vipcode.cn/'#line:17
global filename #line:19
filename =""#line:20
class PyQt5_QDialog (QDialog ):#line:23
    def __init__ (O0OO0000OOO0000OO ):#line:24
        super ().__init__ ()#line:25
        O0OO0000OOO0000OO .setObjectName ("dialog")#line:26
        global parwidth #line:27
        parwidth =O0OO0000OOO0000OO .width ()+200 #line:28
    def clear_translate (OO00OOOO000000O00 ):#line:30
        QApplication .processEvents ()#line:31
        OO00OOOO000000O00 .translate_1 .setText ("")#line:32
        OO00OOOO000000O00 .translate_2 .setText ("")#line:33
    def initChat (O0O000O0OO000O0OO ,OOOO0O000O0OO0O00 ):#line:35
        O0O000O0OO000O0OO .a =ChatT (OOOO0O000O0OO0O00 )#line:36
        O0O000O0OO000O0OO .a .start ()#line:37
    def playGif (O000O0OO0OOO00O00 ,OOOO0O0O0OO0O000O ):#line:39
        O000O0OO0OOO00O00 .gif =QMovie ('../RESOURCE/gif/'+OOOO0O0O0OO0O000O +'.gif')#line:41
        O000O0OO0OOO00O00 .gif .setScaledSize (O000O0OO0OOO00O00 .gifLabel .size ())#line:43
        O000O0OO0OOO00O00 .gifLabel .setMovie (O000O0OO0OOO00O00 .gif )#line:45
        O000O0OO0OOO00O00 .gif .start ()#line:47
    def addmine_label (O000OOO00O0OO0OO0 ):#line:49
        O000OOO00O0OO0OO0 .mine_label =PyQt5_Qlabel (O000OOO00O0OO0OO0 ,42 ,130 ,300 ,2000 )#line:50
        O000OOO00O0OO0OO0 .mine_label .setTextColor ("gray")#line:51
        O000OOO00O0OO0OO0 .mine_label .setFontFitSize (15 )#line:52
        O000OOO00O0OO0OO0 .mine_label .setWordWrap (True )#line:53
        O000OOO00O0OO0OO0 .mine_label .addScorell (42 ,130 ,0 ,48 )#line:54
        O000OOO00O0OO0OO0 .mine_label .setAlignment (Qt .AlignTop )#line:55
        return O000OOO00O0OO0OO0 .mine_label #line:56
    def addtranslate_1 (OO0OOO0OOOO00OO00 ):#line:57
        OO0OOO0OOOO00OO00 .translate_1 =PyQt5_Qlabel (OO0OOO0OOOO00OO00 ,52 ,183 ,300 ,2000 )#line:58
        OO0OOO0OOOO00OO00 .translate_1 .setTextColor ("gray")#line:59
        OO0OOO0OOOO00OO00 .translate_1 .setFontFitSize (15 )#line:60
        OO0OOO0OOOO00OO00 .translate_1 .setWordWrap (True )#line:61
        OO0OOO0OOOO00OO00 .translate_1 .addScorell (52 ,183 ,0 ,45 )#line:62
        OO0OOO0OOOO00OO00 .translate_1 .setAlignment (Qt .AlignTop )#line:63
        return OO0OOO0OOOO00OO00 .translate_1 #line:64
    def addlion_label (OOOOOOO00OO0O000O ):#line:65
        OOOOOOO00OO0O000O .lion_label =PyQt5_Qlabel (OOOOOOO00OO0O000O ,42 ,231 ,300 ,2000 )#line:66
        OOOOOOO00OO0O000O .lion_label .setTextColor ("white")#line:67
        OOOOOOO00OO0O000O .lion_label .setFontFitSize (16 )#line:68
        OOOOOOO00OO0O000O .lion_label .setWordWrap (True )#line:69
        OOOOOOO00OO0O000O .lion_label .addScorell (42 ,240 ,0 ,50 )#line:70
        OOOOOOO00OO0O000O .lion_label .setAlignment (Qt .AlignTop )#line:71
        return OOOOOOO00OO0O000O .lion_label #line:72
    def addtranslate_2 (O000OO0OOO00OOOO0 ):#line:73
        O000OO0OOO00OOOO0 .translate_2 =PyQt5_Qlabel (O000OO0OOO00OOOO0 ,52 ,291 ,300 ,2000 )#line:74
        O000OO0OOO00OOOO0 .translate_2 .setTextColor ("white")#line:75
        O000OO0OOO00OOOO0 .translate_2 .setFontFitSize (16 )#line:76
        O000OO0OOO00OOOO0 .translate_2 .setWordWrap (True )#line:77
        O000OO0OOO00OOOO0 .translate_2 .addScorell (52 ,300 ,0 ,47 )#line:78
        O000OO0OOO00OOOO0 .translate_2 .setAlignment (Qt .AlignTop )#line:79
        return O000OO0OOO00OOOO0 .translate_2 #line:80
    def addTranslate (OO0O0OOOOO00000O0 ):#line:81
        OO0O0OOOOO00000O0 .munu_translate1 =OO0O0OOOOO00000O0 .mine_label .addRightMenu ("翻译")#line:82
        OO0O0OOOOO00000O0 .munu_translate2 =OO0O0OOOOO00000O0 .lion_label .addRightMenu ("翻译")#line:83
        OO0O0OOOOO00000O0 .munu_translate2 .triggered .connect (lambda :translates (OO0O0OOOOO00000O0 .lion_label ,OO0O0OOOOO00000O0 .translate_2 ))#line:84
        OO0O0OOOOO00000O0 .munu_translate1 .triggered .connect (lambda :translates (OO0O0OOOOO00000O0 .mine_label ,OO0O0OOOOO00000O0 .translate_1 ))#line:85
    def setBackgroundColor (OOOO0000OOOO00O0O ,OO00O00O00OOOOOO0 ):#line:87
        OOOO0000OOOO00O0O .setStyleSheet ("#dialog{background-color:"+OO00O00O00OOOOOO0 +"}")#line:88
    def setBackground (O0O00OOO00O0O0000 ,OOO0O00O0O00O0O00 ):#line:89
        O0O00OOO00O0O0000 .setStyleSheet ("#dialog{border-image:url(../RESOURCE/drawable/"+OOO0O00O0O00O0O00 +")}")#line:90
    def initRepeat (OO0OO000O0O00O0OO ,OOO00OO00O00O00OO ):#line:92
        OO0OO000O0O00O0OO .repeatT =RepeatT (OOO00OO00O00O00OO )#line:93
        OO0OO000O0O00O0OO .repeatT .start ()#line:94
    def setResize (OO0OOOOOO000OOO00 ,OO00O0O0OOO0OOO00 ,O0O00OOOO0000O000 ):#line:96
        OO0OOOOOO000OOO00 .resize (OO00O0O0OOO0OOO00 ,O0O00OOOO0000O000 )#line:97
    def addChatButton (OO00O0OO00O0O00O0 ,O00O0O0OOO0OOO0O0 ):#line:99
        OO00O0OO00O0O00O0 .uiSpeech =O00O0O0OOO0OOO0O0 ()#line:100
        OO0O0OOO000000O0O =PyQt5_QPushButton (OO00O0OO00O0O00O0 ,60 ,100 ,57 ,57 )#line:102
        OO0O0OOO000000O0O .setBackground ("liaotian.png")#line:104
        OO0O0OOO000000O0O .setPressedBackground ("liaotian1.png")#line:106
        OO0O0OOO000000O0O .clicked .connect (OO00O0OO00O0O00O0 .chatClicked )#line:108
    def chatClicked (O00OO0OO00O00OOO0 ):#line:109
        O00OO0OO00O00OOO0 .hide ()#line:110
        O00OO0OO00O00OOO0 .uiSpeech .setupUI ()#line:112
        O00OO0OO00O00OOO0 .uiSpeech .showDialog ()#line:113
        O00OO0OO00O00OOO0 .uiSpeech .exec_ ()#line:114
        O00OO0OO00O00OOO0 .show ()#line:116
    def addBodyButton (OOO00OOOOO0O00OO0 ,OO0OO0OO0OO0O00O0 ):#line:118
        OOO00OOOOO0O00OO0 .bodylabel =OO0OO0OO0OO0O00O0 #line:119
        OOO00OOOOO0O00OO0 .head =PyQt5_QPushButton (OOO00OOOOO0O00OO0 ,400 ,300 ,160 ,130 )#line:120
        OOO00OOOOO0O00OO0 .head .setBackgroundColor ("rgba(100,0, 200, 0)")#line:121
        OOO00OOOOO0O00OO0 .body =PyQt5_QPushButton (OOO00OOOOO0O00OO0 ,445 ,430 ,70 ,80 )#line:123
        OOO00OOOOO0O00OO0 .body .setBackgroundColor ("rgba(100,0, 200, 0)")#line:124
        OOO00OOOOO0O00OO0 .leftArm =PyQt5_QPushButton (OOO00OOOOO0O00OO0 ,420 ,430 ,40 ,30 )#line:126
        OOO00OOOOO0O00OO0 .leftArm .setBackgroundColor ("rgba(0,0, 0, 0)")#line:127
        OOO00OOOOO0O00OO0 .rightArm =PyQt5_QPushButton (OOO00OOOOO0O00OO0 ,505 ,430 ,50 ,30 )#line:129
        OOO00OOOOO0O00OO0 .rightArm .setBackgroundColor ("rgba(0,0, 0, 0)")#line:130
        OOO00OOOOO0O00OO0 .leftFoot =PyQt5_QPushButton (OOO00OOOOO0O00OO0 ,440 ,500 ,30 ,30 )#line:132
        OOO00OOOOO0O00OO0 .leftFoot .setBackgroundColor ("rgba(0,0, 0, 0)")#line:133
        OOO00OOOOO0O00OO0 .rightFoot =PyQt5_QPushButton (OOO00OOOOO0O00OO0 ,500 ,500 ,30 ,30 )#line:135
        OOO00OOOOO0O00OO0 .rightFoot .setBackgroundColor ("rgba(0,0, 0, 0)")#line:136
        OOO00OOOOO0O00OO0 .head .clicked .connect (OOO00OOOOO0O00OO0 .headClicked )#line:138
        OOO00OOOOO0O00OO0 .leftArm .clicked .connect (OOO00OOOOO0O00OO0 .armClicked )#line:139
        OOO00OOOOO0O00OO0 .rightArm .clicked .connect (OOO00OOOOO0O00OO0 .armClicked )#line:140
        OOO00OOOOO0O00OO0 .rightFoot .clicked .connect (OOO00OOOOO0O00OO0 .rightFootClicked )#line:141
        OOO00OOOOO0O00OO0 .leftFoot .clicked .connect (OOO00OOOOO0O00OO0 .leftFootClicked )#line:142
        OOO00OOOOO0O00OO0 .body .clicked .connect (OOO00OOOOO0O00OO0 .bodyClicked )#line:143
    def armClicked (O00O0O0O00OO00O00 ):#line:144
        O00O0O0O00OO00O00 .neibu2 ('main_arm')#line:145
        O00O0O0O00OO00O00 .neibu1 ('main_arm')#line:150
    def leftFootClicked (O0O00OOOOOOOOOOOO ):#line:151
        O0O00OOOOOOOOOOOO .neibu2 ('main_leftFoot')#line:152
        O0O00OOOOOOOOOOOO .playAudio ('main_leftFoot')#line:153
    def rightFootClicked (O00OO00O0O00O000O ):#line:154
        O00OO00O0O00O000O .neibu2 ('main_rightFoot')#line:155
        O00OO00O0O00O000O .playAudio ('main_rightFoot')#line:156
    def bodyClicked (O0000000O0OOO00OO ):#line:157
        O0000000O0OOO00OO .neibu2 ('main_body')#line:158
        O0000000O0OOO00OO .playAudio ('main_body')#line:159
    def headClicked (OO00OOOOOO0O00O00 ):#line:160
        OO00OOOOOO0O00O00 .neibu2 ('main_head')#line:161
        OO00OOOOOO0O00O00 .playAudio ('main_head')#line:162
    def neibu2 (OOOO0OOO000000000 ,OO00O0O0O00O0OO0O ):#line:164
        OOOO0OOO000000000 .neigif =PyQt5_QMovie (OO00O0O0O00O0OO0O +'.gif')#line:166
        OOOO0OOO000000000 .neigif .setScaledSize (OOOO0OOO000000000 .bodylabel .size ())#line:168
        OOOO0OOO000000000 .bodylabel .setMovie (OOOO0OOO000000000 .neigif )#line:170
        OOOO0OOO000000000 .neigif .start ()#line:172
        OOOO0OOO000000000 .frameCount =OOOO0OOO000000000 .neigif .frameCount ()#line:173
        OOOO0OOO000000000 .neigif .frameChanged .connect (OOOO0OOO000000000 .neibu3 )#line:175
    def neibu3 (O0OO00000OOOOOOO0 ):#line:176
        O0OO00000OOOOOOO0 .frameCount -=1 #line:178
        if O0OO00000OOOOOOO0 .frameCount ==0 :#line:180
            O0OO00000OOOOOOO0 .neigif .stop ()#line:182
            O0OO00000OOOOOOO0 .neigif =PyQt5_QMovie ('main_lion.gif')#line:184
            O0OO00000OOOOOOO0 .neigif .setScaledSize (O0OO00000OOOOOOO0 .bodylabel .size ())#line:185
            O0OO00000OOOOOOO0 .bodylabel .setMovie (O0OO00000OOOOOOO0 .neigif )#line:187
            O0OO00000OOOOOOO0 .neigif .start ()#line:189
    def neibu1 (O00O0OO000000O000 ,O00000OOO0OO00O00 ):#line:191
        O0O000OO000OOOO0O =PyQt5_QMediaPlayer ()#line:193
        O0O000OO000OOOO0O .prepare_audio (O00000OOO0OO00O00 +'.wav')#line:195
        O0O000OO000OOOO0O .play ()#line:197
class PyQt5_QPushButton (QPushButton ):#line:200
    def __init__ (O0OO00OOO0O00OOO0 ,O0OO0O00O00OO0000 ,x =0 ,y =0 ,width =113 ,height =32 ):#line:201
        super ().__init__ (O0OO0O00O00OO0000 )#line:202
        O0OO00OOO0O00OOO0 .setGeometry (x ,y ,width ,height )#line:203
    def setBackground (OOO00O0O0O0OOO000 ,OO0OOOOO0OOO0OOO0 ):#line:205
        OOO00O0O0O0OOO000 .setStyleSheet (OOO00O0O0O0OOO000 .styleSheet ()+"QPushButton{border-image:url(../RESOURCE/drawable/"+OO0OOOOO0OOO0OOO0 +")}")#line:207
    def setPressedBackground (OOOO0O00O0O0O000O ,OOOOO0O00O000O00O ):#line:209
        OOOO0O00O0O0O000O .setStyleSheet (OOOO0O00O0O0O000O .styleSheet ()+"QPushButton:pressed{border-image:url(../RESOURCE/drawable/"+OOOOO0O00O000O00O +")}")#line:211
    def setBackgroundColor (OOO0O0O0OO000O000 ,O00000O000OO0O0OO ):#line:213
        OOO0O0O0OO000O000 .setStyleSheet (OOO0O0O0OO000O000 .styleSheet ()+"QPushButton{background-color:"+O00000O000OO0O0OO +"}")#line:214
    def setTextColor (O0O0000OOOOO0OOO0 ,OOOO00OOO00O0O000 ):#line:216
        O0O0000OOOOO0OOO0 .setStyleSheet (O0O0000OOOOO0OOO0 .styleSheet ()+"QPushButton{color:"+OOOO00OOO00O0O000 +"}")#line:217
    def setPressedTextColor (OO00O0O0O0000O000 ,O000O00O0OO0OOO0O ):#line:219
        OO00O0O0O0000O000 .setStyleSheet (OO00O0O0O0000O000 .styleSheet ()+"QPushButton:pressed{color:"+O000O00O0OO0OOO0O +"}")#line:220
    def setFontSize (O0OO0O0OOO00OOOOO ,O0O00OOO0OOOOO00O ):#line:222
        O0O0O00000O0OO00O =QFont ()#line:223
        O0O0O00000O0OO00O .setPixelSize (O0O00OOO0OOOOO00O )#line:224
        O0OO0O0OOO00OOOOO .setFont (O0O0O00000O0OO00O )#line:225
class PyQt5_QLineEdit (QLineEdit ):#line:228
    Password =QLineEdit .Password #line:229
    Normal =QLineEdit .Normal #line:230
    NoEcho =QLineEdit .NoEcho #line:231
    PasswordEchoOnEdit =QLineEdit .PasswordEchoOnEdit #line:232
    def __init__ (OOOO0000000OO0000 ,O0O0000O0OO0000OO ,x =0 ,y =0 ,width =113 ,height =21 ):#line:234
        super ().__init__ (O0O0000O0OO0000OO )#line:235
        OOOO0000000OO0000 .setGeometry (x ,y ,width ,height )#line:236
        OOOO0000000OO0000 .setFontSize (14 )#line:237
        OOOO0000000OO0000 .setAlignment (Qt .AlignVCenter )#line:238
    def setFontSize (OO00OO000O0OO00OO ,O00OOOOOOO0O00OO0 ):#line:240
        OO0OO0OOO0000O0OO =QFont ()#line:241
        OO0OO0OOO0000O0OO .setPixelSize (O00OOOOOOO0O00OO0 )#line:242
        OO00OO000O0OO00OO .setFont (OO0OO0OOO0000O0OO )#line:243
    def setBackground (O0OOOO00OO0O00O0O ,O0000000OOO0OOO0O ):#line:245
        O0OOOO00OO0O00O0O .setStyleSheet (O0OOOO00OO0O00O0O .styleSheet ()+"border-image:url(../RESOURCE/drawable/"+O0000000OOO0OOO0O +");")#line:246
    def setBackgroundColor (O0O00O000000O0OOO ,O0OO0000O0O0OO0O0 ):#line:248
        O0O00O000000O0OOO .setStyleSheet (O0O00O000000O0OOO .styleSheet ()+"background-color:"+O0OO0000O0O0OO0O0 +";")#line:249
    def setTextColor (O0O0O0O000OO0O0O0 ,O0O0OO0000OOO00O0 ):#line:251
        O0O0O0O000OO0O0O0 .setStyleSheet (O0O0O0O000OO0O0O0 .styleSheet ()+"color:"+O0O0OO0000OOO00O0 +";")#line:252
    def setDisplayMode (OOO00O000OO0OO00O ,OOOOOOO00O0O00O00 ):#line:254
        if OOOOOOO00O0O00O00 ==PyQt5_QLineEdit .Password :#line:255
            OOO00O000OO0OO00O .setEchoMode (OOOOOOO00O0O00O00 )#line:256
        elif OOOOOOO00O0O00O00 ==PyQt5_QLineEdit .Normal :#line:257
            OOO00O000OO0OO00O .setEchoMode (OOOOOOO00O0O00O00 )#line:258
        elif OOOOOOO00O0O00O00 ==PyQt5_QLineEdit .NoEcho :#line:259
            OOO00O000OO0OO00O .setEchoMode (OOOOOOO00O0O00O00 )#line:260
        elif OOOOOOO00O0O00O00 ==PyQt5_QLineEdit .PasswordEchoOnEdit :#line:261
            OOO00O000OO0OO00O .setEchoMode (OOOOOOO00O0O00O00 )#line:262
class PyQt5_Qlabel (QLabel ):#line:265
    clicked =pyqtSignal (QMouseEvent )#line:266
    def __init__ (O0OOOOO0OO000O00O ,O000O0000OO0OOO00 ,x =0 ,y =0 ,width =60 ,height =16 ):#line:267
        super ().__init__ (O000O0000OO0OOO00 )#line:268
        O0OOOOO0OO000O00O .widget =O000O0000OO0OOO00 #line:269
        O0OOOOO0OO000O00O .zeze =True #line:270
        O0OOOOO0OO000O00O .menu =QMenu (O0OOOOO0OO000O00O )#line:271
        O0OOOOO0OO000O00O .customContextMenuRequested ['QPoint'].connect (lambda :O0OOOOO0OO000O00O .menu .exec_ (QCursor .pos ()))#line:272
        O0OOOOO0OO000O00O .setGeometry (x ,y ,width ,height )#line:273
    def setFontSize (OOO00OOO000O0OO00 ,O0OO0OOOO0O0OO000 ):#line:274
        OO0OOO0O0O00O000O =QFont ()#line:275
        OO0OOO0O0O00O000O .setPixelSize (O0OO0OOOO0O0OO000 )#line:276
        OOO00OOO000O0OO00 .setFont (OO0OOO0O0O00O000O )#line:277
    def setFontFitSize (O00OO00OOOO0OO0OO ,O0OOO0O0OOO0000O0 ):#line:278
        O00OOOO0OO0O00000 =QFont ()#line:279
        O00OOOO0OO0O00000 .setPointSize (O0OOO0O0OOO0000O0 )#line:280
        O00OO00OOOO0OO0OO .setFont (O00OOOO0OO0O00000 )#line:281
    def setBackground (O0O0O0OO00O0OOOO0 ,O00OO0O0OOO00O00O ):#line:282
        O0O0O0OO00O0OOOO0 .setStyleSheet (O0O0O0OO00O0OOOO0 .styleSheet ()+"border-image:url(../RESOURCE/drawable/"+O00OO0O0OOO00O00O +");")#line:283
    def setBackgroundColor (OOOOOOO00000000O0 ,O00O000OOO0O0O0OO ):#line:285
        OOOOOOO00000000O0 .setStyleSheet (OOOOOOO00000000O0 .styleSheet ()+"background-color:"+O00O000OOO0O0O0OO +";")#line:286
    def setTextColor (OO000OO000OOOO0O0 ,OOO0OOOO00OOO00O0 ):#line:288
        OO000OO000OOOO0O0 .setStyleSheet (OO000OO000OOOO0O0 .styleSheet ()+"color:"+OOO0OOOO00OOO00O0 +";")#line:289
    def mouseReleaseEvent (OOOOOOOOOOOOO00O0 ,O0OO0OOOO0O0OOOO0 ):#line:290
        OOOOOOOOOOOOO00O0 .released .emit (O0OO0OOOO0O0OOOO0 )#line:291
    released =pyqtSignal (QMouseEvent )#line:292
    pressed =pyqtSignal (QEvent )#line:293
    def mousePressEvent (OO0O0O00000OO00OO ,O00O00OOO000O000O ):#line:294
        OO0O0O00000OO00OO .pressed .emit (O00O00OOO000O000O )#line:295
        if O00O00OOO000O000O .buttons ()==Qt .LeftButton :#line:296
            OO0O0O00000OO00OO .clicked .emit (O00O00OOO000O000O )#line:297
    moved =pyqtSignal (QMouseEvent )#line:298
    def mouseMoveEvent (O0O000000OOOO00O0 ,O00OO00OOO0O000O0 ):#line:299
        O0O000000OOOO00O0 .moved .emit (O00OO00OOO0O000O0 )#line:300
    doubleclicked =pyqtSignal (QMouseEvent )#line:301
    def mouseDoubleClickEvent (O00OOOO000OO0OOOO ,O0O00OOO00000OO0O ):#line:302
        if O0O00OOO00000OO0O .buttons ()==Qt .LeftButton :#line:303
            O00OOOO000OO0OOOO .doubleclicked .emit (O0O00OOO00000OO0O )#line:304
    entered =pyqtSignal (QEnterEvent )#line:305
    def enterEvent (O00O000OO00000OO0 ,OOO000000O0O0OO00 ):#line:306
        O00O000OO00000OO0 .entered .emit (OOO000000O0O0OO00 )#line:307
    leaved =pyqtSignal (QEvent )#line:309
    def leaveEvent (O000O0000000O00OO ,OOO00O000OOO0OOOO ):#line:310
        O000O0000000O00OO .leaved .emit (OOO00O000OOO0OOOO )#line:311
    def addScorell (OO0O0O000OOOOOOOO ,OO0O0OOOO0O00000O ,OOO00000OO0O0O00O ,O00OO0OO0OO000O0O ,O00000000OO00O0OO ):#line:313
        O00OO0OO0OO000O0O =parwidth #line:314
        OO0O0O000OOOOOOOO .a =PyQt5_QGroupBox (OO0O0O000OOOOOOOO .parent (),OO0O0OOOO0O00000O ,OOO00000OO0O0O00O ,O00OO0OO0OO000O0O ,O00000000OO00O0OO )#line:315
        OO0O0O000OOOOOOOO .a .setBorderWidth (0 )#line:316
        OO0O0O000OOOOOOOO .scroll =QScrollArea ()#line:317
        OO0O0O000OOOOOOOO .scroll .setWidget (OO0O0O000OOOOOOOO )#line:318
        OO0O0O000OOOOOOOO .scroll .setStyleSheet ("background-color:rgba(0,0,0,0)")#line:319
        OO0O0O000OOOOOOOO .vbox =QVBoxLayout ()#line:320
        OO0O0O000OOOOOOOO .vbox .setContentsMargins (0 ,0 ,0 ,0 )#line:321
        OO0O0O000OOOOOOOO .vbox .addWidget (OO0O0O000OOOOOOOO .scroll )#line:322
        OO0O0O000OOOOOOOO .a .setLayout (OO0O0O000OOOOOOOO .vbox )#line:323
    def setSize (OO00OO0000O000OO0 ,OOO0OOOO0O00000O0 ):#line:325
        OO00OO0000O000OO0 .setFixedSize (OOO0OOOO0O00000O0 )#line:326
    def refresh (OO0OO0OOOO000O00O ):#line:327
        if OO0OO0OOOO000O00O .zeze :#line:328
            OO0OO0OOOO000O00O .widget .resize (OO0OO0OOOO000O00O .widget .width ()+1 ,OO0OO0OOOO000O00O .widget .height ()+1 )#line:329
            OO0OO0OOOO000O00O .zeze =False #line:330
        else :#line:331
            OO0OO0OOOO000O00O .widget .resize (OO0OO0OOOO000O00O .widget .width ()-1 ,OO0OO0OOOO000O00O .widget .height ()-1 )#line:332
            OO0OO0OOOO000O00O .zeze =True #line:333
    def addRightMenu (O0OOO0000O00OOO00 ,O000O0O000OOOO0O0 ):#line:334
        O0OOO0000O00OOO00 .setContextMenuPolicy (Qt .CustomContextMenu )#line:335
        O0OOO0000O00OOO00 .menuAction =QAction (O000O0O000OOOO0O0 ,O0OOO0000O00OOO00 )#line:336
        O0OOO0000O00OOO00 .menu .addAction (O0OOO0000O00OOO00 .menuAction )#line:337
        return O0OOO0000O00OOO00 .menuAction #line:338
class PyQt5_QMovie (QMovie ):#line:339
    def __init__ (O0O00OOO00OOO00O0 ,OOO0O0OOOO00OO00O ):#line:340
        super ().__init__ ("../RESOURCE/gif/"+OOO0O0OOOO00OO00O )#line:341
class PyQt5_QMediaPlayer ():#line:343
    def __init__ (OO00OO000OO00OOOO ):#line:344
        pygame .mixer .init ()#line:345
        OO00OO000OO00OOOO .music =pygame .mixer .music #line:346
    def prepare_audio (OO0OOOO0OO000OOOO ,OO0000O0O0000O0OO ):#line:347
        OO0OOOO0OO000OOOO .music .load ("../RESOURCE/audio/"+OO0000O0O0000O0OO )#line:348
    def prepare_voice (O0OO0OOOO00O000O0 ,OOOOO0OO0O0000OO0 ):#line:349
        O0OO0OOOO00O000O0 .music .load ("../RESOURCE/voice/"+OOOOO0OO0O0000OO0 )#line:350
    def play (O0OO0O0OO0O000000 ,loops =1 ,start =0.0 ):#line:351
        if loops ==0 :#line:352
            O0OO0O0OO0O000000 .music .play (-1 ,start )#line:353
        elif loops <0 :#line:354
            pass #line:355
        elif loops >0 :#line:356
            O0OO0O0OO0O000000 .music .play (loops -1 ,start )#line:357
    def stop (OO0O0O0OOO000OO00 ):#line:358
        OO0O0O0OOO000OO00 .music .stop ()#line:359
    def pause (OO0OO00O000O00OOO ):#line:360
        OO0OO00O000O00OOO .music .pause ()#line:361
    def setVolume (O0OO0OO0O0OO00OO0 ,O0O0OO0OO0O0OO000 ):#line:362
        O0OO0OO0O0OO00OO0 .music .set_volume (O0O0OO0OO0O0OO000 )#line:363
    def isPlaying (OO0OO0OOO00OOO00O ):#line:364
        if OO0OO0OOO00OOO00O .music .get_busy ()==1 :#line:365
            return True #line:366
        else :#line:367
            return False #line:368
class PyQt5_QCheckBox (QCheckBox ):#line:372
    def __init__ (OO0O0000O0OOOO0OO ,O00000OO00O0OOOO0 ,x =0 ,y =0 ,width =20 ,height =20 ):#line:373
        super ().__init__ (O00000OO00O0OOOO0 )#line:374
        OO0O0000O0OOOO0OO .setGeometry (x ,y ,width ,height )#line:375
        OO0O0000O0OOOO0OO .isIndicator =True #line:376
        OO0O0000O0OOOO0OO .image_name_normal =""#line:377
        OO0O0000O0OOOO0OO .image_name_pressed =""#line:378
    def setIndicator (O00OO0000OO0O0O0O ,OO00O0O0OO00O0000 ):#line:380
        O00OO0000OO0O0O0O .isIndicator =OO00O0O0OO00O0000 #line:381
        O00OO0000OO0O0O0O .setStyleSheet ("")#line:382
        if O00OO0000OO0O0O0O .image_name_normal !="":#line:383
            O00OO0000OO0O0O0O .setUncheckedBackground (O00OO0000OO0O0O0O .image_name_normal )#line:384
        if O00OO0000OO0O0O0O .image_name_pressed !="":#line:385
            O00OO0000OO0O0O0O .setCheckedBackground (O00OO0000OO0O0O0O .image_name_pressed )#line:386
    def setUncheckedBackground (O00O000O00O00O000 ,OOO000000OOO0O000 ):#line:388
        if O00O000O00O00O000 .isIndicator :#line:389
            O00O000O00O00O000 .setStyleSheet (O00O000O00O00O000 .styleSheet ()+"QCheckBox:unchecked{width:"+str (O00O000O00O00O000 .width ())+"px;height:"+str (O00O000O00O00O000 .height ())+"px;border-image:url(../RESOURCE/drawable/"+OOO000000OOO0O000 +")}")#line:392
        else :#line:393
            O00O000O00O00O000 .setStyleSheet (O00O000O00O00O000 .styleSheet ()+"QCheckBox:indicator:unchecked{width:"+str (O00O000O00O00O000 .width ())+"px;height:"+str (O00O000O00O00O000 .height ())+"px;border-image:url(../RESOURCE/drawable/"+OOO000000OOO0O000 +")}")#line:396
        O00O000O00O00O000 .image_name_normal =OOO000000OOO0O000 #line:397
    def setCheckedBackground (O00OO0O0OOO0000OO ,OO00OO0OOO0OO0O0O ):#line:399
        if O00OO0O0OOO0000OO .isIndicator :#line:400
            O00OO0O0OOO0000OO .setStyleSheet (O00OO0O0OOO0000OO .styleSheet ()+"QCheckBox:checked{width:"+str (O00OO0O0OOO0000OO .width ())+"px;height:"+str (O00OO0O0OOO0000OO .height ())+"px;border-image:url(../RESOURCE/drawable/"+OO00OO0OOO0OO0O0O +")}")#line:403
        else :#line:404
            O00OO0O0OOO0000OO .setStyleSheet (O00OO0O0OOO0000OO .styleSheet ()+"QCheckBox:indicator:checked{width:"+str (O00OO0O0OOO0000OO .width ())+"px;height:"+str (O00OO0O0OOO0000OO .height ())+"px;border-image:url(../RESOURCE/drawable/"+OO00OO0OOO0OO0O0O +")}")#line:407
        O00OO0O0OOO0000OO .image_name_pressed =OO00OO0OOO0OO0O0O #line:408
class PyQt5_QRadioButton (QRadioButton ):#line:411
    def __init__ (O0OO00O00OOO00OOO ,OO0000OOO00O0OO0O ,x =0 ,y =0 ,width =20 ,height =20 ):#line:412
        super ().__init__ (OO0000OOO00O0OO0O )#line:413
        O0OO00O00OOO00OOO .setGeometry (x ,y ,width ,height )#line:414
        O0OO00O00OOO00OOO .isIndicator =True #line:415
        O0OO00O00OOO00OOO .image_name_normal =""#line:416
        O0OO00O00OOO00OOO .image_name_pressed =""#line:417
    def setFontSize (O00OOO0OO00OOO0OO ,OOO00O0O000O0OO0O ):#line:419
        OO0O00OO00OOO0O00 =QFont ()#line:420
        OO0O00OO00OOO0O00 .setPixelSize (OOO00O0O000O0OO0O )#line:421
        O00OOO0OO00OOO0OO .setFont (OO0O00OO00OOO0O00 )#line:422
    def setTextColor (O0OO000OO0000000O ,OOO0OOOO000OO00O0 ):#line:424
        O0OO000OO0000000O .setStyleSheet (O0OO000OO0000000O .styleSheet ()+"color:"+OOO0OOOO000OO00O0 +";")#line:425
    def setIndicator (O0O000O00O0OOOOOO ,OO0O0OO00OOO00OO0 ):#line:427
        O0O000O00O0OOOOOO .isIndicator =OO0O0OO00OOO00OO0 #line:428
        O0O000O00O0OOOOOO .setStyleSheet ("")#line:429
        if O0O000O00O0OOOOOO .image_name_normal !="":#line:430
            O0O000O00O0OOOOOO .setUncheckedBackground (O0O000O00O0OOOOOO .image_name_normal )#line:431
        if O0O000O00O0OOOOOO .image_name_pressed !="":#line:432
            O0O000O00O0OOOOOO .setCheckedBackground (O0O000O00O0OOOOOO .image_name_pressed )#line:433
    def setUncheckedBackground (OO00OO0OOOOOOOO0O ,O000O0O0OOOOOO00O ):#line:435
        if OO00OO0OOOOOOOO0O .isIndicator :#line:436
            OO00OO0OOOOOOOO0O .setStyleSheet (OO00OO0OOOOOOOO0O .styleSheet ()+"QRadioButton:unchecked{width:"+str (OO00OO0OOOOOOOO0O .width ())+"px;height:"+str (OO00OO0OOOOOOOO0O .height ())+"px;border-image:url(../RESOURCE/drawable/"+O000O0O0OOOOOO00O +")}")#line:439
        else :#line:440
            OO00OO0OOOOOOOO0O .setStyleSheet (OO00OO0OOOOOOOO0O .styleSheet ()+"QRadioButton:indicator:unchecked{width:"+str (OO00OO0OOOOOOOO0O .width ())+"px;height:"+str (OO00OO0OOOOOOOO0O .height ())+"px;border-image:url(../RESOURCE/drawable/"+O000O0O0OOOOOO00O +")}")#line:443
        OO00OO0OOOOOOOO0O .image_name_normal =O000O0O0OOOOOO00O #line:444
    def setCheckedBackground (OOOOOO00O000OOOOO ,OOOO0O000OOOOO000 ):#line:446
        if OOOOOO00O000OOOOO .isIndicator :#line:447
            OOOOOO00O000OOOOO .setStyleSheet (OOOOOO00O000OOOOO .styleSheet ()+"QRadioButton:checked{width:"+str (OOOOOO00O000OOOOO .width ())+"px;height:"+str (OOOOOO00O000OOOOO .height ())+"px;border-image:url(../RESOURCE/drawable/"+OOOO0O000OOOOO000 +")}")#line:450
        else :#line:451
            OOOOOO00O000OOOOO .setStyleSheet (OOOOOO00O000OOOOO .styleSheet ()+"QRadioButton:indicator:checked{width:"+str (OOOOOO00O000OOOOO .width ())+"px;height:"+str (OOOOOO00O000OOOOO .height ())+"px;border-image:url(../RESOURCE/drawable/"+OOOO0O000OOOOO000 +")}")#line:454
        OOOOOO00O000OOOOO .image_name_pressed =OOOO0O000OOOOO000 #line:455
class PyQt5_QGroupBox (QGroupBox ):#line:458
    def __init__ (OOOOOOO0OOOOOO0O0 ,OOO00OOO0OOOO00OO ,x =0 ,y =0 ,width =120 ,height =80 ):#line:459
        super ().__init__ (OOO00OOO0OOOO00OO )#line:460
        OOOOOOO0OOOOOO0O0 .setGeometry (x ,y ,width ,height )#line:461
        OOOOOOO0OOOOOO0O0 .setObjectName ("groupbox")#line:462
    def setBackground (OOOO00OOO0OO0O000 ,OO0OO0O000O0OOO0O ):#line:464
        OOOO00OOO0OO0O000 .setStyleSheet ("#groupbox{border-image:url(../RESOURCE/drawable/"+OO0OO0O000O0OOO0O +")}")#line:465
    def setBackgroundColor (OOO0O00000O0O0000 ,O0000OO0O0O0O0O0O ):#line:467
        OOO0O00000O0O0000 .setStyleSheet ("#groupbox{background-color:"+O0000OO0O0O0O0O0O +"}")#line:468
    def setBorderWidth (O00OOO000O0OO0OO0 ,OOO00000OOOO000OO ):#line:470
        O00OOO000O0OO0OO0 .setStyleSheet (O00OOO000O0OO0OO0 .styleSheet ()+"border-width:"+str (OOO00000OOOO000OO )+"px;border-style:solid;")#line:471
def getQuestion (OO0O00OO0OOOO0O0O ):#line:474
    try :#line:475
        OOOOOOO0O00OO00O0 =ipStr +'ti/findById.do?id=%d'%OO0O00OO0OOOO0O0O #line:477
        OOOOOOO0O00OO00O0 =urllib .request .Request (url =OOOOOOO0O00OO00O0 )#line:478
        OOOOOOO0O00OO00O0 .add_header ('Content-Type','application/json')#line:479
        O000OOO000O00OOOO =urllib .request .urlopen (OOOOOOO0O00OO00O0 )#line:480
    except urllib .error .URLError as O0O00000O00O00O0O :#line:481
        O00O000OOO000OOO0 ={"id":1 ,"wenti":"由于网络问题未找到所需内容，请检查您的网络","daan":"0","jiexi":"  ","a":" ","b":" ","c":" ","d":" "}#line:482
        return O00O000OOO000OOO0 #line:483
    O00O000OOO000OOO0 =json .loads (O000OOO000O00OOOO .read ().decode ('utf-8'))#line:485
    if O00O000OOO000OOO0 :#line:487
        if O00O000OOO000OOO0 ["state"]!=0 :#line:488
            return {"id":1 ,"wenti":O00O000OOO000OOO0 ["message"],"daan":"0","jiexi":"  ","a":" ","b":" ","c":" ","d":" "}#line:489
        else :#line:490
            return O00O000OOO000OOO0 ["data"]#line:491
def reductionRadioBtn (OO0O0O00OOOO000O0 ):#line:492
    for O0000O00OO0OOOOOO in range (len (OO0O0O00OOOO000O0 )):#line:493
        OO0O0O00OOOO000O0 [O0000O00OO0OOOOOO ].setCheckable (False )#line:495
        OO0O0O00OOOO000O0 [O0000O00OO0OOOOOO ].setCheckable (True )#line:496
class PyQt5_QSystemTrayIcon (QSystemTrayIcon ):#line:497
    def __init__ (O0OO0O0OO0OO000O0 ,parent =None ):#line:498
        super (PyQt5_QSystemTrayIcon ,O0OO0O0OO0OO000O0 ).__init__ (parent )#line:499
        O0OO0O0OO0OO000O0 .menu =QMenu ()#line:500
        O0OO0O0OO0OO000O0 .setContextMenu (O0OO0O0OO0OO000O0 .menu )#line:501
    def addMenu (OOOOOO0O00000000O ,O0000O0O00O0OOO0O ):#line:502
        OOOOOO0O00000000O .menuAction =QAction (O0000O0O00O0OOO0O ,OOOOOO0O00000000O )#line:503
        OOOOOO0O00000000O .menu .addAction (OOOOOO0O00000000O .menuAction )#line:504
        return OOOOOO0O00000000O .menuAction #line:505
    def _setIcon (O0O0OO0OO000OO0OO ,OO0O0O0O00OOOOO0O ):#line:506
        O0O0OO0OO000OO0OO .setIcon (QIcon ("../RESOURCE/drawable/"+OO0O0O0O00OOOOO0O ))#line:507
class PyQt5_Animation (QPropertyAnimation ):#line:510
    animFinished =pyqtSignal ()#line:511
    def __init__ (O0O0OO0O0O0O0000O ,QWidget =None ):#line:512
        super (PyQt5_Animation ,O0O0OO0O0O0O0000O ).__init__ ()#line:513
        O0O0OO0O0O0O0000O .setPropertyName (b"geometry")#line:514
        O0O0OO0O0O0O0000O .setTargetObject (QWidget )#line:515
        O0O0OO0O0O0O0000O .finished .connect (O0O0OO0O0O0O0000O .aFinished )#line:516
        O0O0OO0O0O0O0000O .widget =QWidget #line:517
        O0O0OO0O0O0O0000O .valueChanged .connect (O0O0OO0O0O0O0000O .up )#line:518
        O0O0OO0O0O0O0000O .ze =True #line:519
    def up (OO00O00O00000OO0O ):#line:520
        if OO00O00O00000OO0O .ze :#line:521
            OO00O00O00000OO0O .widget .resize (OO00O00O00000OO0O .widget .width ()+1 ,OO00O00O00000OO0O .widget .height ()+1 )#line:522
            OO00O00O00000OO0O .ze =False #line:523
        else :#line:524
            OO00O00O00000OO0O .widget .resize (OO00O00O00000OO0O .widget .width ()-1 ,OO00O00O00000OO0O .widget .height ()-1 )#line:525
            OO00O00O00000OO0O .ze =True #line:526
    def setStartValues (O0O00OOO0O0OO00O0 ,OOO000OOOO0OOO0O0 ,OO00O0O00O00O0O0O ,O00O00O0O00000000 ,O0OO00O00OO0000O0 ):#line:528
        O0O00OOO0O0OO00O0 .setStartValue (QRect (OOO000OOOO0OOO0O0 ,OO00O0O00O00O0O0O ,O00O00O0O00000000 ,O0OO00O00OO0000O0 ))#line:529
    def setEndValues (OO0O0O00OOO000OO0 ,O000OOOO00O0O0OO0 ,OOOO0O00000OO0OOO ,O0OO0OOO000O00O00 ,O0O0OOOOOOOO00O00 ):#line:530
        OO0O0O00OOO000OO0 .setEndValue (QRect (O000OOOO00O0O0OO0 ,OOOO0O00000OO0OOO ,O0OO0OOO000O00O00 ,O0O0OOOOOOOO00O00 ))#line:531
    def setMode (OOOOOO0O0OO0OO000 ,OOO0OO0OOOO0OOO0O ):#line:532
        OOOOOO0O0OO0OO000 .setEasingCurve (OOO0OO0OOOO0OOO0O )#line:533
    def aFinished (OO000O0OOOOOO0O0O ):#line:534
        OO000O0OOOOOO0O0O .animFinished .emit ()#line:535
class Mode ():#line:537
    InOut =QEasingCurve .InOutBack #line:539
    OutIn =QEasingCurve .OutInBack #line:540
    InZero =QEasingCurve .InQuart #line:542
    OutZero =QEasingCurve .OutQuart #line:543
    InElastic =QEasingCurve .InElastic #line:545
    OutElastic =QEasingCurve .OutElastic #line:546
    InBounce =QEasingCurve .InBounce #line:548
    OutBounce =QEasingCurve .OutBounce #line:549
class PyQt5_FramelessBox (QDialog ):#line:551
    def __init__ (O00O0OOOOO0O00000 ):#line:552
        super ().__init__ ()#line:553
        O00O0OOOOO0O00000 .resize (340 ,340 )#line:554
        O00O0OOOOO0O00000 .setObjectName ("FramelessBox")#line:555
        O00O0OOOOO0O00000 .setWindowFlags (O00O0OOOOO0O00000 .windowFlags ()|Qt .FramelessWindowHint )#line:556
    def setWindowsTop (OO00O00OO0000OOOO ,OOO00000O0OO00OO0 ):#line:558
        if OOO00000O0OO00OO0 :#line:559
            OO00O00OO0000OOOO .setWindowFlags (OO00O00OO0000OOOO .windowFlags ()|Qt .WindowStaysOnTopHint )#line:560
    def setResize (OO00OOO000O0O0O0O ,O0O0OOO00000000O0 ,OOO00OO0O00O0OOOO ):#line:561
        OO00OOO000O0O0O0O .resize (O0O0OOO00000000O0 ,OOO00OO0O00O0OOOO )#line:562
    def setWindowstransparent (O0OOOO0OO0OO000OO ,OO000000O0OOO0O0O ):#line:563
        if OO000000O0OOO0O0O :#line:564
            O0OOOO0OO0OO000OO .setAttribute (Qt .WA_TranslucentBackground ,True )#line:565
def getDesktopWidth ():#line:567
    return QApplication .desktop ().width ()#line:568
def getDesktopHeight ():#line:570
    return QApplication .desktop ().height ()#line:571
def writeDocument (O0O0O00O00OOOO0O0 ,O0O0OOOOOO0OO0000 ,OOO0O00O00OOOO00O ):#line:574
    OOOO0O0000O0000O0 =wave .open (O0O0O00O00OOOO0O0 ,'wb')#line:575
    OOOO0O0000O0000O0 .setnchannels (1 )#line:576
    OOOO0O0000O0000O0 .setsampwidth (2 )#line:577
    OOOO0O0000O0000O0 .setframerate (OOO0O00O00OOOO00O )#line:578
    OOOO0O0000O0000O0 .writeframes (b"".join (O0O0OOOOOO0OO0000 ))#line:579
    OOOO0O0000O0000O0 .close ()#line:580
def SentContent (OO0OOO0O0OOOO000O ):#line:583
    O0O0O000000OOOO00 =json .dumps ({"reqType":0 ,"perception":{"inputText":{"text":OO0OOO0O0OOOO000O }},"userInfo":{"apiKey":"be0b3a4918ef433fbf72400d15a836f5","userId":"5b2e1c710b814fdd"}})#line:595
    return O0O0O000000OOOO00 #line:596
def roleSpeak (O00O0OOOOO000OOOO ,O000O0OOOOOO0O0O0 ):#line:599
    if O00O0OOOOO000OOOO =='男孩':#line:600
        OO0O00O0O0OOOOOOO =1 #line:601
    elif O00O0OOOOO000OOOO =='大叔':#line:602
        OO0O00O0O0OOOOOOO =3 #line:603
    elif O00O0OOOOO000OOOO =='女孩':#line:604
        OO0O00O0O0OOOOOOO =0 #line:605
    else :#line:606
        OO0O00O0O0OOOOOOO =4 #line:607
    OOOO00O00OO00OOO0 =client .synthesis (O000O0OOOOOO0O0O0 ,'zh',1 ,{'vol':15 ,'per':OO0O00O0O0OOOOOOO ,'spd':4 ,'pit':9 ,})#line:610
    return OOOO00O00OO00OOO0 #line:611
def record ():#line:613
    p = PyAudio()
    OO000OOOO000OOO0O =p.open (format =paInt16 ,channels =1 ,rate =8000 ,input =True ,frames_per_buffer =4800 )#line:614
    OO0OO0OO0000OO000 =[]#line:615
    O000000O00OOO0O0O =0 #line:616
    OOO0000OOO000OOOO =7 #line:617
    OO0O00O0OO00O0O0O =OO000OOOO000OOO0O .read (4800 )#line:618
    OO0OO0OO0000OO000 .append (OO0O00O0OO00O0O0O )#line:619
    O0000OO0OO00OOO0O =np .fromstring (OO0O00O0OO00O0O0O ,dtype =np .int16 )#line:620
    OOO0000OOO000OOOO =np .max (O0000OO0OO00OOO0O )#line:621
    O000O0000O00OOOO0 =""#line:622
    if OOO0000OOO000OOOO >=2000 :#line:623
        while OOO0000OOO000OOOO >=2000 :#line:624
            OO0O00O0OO00O0O0O =OO000OOOO000OOO0O .read (4800 )#line:625
            OO0OO0OO0000OO000 .append (OO0O00O0OO00O0O0O )#line:626
            O0000OO0OO00OOO0O =np .fromstring (OO0O00O0OO00O0O0O ,dtype =np .int16 )#line:627
            OOO0000OOO000OOOO =np .max (O0000OO0OO00OOO0O )#line:628
        QApplication .processEvents ()#line:629
        writeDocument ('../RESOURCE/voice/input.wav',OO0OO0OO0000OO000 ,8000 )#line:630
        OO000OOOO000OOO0O.stop_stream()
        OO000OOOO000OOO0O .close ()#line:631
        p.terminate()
        O000O0000O00OOOO0 ="执行"#line:632
    return O000O0000O00OOOO0 #line:633
def Magic_Sound ():#line:636
    OO0OO0O0O00O000OO ,OOO000000OOOO0OO0 =sf .read ("../RESOURCE/voice/input.wav")#line:637
    plt .plot (OO0OO0O0O00O000OO )#line:638
    OOO000000OOOO0OO0 =int (OOO000000OOOO0OO0 *1.3 )#line:639
    sf .write ("../RESOURCE/voice/output.wav",OO0OO0O0O00O000OO ,OOO000000OOOO0OO0 )#line:640
def translateContent ():#line:643
    try :#line:644
        OO0OOOOO0OOOO0OO0 =client .asr (readDocument ('../RESOURCE/voice/input.wav'),'wav',8000 ,{'dev_pid':'1536',})#line:647
    except (requests .exceptions .ConnectionError )as OOOO0000O00OOOO00 :#line:648
        print ("网络异常...")#line:649
        return "网络异常"#line:650
    else :#line:651
        return OO0OOOOO0OOOO0OO0 #line:652
def readDocument (OO00OO00O000OO000 ):#line:655
    with open (OO00OO00O000OO000 ,'rb')as O0OO0OOO0O000O00O :#line:656
        return O0OO0OOO0O000O00O .read ()#line:657
def play_chat (OOO00000000O00000 ):#line:660
    pygame .mixer .init ()#line:661
    OO00OO00O00OOO000 =pygame .mixer .music .load (OOO00000000O00000 )#line:662
    pygame .mixer .music .play ()#line:663
    while (pygame .mixer .music .get_busy ()==1 ):#line:664
        time .sleep (0.000001 )#line:665
        QApplication .processEvents ()#line:666
    OO00OO00O00OOO000 =pygame .mixer .music .load ('../RESOURCE/voice/empty.mp3')#line:667
def translates (O0O00O0O0O0OO0OO0 ,O0OOO0OOOOO00OOOO ):#line:670
    OO000000O0O0OO0O0 =O0O00O0O0O0OO0OO0 .text ()#line:671
    OOO00OOO0OO00O000 ='20180118000116417'#line:672
    O0O0O00O00OO000O0 ='dfp7pBcNo7jxJwIkAUuq'#line:673
    OOOO0O00OO0000OOO =None #line:674
    OOO0OOOOOO0O00OOO ='/api/trans/vip/translate'#line:675
    OO0O000OO0OOO00O0 =OO000000O0O0OO0O0 #line:676
    OO0OO00OO00000O00 ='zh'#line:677
    O00O0O00OOOO00OO0 ='en'#line:678
    O000O0O0OO00O0OO0 =random .randint (32768 ,65536 )#line:679
    O0OO000O0O0OOOO0O =OOO00OOO0OO00O000 +OO0O000OO0OOO00O0 +str (O000O0O0OO00O0OO0 )+O0O0O00O00OO000O0 #line:680
    O0OO000O0O0OOOO0O =O0OO000O0O0OOOO0O .encode ('utf-8')#line:681
    O00OOO0OO0000O0OO =hashlib .md5 ()#line:682
    O00OOO0OO0000O0OO .update (O0OO000O0O0OOOO0O )#line:683
    O0OO000O0O0OOOO0O =O00OOO0OO0000O0OO .hexdigest ()#line:684
    OOO0OOOOOO0O00OOO =OOO0OOOOOO0O00OOO +'?appid='+OOO00OOO0OO00O000 +'&q='+urllib .parse .quote (OO0O000OO0OOO00O0 )+'&from='+OO0OO00OO00000O00 +'&to='+O00O0O00OOOO00OO0 +'&salt='+str (O000O0O0OO00O0OO0 )+'&sign='+O0OO000O0O0OOOO0O #line:685
    try :#line:686
        OOOO0O00OO0000OOO =http .client .HTTPConnection ('api.fanyi.baidu.com')#line:687
        OOOO0O00OO0000OOO .request ('GET',OOO0OOOOOO0O00OOO )#line:688
        O000OO0OO0OO00000 =OOOO0O00OO0000OOO .getresponse ()#line:689
        O000OO0OO0OO00000 =json .loads (O000OO0OO0OO00000 .read ().decode ("utf-8"))#line:690
        if OOOO0O00OO0000OOO :#line:691
            OOOO0O00OO0000OOO .close ()#line:692
        O0OOO0OOOOO00OOOO .setText (O000OO0OO0OO00000 ['trans_result'][0 ]['dst'])#line:693
    except :#line:695
        print ("翻译异常")#line:696
        if OOOO0O00OO0000OOO :#line:697
            OOOO0O00OO0000OOO .close ()#line:698
        O0OOO0OOOOO00OOOO .setText ("翻译失败")#line:699
class awaken (QThread ):#line:701
    awakenStoped =pyqtSignal ()#line:702
    awakenStarted =pyqtSignal (str )#line:703
    def __init__ (OO0000O000O0OOO0O ,OOO0OOO0O0OOOO00O ):#line:704
        super ().__init__ ()#line:705
        OO0000O000O0OOO0O .dialog =OOO0OOO0O0OOOO00O #line:706
    def run (O00OO00OO000O0O0O ):#line:707
        in_out (O00OO00OO000O0O0O ,O00OO00OO000O0O0O .dialog )#line:708
    def addOperation (OO000OO0OO00O000O ,OO0OO00O00OOO0OO0 ):#line:709
        OO000OO0OO00O000O .awakenStoped .connect (OO0OO00O00OOO0OO0 )#line:710
        OO000OO0OO00O000O .awakenStoped .emit ()#line:711
def changeVoiceMode (O00OO000OO0O000OO ):#line:714
    global modelflog #line:715
    modelflog =O00OO000OO0O000OO #line:716
def getVoiceMode ():#line:718
    return modelflog #line:719
def in_out (O0O00OOOOOOOOO0O0 ,O0O000O00OO0000O0 ):#line:721
    while True :#line:722
        O0O00O00000000O0O =record ()#line:723
        if O0O00O00000000O0O =="执行":#line:724
            O0OOO00OOO00O0O00 =translateContent ()#line:725
            if O0OOO00OOO00O0O00 =="网络异常":#line:726
                changeVoiceMode ('异常')#line:727
            else :#line:728
                if 'err_no'in O0OOO00OOO00O0O00 :#line:729
                    if O0OOO00OOO00O0O00 ['err_no']==0 :#line:730
                        OOO0OOOO00O00O0OO =O0OOO00OOO00O0O00 ['result'][0 ]#line:731
                    else :#line:732
                        OO00O0OOOO00O000O ="err"#line:733
                        OOO0OOOO00O00O0OO =OO00O0OOOO00O000O #line:734
                QApplication .processEvents ()#line:735
                O0O00OOOOOOOOO0O0 .awakenStarted .emit (OOO0OOOO00O00O0OO )#line:736
def always_play ():#line:738
    time .sleep (0.001 )#line:739
    QApplication .processEvents ()#line:740
def stop_play ():#line:741
    OOOO000OO0OOO00OO =pygame .mixer .music .load ('../RESOURCE/voice/empty.mp3')#line:742
class RepeatT (QThread ):#line:744
    def __init__ (OOO0OO0OO00O0OO0O ,O0O000000000000O0 ):#line:745
        super ().__init__ ()#line:746
        OOO0OO0OO00O0OO0O .dialog =O0O000000000000O0 #line:747
    def run (O000O00O000000000 ):#line:748
        record ()#line:749
        Magic_Sound ()#line:750
        O000O00O000000000 .dialog ()#line:751
        pygame.mixer.music.load('../RESOURCE/voice/empty.mp3')
        changeVoiceMode ("唤醒")#line:752
class ChatT (QThread ):#line:754
    def __init__ (O000000000OOOOO0O ,OO0OOO000OO00O00O ):#line:755
        super ().__init__ ()#line:756
        O000000000OOOOO0O .dialog =OO0OOO000OO00O00O #line:757
    def run (O0O0O00OO0O000OO0 ):#line:758
        O0O0O00OO0O000OO0 .dialog ()#line:759
def speechRecognition (O0O000O000OO0000O ,OO0O00O0OOOO0OO00 ):#line:762
    O00OOO0O0OO0OO0O0 =translateContent ()#line:763
    if O00OOO0O0OO0OO0O0 =="网络异常":#line:764
        return "网络异常"#line:765
    if 'err_no'in O00OOO0O0OO0OO0O0 :#line:766
        if O00OOO0O0OO0OO0O0 ['err_no']==0 :#line:767
            return O00OOO0O0OO0OO0O0 ['result'][0 ]#line:768
        else :#line:769
            OO00OO00OO0OO0OOO =OO0O00O0OOOO0OO00 #line:770
            return OO00OO00OO0OO0OOO #line:771
    else :#line:772
        OO00OO00OO0OO0OOO =OO0O00O0OOOO0OO00 #line:773
        return OO00OO00OO0OO0OOO #line:774
def roleChange (O0O0OO000O0000O00 ):#line:777
    global role #line:778
    role =O0O0OO000O0000O00 #line:779
def getRole ():#line:781
    return role #line:782
def getResult (OO000OO00OOOO00O0 ):#line:1
    OO000000OOO00OO0O =json .loads (OO000OO00OOOO00O0 .text )#line:2
    OO000000OOO00OO0O =OO000000OOO00OO0O ["results"][0 ]['values']#line:3
    return OO000000OOO00OO0O 

name="Vipc2"