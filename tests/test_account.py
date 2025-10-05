import time

from base.base_test import BaseTest


class TestAccount(BaseTest):

    def test_change_name(self):
        self.login_page.open()
        self.login_page.login(
            login=self.credentials.LOGIN,
            password=self.credentials.PASSWORD
        )
        time.sleep(3)