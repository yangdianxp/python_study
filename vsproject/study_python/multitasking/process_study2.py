import multiprocessing
import time

def worker(num):
    for i in range(5):
        print("worker:{}".format(num))
        time.sleep(1)

def main():
    po = multiprocessing.Pool(3)
    for i in range(0, 10):
        po.apply_async(worker, (i,))
    po.close()
    po.join()

if __name__ == "__main__":
    main()