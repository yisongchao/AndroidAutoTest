# -*- coding: utf-8 -*-

import unittest
import src.image.image
import os
from src.PO import Utils
import src.PO.BasePage as BP
import time

class test_login(unittest.TestCase):
    driver=0

    @classmethod
    def set_driver(cls,rdriver):
        cls.driver = rdriver

    def setUp(self):
        pass

    def tearDown(self):
        os.remove(self.current_path)

    def runTest(self):
        pass

    def test_login(self, result=None):
        self.bp = BP.BasePage(self.__class__.driver)

        #qq登陆

        createQqLoginButton = None
        try:
            createQqLoginButton = self.bp.WaitUtil_Element("com.wepie.wespy:id/qq_login_frameLayout")
            #time.sleep(2)
            createQqLoginButton.click()
        except Exception as e:
            Utils.logging.error(e)
            print "qq主界面登陆失败"


        #qq登陆界面，查找失败则使用图像对比
        #print TestLogin.driver.contexts
        qqButton = None
        try:#com.tencent.mobileqq:id/name
            qqButton = self.bp.WaitUtil_Element("com.tencent.mobileqq:id/name")
            #qqButton = self.bp.WaitUtil_Element("//android.widget.Button[contains(@text,'登录')]")
            if qqButton.location_once_scrolled_into_view['x']== 0 or qqButton.location_once_scrolled_into_view['y'] == 0:
                raise Exception("定位点为边界点")
            qqButton.click()
        except Exception as e:
#            print os.getcwd()
            #Utils.logging.error(e)
            self.current_path = os.path.join(os.getcwd(),"image/image_repo/login_qq_%s.png" % str(int(time.time())))
            print self.current_path
            try:
                self.bp.get_screenshot_as_file(self.current_path)
            except Exception as e:
                Utils.logging.error(e)
            pts = src.image.image.find_image_position(self.current_path,
                                                      'image/image_repo/login_qq.png',
                                                      outfile='image/image_repo/result.png')
            print pts[2]
            pts2 = src.image.image.find_image_position(self.current_path,
                                                      'image/image_repo/login_logo_qq.png',
                                                      outfile='image/image_repo/result.png')
            print pts2[2]


            self.bp.tap(pts[2])
            time.sleep(0.5)
            self.bp.tap(pts2[2])

        #领取奖励界面关闭
        priceShutdownButton = None

        try:
            priceShutdownButton = self.bp.WaitUtil_Element("com.wepie.wespy:id/reward_pop_get_bt")
            priceShutdownButton.click()
        except:
            print "奖励领取界面失败"

        #公告关闭
        noticeShutdownButton = None
        try:
            noticeShutdownButton = self.bp.WaitUtil_Element("com.wepie.wespy:id/activity_view_close_view")
            noticeShutdownButton.click()
        except:
            print "公告关闭失败"

        # Butoon = None
        # Butoon = self.bp.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.wepie.wespy:id/home_head_image_border")')
        # Butoon.click()