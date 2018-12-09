import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
import os


class BasicSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_button_dropdown(self):
        driver = self.driver
        driver.get("http://10.201.64.35/cgi-bin/webgui2.py")
        #checl that title is corrent
        self.assertIn("Raspberry Pi Temperature Logger", driver.title)
        #Test that each of the time intervals work
        select = Select(driver.find_element_by_name("timeinterval"))
        select.select_by_visible_text("the last 6 hours")


        select = Select(driver.find_element_by_name("timeinterval"))
        select.select_by_visible_text("the last 12 hours")


        select = Select(driver.find_element_by_name("timeinterval"))
        select.select_by_visible_text("the last 24 hours")

        #Test that the update button works
        select = driver.find_element_by_xpath("//input[@value='Display']").click()

        #Test that 


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()