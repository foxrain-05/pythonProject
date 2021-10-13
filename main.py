from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://map.naver.com/v5/search/%EB%8F%99%EB%AC%BC%EB%B3%91%EC%9B%90')

driver.implicitly_wait(3)

driver.quit()