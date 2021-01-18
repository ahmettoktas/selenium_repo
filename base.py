from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseFunctions():
    """
    Base Functions for wait for element, get input, click and click random element
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def click(self, selector):
        """
        Wait for element and click
        :param selector: locator of element to find and click
        """
        self.wait.until(ec.element_to_be_clickable(selector)).click()

    def input(self, selector, parameter):
        """
        Wait for element and send parameters
        :param selector: locator of element to find
        :param parameter: It is the parameter that will be sent to selector
        """
        self.wait.until(ec.visibility_of_element_located(selector)).send_keys(parameter)
