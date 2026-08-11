import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest_check import check
from locators.iframe_locators import IframeLocators
from locators.iframe_locators import NewTabPage
from pages.iframe_page import IframePage

# Iframe -- это темка, когда у нас на основной странице есть какая-то встроенная html-страница (это браузер в браузере)
#           и если мы будем с ней по-обычному взаимодействовать, то тест будет падать в ошибку "InvalidSelectorException", т.к. это другая страница и для работы с ней, нам надо на неё переключиться
#           грубо говоря, сказать Селениуму: "на основной странице у нас есть встроенная страница и мы сейчас будем работать с ней"

#    Тест_1: Переключиться с основной страницы на iframe + Найти там какой-то элемент + Вернуться на основную страницу и работать с ней
def test_iframe_page(browser):

    # iframe_page = IframePage(browser)
    #
    # iframe_page.open_main_page_1()    # Шаг_1: Перехожу на страницу с iframe`ами
    # WebDriverWait(browser, 10).until(EC.frame_to_be_available_and_switch_to_it(IframeLocators.IFRAME_PAGE))    # Шаг_2: Переключаюсь на встроенную в основную страницу
    # (
    #     iframe_page.search_zagolovok_on_iframe_page()    # Шаг_3: Ищу заголовок на встроенной странице
    #     .search_description_on_iframe_page()    # Шаг_4: Ищу описание на встроенной странице
    # )
    #
    # assert iframe_page.search_zagolovok_on_iframe_page() == 'Album example'; print(f'\nНазвание заголовка в iframe`е корректное.')
    # assert iframe_page.search_description_on_iframe_page() == 'Something short and leading about the collection below—its contents, the creator, etc. Make it short and sweet, but not too short so folks don’t simply skip over it entirely.'; print('Описание в iframe`е корректное.')
    #
    # browser.switch_to.default_content()   # Шаг_5: Возвращаюсь на работу с основной страницей
    # iframe_page.search_zagolovok_on_main_page()    # Шаг_6: Ищу заголовок на основной странице
    #
    # assert iframe_page.search_zagolovok_on_main_page() == 'Iframes'; print('Название заголовка на основной странице корректное.')

    """Локаторы, которые используются в тесте"""
    BASE_URL_1 = 'https://www.qa-practice.com/elements/iframe/iframe_page'
    IFRAME_PAGE = (By.CSS_SELECTOR, '.embed-responsive-item')
    IFRAME_ZAGOLOVOK = (By.CSS_SELECTOR, '.fw-light')
    IFRAME_DESCRIPTION = (By.CSS_SELECTOR, '.page-content [class="lead text-muted"]')
    ZAGOLOVOK_ON_MAIN_PAGE = (By.TAG_NAME, 'h1')

    browser.get(BASE_URL_1)
    #   1) Методом "frame_to_be_available_and_switch_to_it" говорим нашему драйверу "найди на странице iframe и работай с ним дальше" (в последующих шагах)
    WebDriverWait(browser, 10).until(EC.frame_to_be_available_and_switch_to_it(IFRAME_PAGE))
    search_zagolovok_iframe = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(IFRAME_ZAGOLOVOK)).text
    search_description_iframe = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(IFRAME_DESCRIPTION)).text
    #    2) Методом "switch_to.default_content" говорим: "вернись на основную страницу и работай с ней"
    browser.switch_to.default_content()
    search_zagolovok_on_main_paige = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(ZAGOLOVOK_ON_MAIN_PAGE)).text

    assert search_zagolovok_iframe == 'Album example'; print(f'\nНазвание заголовка в iframe`е корректное.')
    assert search_description_iframe == 'Something short and leading about the collection below—its contents, the creator, etc. Make it short and sweet, but not too short so folks don’t simply skip over it entirely.'; print('Описание в iframe`е корректное.')
    assert search_zagolovok_on_main_paige == 'Iframes'; print('Название заголовка на основной странице корректное.')

#    Тест_2: Переключиться на таб другой страницы (новой вкладкой) с основной
def test_new_tab_page(browser):

    """Локаторы, которые используются в тесте"""
    BASE_URL_1 = 'https://www.qa-practice.com/elements/new_tab/button'
    ZAGOLOVOK_ON_MAIN_PAGE_1 = (By.TAG_NAME, 'h1')
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, '.content #new-page-button')
    TEXT_IN_NEW_TAB_PAGE = (By.CSS_SELECTOR, '.result #result-text')

    browser.get(BASE_URL_1)
    new_tab_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEW_TAB_BUTTON)).click()
    #    1) Создаём переменную, в которой буду храниться все айдишники табов/страниц, которые используем в тесте + Используем метод "switch_to.window", в аргументе которого будет индекс айдишника страницы, с которой работаем
    tab = browser.window_handles    # Метод "window_handles" хранит в себе ссылки на все табы, которые сейчас открыты
    browser.switch_to.window(tab[1])    # Метод "switch_to.window" говорит: "переключись на таб с индексом 1 и далее работай с этой страницей" (индексы, как мы помним, считаются - 0,1,2...)
    text_in_new_tab_page = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(TEXT_IN_NEW_TAB_PAGE)).text

    assert text_in_new_tab_page == 'I am a new page in a new tab'; print('\nТекст на новой вкладке корректный.')

    #    2) Закрываем новую вкладку, оставаясь/продолжая работать на основной
    browser.close()
    browser.switch_to.window(tab[0])

    zogolovok_on_main_page = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(ZAGOLOVOK_ON_MAIN_PAGE_1)).text

    assert zogolovok_on_main_page == 'Open link in a new tab'; print('Заголовок на основной странице корректный.')
