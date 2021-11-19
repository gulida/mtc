from selenium.webdriver.common.by import By


class NewCaseLocators():
    # person form locators
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

    # PLAINTIFF BLOCK: Adding plaintiff person
    PLAINTIFF_ADD_PERSON = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div[3]/div/div/div/div/p/div['
                                      '1]/div/div[1]/div/button')
    PLAINTIFF_SURNAME = (By.NAME, 'surName')
    PLAINTIFF_FIRSTNAME = (By.NAME, 'firstName')
    PLAINTIFF_DATE_OF_BIRTH = (By.NAME, 'dob')
    PLAINTIFF_GENDER = (By.NAME, 'idSex')
    PLAINTIFF_PIN = (By.NAME, 'pin')
    PLAINTIFF_PASSPORT_NUMBER = (By.NAME, 'passportNumber')
    PLAINTIFF_PASSPORT_DATE_ISSUE = (By.NAME, 'dateIssue')
    PLAINTIFF_PASSPORT_EXPIRE_DATE = (By.NAME, 'expireDate')
    PLAINTIFF_PASSPORT_AUTHORITY = (By.NAME, 'authority')
    PLAINTIFF_SAVE_BUTTON = (By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/button[1]')
    PLAINTIFF_GENDER_SELECT_BTN = (By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div[6]/div/div/div/div/svg')

    # Next Step button after plaintiff block
    NEXT_STEP_BUTTON_AFTER_PLAINTIFF = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div['
                                                  '3]/div/div/div/div/p/div[2]/div[2]/button')

    # Next Step button after defendant block
    NEXT_STEP_BUTTON_AFTER_DEFENDANT = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div['
                                                  '5]/div/div/div/div/p/div[2]/div[2]/button')

    # CLAIM BLOCK: Adding claims
    CLAIM_ADD_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div[7]/div/div/div/div/p/div['
                                  '1]/div/div[1]/div/div/button')
    DEMAND_TEXTAREA = (By.NAME, 'demand')
    DEMAND_SAVE_BUTTON = (By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/div/button[1]')

    # Next Step button after claim block
    NEXT_STEP_BUTTON_AFTER_CLAIM = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div['
                                              '7]/div/div/div/div/p/div[2]/div[2]/button')

    # COMMON INFO BLOCK: Adding common info
    NAME_OF_THE_CLAIM = (By.NAME, 'titleClaim')
    APPLICABLE_RIGHT = (By.NAME, 'idLegalRight')
    STANDING_ORDER = (By.NAME, 'idStandingOrder')
    BASE_OF_DISPUTE = (By.NAME, 'idBaseOfDispute')
    LANGUAGE = (By.NAME, 'idLanguage')

    # Next Step button after common info block
    NEXT_STEP_BUTTON_AFTER_COMMON_INFO = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div['
                                                    '9]/div/div/div/div/p/div/div/div/form/div[2]/div[2]/button')

    # PAYMENT BLOCK: Adding payments
    AMOUNT_OF_CLAIM = (By.NAME, 'amount')
    AMOUNT_OF_CLAIM_VALUTE_NAME = (By.NAME, 'idValute')
    ARBITRATION_FEE = (By.NAME, 'arbitrationFee')
    ARBITRATION_FEE_VALUTE_NAME = (By.NAME, 'arbitrationFeeIdValute')
    REGISTRATION_FEE = (By.NAME, 'registrationFee')
    REGISTRATION_FEE_VALUTE_NAME = (By.NAME, 'registrationFeeIdValute')
    SURCHARGE = (By.NAME, 'surcharge')
    SURCHARGE_VALUTE_NAME = (By.NAME, 'surchargeIdValute')
    DEADLINE_FOR_PAYMENT_OF_THE_ARBITRATION_FEE = (By.NAME, 'dateExpireArbitrationPayment')
    DEADLINE_FOR_ADDITIONAL_PAYMENT_OF_THE_ARBITRATION_FEE = (By.NAME, 'dateExpireArbitrationSurcharge')

    # Next Step button after Payments block
    NEXT_STEP_BUTTON_AFTER_PAYMENTS = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div['
                                                 '11]/div/div/div/div/p/div[3]/div[2]/button')
    # Next Step button after Arbiter block
    NEXT_STEP_BUTTON_AFTER_ARBITER = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div['
                                                '13]/div/div/div/div/p/div[2]/div[2]/button')

    # DOCUMENTS BLOCK: Adding documents
    ADD_DOCUMENT_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div[15]/div/div/div/div/p/div['
                                     '1]/div/div[1]/button[1]')
    DOCUMENT = (By.ID, 'raised-button-file')
    DOCUMENT_DESCRIPTION = (By.NAME, 'idDocumentNavdescription')
    DOCUMENT_ISSUE_DATE = (By.NAME, 'idDocumentNavissueDate')
    DOCUMENT_FILE_TYPE = (By.NAME, 'idDocumentNavidFileType')
    DOCUMENT_TYPE = (By.NAME, 'idDocumentNavidDocumentType')
    DOCUMENT_DATE_END = (By.NAME, 'dateEnd')

    DOCUMENT_SAVE_BUTTON = (By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/div/button[1]')

    # Next Step button after Payments block
    NEXT_STEP_BUTTON_AFTER_DOCUMENTS = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div[15]/div/div/div/div/p/div[2]/div[2]/button')

    # Converting claim template
    TEMPLATE_CONVERT_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div[17]/div/div/div/div/p/div[4]/div[1]/button')

    # Next Step button after Template block
    NEXT_STEP_BUTTON_AFTER_TEMPLATE = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div[17]/div/div/div/div/p/div[5]/div[2]/button')

    # DOCUMENTS BLOCK STEP 10: Adding documents
    ADD_DOCUMENT_BUTTON_10 = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div[19]/div/div/div/div/p/div[1]/div/div[1]/button[1]')
    DOCUMENT_10 = (By.ID, 'raised-button-file')
    DOCUMENT_DESCRIPTION_10 = (By.NAME, 'idDocumentNavdescription')
    DOCUMENT_ISSUE_DATE_10 = (By.NAME, 'idDocumentNavissueDate')
    DOCUMENT_FILE_TYPE_10 = (By.NAME, 'idDocumentNavidFileType')
    DOCUMENT_TYPE_10 = (By.NAME, 'idDocumentNavidDocumentType')
    DOCUMENT_DATE_END_10 = (By.NAME, 'dateEnd')

    DOCUMENT_SAVE_BUTTON_10 = (By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/div/button[1]')

    # Next Step button after Payments block
    NEXT_STEP_BUTTON_AFTER_DOCUMENTS_10 = (
    By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div[19]/div/div/div/div/p/div[2]/div[2]/button')

    # Next Step button after Documents_10 block
    NEXT_STEP_BUTTON_AFTER_NOTIFICATIONS = (
    By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div[21]/div/div/div/div/p/div[2]/div[2]/button')