# coding:utf-8
# author:vanll
# -- demo code --

import requests
import threading
import time

class RequstBaidu():
    def __init__(self,url):
        self.url = url
        print(self.url)

    def requestbaidu(self):
        response = requests.get(self.url)
        resjson = response.text
        print(response,resjson)
        # return resjson


class ThreadContol():
    # def __init__(self,num,func):
    #     self.num = num
    #     self.func = func

    def theadnum(self,num,func):
        for i in range(0,num):
            t = threading.Thread(target=func ,name='demo')
            print(func)
            t.setDaemon(True)
            t.start()
            print('Thnum:{}'.format(i))
            t.join()


    def theadnums(self,num,func):
        thlist = []
        for i in range(0,num):
            t = threading.Thread(target=func,name='demo')
            t.setDaemon(True)
            thlist.append(t)
            print('Thnum:{}'.format(i))

        for t in thlist:
            t.start()


        for t in thlist:
            t.join()


if __name__ == '__main__':
    url = 'https://www.baidu.com/'
    ret = RequstBaidu(url)
    res = ret.requestbaidu
    # print(res)
    Th = ThreadContol()
    thdemo = Th.theadnum(3,res)



















