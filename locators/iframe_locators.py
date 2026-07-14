from selenium.webdriver.common.by import By
#class="xaf9ae18d--_57ad8--iframe" -- клас с айфреймом

class IframeLocators:

    BASE_URL = 'https://irkutsk.cian.ru/'
    URL_WITH_IFRAME = 'https://irkutsk.cian.ru/map/?center=55.01423033025555%2C82.95009544584886&currency=2&deal_type=sale&engine_version=2&floornl=1&is_first_floor=0&maxprice=3500000&offer_type=flat&region=4897&zoom=11'
    INFRA_BUTTON = (By.CSS_SELECTOR, '#map-search-frontend .xaf9ae18d--_69416--large-navigation-btn [data-name="InfrastructureButton"]')