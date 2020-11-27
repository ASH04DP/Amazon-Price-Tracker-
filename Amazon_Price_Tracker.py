import requests
from bs4 import BeautifulSoup
import smtplib
import re


URL = 'https://www.amazon.in/Raspberry-Pi-8GB-Desktop-Computer/dp/B08B9XS3B6/ref=sr_1_2?crid=2T42TSY05QB7S&dchild=1&keywords=raspberry+pi+4+8gb+ram&qid=1596349955&sprefix=raspberry+pi+4+8%2Caps%2C270&sr=8-2'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52'}

#check_price done
def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = price[0:7]
    final_price = re.sub("[₹]", " " , converted_price)
    final_price1 = float(re.sub("[,]", "", final_price))

    print(final_price1)
    print(title.strip())

    if(final_price1 < 3000.0):
        send_mail()




def send_mail():
    gmail_user = "dinakar.pathakota@gmail.com"
    gmail_pwd = "wxqrmgnanlucuwok"
    TO = 'dinakar.pathakota@gmail.com'
    SUBJECT = "Rasberrry Pi4 Price Drop"
    TEXT = "Check out the link   https://www.amazon.in/Raspberry-Pi-8GB-Desktop-Computer/dp/B08B9XS3B6/ref=sr_1_2?crid=2T42TSY05QB7S&dchild=1&keywords=raspberry+pi+4+8gb+ram&qid=1596349955&sprefix=raspberry+pi+4+8%2Caps%2C270&sr=8-2 "
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pwd)
    BODY = '\r\n'.join(['To: %s' % TO,
            'From: %s' % gmail_user,
            'Subject: %s' % SUBJECT,
            '', TEXT])

    server.sendmail(gmail_user, [TO], BODY)
    print ('Mail sent')

check_price()