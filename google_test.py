import unittest
import xmlrunner
from selenium import webdriver

class GoogleTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge() 

    def test_Test_01(self):
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title)

    def test_Verify_Page_Title(self):
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertEqual(driver.title, "Google")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
