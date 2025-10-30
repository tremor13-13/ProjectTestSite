import time
import allure
import pytest
from base.base_test import BaseTest
from faker import Faker
from test_data.name_test_data import CombinedTestCases

faker = Faker()

class TestAccount(BaseTest):

    @pytest.mark.smoke
    def test_change_name(self):
        self.login_page.open()
        self.login_page.login(
            login=self.credentials.LOGIN,
            password=self.credentials.PASSWORD
        )
        self.login_page.take_screenshot("Loggin complited ")
        self.dashboard_page.is_opened()
        self.dashboard_page.go_to_my_info_page()
        time.sleep(3)
        self.myinfopage.personal_details.change_first_last_name(faker.first_name())
        self.myinfopage.personal_details.change_middle_name(faker.last_name())
        time.sleep(5)
        self.myinfopage.personal_details.save_change()
        time.sleep(5)
        self.myinfopage.contact_details.cklic_contact_details()
        self.myinfopage.contact_details.contact_deteals_adress_add(faker.address())
        self.myinfopage.contact_details.save_contact_details()
        self.myinfopage.take_screenshot("Save my info page complited")
        time.sleep(5)

    # Параметризованные тесты (Тест дизайн + предугадывание ошибок)
    @pytest.mark.regression
    @pytest.mark.parametrize("test_data", CombinedTestCases.get_all_cases(),
                             ids=lambda x: f"{x.test_type}_{x.first_name[:5]}_{x.middle_name[:5]}")
    def test_combined_names_validation(self, test_data):
        """
        Тестируем ВЗАИМОДЕЙСТВИЕ полей First Name и Middle Name
        """
        # ПОДГОТОВКА - логинимся и переходим на страницу
        self.login_page.open()
        self.login_page.login(
            login=self.credentials.LOGIN,
            password=self.credentials.PASSWORD
        )
        self.dashboard_page.is_opened()
        self.dashboard_page.go_to_my_info_page()
        time.sleep(5)

        # ДЕЙСТВИЕ - заполняем ОБА поля
        with allure.step(f"Заполняем First: '{test_data.first_name}', Middle: '{test_data.middle_name}'"):
            # Заполняем First Name
            self.myinfopage.personal_details.change_first_last_name(test_data.first_name)
            # Заполняем Middle Name
            self.myinfopage.personal_details.change_middle_name(test_data.middle_name)
            # Сохраняем
            self.myinfopage.personal_details.save_change()
            time.sleep(6)

        # ПРОВЕРКА
        if test_data.expected_result == "success":
            # Если ожидаем успех - проверяем что нет ошибок
            assert not self.myinfopage.personal_details.error_first_name()
            assert not self.myinfopage.personal_details.error_big_name()
            print(f"Тест прошел как и ожидалось first = '{test_data.first_name}'- Middle = '{test_data.middle_name}'")

        else:
            error_first_name = self.myinfopage.personal_details.error_first_name()
            error_big_name = self.myinfopage.personal_details.error_big_name()
            if error_first_name or error_big_name:
                print( f"Ожидаемая ошибка для комбинации: First='{test_data.first_name}', Middle='{test_data.middle_name}'")
            else:
                pytest.fail(
                     f"Ошибка не ожидалась для комбинации: First='{test_data.first_name}', Middle='{test_data.middle_name}'")

