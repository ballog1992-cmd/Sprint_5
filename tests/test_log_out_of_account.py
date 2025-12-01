from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from curl import *


class TestLogOutFromHomePageButton:

    def test_log_out_home_page_button(self, main_page, login):

        main_page.find_element(*Locators.BUTTON_TRANSFER_LOGIN_PAGE).click()
        login(main_page)

        wait = WebDriverWait(main_page, 10)

        wait.until(EC.element_to_be_clickable(Locators.ACCOUNT_LINK)).click()

        wait.until(EC.url_contains("/account/profile"))
        wait.until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)).click()

        wait.until(EC.url_to_be(login_form))

        current_url = main_page.current_url
        assert current_url == login_form
