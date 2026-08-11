from selenium.webdriver.common.by import By

class IframeLocators:

    BASE_URL_1 = 'https://www.qa-practice.com/elements/iframe/iframe_page'
    IFRAME_PAGE = (By.CSS_SELECTOR, '.embed-responsive-item')
    IFRAME_ZAGOLOVOK = (By.CSS_SELECTOR, '.fw-light')
    IFRAME_DESCRIPTION = (By.CSS_SELECTOR, '.page-content [class="lead text-muted"]')
    ZAGOLOVOK_ON_MAIN_PAGE = (By.TAG_NAME, 'h1')

class NewTabPage:

    BASE_URL_2 = 'https://www.qa-practice.com/elements/new_tab/button'
    ZAGOLOVOK_ON_MAIN_PAGE_1 = (By.TAG_NAME, 'h1')
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, '.content #new-page-button')
    TEXT_IN_NEW_TAB_PAGE = (By.CSS_SELECTOR, '.result #result-text')
