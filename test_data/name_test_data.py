# test_data/name_test_data.py
from dataclasses import dataclass
from typing import List
from faker import Faker
import random
import string
faker = Faker()


@dataclass
class CombinedTestData:
    first_name: str  # для поля First Name
    middle_name: str  # для поля Middle Name
    test_type: str  # тип теста
    expected_result: str  # ожидаемый результат

def generate_name(length=5):
    """Генерирует случайное имя из букв заданной длины"""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

class CombinedTestCases:
    # ОБА поля валидные - ДОЛЖНО РАБОТАТЬ
    BOTH_VALID = [
        CombinedTestData("John", "Michael", "both_valid_typical", "success"),
        CombinedTestData(faker.first_name(), faker.last_name(), "both_valid_random", "success"),
        CombinedTestData("Anna-Maria", "Van Der Berg", "both_valid_complex", "success"),
    ]

    # ОДНО поле пустое - ДОЛЖНА БЫТЬ ОШИБКА
    # ONE_EMPTY = [
    #     CombinedTestData("", "Michael", "first_empty", "error"),  # First Name пустое
    #     CombinedTestData("John", "", "middle_empty", "error"),  # Middle Name пустое
    #     CombinedTestData("", "", "both_empty", "error"),  # Оба пустые
    # ]

    # ГРАНИЧНЫЕ значения для обоих полей
    BOUNDARY = [
        CombinedTestData(generate_name(30), generate_name(30), "max_length", "success"),
        # 30 символов - ДОЛЖНО РАБОТАТЬ
        CombinedTestData(generate_name(31), generate_name(5), "first_too_long", "error"),  # 31 символ - ОШИБКА
        CombinedTestData(generate_name(5), generate_name(31), "middle_too_long", "error"),  # 31 символ - ОШИБКА
    ]

    @classmethod
    def get_all_cases(cls) -> List[CombinedTestData]:
        return cls.BOTH_VALID + cls.BOUNDARY