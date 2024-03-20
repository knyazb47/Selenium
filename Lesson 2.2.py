#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import time
#
# try:
#     link = "https://suninjuly.github.io/selects1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     text_x = browser.find_element(By.ID, 'num1')
#     x = int(text_x.text)
#     text_y = browser.find_element(By.ID, 'num2')
#     y = int(text_y.text)
#     res = x + y
#     select = Select(browser.find_element(By.ID, 'dropdown'))
#     select.select_by_value(str(res))
#
#     # Отправляем заполненную форму
#     button = browser.find_element(By.CSS_SELECTOR, ".btn")
#     button.click()
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
#
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
#     link = "https://SunInJuly.github.io/execute_script.html"
#     browser.get(link)
#     x = browser.find_element(By.ID, 'input_value').text
#     res = calc(x)
#     browser.execute_script("window.scrollBy(0, 200);")
#     browser.find_element(By.ID, 'answer').send_keys(res)
#     browser.find_element(By.ID, 'robotCheckbox').click()
#     browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]').click()
#     browser.find_element(By.CLASS_NAME, "btn").click()
# finally:
#     #ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/file_input.html"
    browser.get(link)
    browser.find_element(By.NAME, 'firstname').send_keys('Sergey')
    browser.find_element(By.NAME, 'lastname').send_keys('Knyazev')
    browser.find_element(By.NAME, 'email').send_keys('kn@mail.ru')
    curren_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(curren_dir, "fff.txt")
    browser.find_element(By.ID, 'file').send_keys(file_path)
    browser.find_element(By.CLASS_NAME, 'btn').click()


finally:
    #ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()