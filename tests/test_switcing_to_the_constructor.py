from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from curl import *


class TestTransitionTheConstructorPage:
    def test_transition_the_constructor_click_logo(self, login_page):
        login_page.find_element(*Locators.CLICK_THE_LOGO_OF_CONSTRUCTOR).click()

        wait = WebDriverWait(login_page, 3)
        wait.until(EC.url_contains(main_site))

        current_url = login_page.current_url
        assert main_site in current_url

    def test_transition_the_constructor_click_constructor_button(self, login_page):
        login_page.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        wait = WebDriverWait(login_page, 10)
        wait.until(EC.url_contains(main_site))

        current_url = login_page.current_url
        assert main_site in current_url
