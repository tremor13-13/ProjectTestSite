import time

import allure

from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Keys



class PersonalDetailsComponent(BasePage):

    _FIRST_NAME_FIELD = "//input[@name= 'firstName']"
    _MIDDLE_NAME_FIELD = "//input[@name= 'middleName']"
    _SUBMIT_BUTTON = "(//button[@type= 'submit'])[1]"
    _FIRSR_NAME_ERROR_EMPTY = "//span[text()='Required']"
    _NAME_ERROR_BIG_NAME = "//span[text()='Should not exceed 30 characters']"


    @allure.step("Изменяем имя пользователя")
    def change_first_last_name(self, first_name):
        first_name_field = self.wait.until(EC.element_to_be_clickable(self._FIRST_NAME_FIELD))
        current_value = first_name_field.get_attribute("value")
        first_name_field.send_keys(Keys.CONTROL + "A", Keys.BACKSPACE)
        WebDriverWait(self.driver, 5).until(
            lambda d: first_name_field.get_attribute("value") == "",
            message="Middle name field not cleared"
        )
        first_name_field.send_keys(first_name)
        assert current_value != first_name_field.get_attribute("value"), "Name was not 'chenged'"


    @allure.step("Изменяем 'отчество' Middle Name")
    def change_middle_name(self, middle_name):
        middle_name_field = self.wait.until(EC.element_to_be_clickable(self._MIDDLE_NAME_FIELD))
        current_value = middle_name_field.get_attribute("value")
        middle_name_field.send_keys(Keys.CONTROL + "A", Keys.BACKSPACE)
        WebDriverWait(self.driver, 5).until(
            lambda a: middle_name_field.get_attribute("value") == "",
            message="Middle name field not cleared"
        )
        middle_name_field.send_keys(middle_name)
        assert current_value != middle_name_field.get_attribute("value"), "Name was not chenged"
        time.sleep(4)


    @allure.step("Сохраняем изменения + скриншот")
    def save_change(self):
        self.wait.until(EC.element_to_be_clickable(self._SUBMIT_BUTTON)).click()
        self.wait_for_loading_complete()
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Personal deteals",
            attachment_type=allure.attachment_type.PNG
        )

    def error_first_name(self):
        """Проверка ошибки при пустом поле First Name"""
        try:
            error = self.wait.until(EC.presence_of_element_located(self._FIRSR_NAME_ERROR_EMPTY))
            return error.text
        except:
            return None

    def error_big_name(self):
        """Проверка на длину введенного текста в поле"""
        try:
            error = self.wait.until(EC.presence_of_element_located(self._NAME_ERROR_BIG_NAME))
            return error.text
        except:
            return None