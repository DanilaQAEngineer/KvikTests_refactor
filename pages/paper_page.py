from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.paper_page_locators import PaperPageLocators


class PaperPageClass(BasePage):

    def __init__(self, browser, url=PaperPageLocators.MAIN_URL_PAGE):  # инициализирую от основного/родительского класса
        super().__init__(browser, url)

    def open_main_page(self):
        self.browser.get('https://www.kvik.ru/')
        return self

    def click_tab_paper(self):
        self.find_clickable_element(PaperPageLocators.PAPER_PAGE).click()
        return self

    def check_h_1(self):
        return self.find_element(PaperPageLocators.H1).text
