import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addini("browser", help="Browser to run tests with")


@pytest.fixture(scope="module")
def driver(pytestconfig):
    browser = pytestconfig.getini("browser")
    if browser == "chrome":
        driver = webdriver.Chrome()  # Make sure to have ChromeDriver installed and in PATH
    elif browser == "firefox":
        driver = webdriver.Firefox()  # Make sure to have GeckoDriver installed and in PATH
    elif browser == "edge":
        driver = webdriver.Edge()  # Make sure to have EdgeDriver installed and in PATH
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(10)
    yield driver
    driver.quit()
