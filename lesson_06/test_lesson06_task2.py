from selenium import webdriver
from selenium.webdriver.common.by import By


def test_session_storage_auth():
    driver = webdriver.Chrome()

    # === Cookie пользователя 1 (получить заранее из реального аккаунта) ===
    cookie_user1 = {
        "name": "session_id",
        "value": "NmVkNTZlM2MtNWI0ZC00ZGVjLTllODgtOWJmN2I1NjdlNGRk",
        "domain": ".gitflic.ru",
        "path": "/",
    }

    # === Cookie пользователя 2 (получить заранее из реального аккаунта) ===
    cookie_user2 = {
        "name": "session_id",
        "value": "MGVlNjBlOTAtNGYzMy00NjQxLWEzMmEtMDE4MTJjY2I2NWZk",
        "domain": ".gitflic.ru",
        "path": "/",
    }

    # 1. Откройте страницу https://gitflic.ru/
    driver.get("https://gitflic.ru/")

    # 2. Установите cookie пользователя 1
    driver.add_cookie(cookie_user1)

    # 3. Обновите страницу
    driver.refresh()

    # 4. Перейдите на страницу пользователя 1
    driver.get("https://gitflic.ru/user/username1")
    url_user1 = driver.current_url

    # 5. Разлогиньтесь (очистите куки)
    driver.delete_all_cookies()
    driver.get("https://gitflic.ru/")

    # 6. Установите cookie пользователя 2
    driver.add_cookie(cookie_user2)

    # 7. Обновите страницу
    driver.refresh()

    # 8. Перейдите на страницу пользователя 2
    driver.get("https://gitflic.ru/user/username2")
    url_user2 = driver.current_url

    # 9. Проверьте, что URL для пользователя 1 и пользователя 2 различаются
    assert url_user1 != url_user2, (
        f"URL должны различаться, но оба равны: {url_user1}"
    )

    driver.quit()
