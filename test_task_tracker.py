import time

from .pages.tracker_main_page import TrackerMainPage
from .pages.tracker_user_page import TrackerUserPage
from .pages.tracker_file_type_grid_page import TrackerFileTypePage


def test_the_system(browser):
    link = "http://194.87.102.173:4105/"
    page = TrackerMainPage(browser, link)
    page.open()
    # page.test_open_user_page()
    time.sleep(4)
    page.test_authorization()
    time.sleep(4)
    user_page = TrackerUserPage(browser, browser.current_url)
    user_page.test_open_file_type_table()
    time.sleep(4)
    file_type_page = TrackerFileTypePage(browser, browser.current_url)
    file_type_page.test_file_type_table()
    time.sleep(4)
