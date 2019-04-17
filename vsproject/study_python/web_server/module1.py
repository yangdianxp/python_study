import re

def main():
    names = ["age", "_age", "1age", "age1", "a_age", "age_1_", "age!", "a#123", "______"]
    for name in names:
        ret = re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name)
        if ret:
            print("变量名:{} 符合要求 {}".format(name, ret.group()))
        else:
            print("变量名:{} 不符合要求".format(name))

if __name__ == "__main__":
    main()
