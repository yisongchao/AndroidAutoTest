# -*- coding: utf-8 -*-

import unittest
import src.PO.BasePage as BP


class test_joinhouse(unittest.TestCase):
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
    def test_joinhouse(self, result=None):
        print self.__class__.driver
        self.bp = BP.BasePage(self.__class__.driver)

        Button = None
        try:
            print self.bp.WaitUtil_Elements("com.wepie.wespy:id/icon")
            Button = self.bp.WaitUtil_Elements("com.wepie.wespy:id/icon")[3]
            #Button = self.bp.WaitUtil_Element("android.widget.TextView[contains(@text,'房间')]")
            Button.click()
        except:
            print "房间界面失败"



        try:
            Button = self.bp.WaitUtil_Element("com.wepie.wespy:id/room_list_search_img")
            Button.click()
        except:
            print "搜索房间界面失败"

        key = "2"
        try:
            self.bp.send_keys('com.wepie.wespy:id/search_room_edit_text',key,True,True)
        except:
            print "输入房间号失败"


        try:
            Button = self.bp.WaitUtil_Element("com.wepie.wespy:id/search_room_enter_tx")
            Button.click()
        except:
            print "确认按钮失败"
            Button = self.bp.WaitUtil_Element("com.wepie.wespy:id/search_room_cancel_tx")
            Button.click()

        # try:
        #     Button = self.bp.WaitUtil_Elements("com.wepie.wespy:id/icon")[2]
        #     Button.click()
        # except:
        #     print "返回主界面失败"




