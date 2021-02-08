#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""抽象工厂"""


# 阅读
class IReadAction(object):
    def read(self):
        raise NotImplementedError


class SpeedReadAction(IReadAction):
    def read(self):
        print("速读")


class IntensiveReadAction(IReadAction):
    def read(self):
        print('精读')


# 笔记
class INoteAction(object):
    def note(self):
        raise NotImplementedError


class FullNoteAction(INoteAction):
    def note(self):
        print("详细笔记")


class NoneNoteAction(INoteAction):
    def note(self):
        print("不做笔记")


class ActionFactory(object):

    def read_action(self):
        raise NotImplementedError

    def note_action(self):
        raise NotImplementedError


class FatherNovelActionFactory(ActionFactory):
    def read_action(self):
        IntensiveReadAction().read()

    def note_action(self):
        FullNoteAction().note()


class FatherJournalActionFactory(ActionFactory):
    def read_action(self):
        SpeedReadAction().read()

    def note_action(self):
        NoneNoteAction().note()


class MotherAndSonActionFactory(ActionFactory):
    def read_action(self):
        SpeedReadAction().read()

    def note_action(self):
        NoneNoteAction().note()


class IBook(object):

    def __init__(self, action_factory):
        self.action_factory = action_factory

    def content(self):
        raise NotImplementedError

    def read(self):
        self.action_factory.read_action()

    def note(self):
        self.action_factory.note_action()


class FatherNovel(IBook):
    def content(self):
        print("这是本推理小说")


class FatherJournal(IBook):
    def content(self):
        print("这是本财经杂志")


class SonNovel(IBook):
    def content(self):
        print("这是本童话书")


class SonJournal(IBook):
    def content(self):
        print("这是本儿童杂志")


class MotherNovel(IBook):
    def content(self):
        print("这是本爱情小说")


class MotherJournal(IBook):
    def content(self):
        print("这是本时尚杂志")


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
            return FatherNovel(FatherNovelActionFactory())
        elif _type == 'journal':
            return FatherJournal(FatherJournalActionFactory())
        else:
            raise ValueError('Father: unknown book type')


class MotherRead(Reader):
    def choice_book(self, _type):
        if _type == 'novel':
            return MotherNovel(MotherAndSonActionFactory())
        elif _type == 'journal':
            return MotherJournal(MotherAndSonActionFactory())
        else:
            raise ValueError('Mother: unknown book type')


class SonRead(Reader):
    def choice_book(self, _type):
        if _type == 'novel':
            return SonNovel(MotherAndSonActionFactory())
        elif _type == 'journal':
            return SonJournal(MotherAndSonActionFactory())
        else:
            raise ValueError('Son: unknown book type')


def main():
    print("家庭阅读日...")
    father = FatherRead()
    mother = MotherRead()
    son = SonRead()

    print('-' * 5, '爸爸', '-' * 5)
    father.read('novel')
    print('-' * 5)
    father.read('journal')
    print('-' * 5, '妈妈', '-' * 5)
    mother.read('novel')
    print('-' * 5, '儿子', '-' * 5)
    son.read('novel')


if __name__ == '__main__':
    main()
