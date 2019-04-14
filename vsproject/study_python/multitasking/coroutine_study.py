from collections import Iterable
from collections import Iterator
import time

class Classmate():
    def __init__(self):
        self.names = list()
    def add(self, name):
        self.names.append(name)
    def __iter__(self):
        return ClassIterator(self)

class ClassIterator(object):
    def __init__(self, obj):
        self.obj = obj
    def __iter__(self):
        pass
    def __next__(self):
        return self.obj.names[0]

def main():
    print(isinstance(5, Iterable))
    print(isinstance([1, 2, 3], Iterable))
    print(isinstance((1, 2, 3), Iterable))
    print(isinstance(range(5), Iterable))
    classmate = Classmate()
    classmate.add("aaa")
    classmate.add("bbb")
    classmate.add("ddd")
    print("判断classmate是否是可以迭代的对象:", isinstance(classmate, Iterable))
    classmate_iterator = iter(classmate)
    print("判断classmate_iterator是否是迭代器:", isinstance(classmate_iterator, Iterator))
    print(next(classmate_iterator))
    for c in classmate:
        print(c)
        time.sleep(1)

if __name__ == "__main__":
    main()