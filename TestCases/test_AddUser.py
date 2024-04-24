import time

import pytest

from PageObject.LoginPage import LoginPage
from PageObject.AddUserPage import addUserPage
from TestData.LoginPageData import DataLoginPage
from Utlities.BaseClass import BaseClass


class TestValidateAddUser(BaseClass):

    def test_addUser(self, getData):
        lgnPage = LoginPage(self.driver)
        lgnPage.addUsername().send_keys(getData["Username"])
        lgnPage.entrePassword().send_keys(getData["Password"])
        lgnPage.submitBtn().click()
        self.verifyClickElement(addUserPage.adminbtn)
        adminUser = addUserPage(self.driver)
        adminUser.clickAddbtn().click()
        adminUser.SetUserRoleESS()
        adminUser.addEmpName()
        adminUser.StatusSelectOPtionsDisabled()
        adminUser.addNewUserName().send_keys(getData["UserName"])
        adminUser.addPass().send_keys(getData["Paswrd"])
        adminUser.addCPass().send_keys(getData["Cpaswrd"])
        adminUser.saveBtnClick().click()
        ExpectedText = "Records Found"
        self.verifyClickElement(addUserPage.adminbtn)

        ActualText = adminUser.textValidate().text
        print(ActualText)
        time.sleep(5)

    @pytest.fixture(params=DataLoginPage.getTestData("addUser"))
    def getData(self, request):
        return request.param
