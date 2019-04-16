from datetime import timedelta, datetime


day = datetime(2018, 1, 2)
sDay = day.strftime('%Y%m%d')
print(sDay)
day = day + timedelta(1)
sDay = day.strftime('%Y%m%d')
print(sDay)


#tmp_str = "("
#for i in range(10):
#    tmp_str += "'" + str(i) + "'" + ", "
#tmp_str = tmp_str.rstrip(", ")
#tmp_str += ")"
#print(tmp_str)
#num = [11, 22]

#def func():
#    num.append([100, 200])
#    #num += [100, 200]

#print(num)
#func()
#print(num)


#import pygame
#pygame.examples

#import os
#print(os.system('dir'))

#def input_password():
#    pwd = input("请输入密码：")
#    if len(pwd) < 8:
#        raise Exception("密码长度不够")
#    return pwd

#while True:
#    try:
#        print(input_password())
#    except Exception as result:
#        print("unknown error:{}".format(result))


#num = 0

#while True:
#    try:
#        num = int(input("请输入一个整数："))

#        result = 8 / num

#        print(result)

#    except ZeroDivisionError:
#        print("除0错误")
#    except ValueError:
#        print("只接受一个数值")
#    except Exception as result:
#        print("未知的错误 ", result)
#    else:
#        print("执行成功")
#    finally:
#        print("总会执行")
#    print("-" * 50)

#except:
#    print("*" * 20)

#print(num)

#class Singleton:
#    __obj = None
#    __init_flag = True

#    def __new__(cls):
#        if cls.__obj == None:
#            cls.__obj = object.__new__(cls)
#        return cls.__obj

#    def __init__(self):
#        if Singleton.__init_flag:
#            print("Singleton init")
#        Singleton.__init_flag = False

#s = Singleton()
#s1 = Singleton()
#print(s)
#print(s1)


#import copy

#class A:
#   def __init__(self, b, c):
#       self.b = b
#       self.c = c

#class B:
#    pass

#class C:
#    pass

#b = B()
#c = C()
#a = A(b, c)

#a1 = a
#print(a, a.b, a.c)
#print(a1, a1.b, a1.c)

#a1 = copy.copy(a)
#print(a, a.b, a.c)
#print(a1, a1.b, a1.c)

#a1 = copy.deepcopy(a)
#print(a, a.b, a.c)
#print(a1, a1.b, a1.c)

#class Man:
#    def eat(self):
#        print("man eat")

#class Chinese(Man):
#    def eat(self):
#        print("Chinese eat")

#class English(Man):
#    def eat(self):
#        print("English eat")

#class Indian(Man):
#    def eat(self):
#        print("Indian eat")

#def man_eat(man):
#    if isinstance(man, Man):
#        man.eat()
#    else:
#        print("is not a man")

#man_eat(Man())
#man_eat(Chinese())
#man_eat(English())
#man_eat(Indian())
#man_eat(str())
#class Person:
#    pass

#class Student(Person):
#    pass

#print(Student.mro())


#class Employee:

#    def __init__(self, name, salary):
#        self.__name = name
#        self.__salary = salary

#    @property
#    def salary(self):
#        return self.__salary

#    @salary.setter
#    def salary(self, salary):
#        if salary < 1000 or salary > 50000:
#            print("input salary is out of range")
#        self.__salary = salary

#    def print(self):
#        print("name:{}, salary:{}".format(self.__name, self.__salary))

#    def __str__(self):
#        return "name:{} salary:{}".format(self.__name, self.__salary)

#class Engineer(Employee):
#    def __init__(self, name, salary, skill):
#        Employee.__init__(self, name, salary)
#        self.__skill = skill

#    @property
#    def skill(self):
#        return self.__skill

#    @property
#    def salary(self):
#        return super().salary + 3000

#    def print(self):
#        Employee.print(self)
#        print("my skill is {}".format(self.__skill))

#    def __str__(self):
#        str = super().__str__()
#        return str + " skill:{}".format(self.__skill)



