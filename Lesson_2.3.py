# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# try:
#     browser = webdriver.Chrome()
#     link = "http://suninjuly.github.io/alert_accept.html"
#     browser.get(link)
#     browser.find_element(By.CLASS_NAME, 'btn').click()
#     alert = browser.switch_to.alert
#     alert.accept()
#     x = browser.find_element(By.ID, 'input_value').text
#     res = calc(x)
#     browser.find_element(By.ID, 'answer').send_keys(res)
#     browser.find_element(By.CLASS_NAME, 'btn').click()
#
# finally:
#     #ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    browser.find_element(By.CLASS_NAME, 'btn').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.ID, 'input_value').text
    res = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(res)
    browser.find_element(By.CLASS_NAME, 'btn').click()

finally:
    #ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()