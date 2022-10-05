#!C:\python\python.exe
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import cgi, cgitb 
import csv
import re             
valid=[]
invalid=[] 
form = cgi.FieldStorage()  
sub = form.getvalue('subject')    
attachment = form.getvalue('attach')  
msg=form.getvalue('message')
cnt= form.getvalue('send')

msg = MIMEMultipart()
regex = re.compile(r'([a-z]+[.-_])*[A-Za-z0-9]+@[gmail$]+(\.[com$]{3})+')
with open('BULKEMAIL.csv', mode ='r') as file:
     csvFile = csv.DictReader(file)
     for lines in csvFile:
         if re.search(regex, str(lines)):
            valid.append(lines)
         else:
            invalid.append(lines)  
target=valid
password = "internpassword@123"
msg['From'] = "exposys6@gmail.com"
msg['To'] = ', '.join(target)
msg['Subject'] = "sub"
msg['message']="msg"
msg.attach(MIMEText(msg, 'plain'))
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
server.login(msg['From'], password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
print("successfully sent email to %s:" % (msg['To']))
