from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
import math

# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/selects1.html   "
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    one = num1.text
    one_int = int(one)

    num2 = browser.find_element(By.ID, "num2")
    two = num2.text
    two_int = int(two)

    summa = one_int + two_int
    summa_str = str(summa)

    select = Select(browser.find_element(By.TAG_NAME,"select"))
    select.select_by_value(summa_str)
    

    # x_element = browser.find_element(By.ID, "treasure")
    # x = x_element.get_attribute("valuex")  
    # y = calc(x)

    # check_box = browser.find_element(By.ID, "robotCheckbox")
    # check_box.click()

    # radio_button = browser.find_element(By.ID, "robotsRule")
    # radio_button.click()

    # input1 = browser.find_element(By.ID, "answer")
    # input1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
  
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()