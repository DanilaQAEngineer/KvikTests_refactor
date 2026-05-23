from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.contact_page import ContactPage


# Кейс: Переход на вкладку "Контакты" и проверка, корректный ли заголовок внутри
def test_get_contacts_page(browser):
    contacts_page = ContactPage(browser)
    (
        contacts_page.open_main_page()
        .click_tab_contact_page()
    )

    assert contacts_page.check_header() == 'Контакты'; print('\nЗаголовок в разделе корректный | +')
