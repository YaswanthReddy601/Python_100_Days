import random
import smtplib
import datetime

random_quote = ""
present_time =datetime.datetime.now()
to_day = present_time.weekday()
if to_day == 4:
    with open("quotes.txt") as all_quotes:
        quotes = all_quotes.readlines()
        random_quote = random.choice(quotes)
print(random_quote)

email= "yaswanthreddy600@gmail.com"
password = "kcmcayxnhswwklee"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(email,password)
    connection.sendmail(from_addr=email,
                        to_addrs="yaswanthreddy601@gmail.com",
                        msg=f"Subject: monday motivation\n{random_quote}")