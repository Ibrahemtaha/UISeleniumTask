import pytest
from selenium import webdriver
from pageObjects.minuteLang import minuteLang
import time
from selenium.webdriver.common.action_chains import ActionChains


class Test_001_requestMore:
    baseURL = "https://www.90min.com/"


    def test_requestmore(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        ## we can use fixure for link, (above)
        self.driver.maximize_window()
        # self.driver.implicitly_wait(3)
        self.lang = minuteLang(self.driver)  #create an object

        #choose a
        self.lang.langList()
        self.lang.esLang()

        act_title = self.driver.title
        if act_title.strip() == "90min | Las últimas noticias de fútbol, fichajes y opinión de los fans":
            assert True



        self.driver.close()

#pytest -v -s testCases/test_requestDemoSilk.py


