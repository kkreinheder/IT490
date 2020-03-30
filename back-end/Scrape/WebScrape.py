import pymysql
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/58.0.3029.110 Safari/537.3'}
url = 'https://www.amazon.com/Dell-Optiplex-Processor-Keyboard-Bluetooth/dp/B07J9J1CJF/ref=sr_1_3?keywords=computer' \
      '&qid=1583718891&sr=8-3 '
response = requests.get(url, headers=headers)
soup = BeautifulSoup(html_doc, 'html.parser')
#soup = BeautifulSoup(response.content, features="lxml")
title = soup.select("#productTitle")[0].get_text().strip()
price = soup.select("#priceblock_saleprice")[0].get_text()

db = pymysql.connect("172.18.0.3", "test", "test", "db-mysql")

cursor = db.cursor()

write = "INSERT INTO user (product_name, product_price) VALUES ('title', 'price')"

try:
    cursor.execute(write)
    db.commit()

except:
    db.rollback()

db.close()
