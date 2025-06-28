//Selenium + PyTest


import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")
    yield driver
    driver.quit()

def test_valid_login(browser):
    login = LoginPage(browser)
    login.login("admin", "password123")
    assert "Dashboard" in browser.title