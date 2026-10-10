import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    # Windows -> Edge. Для macOS замените на webdriver.Safari()
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form(driver):
    wait = WebDriverWait(driver, 10)

    # 1. Открываем страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # 2. Заполняем форму
    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        # zip-code оставляем пустым
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro",
    }

    for name, value in fields.items():
        element = wait.until(
            EC.presence_of_element_located((By.NAME, name))
        )
        element.clear()
        element.send_keys(value)

    # 3. Нажимаем Submit
    submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

    # 4. Проверяем, что Zip code подсвечен красным (danger)
    zip_field = wait.until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )
    zip_class = zip_field.get_attribute("class")
    assert "alert-danger" in zip_class, (
        f"Поле Zip code не подсвечено красным: {zip_class}"
    )

    # 5. Проверяем, что остальные поля подсвечены зелёным (success)
    green_fields = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company",
    ]

    for field_id in green_fields:
        field = driver.find_element(By.ID, field_id)
        field_class = field.get_attribute("class")
        assert "alert-success" in field_class, (
            f"Поле {field_id} не подсвечено зелёным: {field_class}"
        )
