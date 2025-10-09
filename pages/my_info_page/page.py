from base.base_page import BasePage
from data.urls import Urls
from pages.my_info_page.components.personal_details import PersonalDetailsComponent

class MyInfoPage(BasePage):

    _PAGE_URL = Urls.MY_INFO_PAGE


    def __init__(self, driver):
        super().__init__(driver)
        self.personal_details = PersonalDetailsComponent(driver)