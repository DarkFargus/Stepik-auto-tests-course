from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Shiba-Inu")

    button = browser.find_element(By.CSS_SELECTOR, "[type=submit]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла