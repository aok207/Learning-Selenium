# import time
from pathlib import Path
from typing import Union

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver_location: str = str(Path.cwd().parent.joinpath("chromedriver.exe"))
service: Service = Service(executable_path=driver_location)
driver = webdriver.Chrome(service=service)

url: str = "https://orteil.dashnet.org/cookieclicker/"

driver.get(url)

# ids
cookie_id: str = "bigCookie"
cookie_count_id: str = "cookies"
product_price_prefix: str = "productPrice"
product_prefix: str = "product"


# Wait until language picker appears
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

# Choose english
language: WebElement = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

# Wait for another loading
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, cookie_id)))

# Click on cookie
cookie: WebElement = driver.find_element(By.ID, cookie_id)

while True:
    cookie_count: int = int(
        driver.find_element(By.ID, cookie_count_id).text.split(" ")[0].replace(",", "")
    )
    cookie.click()

    for i in range(4):
        product_price: Union[str, int] = driver.find_element(
            By.ID, product_price_prefix + str(i)
        ).text.replace(",", "")

        if not product_price.isdigit():
            continue

        product_price = int(product_price)

        if cookie_count >= product_price:
            product: WebElement = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
