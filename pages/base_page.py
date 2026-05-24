from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Сюда выносим методы, которые будут актуальны для всех страниц

# Создаём и описываем основной/родительский класс:
class BasePage:
    def __init__(self, browser, url, timeout=10):  # Создаём метод (получение браузера), который инициализирует наш класс
        self.browser = browser  # Говорим "Браузер, который принадлежит классу = браузеру, который нам передали"
        self.url = url
        self.timeout = timeout
        self.wait = WebDriverWait(browser, timeout)

    def find(self, args):  # Создаю метод, который упрощает синтаксис функции "Найти элемент на странице": Давай мне любые аргументы,
        return self.browser.find_element(*args)  # а я тебе найду элемент

    def open(self):  # Открыть страницу
        self.browser.get(self.url)

    def find_element(self, locator):  # Найти элемент с явным ожиданием
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable_element(self, locator):  # Найти кликабельный элемент
        return self.wait.until(EC.element_to_be_clickable(locator))

    def go_to_site(self, url):  # Перейти по ссылке
        return self.browser.get(url)

