import requests 
from bs4 import BeautifulSoup

url = 'http://comic.naver.com/webtoon/weekday.nhn'

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

cartoons = soup.find_all("a", attrs={"class":"title"})

# class 속성ㅇ이 title 인 모든 element를 반환
for cartoon in cartoons:
    print(cartoon.get_text())