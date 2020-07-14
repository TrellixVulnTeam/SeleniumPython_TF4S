from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import time

browser_name = "chrome"
if browser_name == "chrome":
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(executable_path="/Users/pradi/Desktop/chromedriver_win32/chromedriver.exe", options=options)
    #driver = webdriver.Chrome(ChromeDriverManager().install())

elif browser_name == "firefox":
    driver = webdriver.Firefox(executable_path="/Users/pradi/Desktop/geckodriver-v0.26.0-win64/geckodriver.exe")
   #driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browser_name == "safari":
    driver = webdriver.Safari()
else:
    print("Please pass the correct browser name : " + browser_name)

driver.implicitly_wait(10)
driver.get("http://www.google.com")
print(driver.title)
driver.find_element(By.NAME, 'q').send_keys("Naveen AutomationLabs")
time.sleep(3)

optionsList = driver.find_elements(By.CSS_SELECTOR,'ul.erkvQe li span')
for s in optionsList:
    print(s.text)

driver.close()