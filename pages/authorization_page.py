# Этот и аналогичные классы уже являются дочерними классами "base_page" ()

# Перед тем как из основного класса что-то наследовать в дочернем классе, нужно импортировать его в текущий файл
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.authorization_locators import AuthorizationLocators    # подтягиваю в класс с методами авторизации класс с локаторами элементов страницы, к которым я буду обращаться


class AuthorizationPage(BasePage):    # Класс "Страница авторизации", наследуемый от родительского класса "BasePage"

    #    Основные методы, которые будут использоваться на странице с логинкой (и после неё)
    def __init__(self, browser, url=AuthorizationLocators.URL_AUTHORIZATION):    # инициализирую от основного/родительского класса
        super().__init__(browser, url)

    def open_authorization_page(self):    # Создаю метод "Открыть страницу авторизации"
        self.browser.get('https://www.kvik.ru/auth/')
        return self

    def enter_email(self, email):    # Создаю метод "Найти на странице поле 'Почта' + Ввести в него email"
        self.find_element(AuthorizationLocators.EMAIL_INPUT).send_keys(email)
        return self

    def enter_password(self, password):    # Создаю метод "Найти на странице поле 'Пароль' + Ввести в него пароль"
        self.find_element(AuthorizationLocators.PASSWORD_INPUT).send_keys(password)
        return self

    def click_login_button(self):    # Создаю метод "Найти на странице кнопку 'Войти' + Нажать на неё"
        self.find_clickable_element(AuthorizationLocators.LOGIN_BUTTON).click()
        return self

    def hleb_kroshki_1(self):    # Создаю метод "Найти на странице хлебные крошки, раздел "Персональные данные""
        return self.find_element(AuthorizationLocators.HLEB_KOSHKI_1).text

    def hleb_kroshki_2(self):    # Создаю метод "Найти на странице хлебные крошки, раздел "История заказов""
        return self.find_element(AuthorizationLocators.HLEB_KOSHKI_2).text

    def click_history_zakazov_tab(self):    # Создаю метод "Найти на странице ЛК таб "История заказов" + Кликни на него"
        self.find_clickable_element(AuthorizationLocators.TAB_HISTORY_ZAKAZOV).click()
        return self

    def search_catalog_button(self):    # Создаю метод "Найти на странице кнопку "Перейти в каталог""
        self.find_element(AuthorizationLocators.CATALOG_BUTTON).is_displayed()
        return self

    def zagolovok_in_lk(self):    # Создаю метод "Найти на странице заголовок "Личный кабинет""
        return self.find_element(AuthorizationLocators.ZAGOLOVOK_IN_LK).text    # Также обязательно использую метод "text", т.к. на тот же ".is_displayed" всегда будет ругаться из-за несовместимого типа данных

    def zagolovok_history_zakazov(self):    # Создаю метод "Найти на странице заголовок "История заказов""
        return self.find_element(AuthorizationLocators.ZAGOLOVOK_HISTORY_ZAKAZOV).text

    def search_tab_pers_date(self):    # Создаю метод "Найди на странице ЛК таб "Персональные данные""
        self.find_element(AuthorizationLocators.TAB_PERS_DATA).is_displayed()
        return self

    def forma_test_data(self):    # Создаю метод "Найди на странице ЛК (таб "Персональные данные") форму редактирования личных данных"
        self.find_element(AuthorizationLocators.FORMA_PERS_DATA).is_displayed()
        return self

    def search_tab_history_zakazov(self):    # Создаю метод "Найди на странице ЛК таб "История заказов""
        self.find_element(AuthorizationLocators.TAB_HISTORY_ZAKAZOV).is_displayed()
        return self

    def search_tab_smena_parol(self):    # Создаю метод "Найди на странице ЛК таб "Сменить пароль""
        self.find_element(AuthorizationLocators.TAB_SMENA_PAROL).is_displayed()
        return self

    def search_exit_button(self):    # Создаю метод "Найти кнопку «Выйти», когда она появится на экране"
        self.find_element(AuthorizationLocators.EXIT_BUTTON).is_displayed()
        return self
