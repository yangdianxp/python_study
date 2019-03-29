f1 = open('test.txt','w')
for i in range(0x2435acd30000, 0x2435acd31000):
    f1.write(str(hex(i)).replace("0x", "").upper() + "\n")
f1.close()
