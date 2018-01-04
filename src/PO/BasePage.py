# -*- coding: utf-8 -*-
__author__ = 'yisongchao'

"""
@author:yisongchao
@time: 17/10/18 
"""

import Utils as U
import time

#po模式中的base，用于封装通用方法
class BasePage():
    def __init__(self, appium_driver):
        self.driver = appium_driver

    # 重新封装单个元素定位方法
    def WaitUtil_Element(self,loc,wait=10):
        stamp_time = int(time.time())
        for i in range(0,wait):
            if stamp_time + 20 > int(time.time()):
                time.sleep(2)
                try:
                    tmp = self.__find_element(loc)
                    return tmp
                except:
                    continue
                raise Exception("Cannot find %s in %d seconds" % (loc,wait))
            else:
                raise Exception("Cannot find %s in %d seconds" % (loc, wait))

    def __find_element(self, loc):
        element = ""
        if(loc.startswith("//")):
            element = self.driver.find_element_by_xpath(loc)
        elif(":id/" in loc or ":string/" in loc):
            element = self.driver.find_element_by_id(loc)
        else:
            try:
                element = self.driver.find_element_by_name(loc)
            except:
                element = self.driver.find_element_by_class_name(loc)
        #print element.location_once_scrolled_into_view
        # if element.location_once_scrolled_into_view['x']== 0 or element.location_once_scrolled_into_view['y'] == 0:
        #     raise Exception("定位点为边界点")
        return element

    def WaitUtil_Elements(self,loc,wait=10):
        stamp_time = time.time()
        for i in range(0,wait):
            time.sleep(1)
            try:
                tmp = self.__find_elements(loc)
                return tmp
            except:
                continue
            raise Exception("Cannot find %s in %d seconds" % (loc,wait))


    def __find_elements(self, loc):
        elements = []
        if (loc.startswith("//")):
            elements = self.driver.find_elements_by_xpath(loc)
        elif (":id/" in loc or ":string/" in loc):
            elements = self.driver.find_elements_by_id(loc)
        else:
            try:
                elements = self.driver.find_elements_by_name(loc)
            except:
                elements = self.driver.find_elements_by_class_name(loc)
        return elements


            # 重新封装输入方法

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            if click_first:
                self.WaitUtil_Element(loc).click()
            if clear_first:
                self.WaitUtil_Element(loc).clear()
            self.WaitUtil_Element(loc).send_keys(value)
        except AttributeError:
            U.Logging.error(u"%s 页面中未能找到 %s 元素" % (self, loc))

            # 重新封装按钮点击方法

    def clickButton(self, loc, find_first=True):
        try:
            if find_first:
                self.__find_element(loc)
            self.__find_element(loc).click()
        except AttributeError:
            U.Logging.error("%s 页面未能找到 %s 按钮" % (self, loc))

    def swipe(self, st, sy, ex, ey):
        """
        滑动
        分别为:起始点x,y。结束点x,y。与滑动速度。滑动默认800
        """
        return self.driver.swipe(st, sy, ex, ey, duration=900)

    def get_window_size(self):
        """
        获取屏幕分辨率
        {u'width': 1080, u'height': 1920}
        :return: 1080,1920
        """

        screen_size = self.driver.get_window_size()
        width = screen_size['width']
        height = screen_size['height']
        return width, height

    def swipe_ratio(self, st, sy, ex, ey):
        """

        :param st: 起始点宽
        :param sy: 起始点高
        :param ex: 结束点宽
        :param ey: 结束点高
        :return: 滑动动作
        """
        width, height = self.get_window_size()
        return self.swipe(str(st * width), str(sy * height),
                          str(ex * width), str(ey * height))

    def swipe_left(self):
        """
        左滑屏幕
        """
        self.swipe_ratio(0.8, 0.5, 0.2, 0.5)
        U.sleep(1)

    def swipe_right(self):
        """
        右滑屏幕
        """
        self.swipe_ratio(0.2, 0.5, 0.8, 0.5)
        U.sleep(1)

    def swipe_up(self):
        """
        上滑屏幕
        """
        time.sleep(1)
        self.swipe_ratio(0.5, 0.8, 0.5, 0.2)
        time.sleep(1)

    def swipe_down(self):
        """
        下滑屏幕
        """
        time.sleep(1)
        self.swipe_ratio(0.5, 0.2, 0.5, 0.8)
        time.sleep(1)

    def tap(self,pts):
        """
        点击屏幕
        """
        self.driver.tap(pts)
        time.sleep(1)

    def swipe_all(self, t):
        """
        选择如何滑动屏幕
        """
        if t == 'swipe_left':
            self.swipe_left()
        elif t == 'swipe_right':
            self.swipe_right()
        elif t == 'swipe_up':
            self.swipe_up()
        elif t == 'swipe_down':
            self.swipe_down()

    def get_screenshot_as_file(self, file_path):
        """

        :param file_path:
        :return: 获取android设备截图
        """

        return self.driver.get_screenshot_as_file(file_path)

    def start_activity(self, package, activity):
        """
        启动activity
        package:包名
        activity:.activity
        """
        return self.driver.start_activity(package, activity)

    def open_notifications(self):
        """
        打开系统通知栏
        """
        return self.driver.open_notifications()

    def is_app_installed(self, package):
        """
        检查是否安装
        package:包名
        """
        return self.driver.is_app_installed(package)

    def install_app(self, path):
        """
        安装应用
        path:安装路径
        """
        return self.driver.install_app(path)

    def remove_app(self, package):
        """
        删除应用
        package:包名
        """
        return self.driver.remove_app(package)

    def shake(self, ):
        """
        摇晃设备
        """
        return self.driver.shake()

    def close_app(self, ):
        """
        关闭当前应用
        """
        return self.driver.close_app()

    def reset_app(self, ):
        """
        重置当前应用
        """
        return self.driver.reset()

    def current_activity(self, ):
        """
        当前应用的activity
        """
        return self.driver.current_activity

    def send_key_event(self, arg):
        """
        参考文献：http://blog.csdn.net/jlminghui/article/details/39268419
        操作实体按键
        :return:
        """
        event_list = {'entity_home': 3, 'entity_back': 4, 'entity_menu': 82, 'entity_volume_up': 24,
                      'entity_volume_down': 25, "entity_enter": 66}
        if arg in event_list:
            self.driver.keyevent(int(event_list[arg]))

    def toggle_location_services(self):
        """
        开关定位服务
        :return:
        """
        return self.driver.toggle_location_services()


if __name__ == '__main__':
    pass
