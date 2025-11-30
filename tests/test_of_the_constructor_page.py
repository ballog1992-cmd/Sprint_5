from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from curl import *


class TestConstructionTabsIngredientBurger:

    def test_tabs_ingridient_burger_buns(self, main_page):

        main_page.find_element(*Locators.TAB_SAUSES).click()

        wait = WebDriverWait(main_page, 10)
        wait.until(EC.visibility_of_element_located(Locators.TAB_SAUSES))

        main_page.find_element(*Locators.TAB_BUNS).click()

        wait.until(EC.visibility_of_element_located(Locators.TAB_BUNS))

        assert main_page.find_element(*Locators.TAB_BUNS).text == "Булки"

    def test_tabs_ingridient_burger_sauce(self, main_page):

        main_page.find_element(*Locators.TAB_SAUSES).click()

        wait = WebDriverWait(main_page, 10)
        wait.until(EC.visibility_of_element_located(Locators.TAB_SAUSES))

        assert main_page.find_element(*Locators.TAB_SAUSES).text == "Соусы"

    def test_tabs_ingridient_burger_filling(self, main_page):

        main_page.find_element(*Locators.TAB_STUFFING).click()

        wait = WebDriverWait(main_page, 10)
        wait.until(EC.visibility_of_element_located(Locators.TAB_STUFFING))

        assert main_page.find_element(*Locators.TAB_STUFFING).text == "Начинки"
