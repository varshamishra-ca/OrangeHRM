import unittest
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
import time



class MyTest(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            cls.driver = webdriver.Chrome(executable_path="/Users/sumit/selenium/chromedriver")
            cls.driver.implicitly_wait(10)
            cls.driver.maximize_window()
            print("start")


        def test_Login_1(self):
            print(1)
            self.driver.get("https://opensource-demo.orangehrmlive.com")
            time.sleep(3)
            self.driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")
            self.driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
            self.driver.find_element_by_xpath("//input[@id='btnLogin']").click()
            x = self.driver.title
            print(x)
            links = self.driver.find_elements_by_tag_name("a")

            print("Number of links prsent: ", len(links))

            self.assertEqual(len(links),90)
            time.sleep(3)
            self.driver.get_screenshot_as_file("/Users/sumit/Desktop/CACC Barsha/homepage2.png")

        def test_Logout_2(self):
            print(2)
            self.driver.find_element_by_xpath("//a[@id='welcome']").click()
            self.driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()

        @classmethod
        def tearDownClass(cls):
            print("close")
            cls.driver.close()
            cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/sumit/Desktop/CACC Barsha/Reports"),verbocity=2)
