import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest_check import check
from pages.iframe_page import IframePage

def test_iframe_page(browser):

    iframe_page = IframePage(browser)

    (
        iframe_page.open_iframe_page()
    )

    try:
        assert iframe_page.check_name_button() == 'Инфрастурктура'
        print('Название кнопки корректное')
    except AssertionError:

