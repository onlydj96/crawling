import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=6&backgroundColor='
headers1 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

res = requests.get(url, headers=headers1)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

print(res.text)
# print(soup.find("div",  attrs={"class":"c_card"}))