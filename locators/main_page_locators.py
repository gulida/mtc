from selenium.webdriver.common.by import By


class MainPageLocators():
    USERNAME = (By.NAME, 'username')
    PASSWORD = (By.NAME, 'password')
    LOGIN_BUTTON = (
        By.XPATH, '//*[@id="root"]/div/div/div/div/div[3]/main/div[1]/div[1]/div/div/div/form/div[3]/button/span[1]')
