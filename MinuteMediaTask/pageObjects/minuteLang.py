import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class minuteLang:
    button_langList = '//*[@id="mm-root"]/header/div/div[2]/div[2]/button[2]'
    es_button = '//*[@id="mm-root"]/header/div/div[2]/div[2]/ul/li[3]/a'


    def __init__(self,driver):
        self.driver=driver

    def langList(self):
        self.driver.find_element_by_xpath(self.button_langList).click()
    def esLang(self):
        self.driver.find_element_by_xpath(self.es_button).click()



    #     # Language
    # def setLanguage(self, lang):
    #     select = Select(self.driver.find_element_by_xpath('//*[@id="mm-root"]/header/div/div[2]/div[2]/button[2]/div/svg'))
    #     select.select_by_visible_text(lang)
    #     es = '//*[@id="mm-root"]/header/div/div[2]/div[2]/ul/li[3]/a'
    #

