from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url)

# 1. 가는날 선택
browser.find_element(By.CLASS_NAME, 'tabContent_option__2y4c6 select_Date__1aF7Y')


# 여기서부터 안됨


# # 이번달 27일, 28일 선택
# browser.find_elements(By.NAME, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[3]/button')[0].click()
# browser.find_elements(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[1]/td[5]/button').click()