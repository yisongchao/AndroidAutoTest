# -*- coding: utf-8 -*-
"""
封装所需adb操作
"""
from appium import webdriver
import subprocess
import AppiumServer
import time,random

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


def shell(self, args):
    cmd = "%s %s shell %s" % (command, self.device_id, str(args),)
    return subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

def get_activity(device):
    while True:
        # time.sleep(3)
        # print '1st   '
        # cmd = "adb -s %s shell dumpsys activity" % (device)
        # print cmd
       # subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, bufsize=1, close_fds=True)
        time.sleep(2)
        # print '2nd   '
        cmd = "adb %s shell dumpsys activity | grep mFocusedActivity" % (device)
        print cmd
        subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, bufsize=1, close_fds=True)


def kill_installer(device,deadline):
    i = 0
    while i < deadline:
        print 'hhh'
        time.sleep(3)
        i = i+3
        cmd ="%s -s %s shell %s" % ('adb', device, "am force-stop com.android.packageinstaller")
        print cmd
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, close_fds=True)



def get_focused_package_xml(device,path):
    file_name = random.randint(10, 99)
    cmd = "%s -s %s shell %s" % ('adb', device, "uiautomator dump /storage/self/primary/Download/tmp.xml")
    #print cmd
    subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, close_fds=True)
    time.sleep(2)
    cmd = "%s -s %s %s %s" % ('adb', device, "pull /storage/self/primary/Download/tmp.xml",path)
    #print cmd
    subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, close_fds=True)





def get_cpu(self, package_name):
    """
    获取当前cpu百分比
    """
    p = shell(
        'top -n 1 -d 0.5 | %s %s' %
        (find_util, package_name))
    while True:
        r = p.stdout.readline().strip().decode('utf-8')
        if r.endswith(package_name):
            lst = [cpu for cpu in r.split(' ') if cpu]
            return int(lst[2].split('%', 1)[0])


def __mem_pss(self, package_name):
    """
    获取当前应用内存
    """
    p = self.shell(
        'top -n 1 -d 0.5 | %s %s' %
        (find_util, package_name))
    while True:
        r = p.stdout.readline().strip().decode('utf-8')
        if r.endswith(package_name):
            lst = [mem for mem in r.split(' ') if mem]
            return int(lst[6].split('K')[0])



def __mem_mem_total(self):
    p = self.shell('cat proc/meminfo')
    while True:
        r = p.stdout.readline().strip().decode('utf-8')
        if r and 'MemTotal' in r:
            lst = [MemTotal for MemTotal in r.split(' ') if MemTotal]
            return int(lst[1])


def get_mem(self, package_name):
    """
    获取当前内存百分比
    """
    try:
        return int(
            self.__mem_pss(package_name) /
            float(
                self.__mem_mem_total()) *
            100)
    except:
        return None

def __mem_mem_total(self):
    p = shell('cat proc/meminfo')
    while True:
        r = p.stdout.readline().strip().decode('utf-8')
        if r and 'MemTotal' in r:
            lst = [MemTotal for MemTotal in r.split(' ') if MemTotal]
            return int(lst[1])

if __name__ == '__main__':
    print get_device_info()







