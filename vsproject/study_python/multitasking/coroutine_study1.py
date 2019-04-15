
def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        #print(a)
        yield a  
        a, b = b, a + b
        current_num += 1
    return "yangdian"

def create_num2(all_num):
    for i in range(all_num):
        ret = yield i
        print(">>>>>ret>>>>>", ret)

#obj = create_num(10)
#print(obj)

#ret = next(obj)
#print(ret)

#obj2 = create_num(100)

#while True:
#    try:
#        ret = next(obj2)
#        print(ret)
#    except Exception as ret:
#        print(ret.value)
#        break

obj3 = create_num2(100)
ret = obj3.send(None)
print(ret)
ret = obj3.send("yangdian")
print(ret)

#for i in obj:
#    print(i)
