import sys
import time
import json
import requests
import json
from datetime import datetime
from threading import Thread

tbname="btc"
auth_name="tom_first_bitcoin"
auth_pass="tom123_first_bitcoin"
rpcip="http://172.18.171.102:8301"

def get_addr_txs(addr):
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({"jsonrpc": "2.0", "method":"listtransactions", "params": [addr], "id":"1"})
    auth = (auth_name, auth_pass)
    url = rpcip
    r = requests.post(url, data=data, auth=auth, headers=headers, timeout=20)
    txs = r.json()["result"]
    return txs

txs = get_addr_txs("379GSpV2UTi8nY6Gh5VECiL1dcbZ381hzj")
print(txs)


#import requests

#def test():
#    for i in range(5):
#        yield i

#for i in test():
#    print(i)

#a = "{:^6d} {:^6d} {:^6d}".format(123, 456, 789)
#print(a)

#print("Sammy ate {0:f} percent of a {1}!".format(75, "pizza"))

#name = "Eric"
#age = 74
#str = F"Hello, {name}. You are {age}."
#print(str)

#def change_value(a):
#    a = 10

#def change_list(l):
#    l.append(10)

#def change_dict(d):
#    d[10] = 10


#a = 1
#change_value(a)
#print(a)

#test_list = []
#change_list(test_list)
#print(test_list)

#test_dict = {}
#change_dict(test_dict)
#print(test_dict)


#url = "https://free.currconv.com/api/v7/convert?q=USD_PHP&compact=ultra&apiKey=dc20570ebb92caad486c"
#r = requests.get(url, timeout=10)
#print(r)


#def application(env, start_response):
#    start_response('200 OK', [('Content-Type','text/html')])
#    return "Hello World"


#test_dict = {"a":1, "b":2}
##print(test_dict)
##for name, value in test_dict.items():
##    print(name, value)

##for name in test_dict.keys():
##    print(name)

##for value in test_dict.values():
##    print(value)

#keys = [str(i) for i in test_dict.keys()]
#values = [str(i) for i in test_dict.values()]
#sql = """insert into my_table ({}) values ({})""".format(','.join(keys), ','.join(values))
#print(sql)

#class ModelMetaclass(type):
#    def __new__(cls, name, bases, attrs):
#        mappings = dict()
#        for k, v in attrs.items():
#            if isinstance(v, tuple):
#                print('Found mapping:{} ====> {}'.format(k, v))
#                mappings[k] = v

#        for k in mappings.keys():
#            attrs.pop(k)

#        attrs['__mappings__'] = mappings
#        print(mappings)
#        attrs['__table__'] = name
#        print(name)
#        return type.__new__(cls, name, bases, attrs)

#class User(metaclass=ModelMetaclass):
#    uid = ('uid', 'int unsigned')
#    name = ('username', "varchar(30)")
#    email = ('email', "varchar(30)")
#    password = ('password', "varchar(30)")

#    def __init__(self, **kwargs):
#        for name, value in kwargs.items():
#            setattr(self, name, value)

#    def save(self):
#        fields = []
#        args = []
#        for k, v in self.__mappings__.items():
#            fields.append(v[0])
#            args.append(getattr(self, k, None))

#            sql = 'insert into %s (%s) values(%s)' % (self.__table__, ','.join(fields), ','.join([str(i) for i in args]))
#            print('SQL: %s' % sql)

#u = User(uid=12345, name='Michael', email='test@orm.org', password='my-pwd')
#u.save()

#test_dict = {"a":1, "b":2}
#print(test_dict)
#for name, value in test_dict.items():
#    print(name, value)

#元类
##Test = type("Test", (), {"num":100, "num2":200})
##print(help(Test))
##Test1 = type("Test1", (Test, ), {"aaa":500})
##print(help(Test1))

##实例方法
#def test(self):
#    print("实例方法...")

