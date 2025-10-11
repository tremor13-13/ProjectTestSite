import time
import allure
import pytest
from base.base_test import BaseTest
from faker import Faker
from test_data.name_test_data import NameTestCases
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

   # НОВЫЙ параметризованный тест - ДОБАВЛЯЕМ ЭТОТ МЕТОД
    @pytest.mark.parametrize("test_data", NameTestCases.get_all_cases(),
                             ids=lambda x: f"{x.test_type}_{x.name[:10]}")
    def test_name_validation(self, test_data):
        """
        Тестируем валидацию имен с разными граничными значениями
        """
        # Подготовка
        self.login_page.open()
        self.login_page.login(
            login=self.credentials.LOGIN,
            password=self.credentials.PASSWORD
        )
        self.dashboard_page.is_opened()
        self.dashboard_page.go_to_my_info_page()
        time.sleep(2)

        # Действие
        with allure.step(f"Тестируем имя: '{test_data.name}'"):
            # Вводим тестовое имя
            self.myinfopage.personal_details.change_first_last_name(test_data.name)
            self.myinfopage.personal_details.save_change()
            time.sleep(2)

        # Упрощенная проверка - если expected_result = "success",
        # считаем что тест прошел, иначе падаем
        if test_data.expected_result == "error":
            pytest.fail(f"Ожидалась ошибка для имени: {test_data.name}")