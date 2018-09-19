# -*- coding: utf-8 -*-

import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr, formataddr
from email import encoders
import base64 

__doc__ = """
    
    简易的邮件发信工具。支持认证/不认证发信。
    使用UTF-8编码。
    from quickemail import QuickEmail

    1. 发信前先定义发信要素：

        指定主机和端口，必须参数：
        quicksend = QuickEmail('mail.mailsvr.cn', 25)    # SMTP发信端口，默认是25 SSL链接使用465

        定义HELO主机名，参数可省略：
        quicksend._helo('QuickEmail')                 # HELO主机名不能使用有空格的字符串

        认证发信authsend()必须的参数：
        quicksend.mail_user('a')                     # 认证用户名
        quicksend.user_pass('test')                  # 认证用户的密码

        发信人、收信人为必须参数：
        quicksend._mail_from('AA高丽A<a@119.com>')    # 发信人地址，格式为:   显示姓名<email address>
        quicksend._mail_to('一二三<123@119.com>,ABC<abc@119.com>')    # 格式同上，多地址使用逗号","分隔

        抄送人，可省略：
        quicksend._mail_cc('一二三<123@119.com>,中语言C<abc@119.com>,AA高丽A<a@119.com>')

        邮件主题、内容，支持使用HTML： 
        quicksend._mail_subject('mY subject还有中文!')
        quicksend._mail_content('<font color=red>red content一段中文</font>')
        quicksend._is_html(True)

        添加附件，可省略：
        quicksend._mail_attach(['abc.jpg'])           # 添加附件 类型为list
        
        高级定制，可省略：
        quicksend._content_from('邮件显示的假发件人<from@119.com>')      # 定制邮件信体显示的发件人，一般为来隐藏实际的mail_from。
        quicksend._content_to('邮件显示的假收件人<to@119.com>')      # 定制邮件信体显示的收件人，一般为来隐藏实际的mail_to。
        quicksend._content_cc('邮件显示的假抄送人<cc@119.com>')      # 定制邮件信体显示的抄送人，一般为来隐藏实际的mail_cc。
        
    2. 使用creatMsg()建立邮件信体内容

        msg = quicksend.creatMsg()

    3. 使用authsend()或者send()发送邮件

        quicksend.authsend(msg)
        quicksend.send(msg)

"""

__version__ = '0.1.0'

__all__ = ["host", "port", "auth_user", "user_pass", "mail_from", "mail_to", "mail_cc", "mail_bcc", "content_from", "content_to", "content_cc", "mail_subject", "mail_attach", "is_html", "time_out","authsend", "send", "creatMsg"]

__author__ = 'clayboy <clayboy@foxmail.com>'

