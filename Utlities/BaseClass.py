import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setupBrowser")
class BaseClass:

    def verifyTextPresence(self, text):
        element = WebDriverWait(self.driver, 15).until(
            expected_conditions.presence_of_element_located((By.XPATH, text)))
        element.click()

    def verifyClickElement(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator))
        element.click()

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)


