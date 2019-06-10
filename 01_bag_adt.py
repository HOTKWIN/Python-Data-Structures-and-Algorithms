# 抽象数据类型：ADT，组合已有的数据结构来实现一种新的数据类型
#实现一个Bag ADT

#coding: utf8

class Bag(object):

    def __init__(self,maxsize=10):
        self.maxsize = maxsize
        self._items = list()

    def add(self,item):
        if len(self) >= self.maxsize:
            raise Exception('Full')
        self._items.append(item)

    def remove(self,item):
        self._items.remove(item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item


def test_bag():
    bag = Bag()

    bag.add(1)
    bag.add(2)
    bag.add(3)

    assert len(bag) == 3 #检查条件，不符合就终止程序

    bag.remove(3)
    assert len(bag) == 2

    for i in bag:
        print(i)


if __name__ == '__main__':
    test_bag()
