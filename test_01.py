__author__ = 'wanghongxing'



from selenium import webdriver
import unittest
import time
import os


class OpenBrowser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/wanghongxing/myvirtualenv/venv/chromedriver")
        #self.driver = webdriver.PhantomJS(executable_path="/Users/wanghongxing/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs")
        #self.driver = webdriver.PhantomJS(executable_path="/Users/wanghongxing/myvirtualenv/venv/phantomjs")

    def test_open_bing(self):
        "test description hongstarw"

        self.driver.get("https://cn.bing.com/")
        time.sleep(5)
        assert "Bing" in ("Bing")

    def tearDown(self):
        self.driver.close()




if __name__ == "__main__":
    unittest.main()