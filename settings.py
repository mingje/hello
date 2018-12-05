from selenium import webdriver
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

product_list = ["Qvideo","Qget"]
flag = "Qget"
loop_times = 1


class session:

    def setsession(self):
        if flag == "Qvideo":
            self.dc = {}
            self.dc["platformName"] = "Android"
            self.dc["platformVersion"] = "5.1.1"
            self.dc["deviceName"] = "7537c434"
            self.dc["appPackage"] = "com.qnap.qvideo"
            self.dc["appActivity"] = ".Qvideo"
            # desired_caps["appActivity"] = ".login.LoginActivity"
            self.dc["noReset"] = "True"
            self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", self.dc)

        elif flag == "Qget":
            self.dc = {}
            self.dc["platformName"] = "Android"
            self.dc["platformVersion"] = "5.1.1"
            self.dc["deviceName"] = "7537c434"
            self.dc["appPackage"] = "com.qnap.com.qgetpro"
            self.dc["appActivity"] = ".Splash"
            # desired_caps["appActivity"] = ".login.LoginActivity"
            self.dc["noReset"] = "True"
            self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", self.dc)

class profile:
    def __init__(self, n, lanip1, lanip2, wanip, myDDNS, lanport, ac, pwd):
        self.name = n
        self.NASLANIP1 = lanip1
        self.NASLANIP2 = lanip2
        self.WANIP = wanip
        self.myDDNS = myDDNS
        self.lanport = lanport
        self.ac = ac
        self.pwd = pwd

NAS1 = profile("TVS-473", "192.168.79.200", "10.20.241.197", "115.43.107.17","steventvs473.myqnapcloud.com", "8080", "admin", "@dmin1234")
NAS2 = profile("TVS-473", "192.168.79.200", "10.20.241.197", "115.43.107.17", "mingjehouse.myqnapcloud.com", "5001", "cindy", "cindy")







