from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pytest

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    img = browser.find_element(By.ID, 'treasure')
    x = img.get_attribute('valuex')
    y = calc(x)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radio_button = browser.find_element(By.ID, 'robotsRule')
    radio_button.click()

    button_send = browser.find_element(By.CLASS_NAME, 'btn')
    button_send.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()