from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helper import generate_registration_data
from locators import Locators


class TestLoginFromAccountLink:

    def test_login_in_account_link(self, main_page, login):

        main_page.find_element(*Locators.ACCOUNT_LINK).click()

        login(main_page)

        wait = WebDriverWait(main_page, 10)
        checkout_button = wait.until(
            EC.visibility_of_element_located(Locators.CHECKOUT_BUTTON)
        )

        assert checkout_button.text == "Оформить заказ"
