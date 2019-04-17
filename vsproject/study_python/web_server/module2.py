import re

def test():
    html_str = "<h1>aaaaaa</h1>"
    re.match(r"^<(\w*)><(\w*)>.*</\2></\1>", email)
    

def main():
    while True:
        email = input("请输入一个邮箱地址：")
        #. ? 等，仅需要在前面添加一个反斜杠
        ret = re.match(r"(^[a-zA-Z_0-9]{4,20})@(163|126)\.com$", email)
        if ret:
            print("{}符合要求。。。{}".format(email, ret.group(1)))
        else:
            print("{}不符合要求。。。".format(email))

if __name__ == "__main__":
    main()