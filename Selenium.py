# pip install selenium
# pip install webdriver_manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.get('https://www.google.com/')
time.sleep(3)
srch = driver.find_element("xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
srch.send_keys('best movies 2022 site:imdb.com' + Keys.RETURN)
time.sleep(3)
driver.find_element("xpath", '/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/a').click()
time.sleep(3)
driver.find_element("xpath", '/html/body/div[2]/div/div[2]/div[3]/div[1]/div/div[2]/p/a[1]').click()

src = driver.page_source
src.count('lister-item-header')
