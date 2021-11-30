from selenium.webdriver.common.by import By


class TrackerPersonLocators():
    TABLE_NAME = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[2]/h1/span')
    TABLE_HEAD_TITLES = (By.NAME, 'PersonTitle')

    SEARCH_BUTTON = (By.NAME, 'PersonSearchIcon')
    SEARCH_INPUT = (By.NAME, 'PersonCustomSearch')

    # Person grid locators
    LAST_NAME = (By.NAME, 'PersonLastName')
    First_NAME = (By.NAME, 'PersonFirstName')
    FATHER_NAME = (By.NAME, 'PersonSecondName')
    USER_NAME = (By.NAME, 'PersonUserName')

    # ADD EDIT FORM LOCATORS
    ADD_BUTTON = (By.NAME, 'Person.add')
    CANCEL_BUTTON = (By.NAME, 'Person.cancel')
    SAVE_BUTTON = (By.NAME, 'Person.save')
    EDIT_BUTTON = (By.NAME, 'Person.edit')
    DELETE_BUTTON = (By.NAME, 'Person.delete')

    # Job history block
    JOB_HISTORY_ALL_CARDS = (By.NAME, 'JobHistoryAllCards')
    JOB_HISTORY_CARD_NAME = (By.NAME, 'JobHistoryCard')
    JOB_HISTORY_CARD_TITLE = (By.XPATH, '//*[@name="JobHistoryCardHeader"]/div/span[1]')
    JOB_HISTORY_CARD_EDIT_BTN = (By.NAME, 'JobHistoryCardEdit')
    JOB_HISTORY_CARD_DELETE_BTN = (By.NAME, 'JobHistoryCardDelete')

    # Job history form
    JOB_HISTORY_FORM_DIALOG_TITLE = (By.ID, 'form-dialog-title')
    JOB_HISTORY_DATE_START = (By.NAME, 'dateStart')
    JOB_HISTORY_DATE_FINISH = (By.NAME, 'dateFinish')
    JOB_HISTORY_POSITION = (By.NAME, 'idPost')
    # JOB_HISTORY_DOCUMENT_FILE = (By.NAME, 'idDocumentNavigationName')
    JOB_HISTORY_DOCUMENT_FILE = (By.ID, 'raised-button-file')
    JOB_HISTORY_DOCUMENT_DESCRIPTION = (By.NAME, 'idDocumentNavdescription')
    JOB_HISTORY_DOCUMENT_FILE_TYPE = (By.NAME, 'idDocumentNavidFileType')
    # JOB_HISTORY_DOCUMENT_FILE_TYPE = (By.NAME, 'idDocumentNavidFileType')
    JOB_HISTORY_SAVE_BUTTON = (By.NAME, 'JobHistoryAddEditView.save')
    JOB_HISTORY_CANCEL_BUTTON = (By.NAME, 'JobHistoryAddEditView.cancel')
