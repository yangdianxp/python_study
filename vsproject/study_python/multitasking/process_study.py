import multiprocessing
import time

def test1(num):
    while True:
        print("test1....")
        time.sleep(1)

def test2(num):
    while True:
        print("test2...")
        time.sleep(1)

def main():
    p1 = multiprocessing.Process(target=test1, args=(100000,))
    p2 = multiprocessing.Process(target=test2, args=(100000,))
    p1.start()
    p2.start()

if __name__ == "__main__":
    main()