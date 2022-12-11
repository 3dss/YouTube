# pip install selenium
# pip install webdriver_manager
# pip install bs4
# pip install requests

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

from bs4 import BeautifulSoup

soup = BeautifulSoup(driver.page_source, 'html.parser')

all_img = soup.find_all('img')

all_alt = [x['alt'] if x.has_attr('alt') else '' for x in all_img]
all_src = [x['loadlate'] if x.has_attr('loadlate') else x['src'] for x in all_img]

import requests

for i in all_src:
    try:
        img_req = requests.get(i).content
        with open(f'new_image_{all_alt[all_src.index(i)]}.jpg', 'wb') as file_img:
            file_img.write(img_req)
    except:
        print(i)
