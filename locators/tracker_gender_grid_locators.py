from selenium.webdriver.common.by import By


class TrackerGenderLocators():
    TABLE_NAME = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[2]/h1/span')
    TABLE_HEAD_TITLES = (By.NAME, 'SexTitle')
    TABLE_DATA_NAME = (By.NAME, 'SexName')

    SEARCH_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div[1]/div[2]/button[1]')
    SEARCH_INPUT = (
        By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/input')

    # ADD EDIT FORM LOCATORS
    ADD_BUTTON = (By.NAME, 'Sex.add')
    CANCEL_BUTTON = (By.NAME, 'SexAddEditView.cancel')
    SAVE_BUTTON = (By.NAME, 'SexAddEditView.save')
    EDIT_BUTTON = (By.NAME, 'Sex.edit')

    NAME = (By.NAME, 'name')
    DESCRIPTION = (By.NAME, 'description')
    CODE = (By.NAME, 'code')
