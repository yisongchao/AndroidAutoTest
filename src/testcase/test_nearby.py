# -*- coding: utf-8 -*-

import unittest
import src.image.image
import os
import src.PO.BasePage as BP
import time

class test_nearby(unittest.TestCase):
    driver=0

    @classmethod
    def set_driver(cls,rdriver):
        cls.driver = rdriver

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def runTest(self):
        pass

    @unittest.skip('skip test')
    def test_nearby(self, result=None):
        self.bp = BP.BasePage(self.__class__.driver)

        #qq登陆

        createQqLoginButton = None
        try:
            createQqLoginButton = self.bp.WaitUtil_Elements("com.wepie.wespy:id/icon")[0]
            createQqLoginButton.click()
        except:
            print "附近的人界面失败"


        #qq登陆界面，查找失败则使用图像对比
        #print TestLogin.driver.contexts
        self.bp.swipe_down()

        try:
            createQqLoginButton = self.bp.WaitUtil_Elements("com.wepie.wespy:id/icon")[2]
            createQqLoginButton.click()
        except:
            print "返回主界面失败"




