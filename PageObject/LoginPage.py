from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    userName = (By.XPATH, "//input[@name='username']")
    enterPassword = (By.XPATH, "//input[@name='password']")
    clickSubmit = (By.XPATH, "//button[@type='submit']")
    dashBoard = (By.XPATH, "//span[text()='Dashboard']")

    def addUsername(self):
        return self.driver.find_element(*LoginPage.userName)

    def entrePassword(self):
        return self.driver.find_element(*LoginPage.enterPassword)

    def submitBtn(self):
        return self.driver.find_element(*LoginPage.clickSubmit)

    def dashboard(self):
        return self.driver.find_element(*LoginPage.dashBoard)
