from pages.search_page import SearchPage
from time import sleep


def test_search(browser):
    search = SearchPage(browser)

    (
        search.open_search_page()
        .search_input('Кресло UP_Prestige жест.подл.Самба ткань серая C02/ТК3')
        .click_button_search()
    )

    assert search.check_card_name() == '2 693 руб.'

    (
        search.click_button_plus()
        .click_button_in_basket()    # нужно дописать метод, чтобы провалиться в корзину
    )

    #assert search.check_zagolovok() == 'Корзина'
