from selenium.webdriver.common.by import By


class TrackerUserPageLocators():
    FILE_TYPE = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div[2]/ul/div[1]/li/a')
    PERSON = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div[2]/ul/div[2]/li/a')
    GENDER = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div[2]/ul/div[3]/li/a')
    DOCUMENT = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div[2]/ul/div[7]/li/a/span[1]/span')


