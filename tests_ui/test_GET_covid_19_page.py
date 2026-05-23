from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.covid_19_page import Covid19Page


# Кейс: Переход на вкладку "COVID-19" и проверка, корректный ли заголовок внутри
def test_get_covid_19_page(browser):
    covid_19_page = Covid19Page(browser)
    (
        covid_19_page.open_main_page()
        .click_tab_covid_19()
    )

    assert covid_19_page.check_h_1() == 'COVID-19'; print('\nЗаголовок в разделе корректный | +')
