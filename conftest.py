import pytest
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru', help='Choose language: en or ru')

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_language': language})
    print("\nStart browser for test...")
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.get_screenshot_as_file('capture.png')
    print("\nQuit browser ...")
    browser.quit()