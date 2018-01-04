# -*- coding=utf-8 -*-

import threading
from ma.RunScript import *
from ma.AppiumClient import AppiumClient

class RunTest(threading.Thread):
    def __init__(self,device,port):
        threading.Thread.__init__(self)
        self.device=device
        self.port = port

    def run(self):
        self.client = AppiumClient(self.device,self.port)
        #self.client.server_start()
        self.client.case_start()

def run_test():
    device_l = get_device_info()
    list_test = []
    port = 4900
    for i in device_l:
        port = port +2
        t=RunTest(i,port)
        t.start()
        list_test.append(t)
    for i in list_test:
        i.join()

if __name__ == '__main__':
    run_test()
