from selenium.webdriver.common.by import By


class UserCabinetLocators():
    GENDER = (By.NAME, 'idSex')
    GENDER_ERROR = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div/div/form/div[1]/div[2]/div/div[2]/div[5]/div/p')
    DATE_ISSUE = (By.NAME, 'dateIssue')
    TAB_MENU_CABINET = (By.XPATH, '//*[@id="full-width-tab-2"]')
    SIDE_MENU_USER_CABINET = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div[2]/ul/div/li/a')
    PASSPORT_TERM_CHECKBOX = (By.NAME, 'perpetualPassport')
    PASSPORT_TERM_CHECKBOX_LABEL = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div/div/form/div[1]/div[2]/div/div[2]/div[10]/label/span[2]')

    PIN_FIELD = (
        By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div/div/form/div[1]/div[2]/div/div[2]/div[6]/div/div')

