# 例 
def make_averager():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager

avg = make_averager()
print(avg.__code__)

#b = 6
#def f3(a):
#    global b
#    print(a)
#    print(b)
#    b = 9

#promos = []
#def promotion(promo_func):
#    promos.append(promo_func)
#    return promo_func

#@promotion
#def fidelity(order):
#    """为积分为1000或以上的顾客提供5%折扣"""
#    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

#@promotion
#def bulk_item(order):
#    """单个商品为20个或以上时提供10%折扣"""
#    discount = 0
#    for item in order.cart:
#        if item.quantity >= 20:
#            discount += item.total() * .1
#    return discount

#@promotion
#def large_order(order):
#    """订单中的不同商品达到10个或以上时提供7%折扣"""
#    distinct_items = {item.product for item in order.cart}
#    if len(distinct_items) >= 10:
#        return order.total() * .07
#    return 0

#def best_promo(order):
#    """选择可用的最佳折扣 """
#    return max(promo(order) for promo in promos)

#registry = []
#def register(func):
#    print('running register(%s)' % func)
#    registry.append(func)
#    return func

#@register
#def f1():
#    print('running f1()')

#@register
#def f2():
#    print('running f2()')

#def f3():
#    print('running f3()')

#def main():
#    print('running main()')
#    print('registry ->', registry)
#    f1()
#    f2()
#    f3()

#if __name__=='__main__':
#    main()

#def deco(func):
#    def inner():
#        print('running inner()')
#    return inner
#@deco
#def target():
#    print('running target()')
#target()


## 把函数当成一等对象，实现策略模式
## 一等对象定义：
## 在运行时创建
## 能赋值给变量或数据结构中的元素
## 能作为参数传给函数
## 能作为函数的返回结果

#from collections import namedtuple
#Customer = namedtuple('Customer', 'name fidelity')
#class LineItem:
#    def __init__(self, product, quantity, price):
#        self.product = product
#        self.quantity = quantity
#        self.price = price
#    def total(self):
#        return self.price * self.quantity

#class Order: # 上下文
#    def __init__(self, customer, cart, promotion=None):
#        self.customer = customer
#        self.cart = list(cart)
#        self.promotion = promotion
#    def total(self):
#        if not hasattr(self, '__total'):
#            self.__total = sum(item.total() for item in self.cart)
#            return self.__total
#    def due(self):
#        if self.promotion is None:
#            discount = 0
#        else:
#            discount = self.promotion(self)
#        return self.total() - discount
#    def __repr__(self):
#        fmt = '<Order total: {:.2f} due: {:.2f}>'
#        return fmt.format(self.total(), self.due())

#def fidelity_promo(order):
#    """为积分为1000或以上的顾客提供5%折扣"""
#    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

#def bulk_item_promo(order):
#    """单个商品为20个或以上时提供10%折扣"""
#    discount = 0
#    for item in order.cart:
#        if item.quantity >= 20:
#            discount += item.total() * .1
#    return discount

#def large_order_promo(order):
#    """订单中的不同商品达到10个或以上时提供7%折扣"""
#    distinct_items = {item.product for item in order.cart}
#    if len(distinct_items) >= 10:
#        return order.total() * .07
#    return 0

#promos = [fidelity_promo, bulk_item_promo, large_order_promo]
#def best_promo(order):
#    """选择可用的最佳折扣 """
#    return max(promo(order) for promo in promos)



#import random
#class BingoCage:
#    def __init__(self, items):
#        self._items = list(items)
#        random.shuffle(self._items)
#    def pick(self):
#        try:
#            return self._items.pop()
#        except IndexError:
#            raise LookupError('pick from empty BingoCage')
#    def __call__(self):
#        return self.pick()

#bingo = BingoCage(range(3))
#print("====>1:", bingo.pick())
#print("====>2:", bingo())
#print("====>3:", callable(bingo))

#city = 'São Paulo'
#print("====>1:", city.encode('utf_8')) # ➊
#city.encode('utf_16')
#city.encode('iso8859_1') # ➋
#city.encode('cp437') # ➌
#return codecs.charmap_encode(input,errors,encoding_map)
#UnicodeEncodeError: 'charmap' codec can't encode character '\xe3' in
#position 1: character maps to <undefined>
#city.encode('cp437', errors='ignore') # ➍
#b'So Paulo'
#city.encode('cp437', errors='replace') # ➎
#b'S?o Paulo'
#city.encode('cp437', errors='xmlcharrefreplace') # ➏
#b'São Paulo

