import pytest
from selenium import webdriver
import time

@pytest.fixture()
def setup(browser):
    if browser=="edge":
        driver=webdriver.Edge("Driver/msedgedriver.exe")
        driver.maximize_window()
        print("Launching MS Edge Browser..................")
    elif browser=="chrome":
        driver = webdriver.Chrome("Driver/chromedriver2.exe")
        driver.maximize_window()
        print("Launching Chrome Browser..................")
        time.sleep(5)
    else:
        driver = webdriver.Chrome("Driver/chromedriver2.exe")
        driver.maximize_window()
        time.sleep(3)
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

######################## HTML Reports ##########################

# It is hook for adding environment info in html Reports.
def pytest_configure(config):
    config._metadata['Project Name'] = 'Dr Fleet'
    config._metadata['Module Name'] = 'Login Page'
    config._metadata['Tester Name'] = 'Ujjawal Kumar'

# It is hook for modifying/deleting environment info in html Reports

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Plugins",None)
    metadata.pop("Packages",None)



