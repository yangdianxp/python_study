# 例


#import shutil
#shutil.unpack_archive('Python-3.3.0.tgz')
#shutil.make_archive('py33','zip','Python-3.3.0')
## 获取所有支持的归档格式列表
#shutil.get_archive_formats()

## 拷贝目录的处理方式
#try:
#    shutil.copytree(src, dst)
#except shutil.Error as e:
#    for src, dst, msg in e.args[0]:
#        # src is source name
#        # dst is destination name
#        # msg is error message from exception
#        print(dst, src, msg)

#filename = '/Users/guido/programs/spam.py'
#import os.path
#print(os.path.basename(filename))
#print(os.path.dirname(filename))
#print(os.path.split(filename))
#print(os.path.join('/new/dir', os.path.basename(filename)))
#print(os.path.expanduser('~/guido/programs/spam.py'))

#import shutil
## Copy src to dst. (cp src dst)
#shutil.copy(src, dst)
## Copy files, but preserve metadata (cp -p src dst)
#shutil.copy2(src, dst)
## Copy directory tree (cp -R src dst)
#shutil.copytree(src, dst)
## Move src to dst (mv src dst)
#shutil.move(src, dst)

## 复制过程中，忽略某些文件
#def ignore_pyc_files(dirname, filenames):
#    return [name in filenames if name.endswith('.pyc')]
#shutil.copytree(src, dst, ignore=ignore_pyc_files)

#import os.path
#def read_into_buffer(filename):
#    buf = bytearray(os.path.getsize(filename))
#    with open(filename, 'rb') as f:
#        f.readinto(buf)
#    return buf

## Write a sample file
#with open('sample.bin', 'wb') as f:
#    f.write(b'Hello World')

#buf = read_into_buffer('sample.bin')
#print(buf)
#buf[0:5] = b'Hallo'
#print(buf)
#with open('newsample.bin', 'wb') as f:
#    f.write(buf)

#from functools import partial
#RECORD_SIZE = 32
#with open('somefile.data', 'rb') as f:
#    records = iter(partial(f.read, RECORD_SIZE), b'')
#    for r in records:
#        pass

## gzip compression
#import gzip
#with gzip.open('somefile.gz', 'rt') as f:
#    text = f.read()

## bz2 compression
#import bz2
#with bz2.open('somefile.bz2', 'rt') as f:
#    text = f.read()

## gzip compression
#import gzip
#with gzip.open('somefile.gz', 'wt') as f:
#    f.write(text)

## bz2 compression
#import bz2
#with bz2.open('somefile.bz2', 'wt') as f:
#    f.write(text)
## 当写入压缩数据时，可以使用 compresslevel 这个可选的关键字参数来指定一个压缩级别
#with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
#    f.write(text)
## 可以作用在一个已存在并以二进制模式打开的文件上
## 这样就允许 gzip 和 bz2 模块可以工作在许多类文件对象上，比如套接字，
## 管道和内存中文件等。
#import gzip
#f = open('somefile.gz', 'rb')
#with gzip.open(f, 'rt') as g:
#    text = g.read()

#import io
#s = io.StringIO()
#s.write('Hello World\n')
#print('This is a test', file=s)
#print(s.getvalue())
#s = io.StringIO('Hello\nWorld\n')
#print(s.read(4))
#print(s.read())
## io.StringIO 只能用于文本   io.BytesIO操作二进制数据
#s = io.BytesIO()
#s.write(b'binary data')
#print(s.getvalue())

#with open('somefile', 'xt') as f:
#    f.write('Hello\n')
#import os
#if not os.path.exists('somefile'):
#    with open('somefile', 'wt') as f:
#        f.write('Hello\n')
#else:
#    print('File already exists!')

#print('ACME', 50, 91.5)
#print('ACME', 50, 91.5, sep=',')
#print('ACME', 50, 91.5, sep=',', end='!!\n')
#for i in range(5):
#    print(i, end=' ')
#row = ('ACME', 50, 91.5)
#print(*row, sep=',')

# iter 函数接受一个可选的 callable 对象和一个标记 (结尾) 值作为输入参数。
# 当以这种方式使用的时候，它会创建一个迭代器，这个迭代器会不断调用 callable 
# 对象直到返回值和标记值相等为止。
#import sys
#f = open('/etc/passwd')
#for chunk in iter(lambda: f.read(10), ''):
#    n = sys.stdout.write(chunk)

