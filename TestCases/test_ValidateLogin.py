import string
import time

import pytest

from PageObject.LoginPage import LoginPage
from TestData import LoginPageData
from TestData.LoginPageData import DataLoginPage
from Utlities.BaseClass import BaseClass


class TestUserLogin(BaseClass):

    def test_login(self, getData):
        lgnPage = LoginPage(self.driver)
        lgnPage.addUsername().send_keys(getData["Username"])
        lgnPage.entrePassword().send_keys(getData["Password"])
        lgnPage.submitBtn().click()
        time.sleep(2)
        actual_message = lgnPage.dashboard().text
        assert "Dashboard" in actual_message

    @pytest.fixture(params=DataLoginPage.getTestData("login"))
    def getData(self, request):
        return request.param
