import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from curl import *
from data import ButtonTexts


@pytest.mark.parametrize("tab_text,tab_locator", [
     
    
    (ButtonTexts.text_tub_sause, Locators.TAB_SAUSES),
    (ButtonTexts.text_tub_filling, Locators.TAB_STUFFING),
    (ButtonTexts.text_tub_buns, Locators.TAB_BUNS)
])
class TestConstructionTabsIngredientBurger:
    def test_tabs_ingridient_burger(self, konstructor_page, tab_text,tab_locator):

        konstructor_page.find_element(*tab_locator).click()

        wait = WebDriverWait(konstructor_page, 10)
        wait.until(EC.text_to_be_present_in_element(Locators.ACTIVE_TAB, tab_text))

        active_tab = konstructor_page.find_element(*Locators.ACTIVE_TAB)
        assert active_tab.text == tab_text