#import struct
#fmt = '<3s3sHH' # ➊
#with open('giphy.gif', 'rb') as fp:
#    img = memoryview(fp.read()) # ➋

#header = img[:10] # ➌
#print("====>1:", bytes(header)) # ➍
#print("====>2:", struct.unpack(fmt, header)) # ➎
#del header # ➏
#del img

#import collections
#ct = collections.Counter('abracadabra')
#print("====>1:", ct)
#ct.update('aaaaazzz')
#print("====>2:", ct)
#print("====>3:", ct.most_common(2))


## 处理键不存在的情况
#import sys
#import re
#import collections
#WORD_RE = re.compile(r'\w+')
#index = collections.defaultdict(list)
#with open(sys.argv[1], encoding='utf-8') as fp:
#    for line_no, line in enumerate(fp, 1):
#        for match in WORD_RE.finditer(line):
#            word = match.group()
#            column_no = match.start()+1
#            location = (line_no, column_no)
#            index[word].append(location)
## 以字母顺序打印出结果
#for word in sorted(index, key=str.upper):
#    print(word, index[word])

#import sys
#import re
#WORD_RE = re.compile(r'\w+')
#index = {}
#with open(sys.argv[1], encoding='utf-8') as fp:
#    for line_no, line in enumerate(fp, 1):
#        for match in WORD_RE.finditer(line):
#            word = match.group()
#            column_no = match.start()+1
#            location = (line_no, column_no)
#            index.setdefault(word, []).append(location)
## 以字母顺序打印出结果
#for word in sorted(index, key=str.upper):
#    print(word, index[word])

#import sys
#import re
#WORD_RE = re.compile(r'\w+')
#index = {}
#with open(sys.argv[1], encoding='utf-8') as fp:
#    for line_no, line in enumerate(fp, 1):
#        for match in WORD_RE.finditer(line):
#            word = match.group()
#            column_no = match.start()+1
#            location = (line_no, column_no)
#            # 这其实是一种很不好的实现，这样写只是为了证明论点
#            occurrences = index.get(word, [])
#            occurrences.append(location)
#            index[word] = occurrences
## 以字母顺序打印出结果
#for word in sorted(index, key=str.upper):
#    print(word, index[word])


#l = list(range(10))
#print(l)
#l[2:5] = [20, 30]
#del l[5:7]
#print(l)
#l[3::2] = [11, 22]
#print(l)
#l[2:5] = [100]
#print(l)

#from collections import namedtuple
#City = namedtuple('City', 'name country population coordinates')
#tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
#print(tokyo)
#print(tokyo.population)
#print(tokyo.coordinates)
#print(tokyo[1])

#print(City._fields)

#LatLong = namedtuple('LatLong', 'lat long')
#delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
#delhi = City._make(delhi_data)
#print(delhi._asdict())

#for key, value in delhi._asdict().items():
#    print(key + ':', value)

#print("{}/{}".format(('USA', '31195855')))

#symbols = '$¢£¥€¤'
#print(tuple(ord(symbol) for symbol in symbols))
#import array
#print(array.array('I', (ord(symbol) for symbol in symbols)))

## 使用列表推导计算笛卡儿积
#colors = ['black', 'white']
#sizes = ['S', 'M', 'L']
#tshirts = [(color, size) for color in colors for size in sizes]
#print(tshirts)

#from math import hypot
#class Vector:
#    def __init__(self, x=0, y=0):
#        self.x = x
#        self.y = y
#    def __repr__(self):
#        return 'Vector(%r, %r)' % (self.x, self.y)
#    def __abs__(self):
#        return hypot(self.x, self.y)
#    def __bool__(self):
#        return bool(abs(self))
#    def __add__(self, other):
#        x = self.x + other.x
#        y = self.y + other.y
#        return Vector(x, y)
#    def __mul__(self, scalar):
#        return Vector(self.x * scalar, self.y * scalar)

#v1 = Vector(2, 4)
#v2 = Vector(2, 1)
#print(v1 + v2)
#print(abs(v1))
#print(v1 * 3)

#import collections
#Card = collections.namedtuple('Card', ['rank', 'suit'])
#class FrenchDeck:
#    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
#    suits = 'spades diamonds clubs hearts'.split()
#    def __init__(self):
#        self._cards = [Card(rank, suit) for suit in self.suits
#                                        for rank in self.ranks]
#    def __len__(self):
#        return len(self._cards)

#    def __getitem__(self, position):
#        return self._cards[position]

