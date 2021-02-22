#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""装饰器实现单例模式"""


def singleton(cls):
    instance = {}

    def _singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return _singleton


@singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x

    def __str__(self):
        return str(self.x)


if __name__ == '__main__':
    a1 = A(2)
    a2 = A(3)
    print(id(a1), a1)
    print(id(a2), a2)
