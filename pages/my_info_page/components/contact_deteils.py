import time

import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from allure_commons.types import Severity

class ContactDetails(BasePage):

    _CKLIC_CONTACT_DETAILS = "//a[text()='Contact Details']"
    _ADDRESS_FIELD = "(//input[contains(@class, 'oxd-input')])[2]"
    _SUBMIT_BUTTON = "//button[@type='submit']"




    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.step("Переход на компонет Детали контакта")
    def cklic_contact_details(self):
        self.wait.until(EC.element_to_be_clickable(self._CKLIC_CONTACT_DETAILS)).click()

    @pytest.mark.smoke
    @allure.step("Добавляем адресс")
    def contact_deteals_adress_add(self, adress):
        adress_add = self.wait.until(EC.element_to_be_clickable(self._ADDRESS_FIELD))
        current_value = adress_add.get_attribute("value")
        adress_add.send_keys(Keys.CONTROL + "A", Keys.BACKSPACE)
        WebDriverWait(self.driver, 5).until(
            lambda a: adress_add.get_attribute("value") == "",
            message="Address add name field not cleared"
        )
        adress_add.send_keys(adress)
        assert current_value != adress_add.get_attribute("value"), "Adress was not changed"

    @allure.step("Сохраняем изменения")
    def save_contact_details(self):
        self.wait.until(EC.element_to_be_clickable(self._SUBMIT_BUTTON)).click()
        self.wait_for_loading_complete()
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Contact deteals add adress",
            attachment_type=allure.attachment_type.PNG
        )



