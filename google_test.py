import unittest
import xmlrunner
import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

class GoogleTest(unittest.TestCase):
    def setUp(self):
        # Path to the EdgeDriver you manually downloaded and placed in C:\Drivers
        driver_path = r'C:\Drivers\msedgedriver.exe'
        
        # Configure Edge options to handle browser errors and headless mode
        options = Options()
        options.add_argument("--headless")  # Runs browser in background without a window
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        
        # Bypass SSL/Privacy errors shown in image_c7e6f5.png
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--ignore-ssl-errors")
        
        # Initialize the Edge service with the specified driver path
        service = Service(executable_path=driver_path)
        
        try:
            self.driver = webdriver.Edge(service=service, options=options)
            self.driver.implicitly_wait(10) # Wait up to 10 seconds for elements to load
        except Exception as e:
            print(f"Error starting Edge Driver: {e}")
            raise

    def test_test_Test_01(self):
        """Verify that 'Google' is part of the page title"""
        driver = self.driver
        driver.get("http://www.google.com")
        # Checking if 'Google' exists in the title (Bypassing 'Privacy error' title)
        self.assertIn("Google", driver.title)

    def test_test_Verify_Page_Title(self):
        """Verify that the page title is exactly 'Google'"""
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertEqual(driver.title, "Google")

    def tearDown(self):
        # Close the browser session after each test case
        if hasattr(self, 'driver'):
            self.driver.quit()

if __name__ == "__main__":
    # Generate JUnit XML reports in 'test-reports' folder for Jenkins/TestLink integration
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
