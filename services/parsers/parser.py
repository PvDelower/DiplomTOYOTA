import requests
import re
from bs4 import BeautifulSoup

new_n = []
html = 'https://auto.ru/cars/hyundai/solaris/used/'  # Kio Rio2017
r = requests.get(html)
r.encoding = 'unicode'
soup = BeautifulSoup(r.text, 'html.parser' )
n = soup.find_all(class_="ListingItemPrice-module__content")
new_n1 = ""
for i in range(len(n)):
    if n[i].find('span') is not None:
        new_n.append(n[i].text.replace(u'\xa0',' ').replace(u'\u2009', ''))
        for i in range(len(new_n)):
            new_n1 += new_n[i]

print(new_n1)