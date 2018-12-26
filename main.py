# -*- coding: utf-8 -*-
#!/usr/bin/env python
#入口程序
#获得要做的行动，以及行动的目标
import sys, getopt
sys.dont_write_bytecode = True#不生成pyc文件

usage = '''
Usage:
    need:
        -u/--url= target url
    options:
        -P/--port= Port scan
        -U/--Url=  get url
        -A/--all=  all options
        -S/--ssl   SSL SHA
'''
def main(argv):
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hAPUS:u:", ["help", "all","port","Url","ssl","url"])#"ho:"也可以写成'-h-o:'
        flag = 0 #是否存在-u或者url=
        for i in opts:
            if 'u' in i[0]:
                url = i[1]
                flag = 1
                break
        if not flag:
            print usage
            sys.exit(2)
    except getopt.GetoptError:
        print usage
        sys.exit(2)

    for opt,arg in opts:
        if opt in ("-h","--help"):
            print usage
        elif opt in ("-P","--port"):
            #扫描端口
            action = loadAct('portScan')
            action.do(url)
        elif opt in ("-U","--Url"):
            #分析url
            action = loadAct('urlScan')
            action.do(url)
        elif opt in ("-S","--ssl"):
            # SSL证书查询
            action = loadAct('sslScan')
            action.do(url,arg)
        elif opt in ("-A","--all"):
            #ALL
            action = loadAct('urlScan')
            action.do(url)
            action = loadAct('portScan')
            action.do(url)
'''
读取poc
p1 poc类
'''
def loadAct(action):
    p1 = __import__(action)
    p1 = getattr(p1,action)
    return p1()


if __name__ == "__main__":
   main(sys.argv[1:])
