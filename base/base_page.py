import allure
from faker import Faker
from metaclasses.meta_locator import MetaLocator
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(metaclass=MetaLocator):

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 10, pull_frequency=1)
        self.EC = EC
        self.faker = Faker()

    def Open(self):
        with allure.step(f'Open {self._PAGE_URL} page'):
            self.driver.get(self._PAGE_URL)