#import heapq
#a = [1, 4, 7, 10]
#b = [2, 5, 6, 11]
#for c in heapq.merge(a, b):
#    print(c)

#from collections import Iterable
#def flatten(items, ignore_types=(str, bytes)):
#    for x in items:
#        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
#            yield from flatten(x)
#        else:
#            yield x
#items = [1, 2, [3, 4, [5, 6], 7], 8]
## Produces 1 2 3 4 5 6 7 8
#for x in flatten(items):
#    print(x)

#items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
#for x in flatten(items):
#    print(x)

#import os
#import fnmatch
#import gzip
#import bz2
#import re

#def gen_find(filepat, top):
#    '''
#    Find all filenames in a directory tree that match a shell wildcard pattern
#    '''
#    for path, dirlist, filelist in os.walk(top):
#        for name in fnmatch.filter(filelist, filepat):
#            yield os.path.join(path,name)

#def gen_opener(filenames):
#    '''
#    Open a sequence of filenames one at a time producing a file object.
#    The file is closed immediately when proceeding to the next iteration.
#    '''
#    for filename in filenames:
#        if filename.endswith('.gz'):
#            f = gzip.open(filename, 'rt')
#        elif filename.endswith('.bz2'):
#            f = bz2.open(filename, 'rt')
#        else:
#            f = open(filename, 'rt', encoding='UTF-8')
#        yield f
#        f.close()

#def gen_concatenate(iterators):
#    '''
#    Chain a sequence of iterators together into a single sequence.
#    '''
#    for it in iterators:
#        yield from it

#def gen_grep(pattern, lines):
#    '''
#    Look for a regex pattern in a sequence of lines
#    '''
#    pat = re.compile(pattern)
#    for line in lines:
#        if pat.search(line):
#            yield line

#lognames = gen_find('*.cpp', r'E:\code\master\huibase\branches\v3s2\src')
#files = gen_opener(lognames)
#lines = gen_concatenate(files)
#pylines = gen_grep('HCIp4Addr', lines)
#for line in pylines:
#    print(line)

#from itertools import chain
#a = [1, 2, 3, 4]
#b = ['x', 'y', 'z']
#for x in chain(a, b):
#    print(x)

#  zip() 会创建一个迭代器来作为结果返回
#headers = ['name', 'shares', 'price']
#values = ['ACME', 100, 490.1]
#s = dict(zip(headers,values))
#print(s)
#for name, val in zip(headers, values):
#    print(name, '=', val)
#a = [1, 2, 3]
#b = [10, 11, 12]
#c = ['x','y','z']
#for i in zip(a, b, c):
#    print(i)

#xpts = [1, 5, 4, 2, 10, 7]
#ypts = [101, 78, 37, 15, 62, 99]
#for x, y in zip(xpts, ypts):
#    print(x,y)

#a = [1, 2, 3]
#b = ['w', 'x', 'y', 'z']
#for i in zip(a,b):
#    print(i)
#from itertools import zip_longest
#for i in zip_longest(a,b):
#    print(i)
#for i in zip_longest(a, b, fillvalue=0):
#    print(i)

#my_list = ['a', 'b', 'c']
#for idx, val in enumerate(my_list):
#    print(idx, val)

#my_list = ['a', 'b', 'c']
#for idx, val in enumerate(my_list, 1):
#    print(idx, val)

#data = [ (1, 2), (3, 4), (5, 6), (7, 8) ]
## Correct!
#for n, (x, y) in enumerate(data):
#    print(n, x, y)

#items = ['a', 'b', 'c']
#from itertools import permutations
#for p in permutations(items):
#    print(p)

#for p in permutations(items, 2):
#    print(p)

#from itertools import combinations
#for c in combinations(items, 3):
#    print(c)

#for c in combinations(items, 2):
#    print(c)

#for c in combinations(items, 1):
#    print(c)

#from itertools import islice
#items = ['a', 'b', 'c', 1, 4, 10, 15]
#for x in islice(items, 3, None):
#    print(x)

#with open('/etc/passwd') as f:
#    for line in f:
#        print(line, end='')

#from itertools import dropwhile
#with open('/etc/passwd') as f:
#    for line in dropwhile(lambda line: line.startswith('#'), f):
#        print(line, end='')

#def count(n):
#    while True:
#        yield n
#        n += 1

#c = count(0)
#import itertools
#for x in itertools.islice(c, 10, 20):
#    print(x)

