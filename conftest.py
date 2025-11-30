import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from curl import *
from locators import Locators
from data import Credentials
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def main_page(driver):
    driver.get(main_site)
    return driver


@pytest.fixture(scope="function")
def regestration_page(driver):
    driver.get(regestration_form)
    return driver


@pytest.fixture(scope="function")
def recovery_password_page(driver):
    driver.get(password_recovery_page)
    return driver


@pytest.fixture(scope="function")
def login_page(driver):
    driver.get(login_form)
    return driver


@pytest.fixture
def login():
    def _login(driver):
        wait = WebDriverWait(driver, 10)

        email_field = wait.until(EC.presence_of_element_located(Locators.EMAIL))
        email_field.send_keys(Credentials.email)

        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        wait.until(EC.presence_of_element_located(Locators.CHECKOUT_BUTTON))

    return _login