#beer_card = Card('7', 'diamonds')
#print(beer_card)

#deck = FrenchDeck()
#len(deck)
#print(deck[0])
#print(deck[-1])

## 随机抽取一张纸牌
#from random import choice
#print(choice(deck))
#print(choice(deck))
#print(choice(deck))
## 自动支持切片
#print(deck[:3])
#print(deck[12::13])
## 可迭代
#for card in deck: # doctest: +ELLIPSIS
#    print(card)
## 反向迭代
#for card in reversed(deck): # doctest: +ELLIPSIS
#    print(card)
## 可使用in 运算符
#print(Card('Q', 'hearts') in deck)
## 排序
#suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
#def spades_high(card):
#    rank_value = FrenchDeck.ranks.index(card.rank)
#    return rank_value * len(suit_values) + suit_values[card.suit]
#card_test = Card('A', 'clubs')
#print(spades_high(card_test))
#for card in sorted(deck, key=spades_high): # doctest: +ELLIPSIS
#    print(card)

#from requests import Request, Session
#from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
#import json

#url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
#parameters = {
#  'start':'1',
#  'limit':'1',
#  'convert':'BTC'
#}
#headers = {
#  'Accepts': 'application/json',
#  'X-CMC_PRO_API_KEY': '1b280832-12bb-46d7-9e48-2801802ad059',
#}

#session = Session()
#session.headers.update(headers)

#try:
#  response = session.get(url, params=parameters)
#  data = json.loads(response.text)
#  print(data)
#except (ConnectionError, Timeout, TooManyRedirects) as e:
#  print(e)

##session = Session()
##session.headers.update(headers)

#def get_price(bc):
#    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
#    parameters = {
#        'start':'1',
#        'limit':'1'
#    }
#    parameters['convert'] = bc
#    print(parameters)
#    headers = {
#        'Accepts': 'application/json',
#        'X-CMC_PRO_API_KEY': '1b280832-12bb-46d7-9e48-2801802ad059',
#    }
#    print(headers)
#    try:
#        response = requests.get(url, params=parameters, headers=headers)
#        res = json.loads(response.text)
#        error_code = res['status']['error_code']
#        print(error_code)
#        if error_code != 0:
#            return
#        data = res['data']

#    except (ConnectionError, Timeout, TooManyRedirects) as e:
#        print(e)

#def get_price(bc):

#    url = "https://api.coinmarketcap.com/v1/ticker/%s" % get_name(bc)
#    logging.info(url)
#    print(url)
#    r = requests.get(url, timeout=10)
#    resjs = r.json()
#    #print(resjs)
#    logging.info(resjs)
#    en = resjs[0]
#    price_usd = en["price_usd"]
#    h24_volume = en["24h_volume_usd"]
#    ffl = en["percent_change_24h"]

#    return {"price": price_usd, "volume": str(float(h24_volume) / float(price_usd)), "ff": ffl}


#types = ['BTC', 'ETH', 'BCH']
#for t in types:
#    get_price(t)


#names = ["id", "name", "phone"]
#values = [[1, "wanbao", 13786135412],
#          [2, "liuliu", 15555555555]]
#for v in values:
#    print(dict(zip(names, v)))

## 修改已经存在的工作簿(表)
#import openpyxl
#workbook=openpyxl.load_workbook("myfile.xlsx")
#worksheet=workbook.worksheets[0]
##在第一列之前插入一列
#worksheet.insert_cols(1)  #
 
#for index,row in enumerate(worksheet.rows):
#    if index==0:
#        row[0].value="编号"  #每一行的一个row[0]就是第一列
#    else:
#        row[0].value=index
#worksheet.cell(2,3,'0')
#worksheet["B2"]="Peking"
#taiwan=[32,"台湾省"]
#worksheet.append(taiwan)
#workbook.save(filename="myfile.xlsx")


## 使用openpyxl模块对xlsx文件进行写操作
#import openpyxl
## 创建一个Workbook对象，相当于创建了一个Excel文件
#workbook=openpyxl.Workbook()

##获取当前活跃的worksheet,默认就是第一个worksheet
#worksheet = workbook.active
#worksheet.title="mysheet"

#worksheet2 = workbook.create_sheet()   #默认插在工作簿末尾
##worksheet2 = workbook.create_sheet(0)  #插入在工作簿的第一个位置
#worksheet2.title = "New Title"

