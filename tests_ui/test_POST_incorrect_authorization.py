import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.authorization_page import AuthorizationPage

URL = 'https://www.kvik.ru/'
L_KABINET_BUTTON = (By.XPATH, '//*[@class="avtorization-call enter reg"]')
EMAIL_INPUT = (By.XPATH, '//*[@name="USER_LOGIN"]')
PASSWORD_INPUT = (By.XPATH, '//*[@name="USER_PASSWORD"]')
LOGIN_BUTTON = (By.XPATH, '//*[@name="Login"]')
ERROR_TEXT = (By.CSS_SELECTOR, '.errortext')
wait = WebDriverWait
BUTTON_REGISTRATION = (By.CSS_SELECTOR, '.form_wrapp [class="button30 user-ic"]')

# Кейс: НЕ авторизация на сайте (перебираю разные недействительные тестовые данные с использованием параметризации)
@pytest.mark.parametrize(    # К функции/тесту создаю маркировку "parametrize"
    'test_data',    # Создаю что-то вроде переменной/объекта с тестовыми данными, которые буду использовать в тесте
    [    # Открываю массив, в котором будут храниться все тестовые данные: что-то вроде "ключ-значение"
    # для понятности и читаемости результатов можно использовать Пайтестовый метод "param": в скобках указываем тестовые данные, которые будем гонять, через запятую в переменной "id" создаём понятное имя этих данных
        pytest.param(('itsamono@gmai.com', 'Parol_808'), id='TC_1: email=False, password=True'),    # Указываю некорректные тестовые данные для первого кейса: email-, password+
        pytest.param(('itsamono@gmail.com', 'parol_808'), id='TC_2: email=True, password=False'),    # Указываю некорректные тестовые данные для второго кейса: email+, password-
        pytest.param(('', 'Parol_808'), id='TC_3: email=NULL, password=True'),    # Указываю некорректные тестовые данные для первого кейса: email-, password+
        pytest.param(('itsamono@gmail.com', ''), id='TC_4: email=True, password=NULL'),    # Указываю некорректные тестовые данные для второго кейса: email+, password-
        pytest.param(('', ''), id='TC_5: email=NULL, password=NULL')    # Указываю некорректные тестовые данные для второго кейса: email-, password-
    ]
)
def test_incorrect_auth(browser, test_data):    # В аргументах функции/теста после фикстуры через запятую указываю название этой переменной/объекта, из которой буду забирать тестовые данные
    email, password = test_data    # Создаю переменную + Через равно указываю имя переменной/объекта, из которой должны браться тестовые данные
    browser.get(URL)

    lk_button = wait(browser, 10).until(EC.element_to_be_clickable(L_KABINET_BUTTON)).click()

    email_input = wait(browser, 10).until(EC.element_to_be_clickable(EMAIL_INPUT)).send_keys(email)    # В аргументе команды "Ввести" указываю первую переменную, из которой нужно взять и ввести значение (почта)

    password_input = wait(browser, 10).until(EC.element_to_be_clickable(PASSWORD_INPUT)).send_keys(password)    # В аргументе команды "Ввести" указываю вторую переменную, из которой нужно взять и ввести значение (пароль)

    login_button = wait(browser, 10).until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()

    error_text = wait(browser, 10).until(EC.visibility_of_element_located(ERROR_TEXT)).text
    button_registr = wait(browser, 10).until(EC.element_to_be_clickable(BUTTON_REGISTRATION)).text

    assert error_text == 'Неверный логин или пароль.'    # Проверяю, что после некорректного логина на странице есть сообщение с ошибкой
    assert browser.find_element(By.CSS_SELECTOR, '.form_wrapp [class="button30 user-ic"]').is_displayed()    # Проверяю, что после некорректного логина на странице есть кнопка регистрации

# Кейс: Авторизация на сайте с некорректными данными (с использованием ООП)
@pytest.mark.parametrize(
    'test_data',
    [
        pytest.param(('itsamono@gmai.com', 'Parol_808'), id='TC_1: email=False, password=True'),
        pytest.param(('itsamono@gmail.com', 'parol_808'), id='TC_2: email=True, password=False'),
        pytest.param(('', 'Parol_808'), id='TC_3: email=NULL, password=True'),
        pytest.param(('itsamono@gmail.com', ''), id='TC_4: email=True, password=NULL'),
        pytest.param(('', ''), id='TC_5: email=NULL, password=NULL')
    ]
)
def test_incorrect_login(browser, test_data):
    authorization_page = AuthorizationPage(browser)
    email, password = test_data

    (
        authorization_page.open_authorization_page()
        .enter_email(email)
        .enter_password(password)
        .click_login_button()
    )
