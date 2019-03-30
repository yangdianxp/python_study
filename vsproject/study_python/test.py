a = [20, 30]
print(id(a))
print(a)
a.append(50)
print(id(a))
print(a)

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
