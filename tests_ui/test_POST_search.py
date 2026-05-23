import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://www.kvik.ru/'
SEARCH_INPUT = (By.XPATH, '//*[@id="title-search-input-2"]')
SEARCH_BUTTON = (By.CSS_SELECTOR, '.submit.hover')
H1 = (By.TAG_NAME, 'h1')
SCROLL_BUTTON = (By.CSS_SELECTOR, '.scrollup')
wait = WebDriverWait
FORM_AFTER_SEARCH = (By.CSS_SELECTOR, '.search-page [value="Искать"]')

@pytest.mark.func    # ←  добавил маркировку, чтоб при прогоне тестов из этого файла воспроизводились только помеченные: в терминале пишу команду == pytest -m func -v (название файла).py
def test_search(browser):
    browser.get(URL)

    search_input = wait(browser, 10).until(EC.element_to_be_clickable(SEARCH_INPUT)).send_keys('Клейкие закладки')

    search_button = wait(browser, 10).until(EC.element_to_be_clickable(SEARCH_BUTTON)).click()

    search_result = wait(browser, 10).until(EC.visibility_of_element_located(H1)).text

    form_after_search = wait(browser, 10).until(EC.visibility_of_element_located(FORM_AFTER_SEARCH)).text

    assert search_result == 'Поиск'    # Проверяю, что на странице с результатами есть заголовок "Поиск"
    print('\nЗаголовок "Поиск" есть.')
    assert browser.find_element(By.CSS_SELECTOR, '.search-page [value="Искать"]').is_displayed()    # Проверяю, что на странице с результатами есть форма поиска
    print('Форма поиск есть.')
    # assert browser.find_element(By.CSS_SELECTOR, '.scrollup').is_displayed()
    # print('Кнопка "Наверх" есть.')

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    wait(browser, 10).until(EC.element_to_be_clickable(SCROLL_BUTTON)).click()
