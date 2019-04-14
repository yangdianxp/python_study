
def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        #print(a)
        yield a  
        a, b = b, a + b
        current_num += 1

obj = create_num(10)
print(obj)

ret = next(obj)
print(ret)

#for i in obj:
#    print(i)
