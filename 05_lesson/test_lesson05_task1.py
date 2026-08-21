from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    driver.get("https://httpbin.qa-territory.online")
    
    link = driver.find_element(By.LINK_TEXT, "HTML Form")
    link.click()
    
    expected_url = "https://httpbin.qa-territory.online/forms/post"
    assert driver.current_url == expected_url, f"Ожидался URL {expected_url}, получен {driver.current_url}"
    
    driver.back()
    
    home_url = "https://httpbin.qa-territory.online"
    assert driver.current_url == home_url, f"Ожидался URL {home_url}, получен {driver.current_url}"

    driver.quit()
