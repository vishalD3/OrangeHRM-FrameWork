import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from TestData.LoginPageData import DataLoginPage
from Utlities.BaseClass import BaseClass


class addUserPage:
    def __init__(self, driver):
        self.driver = driver

    adminbtn = (By.XPATH, "//span[text()='Admin']")
    addbtn = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
    addUserRole = (By.XPATH, "//div[@class='oxd-select-text-input']")
    Sele_AddUserRole_DropDown = (By.XPATH, "//div[./div/label[text()='User Role']]//*[text()='+UserRoleData+']")
    empName = (By.XPATH, "//div[@class='oxd-autocomplete-wrapper']//div/input[@placeholder='Type for hints...']")
    StatusFrom_DropDown = (By.XPATH, f"(//div[@class='oxd-select-text-input'])[2]")
    addUserName = (By.XPATH, "//div[./div/label[text()='Username']]//input")
    addPassword = (By.XPATH, "//div[./div/label[text()='Password']]//input")
    addCPassword = (By.XPATH, "//div[./div/label[text()='Confirm Password']]//input")
    btnSave = (By.XPATH, "//div[@class = 'oxd-form-actions']/button[2]")
    RecordText = (By.XPATH, "//span[@class='oxd-text oxd-text--span']")

    def clickAdmin(self):
        return self.driver.find_element(*addUserPage.adminbtn)

    def clickAddbtn(self):
        return self.driver.find_element(*addUserPage.addbtn)

    def SetUserRoleAdmin(self):
        drop_down = []
        drop_down.append(self.driver.find_element(*addUserPage.addUserRole))
        for drop_down_element in drop_down:
            drop_down_element.click()
            drop_down_element.send_keys(Keys.DOWN)
            time.sleep(1)
            drop_down_element.send_keys(Keys.RETURN)
            time.sleep(1)

    def SetUserRoleESS(self):
        drop_down = []
        drop_down.append(self.driver.find_element(*addUserPage.addUserRole))
        for drop_down_element in drop_down:
            drop_down_element.click()
            drop_down_element.send_keys(Keys.DOWN)
            time.sleep(1)
            drop_down_element.send_keys(Keys.DOWN)
            time.sleep(1)
            drop_down_element.send_keys(Keys.RETURN)
            time.sleep(1)

    def addEmpName(self):
        empNamelist = []
        empNamelist.append(self.driver.find_element(*addUserPage.empName))
        for listName in empNamelist:
            listName.send_keys("ch")
            time.sleep(1)
            listName.send_keys(Keys.DOWN)
            time.sleep(1)
            listName.send_keys(Keys.DOWN)
            time.sleep(1)
            listName.send_keys(Keys.RETURN)

    def StatusSelectOPtionsDisabled(self):

        statuDrpDown = []
        statuDrpDown.append(self.driver.find_element(*addUserPage.StatusFrom_DropDown))
        for statusOpt in statuDrpDown:
            statusOpt.click()
            statusOpt.send_keys(Keys.DOWN)
            time.sleep(1)
            statusOpt.send_keys(Keys.DOWN)
            time.sleep(1)
            statusOpt.send_keys(Keys.RETURN)
            time.sleep(1)

    def StatusSelectOPtionsEnabled(self):

        statuDrpDown = []
        statuDrpDown.append(self.driver.find_element(*addUserPage.StatusFrom_DropDown))
        for statusOpt in statuDrpDown:
            statusOpt.click()
            statusOpt.send_keys(Keys.DOWN)
            time.sleep(1)
            statusOpt.send_keys(Keys.RETURN)
            time.sleep(1)

    def addNewUserName(self):
        return self.driver.find_element(*addUserPage.addUserName)

    def addPass(self):
        return self.driver.find_element(*addUserPage.addPassword)

    def addCPass(self):
        return self.driver.find_element(*addUserPage.addCPassword)

    def saveBtnClick(self):
        return self.driver.find_element(*addUserPage.btnSave)

    def textValidate(self):
        return self.driver.find_element(*addUserPage.RecordText)


