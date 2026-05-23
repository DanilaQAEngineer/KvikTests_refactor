from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PaperPage(BasePage):


    MAIN_URL_PAGE = 'https://www.kvik.ru/'
    PAPER_PAGE = (By.CSS_SELECTOR, '.wrapper_inner #li-a-2')
    H1 = (By.TAG_NAME, 'h1')
    H2 = (By.TAG_NAME, 'h2')


    def __init__(self, browser, url=MAIN_URL_PAGE):  # инициализирую от основного/родительского класса
        super().__init__(browser, url)

    def open_main_page(self):
        self.browser.get('https://www.kvik.ru/')
        return self

    def click_tab_paper(self):
        self.find_clickable_element(self.PAPER_PAGE).click()
        return self

    def check_h_1(self):
        return self.find_element(self.H1).text
