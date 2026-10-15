import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture
def driver() -> WebDriver:
    d = webdriver.Chrome()
    d.maximize_window()
    yield d
    d.quit()