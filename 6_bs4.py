import requests 
from bs4 import BeautifulSoup

url = 'http://comic.naver.com/webtoon/weekday.nhn'

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
# print(soup.title)
# print(soup.title.get_text())

# print(soup.a)  # soup으로 가져온 element info중에 처음 나오는 a 정보를 가져옴
# print(soup.a.attrs)  # a tag의 속성
# print(soup.a['href'])  # a tag의 href의 속성값만 추출


# print(soup.find("a",  attrs={"class":"Nbtn_upload"}))  # a tag 속성 중 class가 Nbtn_upload인 경우를 찾아줌

# rank1 = soup.find("li",  attrs={"class":"rank01"})
# print(rank1.a.get_text())  # soup으로 찾은 객체중 a tag것만 가져오기
# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling  # 다음 것으로 넘어가기. 하지만 중간에 띄워져 있으면 두 번 써야됨
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())


# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())


# print(rank1.parent)

# rank2 = rank1.find_next_sibling('li')  # li의 해당하는 tag의 다음 것으로 넘어가기 때문에 번거롭게 쓰기 않아도 됨
# print(rank2.a.get_text())

# rank1.find_next_siblings('li')
# print(rank1.a.get_text())


webtoon = soup.find("a", text='대학원 탈출일지-71화-돌아온 세미나(1)') # 모든 text중에서 element가 a이고 text가 변수값인 값
print(webtoon)