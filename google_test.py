import unittest
import xmlrunner
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

class GoogleTest(unittest.TestCase):
    def setUp(self):
        # Path where you saved the driver manually
        driver_path = r'C:\Drivers\msedgedriver.exe'
        
        options = Options()
        options.add_argument("--headless")  # Run in background
        
        # Pointing to the specific driver path
        service = Service(executable_path=driver_path)
        
        try:
            self.driver = webdriver.Edge(service=service, options=options)
            self.driver.implicitly_wait(10)
        except Exception as e:
            print(f"Driver start error: {e}")
            raise

    def test_test_Test_01(self):
        self.driver.get("http://www.google.com")
        self.assertIn("Google", self.driver.title)

    def test_test_Verify_Page_Title(self):
        self.driver.get("http://www.google.com")
        self.assertEqual(self.driver.title, "Google")

    def tearDown(self):
        if hasattr(self, 'driver'):
            self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
