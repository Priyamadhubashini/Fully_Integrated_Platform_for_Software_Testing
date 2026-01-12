import unittest
from selenium import webdriver

class GoogleTest(unittest.TestCase):
    
    def setUp(self):
        """
        Setup: This method runs before every individual test case.
        It initializes the Chrome browser instance.
        """
        self.driver = webdriver.Chrome()

    def Test_01(self):
        """
        Test Case ID: MAP-1
        Name: Test_01
        Description: Checks if the word 'Google' is present in the website title.
        """
        driver = self.driver
        driver.get("http://www.google.com")
        # Validate that 'Google' is part of the page title
        self.assertIn("Google", driver.title)

    def Verify_Page_Title(self):
        """
        Test Case ID: MAP-2
        Name: Verify_Page_Title
        Description: Verifies that the page title is exactly 'Google'.
        """
        driver = self.driver
        driver.get("http://www.google.com")
        print("Executing: Verify_Page_Title Automation logic...")
        # Validate that the title matches 'Google' exactly
        self.assertEqual(driver.title, "Google")

    def tearDown(self):
        """
        Teardown: This method runs after every test case.
        It closes the browser to free up system resources.
        """
        self.driver.quit()

if __name__ == "__main__":
    # Standard entry point to run the unittest suite
    unittest.main()
