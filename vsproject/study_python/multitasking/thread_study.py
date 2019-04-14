import time
import threading

g_nums = [11, 22]

def sing(temp):
    print(temp)
    for i in range(5):
        print("...singing...")
        time.sleep(1)

def dance():
    for i in range(5):
        print("...dumping...")
        time.sleep(1) 

def main():
    t1 = threading.Thread(target=sing, args=(g_nums,))
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    #print(threading.enumerate())

if __name__ == "__main__":
    main()