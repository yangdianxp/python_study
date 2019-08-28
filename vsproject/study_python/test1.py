# 例
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

import re
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(change_date, text))
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext, n)

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
