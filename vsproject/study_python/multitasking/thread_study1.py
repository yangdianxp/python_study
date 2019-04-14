import time
import threading

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self):
        print("my name is {}".format(self.name))

def main():
    p = Person("yd", "man")
    t1 = threading.Thread(target=p)
    t1.start()

if __name__ == "__main__":
    main()