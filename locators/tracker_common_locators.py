from selenium.webdriver.common.by import By


class TrackerCommonLocators():
    DISMISS = (By.XPATH, 'AlertButtonNo')
    ACCEPT = (By.NAME, 'AlertButtonYes')
    MESSAGE = (By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/p')

    SHOWED_ITEM_COUNT = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div[4]/table/tfoot/tr/td/div/div/div/p[2]')

    PAGINATION_BACK_BUTTON = (By.ID, 'pagination-back')
    PAGINATION_NEXT_BUTTON = (By.ID, 'pagination-next')