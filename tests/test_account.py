import time

from base.base_test import BaseTest


class TestAccount(BaseTest):

    def test_change_name(self):
        self.login_page.open()
        self.login_page.login(
            login=self.credentials.LOGIN,
            password=self.credentials.PASSWORD
        )
        self.dashboard_page.is_opened()
        self.dashboard_page.go_to_my_info_page()
        time.sleep(3)
        self.personal_details_component.change_first_name("Alex")


        time.sleep(3)