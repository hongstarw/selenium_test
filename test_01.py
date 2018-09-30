__author__ = 'wanghongxing'



from selenium import webdriver
import unittest
import time


class OpenBrowser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver")

    def test_open_bing(self):
        self.driver.get("https://cn.bing.com/")
        time.sleep(5)
        assert "Bing" in self.driver.title

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()