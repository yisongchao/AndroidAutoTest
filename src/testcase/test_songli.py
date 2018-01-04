# -*- coding: utf-8 -*-

import unittest
import src.image.image
import os
import src.PO.BasePage as BP
from src.ma.RunScript import get_focused_package_xml
import time

class test_songli(unittest.TestCase):
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
    def test_songli(self, result=None):
        self.bp = BP.BasePage(self.__class__.driver)
        print self.__class__.driver
        Button = None
        try:
            Button = self.bp.WaitUtil_Element("com.wepie.wespy:id/home_head_image_border")
            Button.click()
        except:
            print "进入个人资料界面失败"
            # print self.__class__.driver.desired_capabilities['deviceName']
            # get_focused_package_xml(self.__class__.driver.capabilities['deviceName'],'/')



        try:
            Button = self.bp.WaitUtil_Element('com.wepie.wespy:id/send_flower_btn')
          #  Button.click()
            #Button = self.__class__.driver.find_element_by_id('com.wepie.wespy:id/send_flower_btn')
            Button.click()
        except:
            print "送礼界面失败"
            #get_focused_package_xml()

        try:
            Button = self.bp.WaitUtil_Elements("com.wepie.wespy:id/gift_cell_gift_icon_lay")[6]
            Button.click()
        except:
            print "选中大白失败"

        try:
            Button = self.bp.WaitUtil_Element("com.wepie.wespy:id/gift_num_lay")
            Button.click()
        except:
            print "选中数量失败"

        try:
            Button = self.bp.WaitUtil_Element("//android.widget.TextView[@text='6']")
            Button.click()
        except:
            print "选中数量具体值失败"

        try:
            Button = self.bp.WaitUtil_Element("com.wepie.wespy:id/care_gift_send_bt")
            Button.click()
        except:
            print "送礼失败"

        i=0
        for i in range(0,70):
            i=i+1
            try:
                Button = self.bp.WaitUtil_Element("com.wepie.wespy:id/wp_title_right_tx")
                Button.click()
            except:
                print "送礼失败"

            try:
                Button = self.bp.WaitUtil_Element("com.wepie.wespy:id/send_flower_btn")
                #Button = self.bp.WaitUtil_Element("//android.widget.TextView[contains(@text,'送礼物')]")
                Button.click()
            except:
                print "送礼界面失败"

            try:
                Button = self.bp.WaitUtil_Elements("com.wepie.wespy:id/gift_cell_gift_icon_lay")[6]
                Button.click()
            except:
                print "选中大白失败"

            try:
                Button = self.bp.WaitUtil_Element("com.wepie.wespy:id/gift_num_lay")
                Button.click()
            except:
                print "选中数量失败"

            try:
                #Button = self.bp.WaitUtil_Element("//android.widget.TextView[contains(@text,'3')]")
                Button = self.bp.WaitUtil_Element("//android.widget.TextView[@text='6']")
                Button.click()
            except:
                print "选中数量具体值失败"

            try:
                Button = self.bp.WaitUtil_Element("com.wepie.wespy:id/care_gift_send_bt")
                Button.click()
            except:
                print "送礼失败"





