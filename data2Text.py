# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import re
import time
class data2Text:
    PATH = 'C:/Users/yuban/.auto/'


    url = ''
    # 构造函数,创建目标网站文件夹，并将OS操作目录改为目标网站文件夹
    def __init__(self,url):
        self.url = url
        if not os.path.exists(self.PATH):
            os.mkdir(self.PATH)
        os.chdir(self.PATH)
        if not os.path.exists(self.url):
            os.mkdir(self.url)
        os.chdir(self.url)
    # ssl相关信息，如果已存在，直接读取，不存在则写入
    # data包含
    # firstSeen
    # ipAddresses
    # lastSeen
    def sslInfo(self,data):
        os.chdir(self.PATH+self.url) # 以防万一
        with open("sslInfo.txt","wb") as f:
            f.write('\r\n'.join(data))

    # 检测对应文件是否存在，存在则输出内容
    def getInfo(self,txt):
        os.chdir(self.PATH+self.url) # 以防万一
        if os.path.exists(txt):
            with open(txt,"rb") as f:
                for i in f.readlines():
                    print i
            return 1
        else:
            return 0
    # API查询相关操作
    def APIInfo(self):
        os.chdir(self.PATH)
        if not os.path.exists(time.strftime("%Y-%m-%d")):
            os.mkdir(time.strftime("%Y-%m-%d"))
        os.chdir(time.strftime("%Y-%m-%d"))
        if not os.path.exists('api.txt'):
            with open('api.txt','wb') as f:
                f.write("Count: 1/15")
                print("Count: 1/15")
        else:
            with open('api.txt','rb') as f:
                text = re.findall(r'([0-9]+)',f.readline())
                num = text[0]
                if text[1] == num:
                    print("[-]API Count Zero!")
                    exit()
            with open('api.txt','wb') as f:
                f.write("Count: {0}/15".format(int(num)+1))
                print("Count: {0}/15".format(int(num)+1))









# a = data2Text("example.com")
# a.sslInfo(['FirstSeen:2015-02-09', 'LastSeen:2017-01-09', '194.42.46.143', '194.42.46.243'])
# a.APIInfo()
