from typing import Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from lesson_10.pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    USERNAME: Tuple[str, str] = ("id", "user-name")
    PASSWORD: Tuple[str, str] = ("id", "password")
    LOGIN_BTN: Tuple[str, str] = ("id", "login-button")
    ERROR: Tuple[str, str] = ("css selector", "h3[data-test='error']")

    def __init__(self, driver: WebDriver) -> None:
        """Страница авторизации.

        :param driver: Экземпляр WebDriver.
        :return: None
        """
        super().__init__(driver)

    def open_page(self) -> "LoginPage":
        """Открыть страницу логина.

        :return: Экземпляр LoginPage.
        """
        self.open(self.URL)
        return self

    def login(self, username: str, password: str) -> None:
        """Заполнить форму и нажать кнопку входа.

        :param username: Логин.
        :param password: Пароль.
        :return: None
        """
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def get_error(self) -> str:
        """Получить текст ошибки авторизации.

        :return: Текст ошибки.
        """
        return self.get_text(self.ERROR)
