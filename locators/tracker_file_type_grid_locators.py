from selenium.webdriver.common.by import By


class TrackerFileTypeLocators():
    TABLE_NAME = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[3]/div/div[1]/div[1]/div/h6')
    TABLE_HEAD = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[3]/div/div[3]/table/thead/tr/th')
    HEAD_TITLE_LINK_START = '//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[3]/div/div[3]/table/thead/tr/th['
    HEAD_TITLE_LINK_END = ']/span/button/span[1]/div/div[1]'
    HEAD_TITLE_LINK1 = '//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[3]/div/div[3]/table/thead/tr/th[2]/div'
    HEAD_TITLE_LINK2 = '//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[3]/div/div[3]/table/thead/tr/th[3]/span/button/span[1]/div/div[1]'
    HEAD_TITLE_LINK3 = '//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[3]/div/div[3]/table/thead/tr/th[4]/span/button/span[1]/div/div[1]'
    HEAD_TITLE_LINK4 = '//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[3]/div/div[3]/table/thead/tr/th[5]/span/button/span[1]/div/div[1]'


    TABLE_BODY_ELEMENTS = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[3]/div/div[3]/table/tbody')