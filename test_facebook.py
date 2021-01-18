from base import BaseFunctions
from locators import Facebook
from selenium import webdriver
import unittest


class TestRun(unittest.TestCase, BaseFunctions):
    """Test case is:
        1 - Navigate to site.
        2 - Click to sign up button.
        """

    def setUp(self):
        self.driver = webdriver.Chrome("C://chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(Facebook.website_link)
        self.base = BaseFunctions(driver=self.driver)

    def test(self):
        self.base.click(Facebook.sign_up)

    def TearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
