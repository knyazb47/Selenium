from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestNew(unittest.TestCase):
    def test_1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]').send_keys('Sergey')
            browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]').send_keys('Knyazev')
            browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]').send_keys('Knyazb.serg@mail.ru')
            browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your phone:"]').send_keys('+7 911-111-11 11')
            browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your address:"]').send_keys('Home sweet home')
            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, ".btn")
            button.click()
            actual_result = browser.find_element(By.TAG_NAME, 'h1').text
            expected_result = 'Congratulations! You have successfully registered!'
            print(type(actual_result))
            self.assertEquals(actual_result, expected_result, "Регестрация не пройдена")
        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]').send_keys('Sergey')
            browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]').send_keys('Knyazev')
            browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]').send_keys('Knyazb.serg@mail.ru')
            browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your phone:"]').send_keys('+7 911-111-11 11')
            browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your address:"]').send_keys('Home sweet home')
            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, ".btn")
            button.click()
            actual_result = browser.find_element(By.TAG_NAME, 'h1').text
            expected_result = 'Congratulations! You have successfully registered!'
            self.assertEquals(actual_result, expected_result, "Не верный резултат")
        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()

if __name__ == "__main__":
    unittest.main()