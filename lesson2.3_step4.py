from cgitb import text
from ntpath import join
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from math import log, sin
import os



try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    buttonOne = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    buttonOne.click()

    alertOne = browser.switch_to.alert
    alertOne.accept()

    valueOne = browser.find_element(By.ID, "input_value")
    valueText = valueOne.text
    valueInt = int(valueText)
    
    x = log(abs(12*sin(valueInt)))

    input = browser.find_element(By.ID, "answer")
    input.send_keys(x)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