#from collections import deque
#class linehistory:
#    def __init__(self, lines, histlen=3):
#        self.lines = lines
#        self.history = deque(maxlen=histlen)
#    def __iter__(self):
#        for lineno, line in enumerate(self.lines, 1):
#            self.history.append((lineno, line))
#            yield line
#    def clear(self):
#        self.history.clear()

#with open('somefile.txt') as f:
#    lines = linehistory(f)
#    for line in lines:
#        if 'python' in line:
#            for lineno, hline in lines.history:
#                print('{}:{}'.format(lineno, hline), end='')

#class Countdown:
#    def __init__(self, start):
#        self.start = start
#    # Forward iterator
#    def __iter__(self):
#        n = self.start
#        while n > 0:
#            yield n
#            n -= 1
#    # Reverse iterator
#    def __reversed__(self):
#        n = 1
#        while n <= self.start:
#            yield n
#            n += 1
#for rr in reversed(Countdown(30)):
#    print(rr)

#for rr in Countdown(30):
#    print(rr)

#a = [1, 2, 3, 4]
#for x in reversed(a):
#    print(x)

#class Node:
#    def __init__(self, value):
#        self._value = value
#        self._children = []
#    def __repr__(self):
#        return 'Node({!r})'.format(self._value)
#    def add_child(self, node):
#        self._children.append(node)
#    def __iter__(self):
#        return iter(self._children)
#    def depth_first(self):
#        yield self
#        for c in self:
#            yield from c.depth_first()

## Example
#if __name__ == '__main__':
#    root = Node(0)
#    child1 = Node(1)
#    child2 = Node(2)
#    root.add_child(child1)
#    root.add_child(child2)
#    child1.add_child(Node(3))
#    child1.add_child(Node(4))
#    child2.add_child(Node(5))
#    for ch in root.depth_first():
#        print(ch)
#    # Outputs Node(0), Node(1), Node(3), Node(4), Node(2), Node(5)

#def frange(start, stop, increment):
#    x = start
#    while x < stop:
#        yield x
#        x += increment

#for n in frange(0, 4, 0.5):
#    print(n)

#class Node:
#    def __init__(self, value):
#        self._value = value
#        self._children = []
#    def __repr__(self):
#        return 'Node({!r})'.format(self._value)
#    def add_child(self, node):
#        self._children.append(node)
#    def __iter__(self):
#        return iter(self._children)

## Example
#if __name__ == '__main__':
#    root = Node(0)
#    child1 = Node(1)
#    child2 = Node(2)
#    root.add_child(child1)
#    root.add_child(child2)
#    # Outputs Node(1), Node(2)
#    for ch in root:
#        print(ch)

#def manual_iter():
#    with open('/etc/passwd') as f:
#        try:
#            while True:
#            line = next(f)
#            print(line, end='')
#        except StopIteration:
#            pass

#from datetime import datetime
#text = '2012-09-20'
#y = datetime.strptime(text, '%Y-%m-%d')
#z = datetime.now()
#diff = z - y
#print(diff)
#nice_z = datetime.strftime(z, '%A %B %d, %Y')
#print(nice_z)

#from datetime import timedelta
#from datetime import datetime
#a = datetime(2012, 9, 23)
#print(a + timedelta(days=10))
#b = datetime(2012, 12, 21)
#d = b - a
#print(d)
#print(d.days)
#now = datetime.today()
#print(now)
#print(now + timedelta(minutes=10))

#from datetime import timedelta
#a = timedelta(days=2, hours=6)
#b = timedelta(hours=4.5)
#c = a + b
#print(c.days)
#print(c.seconds)
#print(c.seconds / 3600)
#print(c.total_seconds() / 3600)

#import random
#values = [1, 2, 3, 4, 5, 6]
#print(random.choice(values))
#random.shuffle(values)
#print(values)
## 生成随机整数
#print(random.randint(0,10))
#print(random.randint(0,10))
## 生成 0 到 1 范围内均匀分布的浮点数
#print(random.random())
#print(random.random())

#import numpy as np
#a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
#print(a)
## Select row 1
#print(a[1])
## Select column 1
#print(a[:,1])
## Select a subregion and change it
#print(a[1:3, 1:3])
#a[1:3, 1:3] += 10
#print(a)
## Broadcast a row vector across an operation on all rows
#print(a + [100, 101, 102, 103])
## Conditional assignment on an array
#print(np.where(a < 10, a, 10))

