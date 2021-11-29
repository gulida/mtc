from selenium.webdriver.common.by import By


class TrackerCommonLocators():
    DISMISS = (By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[2]')
    ACCEPT = (By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[1]')
    MESSAGE = (By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/p')

    PAGINATION_BACK_BUTTON = (By.ID, 'pagination-back')
    PAGINATION_NEXT_BUTTON = (By.ID, 'pagination-next')
