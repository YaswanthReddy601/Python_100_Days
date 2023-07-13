import smtplib


Email = "yaswanthreddy600@gmail.com"
password = input("password : ")

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(Email, password)

To = "yaswanthreddy601@gmail.com"
message = "Hello World"

server.sendmail(Email, To, message)

print("mail sent")

server.close()


