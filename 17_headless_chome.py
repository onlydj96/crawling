from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('window-size=1920x1080')

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = 'https://play.google.com/store/movies/collection/topselling_paid?clp=ChcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljLCcE4&gsr=ChkKFwoVCg90b3BzZWxsaW5nX3BhaWQQBxgE:S:ANO1ljKn82s&hl=ko&gl=US'
browser.get(url)

# 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 3080)") # 모니터(해상도) 높이인 1080 위치로 스크롤 내리기


# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")


import time

interval = 2 # 2초에 한번씩 스크롤을 내리자

# 현재 문서 높이를 가져와서 저장

prev_height = browser.execute_script('return document.body.scrollHeight')

# 반복 수행

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    
    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script('return document.body.scrollHeight')

    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료 ")
browser.get_screenshot_as_file("google_movie.png")

import requests
from bs4 import BeautifulSoup


soup = BeautifulSoup(browser.page_source, 'lxml')

movies = soup.find_all("div", attrs={"class":"ULeU3b"})
# print(len(movies))



for movie in movies:
    title = movie.find("div", attrs={'class':'Epkrse'}).get_text()

    # 할인 전 가격
    original_price = movie.find("span", attrs={'class':'SUZt4c P8AFK'})
    if original_price:
        original_price = original_price.get_text()
    
    else:
        # print(title, "  <할인되지 않은 영화 제외>")
        continue
    
    # 할인 된 가격
    price = movie.find('span', attrs={'class':'VfPpfd VixbEe'}).get_text()

    # 링크 
    link = movie.find('a', attrs={'class':'Si6A0c ZD8Cqc'})['href']
    # 올바른 링크 : https://play.google.com + link

    print(f'제목 : {title}')
    print(f'할인 전 금액 : {original_price}')
    print(f'할인 후 금액 : {price}')
    print("링크 : ", "https://play.google.com" + link)
    print("-"*100)