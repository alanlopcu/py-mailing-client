import smtplib
import os
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

path='src\\mailclient\\'

#cwd = os.getcwd()
#cwd = cwd
#files = os.listdir(cwd)
#print("Files in %r: %s" % (cwd, files))

server = smtplib.SMTP('smtp.randomdomain.com',25)

server.ehlo()

with open(path+'password.txt','r') as f:
    password = f.read()
    
server.login('sendermail@randomdomain.com',password)

msg = MIMEMultipart()
msg['From'] = 'Ex: John Doe'
msg['To'] = 'destinationmail@domaindestination.com'
msg['Subject'] = 'Testing PY mailing client'

with open(path+'message.txt','r') as f:
    message = f.read()
    
msg.attach(MIMEText(message,'plain'))

filename = path+'landscape.jpg'
attachment = open(filename,'rb')

p = MIMEBase('application','octect-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)

p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('sendermail@randomdomain.com','destinationmail@randomdomain.com',text)