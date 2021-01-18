from base import BaseFunctions
from locators import Google
from selenium import webdriver
import unittest


class TestRun(unittest.TestCase, BaseFunctions):
    """Test case is:
        1 - Navigate to site.
        2 - Send text to search bar.
        3 - Click to search button.
        """

    def setUp(self):
        self.driver = webdriver.Chrome("C://chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(Google.website_link)
        self.base = BaseFunctions(driver=self.driver)

    def test(self):
        self.base.input(Google.search_bar, Google.text)
        self.base.click(Google.search_button)

    def TearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
