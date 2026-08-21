from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    name_field = driver.find_element(By.NAME, "custname")
    
    name_field.send_keys("Иван Иванов")
    
    submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    submit_button.click()
    
    expected_url = "https://httpbin.qa-territory.online/post"
    assert driver.current_url == expected_url, f"Ожидался URL {expected_url}, получен {driver.current_url}"

    driver.quit()