#worksheet2 = workbook.create_sheet()   #默认插在工作簿末尾
##以下是我们要写入的数据
#Province=['北京市', '天津市', '河北省', '山西省', '内蒙古自治区', '辽宁省',
#          '吉林省', '黑龙江省', '上海市', '江苏省', '浙江省', '安徽省', '福建省',
#          '江西省', '山东省', '河南省', '湖北省', '湖南省', '广东省', '广西壮族自治区',
#          '海南省', '重庆市', '四川省', '贵州省', '云南省', '西藏自治区', '陕西省', '甘肃省',
#          '青海省', '宁夏回族自治区', '新疆维吾尔自治区']
 
#Income=['5047.4', '3247.9', '1514.7', '1374.3', '590.7', '1499.5', '605.1', '654.9',
#        '6686.0', '3104.8', '3575.1', '1184.1', '1855.5', '1441.3', '1671.5', '1022.7',
#        '1199.2', '1449.6', '2906.2', '972.3', '555.7', '1309.9', '1219.5', '715.5', '441.8',
#        '568.4', '848.3', '637.4', '653.3', '823.1', '254.1']
 
#Project=['各省市', '工资性收入', '家庭经营纯收入', '财产性收入', '转移性收入', '食品', '衣着',
#         '居住', '家庭设备及服务', '交通和通讯', '文教、娱乐用品及服务', '医疗保健', '其他商品及服务']
 
##写入第一行数据，行号和列号都从1开始计数
#for i in range(len(Project)):
#    worksheet.cell(1, i+1,Project[i])
 
##写入第一列数据，因为第一行已经有数据了，i+2
#for i in range(len(Province)):
#    worksheet.cell(i+2,1,Province[i])
 
##写入第二列数据
#for i in range(len(Income)):
#    worksheet.cell(i+2,2,Income[i])

#workbook.save(filename='myfile.xlsx')

## 使用openpyxl模块对xlsx文件进行读操作
#import openpyxl
##获取 工作簿对象
#workbook=openpyxl.load_workbook("优先额度与转入额度异常.xlsx")
##获取工作簿 workbook的所有工作表
#shenames=workbook.sheetnames
#print(shenames)
##获得工作簿的表名后，就可以获得表对象
#worksheet1=workbook[shenames[1]]
#print(worksheet1)
##还可以通过索引方式获取表对象
#worksheet=workbook.worksheets[0]
#print(worksheet)
##获取当前活跃的worksheet,默认就是第一个worksheet
#ws = workbook.active
#print(ws)
#name=worksheet.title  #获取表名
#print(name)
##for row in worksheet.rows:
##    for cell in row:
##        print(cell.value, end=" ")
##    print()

##for col in worksheet.columns:
##    for cell in col:
##        print(cell.value,end=" ")
##    print()

#for i in range(1, 4):
#    for j in range(1, 9):
#        value = worksheet.cell(row=i, column=j).value
#        print(value, type(value), end=" ")
#    print()

##精确读取表格中的某一单元格
#content_A1= worksheet['A1'].value
#print(content_A1)

# 获取某一块的数据


## 使用xlwt模块对xls文件进行写操作

## 导入xlwt模块
#import xlwt
 
##创建一个Workbook对象，相当于创建了一个Excel文件
#book=xlwt.Workbook(encoding="utf-8",style_compression=0)
 
#'''
#Workbook类初始化时有encoding和style_compression参数
#encoding:设置字符编码，一般要这样设置：w = Workbook(encoding='utf-8')，就可以在excel中输出中文了。默认是ascii。
#style_compression:表示是否压缩，不常用。
#'''

## 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
#sheet = book.add_sheet('test01', cell_overwrite_ok=True)
## 其中的test是这张表的名字,cell_overwrite_ok，表示是否可以覆盖单元格，其实是Worksheet实例化的一个参数，默认值是False

## 向表test中添加数据
#sheet.write(0, 0, '各省市')  # 其中的'0-行, 0-列'指定表中的单元，'各省市'是向该单元写入的内容
#sheet.write(0, 1, '工资性收入')

##也可以这样添加数据
#txt1 = '北京市'
#sheet.write(1,0, txt1)  
#txt2 = 5047.4
#sheet.write(1, 1, txt2)

##添加第二个表
#sheet2=book.add_sheet("test02",cell_overwrite_ok=True)
 
#Province=['北京市', '天津市', '河北省', '山西省', '内蒙古自治区', '辽宁省',
#          '吉林省', '黑龙江省', '上海市', '江苏省', '浙江省', '安徽省', '福建省',
#          '江西省', '山东省', '河南省', '湖北省', '湖南省', '广东省', '广西壮族自治区',
#          '海南省', '重庆市', '四川省', '贵州省', '云南省', '西藏自治区', '陕西省', '甘肃省',
#          '青海省', '宁夏回族自治区', '新疆维吾尔自治区']
 
