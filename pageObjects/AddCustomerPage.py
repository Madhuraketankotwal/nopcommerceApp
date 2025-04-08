import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common .by import By

class AddCustomer:
    lnkCustomers_menu_xpath="/html/body/div[3]/aside/div/nav/ul/li[4]/a"
    lnkCustomers_menuitem_xpath="/html/body/div[3]/aside/div/nav/ul/li[4]/ul/li[1]/a/p"
    btnAddnew_xpath="/html/body/div[3]/div[1]/form[1]/div/div/a"
    txtEmail_xpath="//input[@id='Email']"
    txtPassword_xpath="//input[@id='Password']"
    txtFirstname_xpath="//input[@id='FirstName']"
    txtLastname_xpath="//input[@id='LastName']"
    rdGenderMale_id="//input[@id='Gender_Male']"
    rdGenderFemale_id="//input[@id='Gender_Female']"
    txtCompanyName_xpath="//input[@id='Company']"
    chkIsTax_xpath="/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[7]/div[2]/input"
    txtCustomerRole_xpath="//div[@class='input-group-append input-group-required']"
    lstitemAdminstrators_xpath="//li[@id='select2-SelectedCustomerRoleIds-result-0sfd-1']"
    lstitemForumModerators_xpath="//li[@id='select2-SelectedCustomerRoleIds-result-venj-2']"
    lstitemRegistered_xpath="//li[@id='select2-SelectedCustomerRoleIds-result-ui6o-3']"
    lstitemGuests_xpath="//li[@id='select2-SelectedCustomerRoleIds-result-i8ce-4']"
    lstitemVendors_xpath="//li[@id='select2-SelectedCustomerRoleIds-result-iax1-5']"
    drpMangrOfVendor_xpath="//select[@id='VendorId']"
    txtAdminComment_xpath="//textarea[@id='AdminComment']"
    btnSave_xpath="//button[@name='save']"


    def _init_(self,driver):
        self.driver=driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_Keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.txtPassword_xpath).send_keys(password)

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH,self.txtFirstname_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH,self.txtLastname_xpath).send_keys(lname)

    def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element(By.ID,self.rdGenderMale_id).click()
        elif gender=='Female':
            self.driver.find_element(By.ID,self.rdGenderFemale_id).click()
        else:
            self.driver.find_element(By.ID,self.rdGenderMale_id).click()

    def setCompanyName(self,compname):
        self.driver.find_element(By.XPATH,self.txtCompanyName_xpath).send_keys(compname)

    def clickTextExempt(self):
        self.driver.find_element(By.XPATH,self.chkIsTax_xpath).click()

    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH,self.txtCustomerRole_xpath).click()
        time.sleep(3)
        if role=='Registered':
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role=='Administrators':
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemAdminstrators_xpath)
        elif role=='Guests':
             time.sleep(3)
             self.driver.find_element(By.XPATH,("//*[@id=SelectedCustomerRoleIds_taglist']/li/span[2]")).click()
             self.listitem=self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        elif role=='Registered':
             self.listitem=self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role=='Vendors':
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemVendors_xpath)
        else:
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)

        self.driver.execute_script("arguments[0].click();",self.listitem)

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.drpMangrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setAdminComment(self,comment):
        self.driver.find_element(By.XPATH,self.txtAdminComment_xpath).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()