##Test3 = type("Test3", (), {"test":test})
##t = Test3()
##t.test()

##类方法
#@classmethod
#def test_3(cls):
#    print("----这是类方法----")

##Test4 = type("Test4", (), {"test":test, "test_3":test_3})
##print(help(Test4))

##静态方法
#@staticmethod
#def test_4():
#    print("----这是静态方法----")

#Test5 = type("Test5", (), {"test":test, "test_3":test_3, "test_4":test_4})
#print(help(Test5))



#日志
#import logging
#logger = logging.getLogger()
#logger.setLevel(logging.INFO) # Log等级总开关

#logfile = './log.txt'
#fh = logging.FileHandler(logfile, mode='a')
#fh.setLevel(logging.DEBUG)

#ch = logging.StreamHandler()
#ch.setLevel(logging.WARNING)

#formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s')
#fh.setFormatter(formatter)
#ch.setFormatter(formatter)

#logger.addHandler(fh)
#logger.addHandler(ch)

#logging.info('这是 logging info message')
#logging.debug('这是 logging debug message')
#logging.warning('这是 logging warning message')
#logging.error('这是 logging error message')
#logging.critical('这是 logging critical message')


#logging.basicConfig(level=logging.DEBUG,
#                    filename='./log.txt',
#                    filemode='w',
#                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s')

#logging.info('这是 logging info message')
#logging.debug('这是 logging debug message')
#logging.warning('这是 logging warning message')
#logging.error('这是 logging error message')
#logging.critical('这是 logging critical message')


#给装饰器传参数
#def set_level(level_num):
#    print("level_num:", level_num)
#    def set_func(func):
#        def call_func(*args, **kwargs):
#            if level_num == 1:
#                print("11111111111111")
#            elif level_num == 2:
#                print("22222222222222")
#            return func(*args, **kwargs)
#        return call_func
#    return set_func

#@set_level(1)
#def test1():
#    print("-------test1---------")

#@set_level(2)
#def test2():
#    print("-------test2---------")

#test1()
#test2()


##任意思参数的装饰器
#def set_func(func):
#    print("---开始进行装饰")
#    def call_func(*args, **kwargs):
#        print("11111111111")
#        print("22222222222")
#        func(*args, **kwargs)
#    return call_func

#@set_func
#def test1(num, *args, **kwargs):
#    print("-------test1---------{}".format(num))
#    print("-------test2---------{}", args)
#    print("-------test2---------{}", kwargs)

#test1(100)
#test1(100, 200)
#test1(100, 200, 300, mm = 100)

##装饰器演示
#def set_func(func):
#    def call_func():
#        print("11111111111")
#        print("22222222222")
#        func()
#    return call_func

#@set_func
#def test1():
#    print("-------test1----------")

#test1()

#foo = lambda x: x + 1
#print((lambda x: x + 1)(2))

#x = 300
#def test1():
#    x = 200
#    def test2():
#        nonlocal x
#        print("===>", x)
#        x = 100
#        print("===>", x)
#    return test2

#test2_obj = test1()
#test2_obj()


#闭包
#def line(k, b):
#    def create_y(x):
#        print(k * x + b)
#    return create_y

#line_obj = line(1, 2)
#line_obj(0)
#line_obj(1)
#line_obj(2)

#from datetime import timedelta, datetime
#import sys

#test_list = [[1, 2], [3, 4], [5, 6]]
#for i, j in test_list:
#    print(i, j)

#try:
#    a = test_list[4]
#    print(a)
#except Exception as result:
#    info = sys.exc_info()[2].tb_frame.f_back
#    temp = "filename:{}\nlines:{}\terror:{}"
#    print(temp.format(info.f_code.co_filename, info.f_lineno, result))

#day = datetime(2018, 1, 2)
#sDay = day.strftime('%Y%m%d')
#print(sDay)
#day = day + timedelta(1)
#sDay = day.strftime('%Y%m%d')
#print(sDay)


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
