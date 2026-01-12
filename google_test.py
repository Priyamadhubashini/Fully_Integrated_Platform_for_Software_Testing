import unittest
from selenium import webdriver

class GoogleTest(unittest.TestCase):
    def setUp(self):
        # Initialize the Chrome browser before starting each test
        self.driver = webdriver.Chrome()

    # Test Case 1: Checking if 'Google' is in the title
    def test_search(self):
        driver = self.driver
        driver.get("http://www.google.com")
        # Assert that 'Google' word is in the page title
        self.assertIn("Google", driver.title)

    # Test Case 2: Verifying the exact title of the page
    def test_page_title(self):
        driver = self.driver
        driver.get("http://www.google.com")
        print("Verifying the exact page title...")
        # Assert that the title matches 'Google' exactly
        self.assertEqual(driver.title, "Google")

    def tearDown(self):
        # Close the browser after the test completes to free resources
        self.driver.quit()

if __name__ == "__main__":
    # Start the test execution suite
    unittest.main()
