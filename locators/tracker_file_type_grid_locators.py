from selenium.webdriver.common.by import By


class TrackerFileTypeLocators():
    TABLE_NAME = (By.NAME, 'FileTypeTitleName')
    COLUMN_TITLES = (By.NAME, 'FileTypeTitle')
    COLUMN_DATA_NAME = (By.NAME, 'FileTypeName')
    COLUMN_DATA_DESCRIPTION = (By.NAME, 'FileTypeDescription')
    COLUMN_DATA_CODE = (By.NAME, 'FileTypeCode')

    SEARCH_BUTTON = (By.NAME, 'FileTypeSearchIcon')
    SEARCH_INPUT = (By.NAME, 'FileTypeCustomSearch')

    # ADD EDIT FORM LOCATORS
    ADD_BUTTON = (By.NAME, 'FileTypeAddItem')
    CANCEL_BUTTON = (By.NAME, 'FileTypeAddEditViewCancelItem')
    SAVE_BUTTON = (By.NAME, 'FileTypeAddEditViewSaveItem')
    EDIT_BUTTON = (By.NAME, 'FileTypeEditItem')
    DELETE_BUTTON = (By.NAME, 'FileTypeDeleteItem')

    # File type grid locators
    NAME = (By.ID, 'FileTypeName')
    DESCRIPTION = (By.ID, 'FileTypeDescription')
    CODE = (By.ID, 'FileTypeCode')

