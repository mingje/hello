import unittest
from HtmlTestRunner import HTMLTestRunner
import HtmlTestRunner
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time
import os
from selenium import webdriver
import selenium
from selenium.common.exceptions import NoSuchElementException

x = 1
y = 1
class yu(unittest.TestCase):
    def test_minus1(self):
        print("qq")
    def test_uu(self):
        print("kk")
    def test_add(self):
        return x + y
    def test_mul(self):
        return x * y
    def test_minus(self):
        return x - z






if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [yu("test_add"), yu("test_mul"), yu("test_minus"), yu("test_d")]
    suite.addTests(tests)
    runner = HTMLTestRunner(output='example_suite',report_title="test11", descriptions="good")

    runner.run(suite)
