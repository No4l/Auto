# -*- coding: utf-8 -*-
#!/usr/bin/env python
from action import action
import threading
import socket
import time
import sys
sys.dont_write_bytecode = True#不生成pyc文件
lock = threading.Lock()
threads = []
class portScan(action):
    def do(self,url):
    	domain = url
    	ip = self.Get_ip(domain)
    	print("[+] IP: "+ip)
    	for n in range(1,76):
    		for p in range((n-1)*880,n*880):
    			t = threading.Thread(target=self.PortScan,args=(ip,p))
    			threads.append(t)
    			t.start()
    		for t in threads:
    			t.join()
    	print("Port scan completed!")


    def Get_ip(self,domain):
    	try:
    		return socket.gethostbyname(domain) #通过域名获取IP
    	except socket.error as e:
    		print('[-]%s: %s'%(domain,e))
    		return 0

    def PortScan(self,ip,port):
    	try:
    		s = socket.socket()
    		s.settimeout(1)
    		s.connect((ip,port))
    		lock.acquire()
    		openstr = "[+] PORT:" + str(port) + " OPEN "
    		print(openstr)
    		lock.release()
    		s.close()
    	except:
    		pass
