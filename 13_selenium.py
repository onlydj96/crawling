from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome() #executable_path= 'C:\study\crawling\chromedriver.exe') # chrome driver가 다른 경로일 경우 경로를 써주어야함

# 1. 네이버로 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 동작
elem = browser.find_element(By.CLASS_NAME, 'link_login')
elem.click()

# 3. id, pw 입력
browser.find_element(By.ID, 'id').send_keys("naver_id")
browser.find_element(By.ID, 'pw').send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element(By.ID, 'log.login').click()

# 5. ID 다시 입력
browser.find_element(By.ID, 'id').clear()
browser.find_element(By.ID, 'id').send_keys("new_naver_id")

# 6. html 정보 출력
print(browser.page_source)


# 7. 브라우저 종료
browser.quit()

# while True:
#     pass