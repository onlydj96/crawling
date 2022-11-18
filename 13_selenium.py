from selenium import webdriver

browser = webdriver.Chrome('chromedriver.exe') # chrome driver가 다른 경로일 경우 경로를 써주어야함
browser.get("http://naver.com")