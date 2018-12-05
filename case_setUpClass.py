#相依測試案例, 每個def 是有順序的案例只建立一次session

import os
import time
import settings
import unittest
from selenium import webdriver
from appium import webdriver
import settings
from BeautifulReport import BeautifulReport
from settings import session


current_path = os.getcwd()
report = os.path.join(current_path, "Report")
now = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(time.time()))

report_title = "Example_" + now + ".html"
des = "相依測試案例"


class yy(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        session.setsession(self)
        print("one time")
    def test_d1(self):
        print("D1")
        self.driver.find_element_by_xpath("xpath=//*[@text='忽略']").click()
    def test_d2(self):
        print("D3")
        self.driver.find_element_by_xpath("xpath=//*[@text='新增 NAS']").click()
    def test_d3(self):
        print("D3")
        self.driver.find_element_by_xpath("xpath=//*[@text='手動新增NAS']").click()
    def test_d4(self):
        print("d4")
        self.driver.find_element_by_xpath("xpath=//*[@id='server_host_edit']").send_keys("abcd")
    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        print("one time close")


for i in range(settings.loop_times):
    if __name__ == '__main__':
        suite = unittest.TestSuite()
        tests = ["test_d1", "test_d2", "test_d3", "test_d4"]
        # suite.addTests(unittest.makeSuite(yu))
        # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(yu))
        suite = unittest.TestSuite(map(yy, tests))

        # suite.addTests(suite1)
        print(suite)
        result = BeautifulReport(suite)
        result.report(description=des, filename=report_title, log_path=report)



