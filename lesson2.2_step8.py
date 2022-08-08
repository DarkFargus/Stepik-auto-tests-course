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
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    first_name.send_keys("Andrey")

    last_name = browser.find_element(By.CSS_SELECTOR,"[name='lastname']")
    last_name.send_keys("Sh")

    emailInput = browser.find_element(By.CSS_SELECTOR,"[name='email']")
    emailInput.send_keys("bla@bla.ru")

    files = os.path.abspath(os.path.dirname(__file__))
    file = os.path.join(files, "text.txt")

    joinFile = browser.find_element(By.ID, "file")
    joinFile.send_keys(file)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