#eng1 = Engineer("yangdian", 3000, "coding")
#print(eng1.__dict__)
#print(eng1.__class__)
#print(eng1.__dir__)
#print(Engineer.__bases__)
#print(Engineer.mro())
#print(Engineer.__base__)
#print(Employee.__subclasses__())

#print(str(eng1))
#print(eng1.salary)

#eng1.print()
#print(eng1.skill)
#print(eng1.salary)


#emp1 = Employee("yangdian", 3000)
#print(emp1.salary)
#emp1.salary = 30000
#emp1.salary = 80000
#print(emp1.salary)
#emp1.print()

#class Employee:
#    def __init__(self):
#        self.name = "yd"
#        self.__age = 18

#    def __print(self):
#        print("age:{}".format(self.__age))


#e = Employee()
#print(e.name)
#print(e._Employee__age)
#print(e._Employee__print())


#class Student:
#    company = "gaosheng"
#    count = 0

#    def __init__(self, name, score):
#        self.name = name
#        self.score = score
#        Student.count += 1
#        #print(self)
#        #print(id(self))
#        #print(type(self))

#    def say_score(self):
#        print("{}:{}".format(self.name, self.score))

#    def __del__(self):
#        print("delete obj")

#    def __call__(self):
#        return dict(name = self.name, score = self.score)

#    @classmethod
#    def print_company(cls):
#        print("company:{}".format(cls.company))

#    @staticmethod
#    def add(a, b):
#        print("a + b = {}".format(a + b))
    

#Student.print_company()
#Student.add(2, 3)


#s1 = Student("yd", 18)
#s1.say_score()
#print(s1())

#def print_hello(self):
#    print("hello")

#Student.__call__ = print_hello
#print(s1())

#del s1
#Student.say_score(s1)

#s2 = Student("yy", 200)
#s3 = Student("qq", 500)
#print("count:{}".format(Student.count))

#print(dir(s1))
#print(s1.__dict__)
#print(isinstance(s1, Student))

#print(Student)
#print(id(Student))
#print(type(Student))

#print(s1)
#print(id(s1))
#print(type(s1))
#def first():
#    a = 20
#    def second():
#        nonlocal a
#        a = 30
#        def third():
#            nonlocal a
#            a = 40
#        third()
#    second()
#    print(a)

#first()



#a = 10

#def outer():
#    global a
#    b = 10
#    a = 20
#    def inner():
#        global a
#        nonlocal b
#        b = 20
#        a = 40
#    inner()
#    print(b)

#outer()
#print(a)

#d = dict(a = 100, b = 200)
#print(eval("a+b", d))

#a = 10
#b = 20

#print(eval("a+b"))

#g = [lambda a : a + 2, lambda a : a * 2, lambda a : a ** 2]
#print(g[0](3), g[1](3), g[2](3))

#f = lambda a, b, c : a+b+c 
#print(f)
#print(id(f))
#print(type(f))
#print(f(1, 2, 3))

#def func(a, b, *c):
#    print(a, b, c)

#def func1(a, b, **c):
#    print(a, b, c)

#def func2(a, b, *c, **d):
#    print(a, b, c, d)

#func(1, 2, 3, 4, 5, 6)
#func1(1, 2, name="yangdian", age=18)
#func2(1, 2, 3, 4, name="yangdian", age=18)


#import copy

#引用拷贝
#a = [10, 20, [100, 200]]
#b = a
#print("id(a):{}".format(id(a)))
#print("id(b):{}".format(id(b)))
#b.append(30)
#b[2].append(300)
#print(a)
#print(b)

#浅拷贝
#a = [10, 20, [100, 200]]
#b = copy.copy(a)
#print("id(a):{}".format(id(a)))
#print("id(b):{}".format(id(b)))
#b.append(30)
#b[2].append(300)
#print(a)
#print(b)

#深拷贝
#a = [10, 20, [100, 200]]
#b = copy.deepcopy(a)
#print("id(a):{}".format(id(a)))
#print("id(b):{}".format(id(b)))
#b.append(30)
#b[2].append(300)
#print(a)
#print(b)

