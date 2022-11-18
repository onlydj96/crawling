import requests
import re
from bs4 import BeautifulSoup

url = 'https://search.11st.co.kr/Search.tmall?kwd=%25EB%2585%25B8%25ED%258A%25B8%25EB%25B6%2581#pageNum%%2%%page%%1'
headers1 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

res = requests.get(url, headers=headers1)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
print(soup.find("div",  attrs={"class":"c_card"}))
# items = soup.find_all('div', attrs={'class':'c_card c_card_list'})
# print(items)
# print(items[0].find('div', attrs={'class':'name'}).get_text())

# for item in items: