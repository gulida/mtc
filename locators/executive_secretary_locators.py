from selenium.webdriver.common.by import By


class ExecutiveSecretaryLocators():
    SIDE_MENU_OPEN_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[1]/button')
    # Active cases
    MENU_CASES = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div[2]/ul/div[1]/li/button')
    ACTIVE_CASES_LINK = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div[2]/ul/div[1]/div/div/div/div/div[3]/li/a')
    FIRST_CASE_EDIT_BTN = (By.XPATH, '//*[@id="MUIDataTableBodyRow-0"]/td[1]/div[2]/button[1]')


    MENU_CLAIM = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div[2]/ul/div[2]/li/button')
    NEW_CLAIM_LINK = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div[2]/ul/div[2]/div/div/div/div/div[2]/li/a')

