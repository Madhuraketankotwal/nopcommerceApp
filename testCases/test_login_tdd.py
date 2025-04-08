import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from testCases import conftest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test__002_DDT_Login:
    baseUrl=ReadConfig.getApplicationUrl()
    path=r"C:\Users\dhore\PycharmProjects\nopcommerceApp\TestData\Data.xlsx"
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_Login_ddt(self,setup):
        self.logger.info("********************** Test__002_DDT_Login ******************")
        self.logger.info("******************* verify login DDT Page **********************")
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.login=Login(self.driver)

        self.rows=XLUtils.getRowCount(self.path,'sheet1')
        print("Number of Rows i a Excel:",self.rows)

        list_status=[]

        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'sheet1', r, 3)
            self.login.setUserName(self.user)
            time.sleep(5)
            self.login.setPassword(self.password)
            time.sleep(5)
            self.login.clickLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopcommerce administration"

            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("***** Passes *******")
                    self.login.clickLogout()
                    list_status.append("pass")
                elif self.exp=="Fail":
                    self.logger.info("*********** failed **************")
                    self.login.clickLogout()
                    list_status.append("failed")

            elif act_title!=exp_title:
                if self.exp=="Pass":
                    self.logger.info("***** failed *******")
                    list_status.append("fail")
                elif self.exp=="Fail":
                    self.logger.info("*********** pass **************")
                    self.login.clickLogout()
                    list_status.append("pass")

            if "fail" not in list_status:
                self.logger.info("********** login DDT test is pass**********")
                self.driver.close()
                assert True

            else:
                self.logger.info("************** login DDT test failed ************")
                self.driver.close()
                assert False

        self.logger.info("************ End of DDT test ***************")
        self.logger.info("*********** complete tc_loginDDT_002 *************")