## Numpy arrays
#import numpy as np
#ax = np.array([1, 2, 3, 4])
#ay = np.array([5, 6, 7, 8])
#print(ax * 2)
#print(ax + 10)
#print(ax + ay)
#print(ax * ay)
#def f(x):
#    return 3*x**2 - 2*x + 7

#print(f(ax))

## 字节顺序规则(little或big)仅仅指定了构建整数时的字节的低位高位排列方式
#data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
#len(data)
#print(int.from_bytes(data, 'little'))
#print(int.from_bytes(data, 'big'))
#x = 0x010203040506
#print(x.to_bytes(6, 'big'))
#print(x.to_bytes(6, 'little'))


#x = 1234
#print(bin(x))
#print(oct(x))
#print(hex(x))
#print(format(x, 'b'))
#print(format(x, 'o'))
#print(format(x, 'x'))
#x = -1234
#print(format(x, 'b'))
#print(format(x, 'x'))
#int('4d2', 16)
#int('10011010010', 2)
## 八进制的特殊情况
#os.chmod('script.py', 0o755)

#x = 1234.56789
## Two decimal places of accuracy
#print(format(x, '0.2f'))
## Right justified in 10 chars, one-digit accuracy
#print(format(x, '>10.1f'))
## Left justified
#print(format(x, '<10.1f'))
## Centered
#print(format(x, '^10.1f'))
## Inclusion of thousands separator
#print(format(x, ','))
#print(format(x, '0,.1f'))
#print(format(x, 'e'))
#print(format(x, '0.2E'))
#print('The value is {:0,.2f}'.format(x))

#from decimal import Decimal
#a = Decimal('4.2')
#b = Decimal('2.1')
#print(a + b)
#print((a + b) == Decimal('6.3'))

#print(round(1.23, 1))
#print(round(1.27, 1))
#print(round(-1.27, 1))
#print(round(1.25361,3))
#a = 1627731
#print(round(a, -1))
#print(round(a, -2))
#print(round(a, -3))

#class safesub(dict):
#    """ 防止 key 找不到 """
#    def __missing__(self, key):
#        return '{' + key + '}'

#import sys
#def sub(text):
#    return text.format_map(safesub(sys._getframe(1).f_locals))
#name = 'Guido'
#n = 37
#print(sub('Hello {name}'))
#print(sub('You have {n} messages.'))
#print(sub('Your favorite color is {color}'))


#parts = ['Is', 'Chicago', 'Not', 'Chicago?']
#print(' '.join(parts))
#print(','.join(parts))
#print(''.join(parts))
#a = 'Hello' 'World'
#print(a)
#data = ['ACME', 50, 91.1]
#print(','.join(str(d) for d in data))
#a = 1
#b = 2
#c = 3
#print(a, b, c, sep=':')


#text = 'Hello World'
#print(format(text, '>20'))
#print(format(text, '<20'))
#print(format(text, '^20'))
#print(format(text, '=>20s'))
#print(format(text, '*^20s'))
#print('{:>10s} {:>10s}'.format('Hello', 'World'))
#x = 1.2345
#print(format(x, '>10'))
#print(format(x, '^10.2f'))

#print(text.ljust(20))
#print(text.rjust(20))
#print(text.center(20))
#print(text.rjust(20,'='))
#print(text.center(20,'*'))


#s = ' hello       world \n'
#s = s.strip()
#print(s)
#import re
#print(re.sub('\s+', ' ', s))

#with open(filename) as f:
#    lines = (line.strip() for line in f)
#    for line in lines:
#        print(line)

## Whitespace stripping
#s = ' hello world \n'
#print(s.strip())
#print(s.lstrip())
#print(s.rstrip())

## Character stripping
#t = '-----hello====='
#print(t.lstrip('-'))
#print(t.strip('-='))


#s1 = 'Spicy Jalape\u00f1o'
#s2 = 'Spicy Jalapen\u0303o'
#print(s1)
#print(s2)
#import unicodedata
#t1 = unicodedata.normalize('NFC', s1)
#t2 = unicodedata.normalize('NFC', s2)
#print(t1 == t2)

#import re
#text2 = '''/* this is a
#multiline comment */
#'''
#comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
#print(comment.findall(text2))

