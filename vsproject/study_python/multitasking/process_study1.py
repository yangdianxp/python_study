
import multiprocessing
import time

def test1(queue):
    while True:
        queue.put('111');
        queue.put((1, 2, 3))
        queue.put([100, 200, 300])
        time.sleep(1)

def test2(queue):
    while True:
        print(queue.get())

def main():
    queue = multiprocessing.Queue(3)

    p1 = multiprocessing.Process(target=test1, args=(queue,))
    p2 = multiprocessing.Process(target=test2, args=(queue,))
    p1.start()
    p2.start()

if __name__ == "__main__":
    main()