from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
from math import log, sin

# def calc(x):
#   return str(math.log(abs(12*sin(x))))
try: 
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    numberX = browser.find_element(By.ID, "input_value")
    b = numberX.text
    x = int(b)
    print(x)
    y = log(abs(12*sin(x)))
    print(y)

    input  = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    check_box = browser.find_element(By.ID, "robotCheckbox")
    check_box.click()

    radio_button = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_button)
    radio_button.click()    


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
  
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()