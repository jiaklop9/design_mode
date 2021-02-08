#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
工厂方法定义了一个创建对象的接口，但由子类决定要实例化的类是哪个。工厂方法让类把实例化推迟到之类。
符合开闭原则
"""


class Book(object):
    # 产品
    def content(self):
        raise NotImplemented

    def read(self):
        print('阅读')

    def note(self):
        print('记笔记')


class FatherNovel(Book):
    # 产品
    def content(self):
        print('推理小说')


class FatherJournal(Book):
    # 产品
    def content(self):
        print('财经杂志')


class SonNovel(Book):
    # 产品
    def content(self):
        print('童话')


class SonJournal(Book):
    # 产品
    def content(self):
        print('儿童杂志')


class MotherNovel(Book):
    # 产品
    def content(self):
        print('爱情小说')


class MotherJournal(Book):
    # 产品
    def content(self):
        print('时尚杂志')


class Reader(object):
    # 工厂类
    def read(self, _type):
        book = self.choice_book(_type)
        book.content()
        book.read()
        book.note()

    def choice_book(self, _type):
        raise NotImplemented


class FatherRead(Reader):
    def choice_book(self, _type):
        if _type == 'novel':
            return FatherNovel()
        elif _type == 'journal':
            return FatherJournal()
        else:
            raise ValueError('Father: unknown book type')


class MotherRead(Reader):
    def choice_book(self, _type):
        if _type == 'novel':
            return MotherNovel()
        elif _type == 'journal':
            return MotherJournal()
        else:
            raise ValueError('Mother: unknown book type')


class SonRead(Reader):
    def choice_book(self, _type):
        if _type == 'novel':
            return SonNovel()
        elif _type == 'journal':
            return SonJournal()
        else:
            raise ValueError('Son: unknown book type')


def main():
    print("家庭阅读日...")
    father = FatherRead()
    mother = MotherRead()
    son = SonRead()

    print('-' * 5, '爸爸', '-' * 5)
    father.read('novel')
    print('-' * 5, '妈妈', '-' * 5)
    mother.read('novel')
    print('-' * 5, '儿子', '-' * 5)
    son.read('novel')


if __name__ == '__main__':
    main()
