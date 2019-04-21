from contextlib import contextmanager

@contextmanager
def my_open(path, mode):
    f = None
    print("my_open start")
    yield f
    print("my_open end")

with my_open('out.txt', 'w') as f:
    pass
