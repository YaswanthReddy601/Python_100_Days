import getpass
import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)#server domine name, port number
print(server.ehlo())
print(server.starttls())

email = input("Enter gmail: ")
password = input("Password : ")
print(server.login(email,password))

from_add = input()
to_add = input()
subject = input()
message = input()
msg = "Subject: "+subject+"\n"+message

print(server.sendmail(from_add, to_add, message))
print("mail sent")
