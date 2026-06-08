# Этот и аналогичные классы уже являются дочерними классами "base_page" ()

# Перед тем как из основного класса что-то наследовать в дочернем классе, нужно импортировать его в текущий файл
from pages.base_page import BasePage
from locators.contact_page_locators import ContactPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class ContactPage(BasePage):    # Создаю класс тестируемой страницы + В аргументах указываю родительский класс, из которого что-то буду наследовать сюда

    def __init__(self, browser, url=ContactPageLocators.MAIN_URL):  # инициализирую от основного/родительского класса
        super().__init__(browser, url)

    def open_main_page(self):    # Создаю метод "Открыть страницу авторизации"
        self.browser.get('https://www.kvik.ru/')
        return self

    def click_tab_contact_page(self):
        self.find_clickable_element(ContactPageLocators.CONTACTS_PAGE).click()
        return self

    def check_header(self):
        return self.find_element(ContactPageLocators.H1).text
