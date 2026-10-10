import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from lesson_10.pages.login_page import LoginPage
from lesson_10.pages.inventory_page import InventoryPage


@allure.feature("Login")
class TestLogin:

    @allure.title("Успешный вход")
    @allure.description("Проверка входа с валидными кредами")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_success_login(self, driver: WebDriver) -> None:
        page = LoginPage(driver)
        with allure.step("Открыть страницу логина"):
            page.open_page()
        with allure.step("Ввести креды и войти"):
            page.login("standard_user", "secret_sauce")
        with allure.step("Проверить переход на inventory"):
            assert InventoryPage(driver).get_title() == "Products"

    @allure.title("Вход с неверным паролем")
    @allure.description("Проверка сообщения об ошибке")
    @allure.severity(allure.severity_level.NORMAL)
    def test_wrong_password(self, driver: WebDriver) -> None:
        page = LoginPage(driver)
        with allure.step("Открыть страницу логина"):
            page.open_page()
        with allure.step("Ввести неверные креды"):
            page.login("standard_user", "wrong")
        with allure.step("Проверить текст ошибки"):
            assert "Username and password do not match" in page.get_error()
