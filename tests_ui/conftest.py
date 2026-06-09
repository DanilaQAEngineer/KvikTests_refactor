# ______________________________________________________________________________________________________________________
#                                     -- БИБЛИОТЕКИ, КОТОРЫЕ ИСПОЛЬЗУЮ В ТЕСТИРОВАНИИ --
# ______________________________________________________________________________________________________________________
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# #    ↓ Импортирую PYTEST, чтобы запускать тесты
import pytest
# #    ↓ Импортирую из Selenium`а "WEBDRIVER", чтобы взаимодействовать с Хромом
from selenium import webdriver
# #    ↓ Импортирую из WEBDRIVER`а метод "BY", чтобы обращаться к элементам страницы
from selenium.webdriver.common.by import By
# #    ↓ Импортирую из WEBDRIVER`а "WEBDRIVERWAIT", чтобы выставлять ожидаемое время отклика/получения страницы
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# ______________________________________________________________________________________________________________________
#                                                   -- ФИКСТУРЫ --
# ______________________________________________________________________________________________________________________
# Фикстура для UI-тестов
# @pytest.fixture
# def browser():    # Создаю функцию/фикстуру, которая будет использоваться во всех UI-тестах (чтоб она применялась к тесту, её нужно будет в скобках после названия функции/теста указать)
#     driver = webdriver.Chrome()    # Указываю браузер, который будет использоваться в моих тестах
#     driver.maximize_window()    # Обращаюсь к методу, который по открытии браузера будет раскрывать его в полный размер экрана
#     #driver.implicity_wait(5)    # По умолчанию добавил неявное ожидание: если Selenium не находит нужный элемент, он ждёт/ищет ещё 5 секунд и только потом упадёт
#     yield driver  # Добавляю условие: что нужно будет сделать с браузером ПОСЛЕ прогона тестов
#     driver.quit()  # Указываю метод, который закроет браузер, несмотря на результат (успешно/нет)
# ______________________________________________________________________________________________________________________
@pytest.fixture
def browser():
    options = Options()

    #options.add_argument("--disable-save-password-bubble")    # (чтобы уведомлялки/модалки о сохранении пароля на странице скрывались?)
    #options.add_argument("--disable-notifications")    # (чтобы любые уведомлялки/модалки на странице скрывались?)
    options.add_argument("--window-size=1920,1080")    # Добавил, чтоб браузер открывался полность при запуске теста
    options.add_argument("--headless")    # Добавил "безголовый режим", чтоб при запуске тестов не открывался браузер

    driver = webdriver.Chrome(options=options)

    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver
    driver.quit()
