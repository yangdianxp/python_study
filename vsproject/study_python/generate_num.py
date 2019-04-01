f1 = open('mac.txt','w')
num = 0x001829BA0210
for i in [num + x for x in range(5000)]:
    f1.write("00" + str(hex(i)).replace("0x", "").upper() + "\n")
f1.close()
