from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    browser.implicitly_wait(5)
    button = browser.find_element(By.ID, 'book')
    WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button.click()
    x = browser.find_element(By.ID, 'input_value').text
    res = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(res)
    browser.find_element(By.ID, 'solve').click()

finally:
    #ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
