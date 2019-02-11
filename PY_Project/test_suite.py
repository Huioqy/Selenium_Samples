# -*- coding: utf-8 -*-

import unittest
from test_login import TestMathFunc
from HtmlTestRunner import HTMLTestRunner # need to install additionally

if __name__ == '__main__':

    suite = unittest.TestSuite()

    # "addTest": Single TestCase
    suite.addTest(TestMathFunc("test_multi"))

    # “addTests”：Mutilple TestCase
    # control the order of the tests' implementation
    tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
    suite.addTests(tests)

    # # addTests + TestLoader().loadTestsFromName(）
    # # can not control the order
    # suite.addTests(unittest.TestLoader().loadTestsFromNames(['test_mathfunc.TestMathFunc']))

    # # addTests + TestLoader().loadTestsFromTestCase()
    # # can not control the order
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))

    # run
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    # run and log txt
    # with open('UnittestTextReport.txt', 'a') as f:
    #     runner = unittest.TextTestRunner(stream=f, verbosity=2)
    #     runner.run(suite)

    # # run and log html
    # runner = HTMLTestRunner(output='')
    # runner.run(suite)