#Income=['5047.4', '3247.9', '1514.7', '1374.3', '590.7', '1499.5', '605.1', '654.9',
#        '6686.0', '3104.8', '3575.1', '1184.1', '1855.5', '1441.3', '1671.5', '1022.7',
#        '1199.2', '1449.6', '2906.2', '972.3', '555.7', '1309.9', '1219.5', '715.5', '441.8',
#        '568.4', '848.3', '637.4', '653.3', '823.1', '254.1']
 
#Project=['各省市', '工资性收入', '家庭经营纯收入', '财产性收入', '转移性收入', '食品', '衣着',
#         '居住', '家庭设备及服务', '交通和通讯', '文教、娱乐用品及服务', '医疗保健', '其他商品及服务']
 
##填入第一列
#for i in range(0, len(Province)):
#    sheet2.write(i+1, 0, Province[i])
 
##填入第二列
#for i in range(0,len(Income)):
#    sheet2.write(i+1,1,Income[i])
 
##填入第一行
#for i in range(0,len(Project)):
#    sheet2.write(0,i,Project[i])

    
## 最后，将以上操作保存到指定的Excel文件中
#book.save('test1.xls')

#import xlrd
#from datetime import timedelta
#from datetime import datetime

#workbook=xlrd.open_workbook("优先额度与转入额度异常.xlsx")
## 获取所有sheet的名字
#names=workbook.sheet_names()
#print(names)

##由上可知，workbook.sheet_names() 返回一个list对象，可以对这个list对象进行操作
#sheet0_name=workbook.sheet_names()[0]
#print(sheet0_name)

## 通过sheet索引获得sheet对象
#worksheet=workbook.sheet_by_index(0)
#print(worksheet)

## 通过sheet名获得sheet对象
#worksheet=workbook.sheet_by_name("按用户统计最近优先额度表")
#print(worksheet)

#name=worksheet.name  #获取表的姓名
#print(name)

#nrows=worksheet.nrows  #获取该表总行数
#print(nrows) 

#ncols=worksheet.ncols  #获取该表总列数
#print(ncols)

## 按行或列方式获得工作表的数据
## for i in range(nrows): #循环打印每一行
##    print(worksheet.row_values(i))  #以列表形式读出，列表中的每一项是str类型

##通过坐标读取表格中的数据
#cell_value1=worksheet.cell_value(0,0)
#cell_value2=worksheet.cell_value(1,0)
#print(cell_value1)
#print(cell_value2)

#cell_value1=worksheet.cell(0,0).value
#print(cell_value1) 
#cell_value1=worksheet.row(0)[0].value
#print(cell_value1) 

# 读btc等币最新交易列表
#import sys
#import time
#import json
#import requests

#while True:
#    print("111")
#    time.sleep(1)
#    #for i in range(10):
#    #    res = requests.get("https://data.block.cc/api/v1/tickers?market=bitfinex&symbol=BTC")
#    #    print(res.status_code)
#    #    print(res.json()["code"])
#    #    if res.status_code != 200:
#    #        exit(1)
#    #time.sleep(1800)
#    # print(res.json()["data"]["list"][0])



#import csv
#from collections import namedtuple
#with open('优先额度与转入额度异常.xlsx', encoding='UTF-8') as f:
#    f_csv = csv.reader(f)
#    headings = next(f_csv)
#    Row = namedtuple('Row', headings)
#    for r in f_csv:
#        row = Row(*r)
#        print(row)

#import pickle
#f = open('somedata', 'wb')
#pickle.dump([1, 2, 3, 4], f)
#pickle.dump('hello', f)
#pickle.dump({'Apple', 'Pear', 'Banana'}, f)
#f.close()
#f = open('somedata', 'rb')
#print(pickle.load(f))
#print(pickle.load(f))
#print(pickle.load(f))


#import pickle
#hsb_phone = ['13900000000', '14200000000'] # Some Python object
#with open('hsb_phone.data', 'wb') as f:
#   pickle.dump(hsb_phone, f) 

#new_data = []
#with open('hsb_phone.data', 'rb') as f:
#    new_data = pickle.load(f)
#print(new_data)


#myList = [1, 2, 3, -1, -2]
#result = filter(lambda x: x >= 0, myList)
#print(list(result))

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
