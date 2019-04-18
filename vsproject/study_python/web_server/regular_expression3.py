import re

def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)

ret = re.sub(r'\d+', add, "python = 997")
print(ret)

ret = re.sub(r'\d+', add, "python = 99")
print(ret)
