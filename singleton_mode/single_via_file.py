#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
使用模块创建单例：
    Python的模块就是天然的单例模式。因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc文件，而不是再次执行模块代码。
"""


class Singleton(object):
    def foo(self):
        pass


# 该对象即是单例模式的对象
singleton = Singleton()
