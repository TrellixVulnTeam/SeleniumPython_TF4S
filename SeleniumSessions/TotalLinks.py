from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

# driver.get('https://www.freshworks.com//')
driver.get('https://www.amazon.com/')
print(driver.title)

linksList = driver.find_elements(By.TAG_NAME, 'a')
print(len(linksList))

for ele in linksList:
    link_text = ele.text
    print(link_text)
    print(ele.get_attribute('href'))

imageList = driver.find_elements(By.TAG_NAME, 'img')
print(len(imageList))

for ele in imageList:
    print(ele.get_attribute('src'))


driver.close()