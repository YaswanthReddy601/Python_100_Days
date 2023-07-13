import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

F_add = "yaswanthreddy600@gmail.com"
T_add = F_add

msg = MIMEMultipart()
msg["From"] =F_add
msg["To"] = T_add
msg["Subject"] = "Subject"
body = """
    lin1
    lin2
"""
msg.attach(MIMEText(body, "plain"))
file = "cities.csv"
attached = open(file, "rb")

attached_app = MIMEBase("application", "octa-stream")
attached_app.set_payload((attached).read())
encoders.encode_base64(attached_app)

attached_app.add_header("Content-Disposition", "attachment: filename= "+file)
msg.attach(attached_app)

server = smtplib.SMTP("smtm.gmail.com", 587)
server.starttls()

password = input("password: ")
server.login(F_add, password)

text = msg.as_string()

server.sendmail(F_add, T_add, text)

server.quit()