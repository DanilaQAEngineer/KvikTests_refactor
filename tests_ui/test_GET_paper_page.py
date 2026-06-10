import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.paper_page import PaperPageClass


# Кейс: Переход на вкладку "Бумага" и проверка, корректный ли заголовок внутри
# @pytest.mark.smoke
def test_get_paper_page(browser):

    paper_page = PaperPageClass(browser)

    (
        paper_page.open_main_page()
        .click_tab_paper()
    )

    assert paper_page.check_h_1() == 'Бумага'; print('\nЗаголовок в разделе корректный | +')
