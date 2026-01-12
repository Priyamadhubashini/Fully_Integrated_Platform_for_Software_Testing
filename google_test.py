import unittest
from selenium import webdriver

class GoogleTest(unittest.TestCase):
    
    def setUp(self):
        """
        Setup: This method runs before every individual test case.
        """
        self.driver = webdriver.Chrome()

    def test_Test_01(self):
        """
        Test Case: Test_01
        Note: Method must start with 'test_' for unittest to find it.
        """
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title)

    def test_Verify_Page_Title(self):
        """
        Test Case: Verify_Page_Title
        Note: Method must start with 'test_' for unittest to find it.
        """
        driver = self.driver
        driver.get("http://www.google.com")
        print("Executing: Verify_Page_Title Automation logic...")
        self.assertEqual(driver.title, "Google")

    def tearDown(self):
        """
        Teardown: Closes the browser after the test.
        """
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
