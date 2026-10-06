from selenium.webdriver.common.by import By


class InventoryPage:
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_name):
        locator = (
            By.XPATH,
            f"//div[text()='{product_name}']"
            f"/ancestor::div[@class='inventory_item']"
            f"//button"
        )
        self.driver.find_element(*locator).click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
