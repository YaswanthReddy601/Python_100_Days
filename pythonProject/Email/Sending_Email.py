import smtplib


smtp_obj = smtplib.SMTP("smtp.gmail.com",587)#connecting server
print(smtp_obj.ehlo())#checks the server up or not
print(smtp_obj.starttls())#transport layer security for security

email = input("Enter your Email address : ")
password = input("Enter Password : ")
print(smtp_obj.login(email,password))

from_address = email
To_address = email
subject = input("Subject " )
message = input("message : ")
msg = "Subject: "+subject+"\n"+message

print(smtp_obj.sendmail(from_address, To_address, msg))

print(smtp_obj.quit())



