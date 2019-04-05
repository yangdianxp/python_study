d = dict(a = 100, b = 200)
print(eval("a+b", d))

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
