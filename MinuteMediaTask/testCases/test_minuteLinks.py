import pytest
from selenium import webdriver
from pageObjects.minuteLinks import Links
import time
from selenium.webdriver.common.action_chains import ActionChains


class Test_001_requestMore:
    baseURL = "https://www.90min.com/"

    # def test_requestmore_title(self,setup):
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(3)
    #     act_title=self.driver.title
    #     self.driver.close()
    #     if act_title == "Minute Media - We Power Passion - Tech, Media & Advertising Company":
    #         assert True
    #     else:
    #         assert False




    def test_requestmore(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        ## we can use fixure for link, (above)
        self.driver.maximize_window()
        # self.driver.implicitly_wait(3)
        self.link = Links(self.driver)  #create an object

        self.link.testMenu1()
        a = ActionChains(self.driver)
        menu1 = self.driver.find_element_by_xpath('//*[@id="mm-root"]/header/div/div[1]/nav/div/ul/li[1]/span')
        a.move_to_element(menu1).perform()
        assert 'Premier League' == menu1.text

        self.link.testMenu2()
        menu2 = self.driver.find_element_by_xpath('//*[@id="mm-root"]/header/div/div[1]/nav/div/ul/li[2]/a/span').text
        assert 'Main Stories' == menu2

        self.link.testMenu3()
        menu3 = self.driver.find_element_by_xpath('//*[@id="mm-root"]/header/div/div[1]/nav/div/ul/li[3]/a/span').text
        assert 'Transfers' == menu3

        self.link.testMenu4()
        menu4 = self.driver.find_element_by_xpath('//*[@id="mm-root"]/header/div/div[1]/nav/div/ul/li[4]/a/span').text
        assert 'UEFA EURO 2020' == menu4

        self.link.testMenu5()
        menu5 = self.driver.find_element_by_xpath('//*[@id="mm-root"]/header/div/div[1]/nav/div/ul/li[5]/a/span').text
        assert 'FanVoice' == menu5

        self.link.testMenu6()
        menu6 = self.driver.find_element_by_xpath('//*[@id="mm-root"]/header/div/div[1]/nav/div/ul/li[6]/a/span').text
        assert 'The Switch' == menu6

        self.link.testMenu7()
        menu7 = self.driver.find_element_by_xpath('//*[@id="mm-root"]/header/div/div[1]/nav/div/ul/li[7]/span')
        a.move_to_element(menu7).perform()
        assert 'La Liga' == menu7.text

        self.link.testMenu8()
        menu8 = self.driver.find_element_by_xpath('//*[@id="mm-root"]/header/div/div[1]/nav/div/ul/li[8]/span')
        a.move_to_element(menu8).perform()
        assert 'Serie A' == menu8.text

        self.link.testMenu9()
        menu9 = self.driver.find_element_by_xpath('//*[@id="mm-root"]/header/div/div[1]/nav/div/ul/li[9]/span')
        a.move_to_element(menu9).perform()
        assert 'More' == menu9.text

        self.driver.close()

#pytest -v -s testCases/test_requestDemoSilk.py
