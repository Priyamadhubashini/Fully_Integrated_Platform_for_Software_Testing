import unittest
import xmlrunner  # Required to generate JUnit XML reports for Jenkins
from selenium import webdriver
from selenium.webdriver.edge.service import Service

class GoogleTest(unittest.TestCase):
    def setUp(self):
        # Ensure Microsoft Edge is installed on the machine
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(10)

    def test_Test_01(self):
        """Test to verify if 'Google' is in the page title"""
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title)

    def test_Verify_Page_Title(self):
        """Test to verify if the page title exactly matches 'Google'"""
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertEqual(driver.title, "Google")

    def tearDown(self):
        # Close the browser instance after each test
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    # Generates XML reports in the 'test-reports' directory for TestLink integration
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
