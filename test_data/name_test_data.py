from dataclasses import dataclass
from typing import List
from faker import Faker

faker = Faker()


@dataclass
class NameTestData:
    name: str
    test_type: str
    expected_result: str


class NameTestCases:
    # Валидные данные
    VALID = [
        NameTestData(faker.first_name()[:25], "valid_short", "success"),
        NameTestData(faker.first_name()[:49], "valid_long", "success"),
        NameTestData("John", "valid_typical", "success"),
    ]

    # Граничные значения
    BOUNDARY = [
        NameTestData("A", "boundary_min", "error"),
        NameTestData("A" * 50, "boundary_max", "success"),
        NameTestData("A" * 51, "boundary_overflow", "error"),
        NameTestData("", "boundary_empty", "error"),
    ]

    # Специальные случаи
    EDGE_CASES = [
        NameTestData("   ", "edge_whitespace", "success"),
        NameTestData("John123", "edge_alphanumeric", "success"),
    ]

    @classmethod
    def get_all_cases(cls) -> List[NameTestData]:
        return cls.VALID + cls.BOUNDARY + cls.EDGE_CASES