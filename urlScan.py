# -*- coding: utf-8 -*-
#!/usr/bin/env python

from bs4 import BeautifulSoup
from action import action
import requests
import sys
sys.dont_write_bytecode = True#不生成pyc文件

class urlScan(action):
    def do(self,url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }
        try:
            print "http://"+url
            html = requests.get("http://"+url,headers=headers,timeout=1).text
        except:
            print "[-]Connetion Error!"
            sys.exit()
        html = BeautifulSoup(html,'html5lib')
        for i in html.find_all('a'):
            a = str(i.get('href'))
            if (url in a or "http" not in a) and len(a) > 5 and "javascript" not in a:
                print a
        print "[+]Scan url completed!"
