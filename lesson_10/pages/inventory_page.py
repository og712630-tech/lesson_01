from typing import List, Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from lesson_10.pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE: Tuple[str, str] = ("css selector", "span.title")
    ITEMS: Tuple[str, str] = ("css selector", ".inventory_item_name")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def get_title(self) -> str:
        return self.get_text(self.TITLE)

    def get_items(self) -> List[str]:
        return [el.text for el in self.driver.find_elements(*self.ITEMS)]