class QuickEmail:

    _auth_user = None
    _user_pass = None
    _mail_from = ''
    _mail_to = ''
    _mail_cc = None
    _mail_bcc = None
    _mail_subject = ''
    _mail_content = ''
    _mail_attach = None
    _is_html = True
    _time_out = 20
    _helo = "QuickEmail"
    _content_from = None
    _content_to = None
    _content_cc = None

    _content_type = {
    'acp':'audio/x-mei-aac',
    'aif':'audio/aiff',
    'aiff':'audio/aiff',
    'asa':'text/asa',
    'asp':'text/asp',
    'au':'audio/basic',
    'awf':'application/vnd.adobe.workflow',
    'bmp':'application/x-bmp',
    'c4t':'application/x-c4t',
    'cal':'application/x-cals',
    'cdf':'application/x-netcdf',
    'cel':'application/x-cel',
    'cg4':'application/x-g4',
    'cit':'application/x-cit',
    'cml':'text/xml',
    'cmx':'application/x-cmx',
    'crl':'application/pkix-crl',
    'csi':'application/x-csi',
    'cut':'application/x-cut',
    'dbm':'application/x-dbm',
    'dcd':'text/xml',
    'der':'application/x-x509-ca-cert',
    'dib':'application/x-dib',
    'doc':'application/msword',
    'drw':'application/x-drw',
    'dwf':'Model/vnd.dwf',
    'dwg':'application/x-dwg',
    'dxf':'application/x-dxf',
    'emf':'application/x-emf',
    'ent':'text/xml',
    'eps':'application/x-ps',
    'etd':'application/x-ebx',
    'fax':'image/fax',
    'fif':'application/fractals',
    'frm':'application/x-frm',
    'gbr':'application/x-gbr',
    'gif':'image/gif',
    'gp4':'application/x-gp4',
    'hmr':'application/x-hmr',
    'hpl':'application/x-hpl',
    'hrf':'application/x-hrf',
    'htc':'text/x-component',
    'html':'text/html',
    'htx':'text/html',
    'ico':'image/x-icon',
    'iff':'application/x-iff',
    'igs':'application/x-igs',
    'img':'application/x-img',
    'isp':'application/x-internet-signup',
    'java':'java/*',
    'jpe':'image/jpeg',
    'jpeg':'image/jpeg',
    'jpg':'application/x-jpg',
    'jsp':'text/html',
    'lar':'application/x-laplayer-reg',
    'lavs':'audio/x-liquid-secure',
    'lmsff':'audio/x-la-lms',
    'ltr':'application/x-ltr',
    'm2v':'video/x-mpeg',
    'm4e':'video/mpeg4',
    'man':'application/x-troff-man',
    'mdb':'application/msaccess',
    'mfp':'application/x-shockwave-flash',
    'mhtml':'message/rfc822',
    'mid':'audio/mid',
    'mil':'application/x-mil',
    'mnd':'audio/x-musicnet-download',
    'mocha':'application/x-javascript',
    'mp1':'audio/mp1',
    'mp2v':'video/mpeg',
    'mp4':'video/mpeg4',
    'mpd':'application/vnd.ms-project',
    'mpeg':'video/mpg',
    'mpga':'audio/rn-mpeg',
    'mps':'video/x-mpeg',
    'mpv':'video/mpg',
    'mpw':'application/vnd.ms-project',
    'mtx':'text/xml',
    'net':'image/pnetvue',
    'nws':'message/rfc822',
    'out':'application/x-out',
    'p12':'application/x-pkcs12',
    'p7c':'application/pkcs7-mime',
    'p7r':'application/x-pkcs7-certreqresp',
    'pc5':'application/x-pc5',
    'pcl':'application/x-pcl',
    'pdf':'application/pdf',
    'pdx':'application/vnd.adobe.pdx',
    'pgl':'application/x-pgl',
    'pko':'application/vnd.ms-pki.pko',
    'plg':'text/html',
    'plt':'application/x-plt',
    'png':'application/x-png',
    'ppa':'application/vnd.ms-powerpoint',
    'pps':'application/vnd.ms-powerpoint',
    'ppt':'application/x-ppt',
    'prf':'application/pics-rules',
    'prt':'application/x-prt',
    'ps':'application/postscript',
    'pwz':'application/vnd.ms-powerpoint',
    'ra':'audio/vnd.rn-realaudio',
    'ras':'application/x-ras',
    'rdf':'text/xml',
    'red':'application/x-red',
    'rjs':'application/vnd.rn-realsystem-rjs',
    'rlc':'application/x-rlc',
    'rm':'application/vnd.rn-realmedia',
    'rmi':'audio/mid',
    'rmm':'audio/x-pn-realaudio',
    'rms':'application/vnd.rn-realmedia-secure',
    'rmx':'application/vnd.rn-realsystem-rmx',
    'rp':'image/vnd.rn-realpix',
    'rsml':'application/vnd.rn-rsml',
    'rtf':'application/msword',
    'rv':'video/vnd.rn-realvideo',
    'sat':'application/x-sat',
    'sdw':'application/x-sdw',
    'slb':'application/x-slb',
    'slk':'drawing/x-slk',
    'smil':'application/smil',
    'snd':'audio/basic',
    'sor':'text/plain',
    'spl':'application/futuresplash',
    'ssm':'application/streamingmedia',
    'stl':'application/vnd.ms-pki.stl',
    'sty':'application/x-sty',
    'swf':'application/x-shockwave-flash',
    'tg4':'application/x-tg4',
    'tif':'image/tiff',
    'tiff':'image/tiff',
    'top':'drawing/x-top',
    'tsd':'text/xml',
    'uin':'application/x-icq',
    'vcf':'text/x-vcard',
    'vdx':'application/vnd.visio',
    'vpg':'application/x-vpeg005',
    'vsd':'application/x-vsd',
    'vst':'application/vnd.visio',
    'vsw':'application/vnd.visio',
    'vtx':'application/vnd.visio',
    'wav':'audio/wav',
    'wb1':'application/x-wb1',
    'wb3':'application/x-wb3',
    'wiz':'application/msword',
    'wk4':'application/x-wk4',
    'wks':'application/x-wks',
    'wma':'audio/x-ms-wma',
    'wmf':'application/x-wmf',
    'wmv':'video/x-ms-wmv',
    'wmz':'application/x-ms-wmz',
    'wpd':'application/x-wpd',
    'wpl':'application/vnd.ms-wpl',
    'wr1':'application/x-wr1',
    'wrk':'application/x-wrk',
    'ws2':'application/x-ws',
    'wsdl':'text/xml',
    'xdp':'application/vnd.adobe.xdp',
    'xfd':'application/vnd.adobe.xfd',
    'xhtml':'text/html',
    'xls':'application/x-xls',
    'xml':'text/xml',
    'xq':'text/xml',
    'xquery':'text/xml',
    'xsl':'text/xml',
    'xwd':'application/x-xwd',
    'sis':'application/vnd.symbian.install',
    'x_t':'application/x-x_t',
    'apk':'application/vnd.android.package-archive',
    'tif':'image/tiff',
    '0.301':'application/x-301',
    '0.906':'application/x-906',
    'a11':'application/x-a11',
    'ai':'application/postscript',
    'aifc':'audio/aiff',
    'anv':'application/x-anv',
    'asf':'video/x-ms-asf',
    'asx':'video/x-ms-asf',
    'avi':'video/avi',
    'biz':'text/xml',
    'bot':'application/x-bot',
    'c90':'application/x-c90',
    'cat':'application/vnd.ms-pki.seccat',
    'cdr':'application/x-cdr',
    'cer':'application/x-x509-ca-cert',
    'cgm':'application/x-cgm',
    'class':'java/*',
    'cmp':'application/x-cmp',
    'cot':'application/x-cot',
    'crt':'application/x-x509-ca-cert',
    'css':'text/css',
    'dbf':'application/x-dbf',
    'dbx':'application/x-dbx',
    'dcx':'application/x-dcx',
    'dgn':'application/x-dgn',
    'dll':'application/x-msdownload',
    'dot':'application/msword',
    'dtd':'text/xml',
    'dwf':'application/x-dwf',
    'dxb':'application/x-dxb',
    'edn':'application/vnd.adobe.edn',
    'eml':'message/rfc822',
    'epi':'application/x-epi',
    'eps':'application/postscript',
    'exe':'application/x-msdownload',
    'fdf':'application/vnd.fdf',
    'fo':'text/xml',
    'g4':'application/x-g4',
    '':'application/x-',
    'gl2':'application/x-gl2',
    'hgl':'application/x-hgl',
    'hpg':'application/x-hpgl',
    'hqx':'application/mac-binhex40',
    'hta':'application/hta',
    'htm':'text/html',
    'htt':'text/webviewhtml',
    'icb':'application/x-icb',
    'ico':'application/x-ico',
    'ig4':'application/x-g4',
    'iii':'application/x-iphone',
    'ins':'application/x-internet-signup',
    'IVF':'video/x-ivf',
    'jfif':'image/jpeg',
    'jpe':'application/x-jpe',
    'jpg':'image/jpeg',
    'js':'application/x-javascript',
    'la1':'audio/x-liquid-file',
    'latex':'application/x-latex',
    'lbm':'application/x-lbm',
    'ls':'application/x-javascript',
    'm1v':'video/x-mpeg',
    'm3u':'audio/mpegurl',
    'mac':'application/x-mac',
    'math':'text/xml',
    'mdb':'application/x-mdb',
    'mht':'message/rfc822',
    'mi':'application/x-mi',
    'midi':'audio/mid',
    'mml':'text/xml',
    'mns':'audio/x-musicnet-stream',
    'movie':'video/x-sgi-movie',
    'mp2':'audio/mp2',
    'mp3':'audio/mp3',
    'mpa':'video/x-mpg',
    'mpe':'video/x-mpeg',
    'mpg':'video/mpg',
    'mpp':'application/vnd.ms-project',
    'mpt':'application/vnd.ms-project',
    'mpv2':'video/mpeg',
    'mpx':'application/vnd.ms-project',
    'mxp':'application/x-mmxp',
    'nrf':'application/x-nrf',
    'odc':'text/x-ms-odc',
    'p10':'application/pkcs10',
    'p7b':'application/x-pkcs7-certificates',
    'p7m':'application/pkcs7-mime',
    'p7s':'application/pkcs7-signature',
    'pci':'application/x-pci',
    'pcx':'application/x-pcx',
    'pdf':'application/pdf',
    'pfx':'application/x-pkcs12',
    'pic':'application/x-pic',
    'pl':'application/x-perl',
    'pls':'audio/scpls',
    'png':'image/png',
    'pot':'application/vnd.ms-powerpoint',
    'ppm':'application/x-ppm',
    'ppt':'application/vnd.ms-powerpoint',
    'pr':'application/x-pr',
    'prn':'application/x-prn',
    'ps':'application/x-ps',
    'ptn':'application/x-ptn',
    'r3t':'text/vnd.rn-realtext3d',
    'ram':'audio/x-pn-realaudio',
    'rat':'application/rat-file',
    'rec':'application/vnd.rn-recording',
    'rgb':'application/x-rgb',
    'rjt':'application/vnd.rn-realsystem-rjt',
    'rle':'application/x-rle',
    'rmf':'application/vnd.adobe.rmf',
    'rmj':'application/vnd.rn-realsystem-rmj',
    'rmp':'application/vnd.rn-rn_music_package',
    'rmvb':'application/vnd.rn-realmedia-vbr',
    'rnx':'application/vnd.rn-realplayer',
    'rpm':'audio/x-pn-realaudio-plugin',
    'rt':'text/vnd.rn-realtext',
    'rtf':'application/x-rtf',
    'sam':'application/x-sam',
    'sdp':'application/sdp',
    'sit':'application/x-stuffit',
    'sld':'application/x-sld',
    'smi':'application/smil',
    'smk':'application/x-smk',
    'sol':'text/plain',
    'spc':'application/x-pkcs7-certificates',
    'spp':'text/xml',
    'sst':'application/vnd.ms-pki.certstore',
    'stm':'text/html',
    'svg':'text/xml',
    'tdf':'application/x-tdf',
    'tga':'application/x-tga',
    'tif':'application/x-tif',
    'tld':'text/xml',
    'torrent':'application/x-bittorrent',
    'txt':'text/plain',
    'uls':'text/iuls',
    'vda':'application/x-vda',
    'vml':'text/xml',
    'vsd':'application/vnd.visio',
    'vss':'application/vnd.visio',
    'vst':'application/x-vst',
    'vsx':'application/vnd.visio',
    'vxml':'text/xml',
    'wax':'audio/x-ms-wax',
    'wb2':'application/x-wb2',
    'wbmp':'image/vnd.wap.wbmp',
    'wk3':'application/x-wk3',
    'wkq':'application/x-wkq',
    'wm':'video/x-ms-wm',
    'wmd':'application/x-ms-wmd',
    'wml':'text/vnd.wap.wml',
    'wmx':'video/x-ms-wmx',
    'wp6':'application/x-wp6',
    'wpg':'application/x-wpg',
    'wq1':'application/x-wq1',
    'wri':'application/x-wri',
    'ws':'application/x-ws',
    'wsc':'text/scriptlet',
    'wvx':'video/x-ms-wvx',
    'xdr':'text/xml',
    'xfdf':'application/vnd.adobe.xfdf',
    'xls':'application/vnd.ms-excel',
    'xlw':'application/x-xlw',
    'xpl':'audio/scpls',
    'xql':'text/xml',
    'xsd':'text/xml',
    'xslt':'text/xml',
    'x_b':'application/x-x_b',
    'sisx':'application/vnd.symbian.install',
    'ipa':'application/vnd.iphone',
    'xap':'application/x-silverlight-app',
    }

    def __init__(self, host, port=25):
        self._host = host
        self._port = port
 
    def set_host(self, h):
        self._host = h

    def set_port(self, p):
        self._port = p

    def set_auth_user(self, s):
        self._auth_user = s

    def set_user_pass(self, s):
        self._user_pass = s
    
    def set_mail_from(self, s):
        self._mail_from = s
    
    def set_mail_to(self, s):
        self._mail_to = s
    
    def set_mail_cc(self, s):
        self._mail_cc = s

    def set_mail_bcc(self, s):
        self._mail_bcc = s
        
    def set_content_from(self, s):
        self._content_from = s
    
    def set_content_to(self, s):
        self._content_to = s

    def set_content_cc(self, s):
        self._content_cc = s

    def set_mail_subject(self, s):
        self._mail_subject = s

    def set_mail_content(self, s):
        self._mail_content = s

    def set_mail_attach(self, filelist):
        self._mail_attach = filelist

    def set_is_html(self, b):
        self._is_html = b

    def set_time_out(self, t):
        self._time_out = t

    def _format_addr(self, s):
        # input RCPT TO string '一二三<123@119.com>'

        name, addr = parseaddr(s)
        return formataddr(( \
            Header(name, 'utf-8').encode(), addr))

    def _mailto_rebuild(self, toaddr):
        # input RCPT TO 
        # string    # '一二三<123@119.com>,中语言C<abc@119.com>,AA高丽A<a@119.com>' 
        # output format encode mail object

        msg_to = []

        for s in toaddr.split(","):
            name, addr = parseaddr(s)
            msg_to.append((
                "=?utf-8?B?" + base64.b64encode(name.encode("utf-8")).decode("utf-8") + "?=") + ' <' + addr + '>')

        return ','.join(msg_to)

    def creatMsg(self):
        # 邮件信体处理
        
        if self._is_html == True:
            html_plain = 'html'
        else:
            html_plain = 'plain'
        
        msg = MIMEMultipart('')
        msg['Subject'] = self._mail_subject
        
        if self._content_from == None:
            msg['From'] = self._format_addr(self._mail_from)
        else:
            msg['From'] = self._format_addr(self._content_from)

        if self._content_to == None:
            msg['To'] = self._mailto_rebuild(self._mail_to)
        else:
            msg['To'] = self._mailto_rebuild(self._content_to)
        
        
        if self._mail_cc != None or self._content_cc != None:
            if self._content_cc == None:
                msg['CC'] = self._mailto_rebuild(self._mail_cc)
            else:
                msg['CC'] = self._mailto_rebuild(self._content_cc)
                

        msg_html_content = MIMEText(self._mail_content,html_plain,_charset='utf-8')
        msg.attach(msg_html_content)

        if self._mail_attach != None:
            for attach_file in self._mail_attach:
                file_name = os.path.basename(attach_file)
                file_type = file_name.split('.')[-1]

                if os.path.isfile(attach_file):

                    fp = open(attach_file, 'rb')

                    contype = self._content_type.get(file_type)
                    maintype, subtype = contype.split('/', 1)

                    att = MIMEBase(maintype, subtype, name= \
                        "=?utf-8?B?" + base64.b64encode(file_name.encode("utf-8")).decode("utf-8") + "?=")
                    # 加上必要的头信息:
                    att.add_header('Content-Disposition', 'attachment', filename= \
                        "=?utf-8?B?" + base64.b64encode(file_name.encode("utf-8")).decode("utf-8") + "?=")
                    # att.add_header('Content-ID', '<0>')
                    # att.add_header('X-Attachment-Id', '0')
                    # 把附件的内容读进来:
                    att.set_payload(fp.read())
                    # 用Base64编码:
                    encoders.encode_base64(att)
                    # 添加到MIMEMultipart:
                    msg.attach(att)
                    fp.close()
        return msg.as_string()

    def send(self, msgdata):
        """
        # from must be a string
        # rcptto must be list
        """
        smtpfrom = self._mail_from

        if self._mail_cc != None and self._mail_cc != '':
            smtpto = self._mail_to + "," + self._mail_cc
        else:
            smtpto = self._mail_to

        if self._mail_bcc != None and self._mail_bcc != '':
            smtpto = smtpto + "," + self._mail_bcc

        if smtpto == None or smtpto == '':
            return """Must set_mail_to()"""

        if self._port == 465:
            return "Anonymous send must use port 25"
        smtphandle = smtplib.SMTP(timeout=self._time_out)
        try:
            smtphandle.connect(self._host, self._port)
        except Exception as connerror:
            return connerror
        smtphandle.helo(self._helo)
        try:
            smtphandle.sendmail(smtpfrom,smtpto.split(','),msgdata)
        except Exception as senderror:
            smtphandle.quit()
            smtphandle.close()
            return senderror
        smtphandle.quit()
        smtphandle.close()
        return True
        
    def authsend(self, msgdata):
        """
        # from must be a string
        # rcptto must be list
        """
        if self._auth_user == None or self._user_pass == None:
            return """Must set mailuser and password : 
                _set_auth_user('username')
                _set_user_pass('password')"""
        
        smtpfrom = self._mail_from

        if self._mail_cc != None and self._mail_cc != '':
            smtpto = self._mail_to + "," + self._mail_cc
        else:
            smtpto = self._mail_to

        if self._mail_bcc != None and self._mail_bcc != '':
            smtpto = smtpto + "," + self._mail_bcc

        if smtpto == None or smtpto == '':
            return """Must set_mail_to()"""

        if self._port == 465:
            smtphandle = smtplib.SMTP_SSL(timeout=self._time_out)
        else:
            smtphandle = smtplib.SMTP(timeout=self._time_out)
        try:
            smtphandle.connect(self._host, self._port)
        except Exception as connerror:
            return connerror
        smtphandle.ehlo(self._helo)
        try:
            smtphandle.login(self._auth_user, self._user_pass)
        except Exception as autherror:
            return autherror
        try:
            smtphandle.sendmail(smtpfrom,smtpto.split(','),msgdata)
        except Exception as senderror:
            smtphandle.quit()
            smtphandle.close()
            return senderror
        smtphandle.quit()
        smtphandle.close()
        return True
    
if __name__ == '__main__':

    quicksend = QuickEmail('192.168.120.119', 465)
    quicksend.set_auth_user('a')
    quicksend.set_user_pass('test')
    quicksend.set_mail_from('高丽<a@119.com>')
    quicksend.set_mail_to('一二三<123@119.com>,中语言C<abc@119.com>,AA高丽A<a@119.com>')
    quicksend.set_mail_bcc('张三<b@119.com>')
    quicksend.set_mail_subject('mY subject还有中文!')
    quicksend.set_mail_content('<font color=red>red content一段中文</font>')
    quicksend.set_mail_attach(['C:\\Users\\Administrator\\Pictures\\163.com.png'])
    quicksend.set_is_html(True)
    quicksend.set_content_from('假发件人<a@a.com>')
    quicksend.set_content_cc('假抄送人<abc@a.com>')

    
    msg = quicksend.creatMsg()
    # print(msg)
    print(quicksend.authsend(msg))

    
