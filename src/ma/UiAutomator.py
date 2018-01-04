#   -*- coding=utf-8 -*-

from uiautomator import Device
import time
import subprocess

def protect(device ,nub):
    time.sleep(2)
    for i in range(nub):
        d = Device(device)
        el1 = d(text="取消")
        el2 = d(text="确定")
        print d.info
        d.screen.on()
        if el1.exists:
            el1.click()
        if el2.exists:
            el2.click()
        print i
        time.sleep(2)
        d.screen.off()

def get_device_info():
    """
    获取当前电脑连接的devices-安卓
    :return: 返回设备列表
    """
    device_list = []
    for device in subprocess.Popen('adb devices', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, close_fds=True).stdout.readlines():
        if 'device' in device and 'devices' not in device:
            device = device.split('\t')[0]
            device_list.append(device)
    print device_list
    return device_list


if __name__=='__main__':
    for i in get_device_info():
        protect(i,10)