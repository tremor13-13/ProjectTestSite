from data.credentials import Credentials
from pages.login_page.page import LoginPage
from pages.dashboard_page.page import DashboardPage
from pages.my_info_page.page import MyInfoPage


class BaseTest:



    def setup_metod(self):
        self.credentials = Credentials()
        self.login_page = LoginPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)
        self.myinfopage = MyInfoPage(self.driver)

