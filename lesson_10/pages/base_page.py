from typing import Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def find(self, locator: Tuple[str, str]) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator: Tuple[str, str]) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator: Tuple[str, str], text: str) -> None:
        el = self.find(locator)
        el.clear()
        el.send_keys(text)

    def get_text(self, locator: Tuple[str, str]) -> str:
        return self.find(locator).text

    def is_visible(self, locator: Tuple[str, str]) -> bool:
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()