# todo
#def matchcase(word):
#    def replace(m):
#        text = m.group()
#        if text.isupper():
#            return word.upper()
#        elif text.islower():
#            return word.lower()
#        elif text[0].isupper():
#            return word.capitalize()
#        else:
#            return word
#    return replace

#import re
#text = 'UPPER PYTHON, lower python, Mixed Python'
#test_change = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
#print(test_change)

#text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
#from calendar import month_abbr
#def change_date(m):
#    mon_name = month_abbr[int(m.group(1))]
#    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

#import re
#datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
#print(datepat.sub(change_date, text))
#newtext, n = datepat.subn(r'\3-\1-\2', text)
#print(newtext, n)

#import re
#text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
#datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
#print(datepat.sub(r'\3-\1-\2', text))

#text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
#import re
#print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

## 例
#text = 'yeah, but no, but yeah, but no, but yeah'
#print(text.replace('yeah', 'yep'))

## 例
#text = 'yeah, but no, but yeah, but no, but yeah'
## Exact match
#print(text == 'yeah')
## Match at start or end
#print(text.startswith('yeah'))
#print(text.endswith('no'))
## Search for the location of the first occurrence
#print(text.find('no'))

## 例
#text1 = '11/27/2012'
#text2 = 'Nov 27, 2012'
#import re
## Simple matching: \d+ means match one or more digits
#if re.match(r'\d+/\d+/\d+', text1):
#    print('yes')
#else:
#    print('no')

#if re.match(r'\d+/\d+/\d+', text2):
#    print('yes')
#else:
#    print('no')

## 例
#datepat = re.compile(r'\d+/\d+/\d+')
#if datepat.match(text1):
#    print('yes')
#else:
#    print('no')

#if datepat.match(text2):
#    print('yes')
#else:
#    print('no')

## 例
#text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
#print(datepat.findall(text))

## 例
#datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
#m = datepat.match('11/27/2012')
## Extract the contents of each group
#print(m.group(0))
#print(m.group(1))
#print(m.group(3))
#print(m.groups())
#month, day, year = m.groups()
#print(month, day, year)

## Find all matches (notice splitting into tuples)
#print(text)
#datepat.findall(text)
#for month, day, year in datepat.findall(text):
#    print('{}-{}-{}'.format(year, month, day))


#from fnmatch import fnmatch, fnmatchcase
## fnmatch  使用操作系统的模式匹配， fnmatchcase使用程序的模式来匹配（主要是大小写敏感）
#print(fnmatch('foo.txt', '*.txt'))
#print(fnmatch('foo.txt', '?oo.txt'))
#print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
#names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
#print([name for name in names if fnmatch(name, 'Dat*.csv')])

#addresses = [
#    '5412 N CLARK ST',
#    '1060 W ADDISON ST',
#    '1039 W GRANVILLE AVE',
#    '2122 N CLARK ST',
#    '4802 N BROADWAY',
#]
#from fnmatch import fnmatchcase
#print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
#print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])



#from urllib.request import urlopen
## name 必须为无组
#def read_data(name):
#    if name.startswith(('http:', 'https:', 'ftp:')):
#        return urlopen(name).read()
#    else:
#        with open(name) as f:
#            return f.read()


    #filename = 'spam.txt'
    #print(filename.endswith('.txt'))
#print(filename.startswith('file:'))
#url = 'http://www.python.org'
#print(url.startswith('http:'))

## 检查多种匹配可能
#import os
#filenames = os.listdir(r'E:\study\python_study\vsproject\study_python')
#print([name for name in filenames if name.endswith(('.py', '.sln')) ])
#print(any(name.endswith('.py') for name in filenames))


#line = 'asdf fjdk; afed, fjek,asdf, foo'
#import re
#print(re.split(r'[;,\s]\s*', line))
#fields = re.split(r'(;|,|\s)\s*', line)
#print(fields)
#values = fields[::2]
#delimiters = fields[1::2] + ['']
#print(values)
#print(delimiters)
## Reform the line using the same delimiters
#print(''.join(v+d for v,d in zip(values, delimiters)))

#from collections import ChainMap

#values = ChainMap()
#values['x'] = 1
## Add a new mapping
#values = values.new_child()
#values['x'] = 2
## Add a new mapping
#values = values.new_child()
#values['x'] = 3
#print(values)
#print(values['x'])
## Discard last mapping
#values = values.parents
#print(values['x'])
## Discard last mapping
#values = values.parents
#print(values['x'])
#values
#print(values)


