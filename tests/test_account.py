import time

from base.base_test import BaseTest
from faker import Faker
faker = Faker()


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
        self.myinfopage.personal_details.change_first_last_name(faker.last_name())
        self.myinfopage.personal_details.change_middle_name(faker.last_name())
        time.sleep(5)
        self.myinfopage.personal_details.save_change()
        time.sleep(5)
        self.myinfopage.contact_details.cklic_contact_details()
        self.myinfopage.contact_details.contact_deteals_adress_add(faker.address())
        self.myinfopage.contact_details.save_contact_details()
        time.sleep(5)
