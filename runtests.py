__author__ = 'wanghongxing'

from unittest import  TestSuite
from unittest import TestResult
from unittest import  TextTestResult
from test_01 import OpenBrowser
import HTMLTestRunner

import nose
from proboscis import TestProgram

# def suite():
#     suite = TestSuite()
#     suite.addTest(OpenBrowser('test_open_bing'))
#     file = open("result.html","wb")
#     #test_result = TextTestResult(stream=file, descriptions="test", verbosity=2)
#     runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='api test result', description='test result')
#     #suite.run(result=test_result)
#     #print test_result
#     runner.run(suite)




def run_tests():
    nose.run()


def run_test_prob():
    import test_01

    TestProgram().run_and_exit()

if __name__ == "__main__":
    run_tests()