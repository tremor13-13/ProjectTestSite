from data.credentials import Credentials
from pages.login_page.page import LoginPage
from pages.dashboard_page.page import DashboardPage
from pages.my_info_page.page import MyInfoPage
from pages.my_info_page.components.personal_details import PersonalDetailsComponent
from pages.my_info_page.components.contact_deteils import ContactDetails

class BaseTest:

    def setup_method(self):
        self.credentials = Credentials()
        self.login_page = LoginPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)
        self.myinfopage = MyInfoPage(self.driver)
        self.personal_details_component = PersonalDetailsComponent(self.driver)
        self.contact_details_component = ContactDetails(self.driver)

