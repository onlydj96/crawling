import requests 
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/list?titleId=570503&weekday=thu'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

cartoons = soup.find_all('td', attrs={"class":"title"})
# title = cartoons[0].a.get_text()

# link = cartoons[0].a['href']
# print(title)
# print('https://comic.naver.com' + link)  # link가 중간부터 시작할 수도 있음


# 만화 제목 + 링크 가져오기
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a['href']
    print(title, link)


# 평점 구하기
total_rate = 0
cartoons = soup.find_all("div", attrs={"class" :"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    total_rate +=float(rate)

print(f"전체 점수 : {total_rate}")
print(f"평균 점수 : {total_rate/len(cartoons)}")