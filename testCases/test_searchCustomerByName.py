import time
import pytest
from pageObjects.LoginPage import Login
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_SearchCustomerByEmail_005:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def searchCustomerByEmail(self,setup):
        self.logger.info("******************* Test_SearchCustomerByEmail_005 ***************** ")
        self.driver =setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.login=Login(self.driver)
        self.login.setUserName(self.username)
        self.logger.info("******************* set username ***************** ")
        self.login.setPassword(self.password)
        self.logger.info("******************* set password ***************** ")
        self.login.clickLogin()
        self.logger.info("******************* login successfully ***************** ")
        self.logger.info("******************* starting search customer by email ***************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.logger.info("******************* searching customer by Email ***************** ")

        searchcust=SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(3)
        status=searchcust.searchCustomerByName( "Victoria Terces")
        assert True==status
        self.logger.info("******************** customer search by email test case finished")
        self.driver.close();