import time

import allure
from allure_commons.types import Severity

from base.base_page import BasePage
from data.urls import Urls
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    _PAGE_URL = Urls.LOGIN_PAGE
    _USERNAME_FIELD = "//input[@name='username']"
    _PASSWORD_FIELD = "//input[@name='password']"
    _SUBMIT_BUTTON = "//button[@type='submit']"

    @allure.step("Авторизация на сайте")
    def login(self, login, password):
        user_name = self.wait.until(EC.element_to_be_clickable(self._USERNAME_FIELD))
        user_name.send_keys(login)
        user_password = self.wait.until(EC.element_to_be_clickable(self._PASSWORD_FIELD))
        user_password.send_keys(password)
        submit_button = self.wait.until(EC.element_to_be_clickable(self._SUBMIT_BUTTON))
        submit_button.click()
        time.sleep(5)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Login user",
            attachment_type=allure.attachment_type.PNG
        )

