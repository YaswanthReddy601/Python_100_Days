import random
import pandas
import datetime
import smtplib
##################### Hard Starting Project ######################
birthday_dict = {
    "name" : "",
    "month": 0,
    "day": 0
}
present_data = datetime.datetime.now()
this_month = present_data.month
this_day = present_data.day
# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes. 
data = pandas.read_csv("birthdays.csv")
birthday_data = data.to_dict(orient="records")
for x in birthday_data:
    birthday_dict = {
        "name" : x["name"],
        "mail_address" : x["email"],
        "month" : x["month"],
        "day" : x["day"]
    }
# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:

    if this_month == birthday_dict["month"] and this_day == birthday_dict["day"]:
        file = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file) as letter:
            data = letter.read()
            data = data.replace("[NAME]", birthday_dict["name"])
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    # HINT: https://www.w3schools.com/python/ref_string_replace.asp
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            email = "yaswanthreddy600@gmail.com"
            password = "kcmcayxnhswwklee"
            connection.login(email, password)
            to = birthday_dict["mail_address"]
            connection.sendmail(from_addr=email, to_addrs=to, msg=f"Subject: Happy Birthday\n\n {data}")
# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



