import time

from .pages.executive_secretary_page import ExecutiveSecretaryPage
from .pages.main_page import MainPage
from .pages.active_case_page import ActiveCasePage


def test_active_case(browser):
    link = "http://194.87.102.173:3004"
    page = MainPage(browser, link)
    page.open()
    page.test_log_in_system()
    time.sleep(4)
    executive_secretary_page = ExecutiveSecretaryPage(browser, browser.current_url)
    executive_secretary_page.open_active_cases_list()
    time.sleep(10)
    executive_secretary_page.open_active_case()
    time.sleep(5)
    active_page = ActiveCasePage(browser, browser.current_url)
    active_page.edit_plaintiff_person_form()
    time.sleep(10)


