#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import random


class Book(object):
    def content(self):
        raise NotImplemented

    def read(self):
        print('read')

    def note(self):
        print('record')


class Novel(Book):
    def content(self):
        print('这是本小说')


class Journal(Book):
    def content(self):
        print('这是本杂志')


class SimpleFactory(object):
    @classmethod
    def choice_book(cls, _type):
        if _type == 'novel':
            return Novel()
        elif _type == 'journal':
            return Journal()
        else:
            return ValueError('unknown book type')


if __name__ == '__main__':
    types = ['novel', 'journal', 'newspaper']
    book = SimpleFactory.choice_book(random.choice(types))
    book.content()
    book.read()
    book.note()

