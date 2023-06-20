import smtplib


Email = "yaswanthreddy600@gmail.com"
password = input("password : ")

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(Email, password)

From = "yaswanthreddy600@gmail.com"
To = "yaswanthreddy601@gmail.com"
message = "Hello World"

server.sendmail(From, To, message)
print("mail sent")


