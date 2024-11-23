import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"/home/malachy/selenium"
driver =  webdriver.Firefox()

driver.get("https://google.com")


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("tech with tim"+Keys.RETURN)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech With Tim") )
)

link = driver.find_elements(By.PARTIAL_LINK_TEXT, "Tech With Tim")
print(link)
link[0].click()
time.sleep(10)
driver.quit()