#a = {'x': 1, 'z': 3 }
#b = {'y': 2, 'z': 4 }
#from collections import ChainMap
#c = ChainMap(a,b)
#print(c['x']) # Outputs 1 (from a)
#print(c['y']) # Outputs 2 (from b)
#print(c['z']) # Outputs 3 (from a)


#nums = [1, 2, 3, 4, 5]
#s = sum(x * x for x in nums)
#print(s)

## Determine if any .py files exist in a directory
#import os
#files = os.listdir(r'E:\study\python_study\vsproject\study_python')
#if any(name.endswith('.py') for name in files):
#    print('There be python!')
#else:
#    print('Sorry, no python.')

## Output a tuple as CSV
#s = ('ACME', 50, 123.45)
#print(','.join(str(x) for x in s))
## Data reduction across fields of a data structure
#portfolio = [
#    {'name':'GOOG', 'shares': 50},
#    {'name':'YHOO', 'shares': 75},
#    {'name':'AOL', 'shares': 20},
#    {'name':'SCOX', 'shares': 65}
#]
#min_shares = min(s['shares'] for s in portfolio)

#from collections import namedtuple
#Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
## Create a prototype instance
#stock_prototype = Stock('', 0, 0.0, None, None)
## Function to convert a dictionary to a Stock
#def dict_to_stock(s):
#    return stock_prototype._replace(**s)

#a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
#print(dict_to_stock(a))
#b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
#print(dict_to_stock(b))

#from collections import namedtuple
#Stock = namedtuple('Stock', ['name', 'shares', 'price'])
#def compute_cost(records):
#    total = 0.0
#    for rec in records:
#        s = Stock(*rec)
#    total += s.shares * s.price
#    return total

#s = Stock('ACME', 100, 123.45)
#print(s)
## s.shares = 5
#s = s._replace(shares=75)
#print(s)

#from collections import namedtuple
#Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
#sub = Subscriber('jonesy@example.com', '2012-10-19')
#print(sub)
#print(sub.addr)
#print(sub.joined)
#print(len(sub))
#addr, joined = sub
#print(addr, joined)

#prices = {
#    'ACME': 45.23,
#    'AAPL': 612.78,
#    'IBM': 205.55,
#    'HPQ': 37.20,
#    'FB': 10.75
#}
#p1 = dict((key, value) for key, value in prices.items() if value > 200)
#print(p1)

#prices = {
#    'ACME': 45.23,
#    'AAPL': 612.78,
#    'IBM': 205.55,
#    'HPQ': 37.20,
#    'FB': 10.75
#}
#min_price = min(zip(prices.values(), prices.keys()))
#print(min_price)
#prices_sorted = sorted(zip(prices.values(), prices.keys()))
#print(prices_sorted)


#values = ['1', '2', '-3', '-', '4', 'N/A', '5']
#def is_int(val):
#	try:
#		x = int(val)
#		return True
#	except ValueError:
#		return False
#ivals = list(filter(is_int, values))
#print(ivals)
# Outputs ['1', '2', '-3', '4', '5']

#key_values = {'a':1, 'b':2, 'c':'c'}

#def is_int2(key_val):
#    print(key_val)
#    if key_val = 'a' or key_val = 'b':
#        return True
#    return False

#	#try:
#	#	# x = int(key_val.second)
#	#	return True
#	#except ValueError:
#	#	return False

#ivals = dict(filter(is_int2, key_values))
#print(ivals)

#rows = [
#    {'address': '5412 N CLARK', 'date': '07/01/2012'},
#    {'address': '5148 N CLARK', 'date': '07/04/2012'},
#    {'address': '5800 E 58TH', 'date': '07/02/2012'},
#    {'address': '2122 N CLARK', 'date': '07/03/2012'},
#    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
#    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
#    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
#    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
#]
#from operator import itemgetter
#from itertools import groupby
## Sort by the desired field first
#rows.sort(key=itemgetter('date'))
## Iterate in groups
#for date, items in groupby(rows, key=itemgetter('date')):
#	print(date)
#	for i in items:
#		print(' ', i)

#rows = [
#    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
#    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
#    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
#    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
#]

#from operator import itemgetter
#rows_by_fname = sorted(rows, key=itemgetter('fname'))
#rows_by_uid = sorted(rows, key=itemgetter('uid'))
#print(rows_by_fname)
#print(rows_by_uid)
