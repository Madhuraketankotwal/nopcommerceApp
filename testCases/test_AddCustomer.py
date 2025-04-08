import pytest
import time
from pageObjects.LoginPage import Login
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addcustomer(self, setup):
        self.logger.info("***************** Test_003_AddCustomer *********************")
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.login = Login(self.driver)
        self.login.setUserName(self.username)
        self.logger.info("***************** set username *********************")
        self.login.setPassword(self.password)
        self.logger.info("***************** set password *********************")
        self.login.clickLogin()
        self.logger.info("***************** Login successfully *********************")
        self.logger.info("***************** starting add customer test *********************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.addcust.clickOnAddNew()
        self.logger.info("***************** providing customer info *********************")

        self.email=random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Female")
        self.addcust.setFirstName("Madhura")
        self.addcust.setLastName("Dhore")
        self.addcust.setCompanyName("KV9 Audio")
        self.addcust.setAdminComment("this is for testing")
        self.addcust.clickOnSave()
        self.logger.info("***************** saving customer info *********************")
        self.logger.info("***************** add customer validation *********************")
        self.msg=self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.'in self.msg:
            assert True==True
            self.logger.info("************** add customer test case pass *********")
        else:
            self.driver.save_screenshot(".\\screenshot\\" + "test_AddCustomer_scr.png")
            self.logger.error("************** add customer test case failed *********")
            assert True==False

        self.driver.close()
        self.logger.info("************** ending home page title test *********")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))







