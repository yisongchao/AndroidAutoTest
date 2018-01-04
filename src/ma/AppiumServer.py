# -*- coding: utf-8 -*-

import subprocess
import os

class AppiumServer():
    def __init__(self,device):
        self.device = device

    def __log_file(self):
        self.logger = os.path.dirname()

    def Start(self,aport, bpport):
        cmd = "appium -p %s -bp %s -U %s" % (aport, bpport, self.device)
        return subprocess.Popen(cmd, shell=True,stdout = subprocess.PIPE,stderr=subprocess.PIPE, bufsize=1, close_fds=True)
        #stdout = subprocess.PIPE,

if __name__=='__main__':
    server = AppiumServer('3HX7N17401006385')
    server.Start(4711, 4811)
#    print 'xx'
    import RunScript as rs
    for i in rs.get_device_info():
        apps=AppiumServer(i)
        apps.Start(5500,5501)