#import math
#import time
#b = copy.copy(a)
#print(id(a))
#print(id(b))


#def test1():
#    func = math.sqrt
#    time1 = time.time()
#    for i in range(10000000):
#        func(30)
#    time2 = time.time()
#    print(time2 - time1)

#def test2():
#    time1 = time.time()
#    for i in range(10000000):
#        math.sqrt(30)
#    time2 = time.time()
#    print(time2 - time1)

#test1()
#test2()


#def test(x, y, z):
#    print(locals())
#    return [x*10, y*10, z*10]

#print(test(1, 2, 3))
#print(globals())

#def test():
#    '''aaaaaabbbbbbbbbbbb'''
#    print("aaa")

##print(help(test))
#help(test, __doc__)

#print(test)
#print(id(test))
#print(type(test))


#import turtle

#t = turtle.Pen()
#for i in range(1, 200, 10):
#    t.penup()
#    t.goto(0, -i)
#    t.pendown()
#    t.circle(i)


#for i in (x for x in range(1, 10)):
#    print(i)

#cells = [(row, col) for row in range(1, 10) if row % 2 == 0\
#         for col in range(1, 10) if col % 3 == 0]
#print(cells)

#names = ["yang", "dian", "li", "yan"]
#ages = [1, 2, 3, 4]
#jobs = ["laoshi", "cc", "bb"]

#for n, a, j in zip(names, ages, jobs):
#    print("{}, {}, {}".format(n, a, j))

#e = {"a":16, "b":18, "c":20}

#for i in e:
#    print(i, end = " ")
#print()
#for i in e.keys():
#    print(i, end = " ")
#print()
#for i in e.values():
#    print(i, end = " ")

#num = 5
#print(num if num < 10 else 20)
#print(num if num > 10 else 20)

#b = []

#if not b:
#    print(b)

#thisset = set(("Google", "Runoob", "Taobao"))
#thisset.update({1,3})
#print(thisset)
#thisset.update([1,4],[5,6])  
#print(thisset)
#e = {"a":16, "b":18, "c":20}
#thisset.update(e) 
#print(thisset)

#a = {1, 2, 3}
#b = {3, 4, 5}
#d = a.union(b)
#print(d)
#d = a.intersection(b)
#print(d)
#d = a.difference(b)
#print(d)

#k = ["age", "height", "weight"]
#v = [16, 18, 20]
#d = dict(zip(k, v))
#print(d)

#x, y, z = d
#print(x)
#print(y)
#print(z)
#x, y, z = d.values()
#print(x)
#print(y)
#print(z)
#x, y, z = d.items()
#print(x)
#print(y)
#print(z)

#s = """ aaaaaaaaaaaaaaaaa\ 
#aaaaaaaaaaaas"""
#print(s)

#s = "aaaaaaaaaaaaaaaaaaaaaaaaaa\
#    aaaaaaaaaaaaaaaaaaa"
#print(s)

#d = dict.fromkeys(["age", "height", "weight"])
#print(d)

#k = ["age", "height", "weight"]
#v = [16, 18, 20]
#d = dict(zip(k, v))
#print(d)

#e = {"a":16, "b":18, "c":20}

#print(d.update(e))
#print(d)

#for i in e.items():
#    print("{}, {}".format(i[0], i[1]))



#a = (1, 2, 3)
#dict = {}
#dict[a] = "aaaa"

#s = (x * 3 for x in range(5))
#print(s.__next__())
#print(s.__next__())
#print(s.__next__())
#print(s.__next__())
#print(s.__next__())
#try:
#    print(s.__next__())
#except:
#    print("aaa")


#b = [10, 20, 30, 40]
#c = [50, 60, 70, 80]
#d = [100, 200, 300, 400]
#print(list(zip(b, c, d)))

#b = (10, 20, 30, 40)
#c = (50, 60, 70, 80)
#d = (100, 200, 300, 400)
#print(tuple(zip(b, c, d)))

