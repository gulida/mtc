from selenium.webdriver.common.by import By


class TrackerAuthPageLocators():
    EMAIL = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password')
    SIGN_IN_BUTTON = (By.XPATH, '//*[@id="root"]/div/div/div/div/main/div/form/button')

