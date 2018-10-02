__author__ = 'wanghongxing'

from unittest import  TestSuite
from unittest import TestResult
from unittest import  TextTestResult
from test_01 import OpenBrowser
import HTMLTestRunner

def suite():
    print TestResult(verbosity=2)
    suite = TestSuite()
    suite.addTest(OpenBrowser('test_open_bing'))
    file = open("result.html","wb")
    #test_result = TextTestResult(stream=file, descriptions="test", verbosity=2)
    runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='api test result', description='test result')
    #suite.run(result=test_result)
    #print test_result
    runner.run(suite)


if __name__ == "__main__":
    suite()