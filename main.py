import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

service: Service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

# Search for elements in HTML and interact with them
input_ele: WebElement = driver.find_element(By.CLASS_NAME, "gLFyf")
input_ele.clear()
input_ele.send_keys("Python selenium" + Keys.ENTER)

# Wait for elements to load first
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Selenium Python Tutorial"))
)

# Click link
link: WebElement = driver.find_element(By.PARTIAL_LINK_TEXT, "Selenium Python Tutorial")
link.click()

time.sleep(10)

driver.quit()
