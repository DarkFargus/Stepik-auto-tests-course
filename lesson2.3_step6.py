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
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, "trollface")
    button.click()

    new_window2 = browser.window_handles[1]
    browser.switch_to.window(new_window2)
    time.sleep(1)

    valueOne = browser.find_element(By.ID, "input_value")
    valueText = valueOne.text
    valueInt = int(valueText)

    x = log(abs(12*sin(valueInt)))
    print(x)

    answer = browser.find_element(By.NAME, "text")
    answer.send_keys(x)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
