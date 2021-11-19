from selenium.webdriver.common.by import By


class ActiveCaseLocators():
    # Plaintiff block open
    PLAINTIFF_BLOCK = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[3]/div[1]/div[1]/div[1]')
    # Plaintiff edit button
    PLAINTIFF_EDIT_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[3]/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div[3]/button/span[1]')
    # person info
    SURNAME = (By.NAME, 'surName')
    FIRSTNAME = (By.NAME, 'firstName')
    DATE_OF_BIRTH = (By.NAME, 'dob')
    GENDER = (By.NAME, 'idSex')
    PIN = (By.NAME, 'pin')
    PASSPORT_NUMBER = (By.NAME, 'passportNumber')
    PASSPORT_DATE_ISSUE = (By.NAME, 'dateIssue')
    PASSPORT_EXPIRE_DATE = (By.NAME, 'expireDate')
    PASSPORT_AUTHORITY = (By.NAME, 'authority')
    SAVE_BUTTON = (By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/button[1]')
