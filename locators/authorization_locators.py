# ( это класс с локаторами для какой-то одной страницы: описываем его как обычный класс, указывая в переменных ссылки на элементы страницы )

from selenium.webdriver.common.by import By


class AuthorizationLocators:
    """Локаторы страницы авторизации"""

    URL_AUTHORIZATION = 'https://www.kvik.ru/auth/'
    EMAIL_INPUT = (By.CSS_SELECTOR, '.form-block [name="USER_LOGIN"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '.form-block [name="USER_PASSWORD"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.form-block [name="Login"]')

    HLEB_KOSHKI_1 = (By.XPATH, '//div[@class="breadcrumbs"]/span[text()="Персональные данные"]')
    ZAGOLOVOK_IN_LK = (By.TAG_NAME, 'h1')
    TAB_PERS_DATA = (By.CSS_SELECTOR, '.wrapper_inner [href="/personal/personal-data/"]')
    FORMA_PERS_DATA = (By.CSS_SELECTOR, '.form-block [class="main"]')

    TAB_HISTORY_ZAKAZOV = (By.CSS_SELECTOR, '.wrapper_inner [href="/personal/history-of-orders/"]')
    HLEB_KOSHKI_2 = (By.XPATH, '//div[@class="breadcrumbs"]/span[text()="История заказов"]')
    ZAGOLOVOK_HISTORY_ZAKAZOV = (By.CSS_SELECTOR, '.form-block-title')
    CATALOG_BUTTON = (By.CSS_SELECTOR, '.empty_history [class="button30"]')

    TAB_SMENA_PAROL = (By.CSS_SELECTOR, '.wrapper_inner [href = "/personal/change-password/"]')

    EXIT_BUTTON = (By.CSS_SELECTOR, '.wrapper_inner [class="exit"]')
