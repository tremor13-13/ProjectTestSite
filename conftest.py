import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True)
def driver(request):
    print("🚀 STARTING CHROME WITH SELENIUM MANAGER...")

    chrome_options = Options()
    chrome_options.add_argument("--headless=new")

    # ДАЙ SELENIUM САМОМУ РАЗОБРАТЬСЯ С ДРАЙВЕРОМ
    driver = webdriver.Chrome(options=chrome_options)

    print("✅ CHROME STARTED!")
    request.cls.driver = driver
    yield driver
    driver.quit()



# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
#
# @pytest.fixture(autouse=True)
# def driver(request):
#
#     chrome_options = Options()
#     chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
#
#     # Отключаем сохранение паролей
#     chrome_options.add_experimental_option("prefs", {
#         "credentials_enable_service": False,
#         "profile.password_manager_enabled": False
#     })
#
#     driver = webdriver.Chrome(options=chrome_options)
#     request.cls.driver = driver
#     yield driver
#     driver.quit()
#

# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# # для ДОКЕРА - уникальная папка для каждого теста
# import tempfile
# # это тоже для докера что бы тесты запускались в отдельных папках
#
#
# @pytest.fixture(autouse=True) # для запуска на компе нужно с автоюзом
# # @pytest.fixture() # убераю автоюз для докера
# def driver(request):
#     chrome_options = webdriver.ChromeOptions()
#
#     # ВСЕ возможные настройки для блокировки
#     chrome_options.add_experimental_option("excludeSwitches",
#                                            ["enable-automation", "enable-logging", "ignore-certificate-errors"])
#
#     chrome_options.add_experimental_option("prefs", {
#         "profile.default_content_setting_values.notifications": 2,
#         "profile.password_manager_enabled": False,
#         "credentials_enable_service": False,
#         "autofill.profile_enabled": False,
#         "autofill.credit_card_enabled": False,
#         "password_manager_enabled": False,
#         "enable-autofill": False,
#         "signin": False,
#         "translate": False
#     })
#
#     chrome_options.add_argument("--incognito") # при сборке докера отключить!
#     chrome_options.add_argument("--disable-notifications")
#     chrome_options.add_argument("--disable-save-password-bubble")
#     chrome_options.add_argument("--disable-autofill-keyboard-accessory-view")
#     chrome_options.add_argument("--disable-features=PasswordSave,AutofillServerCommunication,TranslateUI")
#     chrome_options.add_argument("--disable-password-manager-reauthentication")
#     chrome_options.add_argument("--disable-password-manager")
#     chrome_options.add_argument("--disable-signin-promo")
#     temp_dir = tempfile.mkdtemp() # настройка для строчки ниже, запуска тестов в отдельных папках для докера
#     chrome_options.add_argument(f"--user-data-dir={temp_dir}") # для запуска тестов в отдельных папках для ДОККЕРА
#
#     #  для Docker:
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument("--headless=new")
#
#     driver = webdriver.Chrome(options=chrome_options)
#     request.cls.driver = driver
#     yield driver
#     driver.quit()