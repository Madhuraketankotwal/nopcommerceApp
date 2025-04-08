from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser")
    elif browser=='firefox':
        driver=webdriver.Firefox()
        print("launching firefox browser")

    else:
        driver=webdriver.Ie()

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

