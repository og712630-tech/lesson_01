import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calc(driver):
    wait = WebDriverWait(driver, 60)  # запас времени с учётом задержки 45 сек

    # 1. Открываем страницу
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    # 2. Устанавливаем задержку = 45
    delay_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
    )
    delay_input.clear()
    delay_input.send_keys("45")

    # 3. Нажимаем 7 + 8 =
    for text in ["7", "+", "8", "="]:
        button = driver.find_element(
            By.XPATH, f"//span[text()='{text}']"
        )
        button.click()

    # 4. Ждём, пока в окне появится результат 15
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), "15"
        )
    )

    result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert result == "15", f"Ожидался результат 15, получен {result}"
