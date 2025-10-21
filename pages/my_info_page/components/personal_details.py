import time

import allure

from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys



class PersonalDetailsComponent(BasePage):

    _FIRST_NAME_FIELD = "//input[@name= 'firstName']"
    _MIDDLE_NAME_FIELD = "//input[@name= 'middleName']"
    _SUBMIT_BUTTON = "(//button[@type= 'submit'])[1]"


    @allure.step("Изменяем имя пользователя")
    def change_first_last_name(self, first_name):
        first_name_field = self.wait.until(EC.element_to_be_clickable(self._FIRST_NAME_FIELD))
        current_value = first_name_field.get_attribute("value")
        first_name_field.send_keys(Keys.CONTROL + "A", Keys.BACKSPACE)
        first_name_field.send_keys(first_name)

        assert current_value != first_name_field.get_attribute("value"), "Name was not 'chenged'"


    @allure.step("Изменяем 'отчество' Middle Name")
    def change_middle_name(self, middle_name):
        middle_name_field = self.wait.until(EC.element_to_be_clickable(self._MIDDLE_NAME_FIELD))
        middle_name_field.send_keys(Keys.CONTROL + "A", Keys.BACKSPACE)
        middle_name_field.send_keys(middle_name)
        time.sleep(4)


    @allure.step("Сохраняемся")
    def save_change(self):
        self.wait.until(EC.element_to_be_clickable(self._SUBMIT_BUTTON)).click()
        self.wait_for_page_load()
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Personal deteals",
            attachment_type=allure.attachment_type.PNG
        )