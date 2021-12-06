import time
from time import process_time, perf_counter

from ..components.time_counter import running_time_counter
from ..pages.tracker_main_page import TrackerMainPage
from ..pages.tracker_user_page import TrackerUserPage
from ..pages.tracker_file_type_grid_page import TrackerFileTypePage


def test_add_entry(browser):
    start = process_time()
    perf_start = perf_counter()
    url = "http://194.87.102.173:4105/"
    main_page = TrackerMainPage(browser, url)
    main_page.open()
    time.sleep(4)
    main_page.test_authorization()
    time.sleep(4)
    user_page = TrackerUserPage(browser, browser.current_url)
    user_page.test_open_file_type_table()
    time.sleep(4)
    file_type_page = TrackerFileTypePage(browser, browser.current_url)
    file_type_page.test_file_type_add_entry()
    time.sleep(3)
    end = process_time()
    running_time_counter(start, end, 'TEST FILE')
    perf_end = perf_counter()
    running_time_counter(perf_start, perf_end, 'TEST FILE')
