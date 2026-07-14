from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.iframe_locators import IframeLocators
import allure

class IframePage(BasePage):

    def __init__(self, browser, url=IframeLocators.BASE_URL):
        super().__init__(browser, url)

    def open_iframe_page(self):
        self.browser.get(IframeLocators.URL_WITH_IFRAME)
        return self

    def click_tab_paper(self):    # Метод клика по кнопке "Инфраструктура"
        self.find_clickable_element(IframeLocators.INFRA_BUTTON).click()
        return self

    def check_name_button(self):
        return self.find_element(IframeLocators.INFRA_BUTTON).text
