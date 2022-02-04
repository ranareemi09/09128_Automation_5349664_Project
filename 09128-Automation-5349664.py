from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.google.com')
driver.implicitly_wait(20)
srch_bar = driver.find_element(By.NAME,"q")
srch_bar.send_keys("java")

srch_bar.submit()

results = driver.find_elements(By.XPATH, "//ntp-realbox[@role='listbox']//cr-most-visited/descendant::dom-if[@style='display']")

count=len(results)
print(results)
print("length of list is:",count)