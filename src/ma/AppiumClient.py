# -*- coding=utf-8  -*-

from appium import webdriver
import sys,time
sys.path.append('../')
sys.path.append('../../')
from devices import config
from AppiumServer import AppiumServer
import unittest
import os
from uiautomator import Device
from RunScript import kill_installer
from src.PO import Utils
from src.testcase import BaseCase

#q = Queue.Queue()
class AppiumClient():
    def __init__(self,device,port = '4600'):
        self.device = device
        self.driver = ''
        self.appium_port = port
        self.appium_bport = int(port)+100

        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['deviceName']=self.device
        self.desired_caps['udid'] = self.device
        self.desired_caps['appPackage'] = 'com.wepie.wespy'
        self.desired_caps['appActivity'] = '.module.login.start.StartActivity'
        #安卓6.0/7.0版本，使用UiAutomator2作为自动化引擎
        #if self.device == '3HX7N17401006385':
        self.desired_caps['automationName'] = 'UiAutomator2'
        self.desired_caps['systemPort'] = int(port) + 3600
        #self.desired_caps['skipUnlock'] = True
        #else:
           # self.desired_caps['automationName'] = 'Appium'

    def __driverStart(self):
        self.driver = webdriver.Remote("http://localhost:%s/wd/hub" % self.appium_port, self.desired_caps)
        #q.put(self.driver)
        return  self.driver

    def __server_start(self):
        self.server =  AppiumServer(self.device)
        self.p = self.server.Start(self.appium_port,self.appium_bport)

    def __logger_file(self):
        pass

    def protect(self,nub):
        time.sleep(2)
        for i in range(nub):
            d = Device(self.device,4600,4620,4630)
            el1 = d(text="取消")
            el2 = d(text="确定")
            print d.info
            if el1.exists:
                el1.click()
            if el2.exists:
                el2.click()
            print i
            time.sleep(2)

    def case_start(self):
        self.__server_start()
        time.sleep(10)
        # 用来杀掉包安装activity
        # protect = threading.Thread(target=kill_installer,args=(self.device,21))
        # protect.setDaemon(True)
        # protect.start()
        #kill_installer(self.device)
        self.driver = self.__driverStart()

            #执行顺序是：先执行test_login，再执行其他，各用例要求执行完成后返回主界面


        test_dir = 'testcase'
        case_l = []
        #suite = unittest.TestSuite()
      #  print self.driver.page_source
        for i in os.listdir(os.path.join(os.getcwd(), test_dir)):
            if i.startswith("test_") and i.endswith('.py'):
                module_name = 'src.testcase.' + i[0:-3]
                module = __import__(module_name, globals(), locals(), [i], -1)
                c = getattr(module, i[0:-3])
                c.set_driver(self.driver)
                suite = unittest.TestLoader().loadTestsFromTestCase(c)
                if i.startswith('test_login'):
                    case_l.insert(0,suite)
                else:
                    case_l.append(suite)
                print case_l

                #suite.addTest(BaseCase.ParametrizedTestCase.parametrize(i, param=self.driver))
                #suite.addTest(BaseCase.ParametrizedTestCase.parametrize(TestOne, param=13))
                #unittest.TextTestRunner(verbosity=2).run(suite)
        alltests = unittest.TestSuite(case_l)
        runner = unittest.TextTestRunner(verbosity=2)
        #使用run()方法运行测试套件（即运行测试套件中的所有用例）
        runner.run(alltests)
        time.sleep(10)
        #完成后关闭服务器及客户端
        self.driver.quit()
        self.p.kill()


if __name__=='__main__':
    test_dir = 'testcase/'
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print os.path.join(base_dir,test_dir)
    case_l = []
    for i in os.listdir(os.path.join(base_dir,test_dir)):
        if i.startswith("test_") and i.endswith('.py'):
            print i
            module_name = 'src.testcase.'+ i[0:-3]
            print module_name
            module = __import__(module_name, globals(), locals(), [i], -1)
            print module
            c = getattr(module, i[0:-3])
            obj = c()
            dir(obj)
            print dir()

