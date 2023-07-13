import requests
from bs4 import BeautifulSoup
import smtplib
product_url="https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B0B8SVGBL4/ref=sr_1_2_sspa?" \
            "crid=3AK9KVLFMVGO2&keywords=samsung+galaxy+flip&qid=1687953871&sprefix=samsung+galaxy+fli%2Caps%2C249&" \
            "sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
head = {
    "Accept-Language" : "en-US,en;q=0.9",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
purchase_price = 88000
response = requests.get(product_url, headers=head)
code = response.text
soup = BeautifulSoup(code, "html.parser")
product_code = soup.find(name="span", id="productTitle").text.strip().split("(")
product = product_code[0]
price_code = soup.find(name="span", class_="a-price-whole")
price_list = price_code.text.strip(".").split(",")
final_price = int(f"{price_list[0]}{price_list[1]}")

if final_price < purchase_price:
    email = "yaswanthreddy600@gmail.com"
    password = "wthroywdddfognpa"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email,password)
        message = f"Subject: Price drop alert\n\nthe product '{product}' you wanted buy, is available for {final_price} rupees now!!"
        connection.sendmail(email, email, msg=message)
        print("mail sent")







