from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

    links = driver.find_elements(By.TAG_NAME, "a")
    
    expected_count = 9
    actual_count = len(links)
    assert actual_count == expected_count, f"Ожидалось {expected_count} ссылок, найдено {actual_count}"
    
    for i, link in enumerate(links):
        assert link.is_displayed(), f"Ссылка с индексом {i} не отображается на странице"
    
    first_link_text = links[0].text
    assert "1" in first_link_text, f"Текст первой ссылки '{first_link_text}' не содержит '1'"

    driver.quit()
