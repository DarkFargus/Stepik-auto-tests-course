from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from cgitb import text
from ntpath import join
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from math import log, sin



try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button2 = browser.find_element(By.ID, "book")
    button2.click()

    button3 = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button3)

    valueOne = browser.find_element(By.ID, "input_value")
    valueText = valueOne.text
    valueInt = int(valueText)
    
    x = log(abs(12*sin(valueInt)))

    input = browser.find_element(By.ID, "answer")
    input.send_keys(x)

    button3.click()
    

   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
