import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class MyAppTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the Chrome Driver
        s=Service('path_to_your_chromedriver')
        self.driver = webdriver.Chrome(service=s)
        self.driver.get("http://localhost:3000")  # URL to your React app

    def test_homepage_loads(self):
        # Test if homepage loads correctly
        self.assertIn("My App", self.driver.title)

    def test_user_data_displayed(self):
        # Test if user data is displayed correctly
        try:
            name_element = self.driver.find_element(By.XPATH, '//p[contains(text(), "Name:")]')
            email_element = self.driver.find_element(By.XPATH, '//p[contains(text(), "Email:")]')
            phone_element = self.driver.find_element(By.XPATH, '//p[contains(text(), "Phone:")]')
            address_element = self.driver.find_element(By.XPATH, '//p[contains(text(), "Address:")]')

            # Assert that each element is not empty
            self.assertTrue(name_element.text.split(': ')[1].strip())
            self.assertTrue(email_element.text.split(': ')[1].strip())
            self.assertTrue(phone_element.text.split(': ')[1].strip())
            self.assertTrue(address_element.text.split(': ')[1].strip())
        except Exception as e:
            print("Error occurred:", e)
            self.fail("User data is not displayed correctly")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
