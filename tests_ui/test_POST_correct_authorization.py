import pytest
from pytest_check import check
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.authorization_page import AuthorizationPage    # Импортирую класс со страницей логинки


# URL = 'https://www.kvik.ru/'
# LK_BUTTON = (By.CSS_SELECTOR, '.top-h-row [class="avtorization-call enter reg"]')
# LK_BUTTON_AFTER_AUTHORISATION = (By.CSS_SELECTOR, '.top-h-row [class="reg "]')
# EMAIL_INPUT = (By.CSS_SELECTOR, '.form-wr [name="USER_LOGIN"]')
# PASSWORD_INPUT = (By.CSS_SELECTOR, '.form-wr [name="USER_PASSWORD"]')
# LOGIN_BUTTON = (By.CSS_SELECTOR, '.form-wr .button30')
# H1 = (By.TAG_NAME, 'h1')
# PERSONAL_DATA_BUTTON = (By.CSS_SELECTOR, '.wrapper_inner [class="current"]')
# wait = WebDriverWait


# Кейс: Авторизация на сайте (тест без ООП)
# @pytest.mark.func    # ← добавил маркировку, чтоб при прогоне тестов из этого файла воспроизводились только помеченные: в терминале пишу команду == pytest -m func -v (название файла).py
# def test_correct_login(browser):
#     browser.get(URL)
#
#     lk_button = wait(browser, 10).until(EC.element_to_be_clickable(LK_BUTTON)).click()
#     email_input = wait(browser, 10).until(EC.element_to_be_clickable(EMAIL_INPUT)).send_keys('itsamono@gmail.com')
#     password_input = wait(browser, 10).until(EC.element_to_be_clickable(PASSWORD_INPUT)).send_keys('Parol_808')
#     login_button = wait(browser, 10).until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()
#     lk_button_after_authorization = wait(browser, 10).until(EC.element_to_be_clickable(LK_BUTTON_AFTER_AUTHORISATION)).click()
#
#     title1 = wait(browser, 10).until(EC.visibility_of_element_located(H1)).text
#     personal_data_button = wait(browser, 10).until(EC.visibility_of_element_located(PERSONAL_DATA_BUTTON))
#
#     assert title1 == '(некорректный заголовок)'    # это некорректный ожидаемый результат
#     assert browser.find_element(PERSONAL_DATA_BUTTON).is_displayed()    # это некорректный ожидаемый результат

# Кейс: Авторизация на сайте (тест с использованием ООП)
# @pytest.mark.func
def test_correct_login(browser):
    authorization_page = AuthorizationPage(browser)    # Обращаюсь к дочернему классу "AuthorizationPage" (в котором описаны все сущности и методы, используемые на странице): говорю "Работаем с такой-то страницей" (создаю сессию для работы со страницой)

    (
        authorization_page.open_authorization_page()    # Перехожу на страницу авторизации
        .enter_email('itsamono@gmail.com')    # Ввожу почту в поле "email"
        .enter_password('Parol_808')    # Ввожу пароль в поле "Пароль"
        .click_login_button()    # Нажимаю кнопку "Войти"
    )

    print('\nПроверки таба "Персональные данные":')
    assert authorization_page.hleb_kroshki_1() == 'Персональные данные'; print('✅ В хлебных крошках есть раздел "Персональные данные"')
    assert authorization_page.zagolovok_in_lk() == 'Личный кабинет'; print('✅ Заголовок "Личный кабинет" есть')    # Добавляю проверку "Правда ли главный заголовок в ЛК = 'Личный кабинет'?"
    #check.equal(authorization_page.zagolovok_in_lk(), 'Личный кабинет'
    assert authorization_page.search_tab_pers_date(); print('✅ Таб "Персональные данные" есть')    # Добавляю проверку "Есть ли на странице ЛК таб 'Персональные данные'?"
    assert authorization_page.forma_test_data(); print('✅ Форма редактирования личных данных есть')    # Добавляю проверку "Есть ли на странице ЛК (таб 'Персональные данные') форма редактирования личных данных?"
    assert authorization_page.search_tab_history_zakazov(); print('✅ Таб "История заказов" есть')    # Добавляю проверку "Есть ли на странице ЛК таб 'История заказов'?"
    assert authorization_page.search_tab_smena_parol(); print('✅ Таб "Сменить пароль" есть')    # Добавляю проверку "Есть ли на странице ЛК таб 'Сменить пароль'?"
    assert authorization_page.search_exit_button(); print('✅ Кнопка "Выйти" есть')    # Добавляю проверку "Есть ли на странице кнопка 'Выйти' после авторизации на сайте?"
    # check.equal(authorization_page.hleb_kroshki_1(), 'Персональные данные', '❌ Хлебные крошки 1'); print('✅ В хлебных крошках есть раздел "Персональные данные"')
    # check.equal(authorization_page.zagolovok_in_lk(), 'Личный кабинет', '❌ Заголовок в ЛК'); print('✅ Заголовок "Личный кабинет" есть')
    # check.is_true(authorization_page.search_tab_pers_date(), '❌ Таб "Персональные данные"'); print('✅ Таб "Персональные данные" есть')
    # check.is_true(authorization_page.forma_test_data(), '❌ Форма редактирования'); print('✅ Форма редактирования личных данных есть')
    # check.is_true(authorization_page.search_tab_history_zakazov(), '❌ Таб "История заказов"'); print('✅ Таб "История заказов" есть')
    # check.is_true(authorization_page.search_tab_smena_parol(), '❌ Таб "Сменить пароль"'); print('✅ Таб "Сменить пароль" есть')
    # check.is_true(authorization_page.search_exit_button(), '❌ Кнопка "Выйти"'); print('✅ Кнопка "Выйти" есть')

    (
        authorization_page.click_history_zakazov_tab()
    )

    print('\nПроверки таба "История заказов":')
    assert authorization_page.hleb_kroshki_2() == 'История заказов'; print('✅ В хлебных крошках есть раздел "История заказов"')
    assert authorization_page.zagolovok_history_zakazov() == 'История заказов'; print('✅ Заголовок "История заказов" есть')
    assert authorization_page.search_catalog_button(); print('✅ Кнопка "Перейти в каталог" есть')    #
    # check.equal(authorization_page.hleb_kroshki_2(), 'История заказов', '❌ Хлебные крошки 2'); print('✅ В хлебных крошках есть раздел "История заказов"')
    # check.equal(authorization_page.zagolovok_history_zakazov(), 'История заказа', '❌ Заголовок "История заказов"'); print('✅ Заголовок "История заказов" есть')
    # check.is_true(authorization_page.search_catalog_button(), '❌ Кнопка "Перейти в каталог"'); print('✅ Кнопка "Перейти в каталог" есть')
