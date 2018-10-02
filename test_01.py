__author__ = 'wanghongxing'



from selenium import webdriver
import unittest
import time
import os


class OpenBrowser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver")

    def test_open_bing(self):
        "test description hongstarw"
        self.driver.get("https://cn.bing.com/")
        time.sleep(5)
        assert "Bing" in ("Bing")

    def tearDown(self):
        self.driver.close()




if __name__ == "__main__":
    unittest.main()