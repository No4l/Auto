# -*- coding: utf-8 -*-
#!/usr/bin/env python

from abc import ABCMeta,abstractmethod
import sys
sys.dont_write_bytecode = True#不生成pyc文件

'''
抽象
python2 __metaclass__ = ABCMeta
python3 类继承ABC
'''
class action():
    __metaclass__ = ABCMeta
    #metaclass = ABCMeta

    #抽象方法，继承的类需要实现
    @abstractmethod
    def do(self,url): pass
