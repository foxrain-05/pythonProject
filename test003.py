from selenium import webdriver
import sys

options = webdriver.ChromeOptions()

options.add_argument("headless")

driver = webdriver.Chrome('chromedriver.exe', options=options)

driver.get('https://www.google.com/maps/search/%EB%8F%99%EB%AC%BC%EB%B3%91%EC%9B%90/@' + sys.argv[1] +',' + sys.argv[2] + ',11z')

driver.implicitly_wait(3)

for i in range(1, 11, 2):
    try:
        driver.find_element_by_xpath(f'//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/div[' + str(i) + ']/div/a').click()
    except:
        print("ERROR")
        continue
    name = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]').text # 이름
    address = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[7]/div[1]/button/div[1]/div[2]/div[1]').text
    try:
        phonenum = ""
        phonenum = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[7]/div[2]/button/div[1]/div[2]/div[1]').text
    except:
        try:
            phonenum = ""
            phonenum = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[7]/div[4]/button/div[1]/div[2]/div[1]').text
        except:
            try:
                phonenum = ""
                phonenum = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[7]/div[3]/button/div[1]/div[2]/div[1]').text
            except:
                phonenum = ""
    if ("02-" or "051-" or "053-" or "032-" or "062-" or "052-" or "044-" or "031-" or "033-" or "043-" or "041-" or "061-" or "054-" or "055-" or "064-")not in phonenum:
            phonenum = ""
    driver.find_element_by_xpath('//*[@id="omnibox-singlebox"]/div[1]/div[1]/button').click()
    print("이름:" + name + "\n주소:" + address + "\n연락처" + phonenum)

driver.quit()

