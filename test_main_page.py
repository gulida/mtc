# def test_quest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     browser.get(link)
#     login_link = browser.find_element_by_css_selector('#login_link')
#     login_link.click()
import time

from .pages.new_case_page import NewCasePage
from .pages.executive_secretary_page import ExecutiveSecretaryPage
from .pages.main_page import MainPage


def test_the_system(browser):
    link = "http://194.87.102.173:3004"
    page = MainPage(browser, link)
    page.open()
    page.test_log_in_system()
    time.sleep(4)
    executive_secretary_page = ExecutiveSecretaryPage(browser, browser.current_url)
    executive_secretary_page.open_new_case_add_steps()
    new_case_page = NewCasePage(browser, browser.current_url)
    new_case_page.fill_in_plaintiff_person_form()
    # executive_secretary_page.open_active_cases_list()
    # time.sleep(10)
    # executive_secretary_page.open_active_case()
    time.sleep(5)