import time
import threading

g_num = 100

class MyThread(threading.Thread):
    def run(self):
        print("{}:{}".format(self.name, g_num))
        for i in range(3):
            time.sleep(1)
            msg = "I'm " + self.name + ' @ ' + str(i)
            print(msg)
            print("{}:{}".format(self.name, g_num))

class MyThread1(threading.Thread):
    def __init__(self):
        global g_num
        super().__init__(target = self.my_func, args=(g_num,))
    def my_func(self, temp):
        print("start thread")
        print("{}:{}".format(self.name, temp))
        temp = 200


def main():
    t = MyThread()
    t.start()
    t = MyThread1()
    t.start()

if __name__ == "__main__":
    main()