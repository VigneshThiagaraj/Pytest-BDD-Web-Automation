from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:

    def __init__ (self, driver):
        self.driver = driver
        self.web_wait = WebDriverWait(self.driver, 30)

    def find_webelement(self, locator):
        return self.driver.find_element(*locator)

    def find_list_webelement(self, locator):
        return self.driver.find_elements(*locator)

    def wait_until_element_visibility(self, locator):
        return self.web_wait.until(expected_conditions.visibility_of(locator))

    def enter_value(self, locator, value):
        element = self.find_webelement(locator)
        self.web_wait.until(expected_conditions.element_to_be_clickable(element))
        element.send_keys(value)

    def click_element(self, locator):
        element = self.find_webelement(locator)
        self.web_wait.until(expected_conditions.element_to_be_clickable(element))
        element.click()