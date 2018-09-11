import sys
if sys.version_info[0] < 3:
  from email.MIMEMultipart import MIMEMultipart
  from email.MIMEText import MIMEText
  from email.MIMEBase import MIMEBase
  from email.MIMEImage import MIMEImage
  
else:
  from email.mime.multipart import MIMEMultipart
  from email.mime.text import MIMEText
  from email.mime.base import MIMEBase
  from email.mime.image import MIMEImage

  
import smtplib

from email import encoders 
import base64

class EnviarEmail:
  
  def __init__(self):
    self.nome = None



  def Enviar(self, params):
    
    obrigatorios = ['from', 'to', 'ip', 'subject', 'content']
    for o in obrigatorios:
      if not o in params:
        print "O campo "+ o + " é obrigatorio"
        return ""
    
    
    fromaddr = params["from"]
    toaddr = params["to"]
    if 'cc' in params:
      cc = params["cc"]
    else:
      cc = ""
    if 'bcc' in params:
      bcc = params["bcc"]
    else:
      bcc = ""
    

    msg = MIMEMultipart()
    
    vbcc = [] if bcc == "" else bcc.split(";")
    vcc = [] if cc == "" else cc.split(";")
    rcpt = vbcc  + vcc + [toaddr]
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Cc'] = cc
    msg['Bcc'] = bcc
    msg['Subject'] = params["subject"]
     
    body = params["content"]
     
    body_type = 'plain'
    if(body.upper().find('<HTML>')>=0):
      body_type = 'html'  
    
    msg.attach(MIMEText(body, body_type))
     
#    if params["attach_file"]:
    if 'file_name' in params:
      filename = params["file_name"][params["file_name"].rfind("/")+1:]
      attachment = open(params["file_name"], "rb")
       
      part = MIMEBase('application', 'octet-stream')
      part.set_payload((attachment).read())
      encoders.encode_base64(part)
      part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
       
      msg.attach(part)
    
    #169.254.8.75 
    #180.128.170.65
    server = smtplib.SMTP(params['ip'], 25) 
    text = msg.as_string()
    server.sendmail(fromaddr, rcpt, text)
    server.quit()
    return "E-mail enviado com sucesso!"
    
