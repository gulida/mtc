import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru-RU', help='Choose language: en-US or ru-RU')


@pytest.fixture(scope="function")
# def browser():
def browser(request):
    language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_language': language})
    print("\nStart browser for test...")
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    # browser.get_screenshot_as_file('capture.png')
    print("\nQuit browser ...")
    browser.quit()
