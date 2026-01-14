import unittest
import xmlrunner
from selenium import webdriver
from selenium.webdriver.edge.options import Options

class GoogleTest(unittest.TestCase):
    def setUp(self):
        # Setting up Edge Options for Headless mode
        options = Options()
        options.add_argument("--headless")  # Run without opening a window
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        
        # Initializing the Edge driver with options
        try:
            self.driver = webdriver.Edge(options=options)
            self.driver.implicitly_wait(10)
        except Exception as e:
            print(f"Error initializing Edge Driver: {e}")
            raise

    def test_test_Test_01(self):
        """Test to verify if 'Google' is in the page title"""
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title)

    def test_test_Verify_Page_Title(self):
        """Test to verify if the page title exactly matches 'Google'"""
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertEqual(driver.title, "Google")

    def tearDown(self):
        if hasattr(self, 'driver'):
            self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
