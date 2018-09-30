__author__ = 'wanghongxing'



from selenium import webdriver
import unittest
import time


class OpenBrowser(unittest.TestCase):

    def test_open_bing(self):
        driver = webdriver.Chrome("chromedriver")
        driver.get("https://cn.bing.com/")
        time.sleep(5)
        assert "Bing" in driver.title