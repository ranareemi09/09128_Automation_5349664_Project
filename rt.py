from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')

textBoxesList = driver.find_elements(By.CLASS_NAME, "text_field")
for i in textBoxesList:
    #i.send_keys("Matrix College")
    print(i.accessible_name)
    if i.accessible_name == "First Name":
        i.send_keys("Reemi")
    elif i.accessible_name == "Last Name":
        i.send_keys("Rana")
    elif i.accessible_name == "Phone":
        i.send_keys("99988857777")

inputElemsList = driver.find_elements(By.CLASS_NAME, "multiple_choice")

for i in inputElemsList:
   print(i.accessible_name)
time.sleep(9)
timeDDL= driver.find_element(By.CSS_SELECTOR, ("input[value=Radio-1]"))
timeDDL.click()

timeDDL = driver.find_element(By.ID, "RESULT_RadioButton-9")

objsel =Select(timeDDL)
objsel.select_by_visible_text("Afternoon")

time.sleep(600)
