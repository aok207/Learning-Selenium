import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

service: Service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

# Search for elements in HTML and interact with them
input_ele: WebElement = driver.find_element(By.CLASS_NAME, "gLFyf")
input_ele.send_keys("Python selenium" + Keys.ENTER)

time.sleep(10)

driver.quit()
