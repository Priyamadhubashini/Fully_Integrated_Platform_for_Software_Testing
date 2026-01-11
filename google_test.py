import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import xmlrunner
import os

class MyGoogleTest(unittest.TestCase):
    def test_01(self): 
        chrome_options = Options()
        chrome_options.add_argument("--headless") 
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.google.com")
        self.assertIn("Google", driver.title)
        driver.quit()

if __name__ == '__main__':
    if not os.path.exists('test-reports'):
        os.makedirs('test-reports')
    with open('test-reports/results.xml', 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output))