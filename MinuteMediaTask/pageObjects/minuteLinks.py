class Links:
    link1 = '//*[@id="mm-root"]/header/div/div[1]/nav/div/ul/li[1]/span'
    link2 = '//*[@id="mm-root"]/header/div/div[1]/nav/div/ul/li[2]/a/span'
    link3 = '//*[@id="mm-root"]/header/div/div[1]/nav/div/ul/li[3]/a/span'
    link4 = '//*[@id="mm-root"]/header/div/div[1]/nav/div/ul/li[4]/a/span'
    link5 = '//*[@id="mm-root"]/header/div/div[1]/nav/div/ul/li[5]/a/span'
    link6 = '//*[@id="mm-root"]/header/div/div[1]/nav/div/ul/li[6]/a/span'
    link7 = '//*[@id="mm-root"]/header/div/div[1]/nav/div/ul/li[7]/span'
    link8 = '//*[@id="mm-root"]/header/div/div[1]/nav/div/ul/li[8]/span'
    link9 = '//*[@id="mm-root"]/header/div/div[1]/nav/div/ul/li[9]/span'
    #link_socialMedia_Tw = '//*[@id="mm-root"]/header/div/div[1]/nav/div/ul/li[3]/a'

    def __init__(self, driver):
        self.driver = driver

    def testMenu1(self):
        self.driver.find_element_by_xpath(self.link1).click()

    def testMenu2(self):
        self.driver.find_element_by_xpath(self.link2).click()

    def testMenu3(self):
        self.driver.find_element_by_xpath(self.link3).click()

    def testMenu4(self):
        self.driver.find_element_by_xpath(self.link4).click()

    def testMenu5(self):
        self.driver.find_element_by_xpath(self.link5).click()

    def testMenu6(self):
        self.driver.find_element_by_xpath(self.link6).click()

    def testMenu7(self):
        self.driver.find_element_by_xpath(self.link7).click()

    def testMenu8(self):
        self.driver.find_element_by_xpath(self.link8).click()

    def testMenu9(self):
        self.driver.find_element_by_xpath(self.link9).click()



