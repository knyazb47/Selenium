import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3')
    serves_chrome = Service()
    browser = webdriver.Chrome(options=options, service=serves_chrome)
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "button.favorite")

# import pytest
#
# @pytest.mark.xfail(strict=True)
# def test_succeed():
#     assert True
#
#
# @pytest.mark.xfail
# def test_not_succeed():
#     assert False
#
#
# @pytest.mark.skip
# def test_skipped():
#     assert False