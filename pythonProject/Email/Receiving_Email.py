import imaplib
mail = imaplib.IMAP4_SSL("imap.gmail.com",993)
email = input("Email : ")
password = input("Password : ")

mail.login(email,password)
for x in mail.list()[1]:
    print(x)

print(mail.select('INBOX'))
typ, data = mail.search(None, 'SUBJECT "Subject"')

email_id = data[0]

result, email_data = mail.fetch(email_id,"(RFC822)")
raw_email = email_data[0][1]
raw_email_ = raw_email.decode("utf-8")

import email
final_email = email.message_from_string(raw_email_)

for x in final_email.walk():

    if x.get_content_type() == "text/html":
        body = x.get_payload(decode=True)
        print(body)

