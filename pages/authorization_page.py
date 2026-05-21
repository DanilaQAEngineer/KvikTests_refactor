# Этот и аналогичные классы уже являются дочерними классами "base_page" ()

# Перед тем как из основного класса что-то наследовать в дочернем классе, нужно импортировать его в текущий файл
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AuthorizationPage(BasePage):    # Класс "Страница авторизации", наследуемый от родительского класса "BasePage"

    #    Локаторы, используемые внутри класса
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

    #    Основные методы, которые будут использоваться на странице с логинкой (и после неё)
    def __init__(self, browser, url=URL_AUTHORIZATION):    # инициализирую от основного/родительского класса
        super().__init__(browser, url)

    def open_authorization_page(self):    # Создаю метод "Открыть страницу авторизации"
        self.browser.get('https://www.kvik.ru/auth/')
        return self

    def enter_email(self, email):    # Создаю метод "Найти на странице поле 'Почта' + Ввести в него email"
        self.find_element(self.EMAIL_INPUT).send_keys(email)
        return self

    def enter_password(self, password):    # Создаю метод "Найти на странице поле 'Пароль' + Ввести в него пароль"
        self.find_element(self.PASSWORD_INPUT).send_keys(password)
        return self

    def click_login_button(self):    # Создаю метод "Найти на странице кнопку 'Войти' + Нажать на неё"
        self.find_clickable_element(self.LOGIN_BUTTON).click()
        return self

    def hleb_kroshki_1(self):    # Создаю метод "Найти на странице хлебные крошки, раздел "Персональные данные""
        return self.find_element(self.HLEB_KOSHKI_1).text

    def hleb_kroshki_2(self):    # Создаю метод "Найти на странице хлебные крошки, раздел "История заказов""
        return self.find_element(self.HLEB_KOSHKI_2).text

    def click_history_zakazov_tab(self):    # Создаю метод "Найти на странице ЛК таб "История заказов" + Кликни на него"
        self.find_clickable_element(self.TAB_HISTORY_ZAKAZOV).click()
        return self

    def search_catalog_button(self):    # Создаю метод "Найти на странице кнопку "Перейти в каталог""
        self.find_element(self.CATALOG_BUTTON).is_displayed()
        return self

    def zagolovok_in_lk(self):    # Создаю метод "Найти на странице заголовок "Личный кабинет""
        return self.find_element(self.ZAGOLOVOK_IN_LK).text    # Также обязательно использую метод "text", т.к. на тот же ".is_displayed" всегда будет ругаться из-за несовместимого типа данных

    def zagolovok_history_zakazov(self):    # Создаю метод "Найти на странице заголовок "История заказов""
        return self.find_element(self.ZAGOLOVOK_HISTORY_ZAKAZOV).text

    def search_tab_pers_date(self):    # Создаю метод "Найди на странице ЛК таб "Персональные данные""
        self.find_element(self.TAB_PERS_DATA).is_displayed()
        return self

    def forma_test_data(self):    # Создаю метод "Найди на странице ЛК (таб "Персональные данные") форму редактирования личных данных"
        self.find_element(self.FORMA_PERS_DATA).is_displayed()
        return self

    def search_tab_history_zakazov(self):    # Создаю метод "Найди на странице ЛК таб "История заказов""
        self.find_element(self.TAB_HISTORY_ZAKAZOV).is_displayed()
        return self

    def search_tab_smena_parol(self):    # Создаю метод "Найди на странице ЛК таб "Сменить пароль""
        self.find_element(self.TAB_SMENA_PAROL).is_displayed()
        return self

    def search_exit_button(self):    # Создаю метод "Найти кнопку «Выйти», когда она появится на экране"
        self.find_element(self.EXIT_BUTTON).is_displayed()
        return self
