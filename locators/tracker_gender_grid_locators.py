from selenium.webdriver.common.by import By


class TrackerGenderLocators():
    TABLE_NAME = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[2]/h1/span')
    TABLE_HEAD_TITLES = (By.NAME, 'SexTitle')
    TABLE_DATA_NAME = (By.NAME, 'SexName')

    SEARCH_BUTTON = (By.NAME, 'SexSearchIcon')
    SEARCH_INPUT = (By.NAME, 'SexCustomSearch')
    SEARCH_INPUT_CLOSE = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/button')

    # ADD EDIT FORM LOCATORS
    ADD_BUTTON = (By.NAME, 'Sex.add')
    CANCEL_BUTTON = (By.NAME, 'SexAddEditView.cancel')
    SAVE_BUTTON = (By.NAME, 'SexAddEditView.save')
    EDIT_BUTTON = (By.NAME, 'Sex.edit')
    DELETE_BUTTON = (By.NAME, 'Sex.delete')

    NAME = (By.ID, 'SexName')
    DESCRIPTION = (By.ID, 'SexDescription')
    CODE = (By.ID, 'SexCode')

