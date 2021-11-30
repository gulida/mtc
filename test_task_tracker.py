import time

from .pages.tracker_main_page import TrackerMainPage
from .pages.tracker_user_page import TrackerUserPage
from .pages.tracker_file_type_grid_page import TrackerFileTypePage
from .pages.tracker_gender_grid_page import TrackerGenderPage
from .pages.tracker_person_grid_page import TrackerPersonPage


def test_the_system(browser):
    link = "http://194.87.102.173:4105/"
    page = TrackerMainPage(browser, link)
    page.open()
    time.sleep(4)
    page.test_authorization()
    time.sleep(4)
    user_page = TrackerUserPage(browser, browser.current_url)
    user_page.test_open_person_table()
    time.sleep(4)
    # user_page.test_open_gender_table()
    # time.sleep(4)
    # gender_page = TrackerGenderPage(browser, browser.current_url)
    # time.sleep(4)
    # gender_page.test_gender_table()
    person_grid_page = TrackerPersonPage(browser, browser.current_url)
    time.sleep(2)
    person_grid_page.test_person_table()

    time.sleep(4)
