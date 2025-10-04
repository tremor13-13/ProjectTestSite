from base.base_page import BasePage
from data.urls import Urls
from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    _PAGE_URL = Urls.LOGIN_PAGE
    _USERNAME_FIELD = "//input[@name='username']"
    _PASSWORD_FIELD = "//input[@name='password']"
    _SUBMIT_BUTTON = "//button[@type='submit']"


    def login(self, login, password):
        user_name: WebElement = self.wait.until(self.EC.element_to_be_clickable(self._USERNAME_FIELD))
        user_name.send_keys(login)
        user_password: WebElement = self.wait.until(self.EC.element_to_be_clickable(self._PASSWORD_FIELD))
        user_password.send_keys(password)
        submit_button: WebElement = self.wait.until(self.EC.element_to_be_clickable(self._SUBMIT_BUTTON))
        submit_button.click()
