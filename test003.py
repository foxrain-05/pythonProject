from selenium import webdriver
import time
driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://www.google.com/maps/search/%EB%8F%99%EB%AC%BC%EB%B3%91%EC%9B%90')

driver.implicitly_wait(3)


for j in range(1):
    scroll_list = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]')
    driver.execute_script("arguments[0].scrollBy(0, 200);", scroll_list)
    for i in range(1, 11, 2):
        driver.find_element_by_xpath(f'//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/div['+ str(i) +']/div/a').click()
        name = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]').text # 이름
        address = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[7]/div[1]/button/div[1]/div[2]/div[1]').text #주소
        driver.find_element_by_xpath('//*[@id="omnibox-singlebox"]/div[1]/div[1]/button').click() # 뒤로가기
        print("이름:" + name + "\n""주소:" + address + "\n")



driver.quit()

