from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.iframe_locators import IframeLocators
import allure

class IframePage(BasePage):

    def __init__(self, browser, url=IframeLocators.BASE_URL_1):
        super().__init__(browser, url)

    def open_main_page_1(self):
        self.browser.get(IframeLocators.BASE_URL_1)
        return self

    def search_zagolovok_on_iframe_page(self):
        return self.find_visibility_element(IframeLocators.IFRAME_ZAGOLOVOK).text

    def search_description_on_iframe_page(self):
        return self.find_visibility_element(IframeLocators.IFRAME_DESCRIPTION).text

    def search_zagolovok_on_main_page(self):
        return self.find_visibility_element(IframeLocators.ZAGOLOVOK_ON_MAIN_PAGE).text

    def switch_in_iframe(self):    # метод переключения на iframe
        WebDriverWait(self.browser, 10).until(EC.frame_to_be_available_and_switch_to_it(IframeLocators.IFRAME_PAGE))
        return self

    def switch_to_default_content(self):    # метод переключения/возврата на основную страницу
        self.browser.switch_to.default_content()
        return self

class NewTabPage(BasePage):

    def __init__(self, browser, url=IframeLocators.BASE_URL_1):
        super().__init__(browser, url)

