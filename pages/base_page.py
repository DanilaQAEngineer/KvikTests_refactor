from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Сюда выносим методы, которые будут актуальны для всех страниц

# Создаём и описываем основной/родительский класс:
class BasePage:

    """1. Конструктор класса (__init__):
    Этот метод запускается автоматически в момент создания объекта страницы. Он инициализирует (сохраняет) базовые настройки для всей страницы"""
    def __init__(self, browser, url, timeout=10):  # Создаём метод (получение браузера), который инициализирует наш класс
        self.browser = browser  # Сохраняю экземпляр браузера, чтобы все методы класса могли им управлять
        self.url = url    # Запоминаю адрес страницы, с которой мы работаем
        self.timeout = timeout    # Устанавливаю время ожидания (по умолчанию 10 секунд)
        self.wait = WebDriverWait(browser, timeout)    # Создаю объект явного ожидания: все последующие методы поиска будут использовать именно его, чтобы не падать с ошибкой, если элемент ещё не прогрузился

    def find(self, args):  # Метод мгновенного поиска: находит элемент на странице мгновенно (без ожиданий)
        return self.browser.find_element(*args)  # *args -- это оператор распаковки (если передадим кортеж (By.ID, "login"), он превратит его в два отдельных аргумента: find_element(By.ID, "login"))

    def open(self):  # Открыть страницу
        self.browser.get(self.url)

    def find_element(self, locator):  # Найти элемент с явным ожиданием
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visibility_element(self, locator):    # найти элемент, когда он отобразится на странице
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable_element(self, locator):  # Найти кликабельный элемент
        return self.wait.until(EC.element_to_be_clickable(locator))

    def go_to_site(self, url):  # Перейти по ссылке
        return self.browser.get(url)
