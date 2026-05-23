from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchPage(BasePage):


    URL_SEARCH = 'https://www.kvik.ru/catalog/?q='
    SEARCH_INPUT = (By.CSS_SELECTOR, '.search-page [type="text"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.search-page .button30')
    CHECK_PRICE = (By.CSS_SELECTOR, '.catalog_item_wrapp .price')
    BUTTON_PLUS = (By.CSS_SELECTOR, '.catalog_item_wrapp .plus')
    BUTTON_IN_BASKET = (By.CSS_SELECTOR, '.counter_wrapp [class="buttons_block clearfix"]')
    ZAGOLOVOK = (By.ID, 'h1')


    def __init__(self, browser, url=URL_SEARCH):
        super().__init__(browser, url)

    def open_search_page(self):
        self.browser.get('https://www.kvik.ru/catalog/?q=')
        return self

    def search_input(self, value):
        self.find_element(self.SEARCH_INPUT).send_keys(value)
        return self

    def click_button_search(self):
        self.find_element(self.SEARCH_BUTTON).click()
        return self

    def check_card_name(self):
        return self.find_element(self.CHECK_PRICE).text

    def click_button_plus(self):
        self.find_element(self.BUTTON_PLUS).click()
        return self

    def click_button_in_basket(self):
        self.find_element(self.BUTTON_IN_BASKET).click()
        return self

    def check_zagolovok(self):
        return self.find_element(self.ZAGOLOVOK).text
