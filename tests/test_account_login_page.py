from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from curl import *
from data import ButtonTexts

class TestSuccessfulLoginFromDifferentPages:

    def test_login_home_page_button(self, main_page, login):

        main_page.find_element(*Locators.BUTTON_TRANSFER_LOGIN_PAGE).click()

        login(main_page)

        wait = WebDriverWait(main_page, 10)
        checkout_button = wait.until(
            EC.visibility_of_element_located(Locators.CHECKOUT_BUTTON)
        )

        assert checkout_button.text == ButtonTexts.button_checkout


    def test_logging_account_the_regestration_page(self, regestration_page, login):

        regestration_page.find_element(*Locators.REG_BUTTON_TRANSFER_LOGIN_PAGE).click()

        login(regestration_page)

        wait = WebDriverWait(regestration_page, 10)
        checkout_button = wait.until(
            EC.visibility_of_element_located(Locators.CHECKOUT_BUTTON)
        )
        assert checkout_button.text == ButtonTexts.button_checkout


    def test_logging_account_the_recovery_password_page(
        self, recovery_password_page, login
    ):

        recovery_password_page.find_element(
            *Locators.PASSWORD_BUTTON_TRANFER_LOGIN_PAGE
        ).click()

        login(recovery_password_page)

        wait = WebDriverWait(recovery_password_page, 10)
        checkout_button = wait.until(
            EC.visibility_of_element_located(Locators.CHECKOUT_BUTTON)
        )
        assert checkout_button.text == ButtonTexts.button_checkout
