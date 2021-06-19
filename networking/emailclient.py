import smtplib
from email.mime.text import MIMEText

body="this is a test email"
msg=MIMEText(body)
msg['From']="aditya.lamaniya@gmail.com"
msg['To']="aditya.lamaniya@gmail.com"
msg['Subject']="test email "

server=smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login("email","password")

server.send_message(msg)
print("mail sent ")

server.quit()