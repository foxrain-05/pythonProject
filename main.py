from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://www.google.com/maps/search/%EB%8F%99%EB%AC%BC%EB%B3%91%EC%9B%90')

driver.implicitly_wait(3)


def get(line):
        driver.find_element_by_xpath(
            '//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/div[' + str(line) + ']/div/a').click()
        name = driver.find_element_by_xpath(
            '//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]').text
        address = driver.find_element_by_xpath(
            '//*[@id="pane"]/div/div[1]/div/div/div[7]/div[1]/button/div[1]/div[2]/div[1]').text
        phone_num = driver.find_element_by_xpath(
            '//*[@id="pane"]/div/div[1]/div/div/div[7]/div[2]/button/div[1]/div[2]/div[1]').text
        driver.find_element_by_xpath(
            '//*[@id="omnibox-singlebox"]/div[1]/div[1]/button').click()
        print("이름:" + name + "\n""주소:" + address + "\n" + "전화번호:" + phone_num + "\n")


for i in range(1, 21, 2):
    get(i)

driver.quit()
