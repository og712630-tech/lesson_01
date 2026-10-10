import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):
    wait = WebDriverWait(driver, 15)

    # 1. Открываем сайт магазина
    driver.get("https://www.saucedemo.com/")

    # 2. Авторизация
    wait.until(
        EC.presence_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 3. Добавляем товары в корзину
    items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie",
    ]
    for item in items:
        button = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                f"//div[text()='{item}']"
                f"/ancestor::div[@class='inventory_item']"
                f"//button"
            ))
        )
        button.click()

    # 4. Переходим в корзину
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    # 5. Нажимаем Checkout
    wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()

    # 6. Заполняем форму своими данными
    wait.until(
        EC.presence_of_element_located((By.ID, "first-name"))
    ).send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    # 7. Continue
    driver.find_element(By.ID, "continue").click()

    # 8. Читаем итоговую стоимость
    total_element = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".summary_total_label")
        )
    )
    total_text = total_element.text  # например "Total: $58.29"

    # 9. Закрываем браузер (делает фикстура), проверяем сумму
    assert total_text == "Total: $58.29", (
        f"Ожидалось 'Total: $58.29', получено '{total_text}'"
    )
