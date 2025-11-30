import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.by import By
from helper import generate_registration_data
from locators import Locators
from curl import login_form


class TestRegistrationWithNewCredentials:
    def test_success_registration(self, regestration_page):
        name, email, password = generate_registration_data()

        regestration_page.find_element(*Locators.REG_NAME).send_keys(name)
        regestration_page.find_element(*Locators.REG_EMAIL).send_keys(email)
        regestration_page.find_element(*Locators.REG_PASSWORD).send_keys(password)
        regestration_page.find_element(*Locators.REG_BUTTON).click()

        wait = WebDriverWait(regestration_page, 10)
        wait.until(EC.url_contains("login"))

        assert regestration_page.current_url == login_form


class TestRegistrationWithInvalidPassword:
    def test_invalid_password_in_regestration(self, regestration_page):
        name, email, _ = generate_registration_data()

        short_password = "12345"

        regestration_page.find_element(*Locators.REG_NAME).send_keys(name)
        regestration_page.find_element(*Locators.REG_EMAIL).send_keys(email)
        regestration_page.find_element(*Locators.REG_PASSWORD).send_keys(short_password)
        regestration_page.find_element(*Locators.REG_BUTTON).click()

        wait = WebDriverWait(regestration_page, 10)
        error_element = wait.until(
            EC.visibility_of_element_located(Locators.ERROR_PASSWORD)
        )

        assert error_element.text == "Некорректный пароль"


class TestRegistrationWithEmptyName:
    def test_empty_name_in_registration(self, regestration_page):
        _, email, password = generate_registration_data()

        initial_url = regestration_page.current_url

        regestration_page.find_element(*Locators.REG_EMAIL).send_keys(email)
        regestration_page.find_element(*Locators.REG_PASSWORD).send_keys(password)
        regestration_page.find_element(*Locators.REG_BUTTON).click()

        wait = WebDriverWait(regestration_page, 10)
        wait.until(EC.url_contains("register"))

        current_url = regestration_page.current_url
        assert "register" in current_url
