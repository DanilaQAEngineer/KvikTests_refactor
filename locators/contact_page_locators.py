from selenium.webdriver.common.by import By


class ContactPageLocators():

    MAIN_URL = 'https://www.kvik.ru/'
    H1 = (By.TAG_NAME, 'h1')
    CONTACTS_PAGE = (By.XPATH, '//*[@id="itemtop4"]')
