import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions



class profile:
    def __init__(self, n, ip, myDDNS, lanport, ac, pwd):
        """
        self.dc = {}
        self.dc["platformName"] = "Android"
        self.dc["platformVersion"] = "5.1.1"
        self.dc["deviceName"] = "7537c434"
        self.dc["appPackage"] = "com.qnap.qvideo"
        self.dc["appActivity"] = ".Qvideo"
        # desired_caps["appActivity"] = ".login.LoginActivity"

        self.dc["noReset"] = "True"
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", self.dc)
        """
        self.name = n
        self.NASLANIP = ip
        self.myDDNS = myDDNS
        self.lanport = lanport
        self.ac = ac
        self.pwd = pwd
    def LAN_login(self):
        self.driver.find_element_by_xpath("xpath=//*[@text='忽略']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='新增 NAS']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='手動新增NAS']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='server_host_edit']").send_keys(NAS1.NASLANIP)
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='user_password_edit']")))
        self.driver.find_element_by_xpath("xpath=//*[@id='user_password_edit']").send_keys(NAS1.pwd)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@text='儲存']")))
        self.driver.find_element_by_xpath("xpath=//*[@text='儲存']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='確認']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='確認']").click()
        flag = 1
        assert flag == 0

NAS1 = profile("TVS-473", "192.168.79.200", "steventvs473.myqnapcloud.com", "8080", "admin", "@dmin1234")
NAS1.LAN_login()


def LAN_login(self):
    '''這是失敗的用例'''
    NAS1 = profile("TVS-473", "192.168.79.200", "10.20.241.197", "115.43.107.17", "steventvs473.myqnapcloud.com",
                   "8080", "admin", "@dmin1234")
    self.driver.find_element_by_xpath("xpath=//*[@text='忽略']").click()
    self.driver.find_element_by_xpath("xpath=//*[@text='新增 NAS']").click()
    self.driver.find_element_by_xpath("xpath=//*[@text='手動新增NAS']").click()
    self.driver.find_element_by_xpath("xpath=//*[@id='server_host_edit']").send_keys(NAS1.NASLANIP2)
    WebDriverWait(self.driver, 30).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='user_password_edit']")))
    self.driver.find_element_by_xpath("xpath=//*[@id='user_password_edit']").send_keys(NAS1.pwd)
    WebDriverWait(self.driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//*[@text='儲存']")))
    self.driver.find_element_by_xpath("xpath=//*[@text='儲存']").click()
    self.driver.find_element_by_xpath("xpath=//*[@text='確認']").click()
    self.driver.find_element_by_xpath("xpath=//*[@text='確認']").click()
    time.sleep(3)
    self.driver.find_element_by_xpath("xpath=//*[@contentDescription='drawer opened']").click()
    self.driver.find_element_by_xpath("//*[@id='qbu_tv_account_subtitle']")
    flag = self.driver.find_element_by_xpath("//*[@id='qbu_tv_account_subtitle']").text
    assert flag == NAS1.NASLANIP2


def WAN_login(self):
    self.driver.find_element_by_xpath("xpath=//*[@text='忽略']").click()
    self.driver.find_element_by_xpath("xpath=//*[@text='新增 NAS']").click()
    self.driver.find_element_by_xpath("xpath=//*[@text='手動新增NAS']").click()
    self.driver.find_element_by_xpath("xpath=//*[@id='server_host_edit']").send_keys(NAS2.WANIP)
    self.driver.find_element_by_xpath("xpath=//*[@id='user_name_edit']").send_keys(NAS2.ac)
    WebDriverWait(self.driver, 30).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='user_password_edit']")))
    self.driver.find_element_by_xpath("xpath=//*[@id='user_password_edit']").send_keys(NAS2.pwd)
    self.driver.find_element_by_xpath("xpath=//*[@text='進階設定']").click()
    self.driver.swipe(669, 748, 672, 563, 503)
    self.driver.swipe(621, 603, 615, 324, 352)
    self.driver.find_element_by_xpath("//*[@id='safe_connection_checkbox']").click()
    self.driver.find_element_by_xpath("xpath=//*[@id='autoport_checkbox']").click()
    self.driver.find_element_by_xpath("xpath=//*[@id='port_simple']").send_keys(NAS2.lanport)
    WebDriverWait(self.driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//*[@text='儲存']")))
    self.driver.find_element_by_xpath("xpath=//*[@text='儲存']").click()
    self.driver.find_element_by_xpath("xpath=//*[@text='確認']").click()
    time.sleep(3)
    self.driver.find_element_by_xpath("xpath=//*[@contentDescription='drawer opened']").click()
    self.driver.find_element_by_xpath("//*[@id='qbu_tv_account_subtitle']")
    flag = self.driver.find_element_by_xpath("//*[@id='qbu_tv_account_subtitle']").text
    assert flag == NAS2.WANIP


