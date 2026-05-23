from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://www.kvik.ru/'
PAPER_PAGE = (By.XPATH, '//*[@id="li-a-2"]')
H1 = (By.TAG_NAME, 'h1')
H2 = (By.TAG_NAME, 'h2')
COVID_19_PAGE = (By.XPATH, '//*[@id="li-a-0"]')
CONTACTS_PAGE = (By.XPATH, '//*[@id="itemtop4"]')
wait = WebDriverWait
KANC_TOV = (By.CSS_SELECTOR, '.catalog_menu [id="a-1"]')
BUTTON_REGISTRATION = (By.CSS_SELECTOR, '.form_wrapp [class="button30 user-ic"]')

# Кейс: Проверка всех вкладок хедера
def test_all_pages(browser):
    browser.get(URL)

    covid_19 = wait(browser, 10).until(EC.element_to_be_clickable(COVID_19_PAGE)).click()
    title_covid_19 = wait(browser, 10).until(EC.visibility_of_element_located(H1)).text

    assert title_covid_19 == 'COVID-19'
    print('Заголовок "COVID-19" есть')

    kanc_tovary = wait(browser, 10).until(EC.element_to_be_clickable(KANC_TOV)).click()
    title_kanc_tovary = wait(browser, 10).until(EC.visibility_of_element_located(H1)).text

    assert title_kanc_tovary == 'Канцтовары'
    print('Заголовок "Канцтовары" есть')

    contacts = wait(browser, 10).until(EC.element_to_be_clickable(CONTACTS_PAGE)).click()
    title_contacts = wait(browser, 10).until(EC.visibility_of_element_located(H1)).text

    assert title_contacts == 'Контакты'
    print('Заголовок "Контакты" есть')
