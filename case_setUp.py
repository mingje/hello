#獨立測試案例, 每個def 都是一個獨立的案例需要重新建立session
import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from BeautifulReport import BeautifulReport
from settings import session
import settings

current_path = os.getcwd()
report = os.path.join(current_path, "Report")
now = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(time.time()))

report_title = "Example_" + now + ".html"
des = "獨立測試案例"




class xx(unittest.TestCase):
    #@classmethod
    def setUp(self):
        print("start")
        session.setsession(self)
    def test_minus1(self):
        '''這是失敗的用例'''
        print("1")
        self.assertEqual(1,2)
    def test_uu(self):
        print("2")
        #yy1 = yy.d1(self)
        #yy1 = yy.d2(self)
    def test_add(self):
        print("3")
    def test_mul(self):
        print("4")
    def test_minus(self):
        print("5")
    #@classmethod
    def tearDown(self):
        print("close")
        self.driver.quit()

for i in range(settings.loop_times):
    if __name__ == '__main__':
        suite = unittest.TestSuite()
        #tests = ["test_minus1", "test_uu", "test_add", "test_mul", "test_minus"]
        suite.addTests(unittest.makeSuite(xx))
        # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(yu))
        #suite = unittest.TestSuite(map(yu, tests))

        # suite.addTests(suite1)
        print(suite)
        result = BeautifulReport(suite)
        result.report(description=des, filename=report_title, log_path=report)