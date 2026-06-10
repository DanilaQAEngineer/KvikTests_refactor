from selenium.webdriver.common.by import By


class PaperPageLocators():

    MAIN_URL_PAGE = 'https://www.kvik.ru/'
    PAPER_PAGE = (By.CSS_SELECTOR, '.wrapper_inner #li-a-2')
    H1 = (By.TAG_NAME, 'h1')
    H2 = (By.TAG_NAME, 'h2')
