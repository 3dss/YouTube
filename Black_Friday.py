pip install notify_run
pip install selenium
pip install webdriver_manager


from notify_run import Notify
notify = Notify()
notify.register()


url = 'https://www.amazon.eg/-/en/Logitech-MK235-Wireless-Keyboard-Mouse/dp/B073H8PH86/ref=sr_1_13?crid=198US168PZBXI&keywords=logitec&qid=1669154721&qu=eyJxc2MiOiIzLjYyIiwicXNhIjoiMi45NSIsInFzcCI6IjAuMDAifQ%3D%3D&sprefix=logitec%2Caps%2C146&sr=8-13'
xpath = '/html/body/div[2]/div[1]/div[6]/div[4]/div[4]/div[9]/div[3]/div[1]/span/span[1]'
wait = 60 # in seconds
my_price = 700 # in EGP


from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

while True:
    driver.get(url)
    time.sleep(3)
    price = driver.find_element("xpath", xpath)
    price_int = float(price.get_attribute("innerHTML")[3:])
    print(price_int)
    if price_int <= my_price:
        notify.send("your item is now under EGP{}".format(my_price), url)
    time.sleep(wait)
