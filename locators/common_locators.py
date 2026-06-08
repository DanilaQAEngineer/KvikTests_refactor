# ОПЦИОНАЛЬНЫЙ ФАЙЛ/КЛАСС С ОБЩИМИ ЛОКАТОРАМИ ВСЕГО СЕРВИСА


from pages.base_page import BasePage
# 👇 Импортируем класс с локаторами
from locators.authorization_locators import AuthorizationLocators


class AuthorizationPage(BasePage):

    def __init__(self, browser, url='https://www.kvik.ru/'):
        super().__init__(browser, url)

    # def click_lk_button(self):
    #     # 👇 Используем локатор из импортированного класса
    #     self.find_clickable_element(AuthorizationLocators.LK_BUTTON).click()
    #     return self

    def enter_email(self, email: str):
        self.find_element(AuthorizationLocators.EMAIL_INPUT).send_keys(email)
        return self

    def enter_password(self, password: str):
        self.find_element(AuthorizationLocators.PASSWORD_INPUT).send_keys(password)
        return self

    def click_login_button(self):
        self.find_clickable_element(AuthorizationLocators.LOGIN_BUTTON).click()
        return self

    # @property
    # def zagolovok_in_lk(self):
    #     # 👇 Возвращаем текст элемента, найденного по локатору
    #     return self.find_element(AuthorizationLocators.ZAGOLOVOK_LK).text.strip()
