import allure
from allure_commons import fixture
from faker import Faker
from selenium.webdriver.remote.webdriver import WebDriver
from metaclasses.meta_locator import MetaLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(metaclass=MetaLocator):

    _MY_INFO_ITEM = "//a/span[text()='My Info']"

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        self.faker = Faker()

    def open(self):
        with allure.step(f'Open {self._PAGE_URL} page'):
            self.driver.get(self._PAGE_URL)

    @allure.step("Проверка то что мы на той странице что надо")
    def is_opened(self):
        self.wait.until(EC.url_to_be(self._PAGE_URL))

    def go_to_my_info_page(self):
        self.wait.until(EC.element_to_be_clickable(self._MY_INFO_ITEM)).click()

