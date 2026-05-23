from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Covid19Page(BasePage):


    URL_MAIN_PAGE = 'https://www.kvik.ru/'
    TAB_COVID_19 = (By.CSS_SELECTOR, '.catalog_menu #li-a-0')
    H1 = (By.TAG_NAME, 'h1')
    COVID_19_PAGE = (By.XPATH, '//*[@id="li-a-0"]')
    HLEB_KROSH = (By.CSS_SELECTOR, '.wrapper_inner #bx_breadcrumb_3')


    def __init__(self, browser, url=URL_MAIN_PAGE):
        super().__init__(browser, url)

    def open_main_page(self):
        self.browser.get('https://www.kvik.ru/')
        return self

    def click_tab_covid_19(self):
        self.find_clickable_element(self.TAB_COVID_19).click()
        return self

    def check_h_1(self):
        return self.find_element(self.H1).text
