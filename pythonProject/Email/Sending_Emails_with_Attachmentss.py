import smtplib

#Multipurpose Internet Mail Extensions
"""MimeText is used for sending text emails."""
from email.mime.text import MIMEText
"""it supports the transfer of single or multiple text and non-text 
attachments( graphics, audio, and video files)."""
from email.mime.multipart import MIMEMultipart
#used to indicate Content-type
from email.mime.base import MIMEBase

#Encodes thefile
from email import encoders

FromAdd = "yaswanthreddy600@gmail.com"
ToAdd = "yaswanthreddy601@gmail.com"

msg = MIMEMultipart()
msg["From"] = FromAdd
msg["To"] = ToAdd
msg["Subject"] = "Subject of the mail"
body = "Body of the mail"

msg.attach(MIMEText(body, "plain"))#plain text
filename = "cities.csv"
attachment = open(filename, "rb")

attachment_app = MIMEBase("application", "octet-stream")
# the carrying capacity of a packet of transmission data unit is called payload
attachment_app.set_payload((attachment).read())
#base64 encoding takes 8-bit binary byte data and encodes it
encoders.encode_base64(attachment_app)

attachment_app.add_header("Content-Disposition", "attachment; filename= " +filename)
msg.attach(attachment_app)


server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

password = input("Enter password: ")
server.login(FromAdd, password)

text = msg.as_string()

server.sendmail(FromAdd, ToAdd, text)

server.quit()