#a = [10, 20, 30, 40]
#b = (10, 20, 30, 40)
#if a == b:
#    print(True)
#c = reversed(a)
#print(c)
#print(id(c))

#from datetime import datetime
#print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

#a = [20, 30]
#print(id(a))
#print(a)
#a.append(50)
#print(id(a))
#print(a)

#print("yang".split("*****"))

#a = list("yang")
#print(a)
#print("aaa".join(a))

#a = list(range(10))
#print(a)

#a = "abc"
#li = ["abc", "a"]
#li1 = ["abc", "a"]
#print("{}, {}".format(id(a), id(li[0])))
#print("{}, {}".format(id(li), id(li1)))

#a = 0b11011011
#b = 0b01100101
#c = a | b
#print(bin(c))

#a = 4 
#print(3 < a < 10)

#import io
#s = "Hello, sxt"
#sio = io.StringIO(s)
#print(sio.getvalue())
#sio.seek(7)
#sio.write("GGGG")
#print(sio.getvalue())


##对齐填充
#a = "{:*>8}".format("245")
#print(a)
#a = "{:*^8}".format("245")
#print(a)
#a = "{:#<8}".format("245")
#print(a)

#a = "我是{name}, 我身高{height}"
#a = a.format(height = 163, name = "杨电")
#print(a)

#a = "aaa_33"
#b = "aaa_33"
##print(a is b)

#a = "_aaa#?.33"
#b = "_aaa#?.33"
##print(a is b)

#a = a.strip("_")
#a = a.rstrip("33")
#print(a)

#import time

#time1 = time.time()
#a = ""
#for i in range(1000000):
#    a += "axt"
#time2 = time.time()
#print("花费时间：" + str(time2 - time1))

#time3 = time.time()
#li = []
#for i in range(1000000):
#    li.append("axt")
#a = "".join(li)
#time4 = time.time()
#print("花费时间：" + str(time4 - time3))


#strings = ["hao", "ba", "xi"]
#a = "*".join(strings)
#print(a)

#a = "abcdefg"
#print(a[1:])
#print(a[1:5])
#print(a[1:5:2])
#print(a[-3:])
#print(a[-6:-3])
#print(a[::-1])

#a = "acbcdc"
#a = a.replace("c", "杨")
#print(a)


#a = "中国人民"
#a = a.replace("中国", "哈哈")
#print(a)

#print(str(3.14e30))

#my_name = input("请输入姓名：")
#print(my_name)


#print("aaa", end = "")
#print("bbb", end = "*")
#print("ccc")
#print("ddd")

#a = "aaa""bbb" 'ccc'
#a *= 3
#print(a)

#print(ord('A'))
#print(ord('杨'))
#print(chr(67))

#x = y = -1000
#z = -1000
#print(id(x))
#print(id(y))
#print(id(z))


#a = 1000
#b = 1000
#print(id(a))
#print(id(b))
#print(a == b)
#print(a is b)

#a = True
#b = False
#print(b or 30)

#import turtle
#import math

##定义多个点的坐标
#x1, y1 = 100, 100
#x2, y2 = 100, -100
#x3, y3 = -100, -100
#x4, y4 = -100, 100
#turtle.penup()
#turtle.goto(x1, y1)
#turtle.pendown()
#turtle.goto(x2, y2)
#turtle.goto(x3, y3)
#turtle.goto(x4, y4)
#distance = math.sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2)
#turtle.write(distance)



#import time

#print(time.time())

#a = 2
#a **= 10
#print(a)

#print(round(3.5))
#print(round(3.4599999999999999))

#print(id(5))
#print(id(0b101))
#print(id(0o5))
#print(id(0x5))

#print(divmod(13, 3))


#a = "我爱你"
#print(id(a))
#print(id("我爱你"))

#a = 5
#c = 5
#print(id(4))
#print(id(5))
#print(id(a))
#print(id(c))
#print(type(5))
#print(type(a))

#import turtle
#t = turtle.Pen()
#for x in range(360):
#    t.forward(x)
#    t.left(59)
