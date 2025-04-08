import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login

from testCases import conftest
from utilities.readProperties import ReadConfig

from utilities.customLogger import LogGen

class Test_Login_001:
    baseUrl=ReadConfig.getApplicationUrl()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()

    logger=LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("******************* test_login_001 **********************")
        self.logger.info("*******************verify homepage title **********************")
        self.driver=setup
        self.driver.get(self.baseUrl)
        time.sleep(3)
        act_title=self.driver.title
        time.sleep(3)

        if act_title=="nopCommerce demo store. Login":
            assert True
            self.driver.close()
            self.logger.info("******************* home page test case pass successfully ********************")

        else:
            self.driver.save_screenshot(".\\screenshot\\" + "test_login.png")
            self.driver.close()
            self.logger.error("******************* home page test case failed **********************")
            assert False

    @pytest.mark.regression
    def test_Login(self,setup):
        self.logger.info("******************* verify login page **********************")
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.login=Login(self.driver)
        self.login.setUserName(self.username)
        self.logger.info("******************* set username successfully **********************")
        time.sleep(3)
        self.login.setPassword(self.password)
        self.logger.info("******************* set password successfully **********************")
        time.sleep(3)
        self.login.clickLogin()
        self.logger.info("******************* click on login btn **********************")
        time.sleep(3)
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("******************* login test case pass successfully **********************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshot\\" + "test_login.png")
            self.driver.close()
            self.logger.error("******************* login test case failed **********************")

