# 例
import win32api
import win32con
import win32gui
from ctypes import *
import time
from PIL import ImageGrab
from io import BytesIO
import requests
import sys
import json
import base64

VK_CODE = {
    'backspace':0x08,
    'tab':0x09,
    'clear':0x0C,
    'enter':0x0D,
    'shift':0x10,
    'ctrl':0x11,
    'alt':0x12,
    'pause':0x13,
    'caps_lock':0x14,
    'esc':0x1B,
    'spacebar':0x20,
    'page_up':0x21,
    'page_down':0x22,
    'end':0x23,
    'home':0x24,
    'left_arrow':0x25,
    'up_arrow':0x26,
    'right_arrow':0x27,
    'down_arrow':0x28,
    'select':0x29,
    'print':0x2A,
    'execute':0x2B,
    'print_screen':0x2C,
    'ins':0x2D,
    'del':0x2E,
    'help':0x2F,
    '0':0x30,
    '1':0x31,
    '2':0x32,
    '3':0x33,
    '4':0x34,
    '5':0x35,
    '6':0x36,
    '7':0x37,
    '8':0x38,
    '9':0x39,
    'a':0x41,
    'b':0x42,
    'c':0x43,
    'd':0x44,
    'e':0x45,
    'f':0x46,
    'g':0x47,
    'h':0x48,
    'i':0x49,
    'j':0x4A,
    'k':0x4B,
    'l':0x4C,
    'm':0x4D,
    'n':0x4E,
    'o':0x4F,
    'p':0x50,
    'q':0x51,
    'r':0x52,
    's':0x53,
    't':0x54,
    'u':0x55,
    'v':0x56,
    'w':0x57,
    'x':0x58,
    'y':0x59,
    'z':0x5A,
    'numpad_0':0x60,
    'numpad_1':0x61,
    'numpad_2':0x62,
    'numpad_3':0x63,
    'numpad_4':0x64,
    'numpad_5':0x65,
    'numpad_6':0x66,
    'numpad_7':0x67,
    'numpad_8':0x68,
    'numpad_9':0x69,
    'multiply_key':0x6A,
    'add_key':0x6B,
    'separator_key':0x6C,
    'subtract_key':0x6D,
    'decimal_key':0x6E,
    'divide_key':0x6F,
    'F1':0x70,
    'F2':0x71,
    'F3':0x72,
    'F4':0x73,
    'F5':0x74,
    'F6':0x75,
    'F7':0x76,
    'F8':0x77,
    'F9':0x78,
    'F10':0x79,
    'F11':0x7A,
    'F12':0x7B,
    'F13':0x7C,
    'F14':0x7D,
    'F15':0x7E,
    'F16':0x7F,
    'F17':0x80,
    'F18':0x81,
    'F19':0x82,
    'F20':0x83,
    'F21':0x84,
    'F22':0x85,
    'F23':0x86,
    'F24':0x87,
    'num_lock':0x90,
    'scroll_lock':0x91,
    'left_shift':0xA0,
    'right_shift ':0xA1,
    'left_control':0xA2,
    'right_control':0xA3,
    'left_menu':0xA4,
    'right_menu':0xA5,
    'browser_back':0xA6,
    'browser_forward':0xA7,
    'browser_refresh':0xA8,
    'browser_stop':0xA9,
    'browser_search':0xAA,
    'browser_favorites':0xAB,
    'browser_start_and_home':0xAC,
    'volume_mute':0xAD,
    'volume_Down':0xAE,
    'volume_up':0xAF,
    'next_track':0xB0,
    'previous_track':0xB1,
    'stop_media':0xB2,
    'play/pause_media':0xB3,
    'start_mail':0xB4,
    'select_media':0xB5,
    'start_application_1':0xB6,
    'start_application_2':0xB7,
    'attn_key':0xF6,
    'crsel_key':0xF7,
    'exsel_key':0xF8,
    'play_key':0xFA,
    'zoom_key':0xFB,
    'clear_key':0xFE,
    '+':0xBB,
    ',':0xBC,
    '-':0xBD,
    '.':0xBE,
    '/':0xBF,
    '`':0xC0,
    ';':0xBA,
    '[':0xDB,
    '\\':0xDC,
    ']':0xDD,
    "'":0xDE}

VK_CODE1 = {
    'A':'a',
    'B':'b',
    'C':'c',
    'D':'d',
    'E':'e',
    'F':'f',
    'G':'g',
    'H':'h',
    'I':'i',
    'J':'j',
    'K':'k',
    'L':'l',
    'M':'m',
    'N':'n',
    'O':'o',
    'P':'p',
    'Q':'q',
    'R':'r',
    'S':'s',
    'T':'t',
    'U':'u',
    'V':'v',
    'W':'w',
    'X':'x',
    'Y':'y',
    'Z':'z',
    ')':'0',
    '!':'1',
    '@':'2',
    '#':'3',
    '$':'4',
    '%':'5',
    '^':'6',
    '&':'7',
    '*':'8',
    '(':'9',
    '=':'+',
    '<':',',
    '_':'-',
    '>':'.',
    '?':'/',
    '~':'`',
    ':':';',
    '{':'[',
    '|':'\\',
    '}':']',
    '"':"'"}

def mouse_click(x=None,y=None):#模拟鼠标单击
    if not x is None and not y is None:
        mouse_move(x,y)
        time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def mouse_dclick(x=None,y=None):#模拟鼠标双击
    if not x is None and not y is None:
        mouse_move(x,y)
        time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)#按下鼠标左键
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)#松开鼠标左键
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def mouse_move(x,y):
    windll.user32.SetCursorPos(x, y)#将鼠标移动到对应位置但是不点击

def key_input(str=''):#输出小写的
    for c in str:
        win32api.keybd_event(VK_CODE[c],0,0,0)#按键
        win32api.keybd_event(VK_CODE[c],0,win32con.KEYEVENTF_KEYUP,0)#释放按键
        time.sleep(0.05)#延时1秒

def key_dinput(str=''):#传进小写的输出大写的
    for c in str:
        win32api.keybd_event(VK_CODE['shift'],0,0,0)#按键
        win32api.keybd_event(VK_CODE[c],0,0,0)#按键
        win32api.keybd_event(VK_CODE['shift'],0,win32con.KEYEVENTF_KEYUP,0)#释放按键
        win32api.keybd_event(VK_CODE[c],0,win32con.KEYEVENTF_KEYUP,0)#释放按键
        time.sleep(0.05)#延时1秒

def key_autinput(str=''):#自动识别上档键和下档建并输出
    for c in str:
        if c in VK_CODE1:
            win32api.keybd_event(VK_CODE['shift'],0,0,0)#按键
            win32api.keybd_event(VK_CODE[VK_CODE1[c]],0,0,0)#按键
            win32api.keybd_event(VK_CODE['shift'],0,win32con.KEYEVENTF_KEYUP,0)#释放按键
            win32api.keybd_event(VK_CODE[VK_CODE1[c]],0,win32con.KEYEVENTF_KEYUP,0)#释放按键
            time.sleep(0.05)#延时1秒
        else:
            win32api.keybd_event(VK_CODE[c],0,0,0)#按键
            win32api.keybd_event(VK_CODE[c],0,win32con.KEYEVENTF_KEYUP,0)#释放按键
            time.sleep(0.05)#延时1秒

    #mouse_click(200, 1080)
    #str = '~!@#$a%^d&*(s)_s+{}f|":h?><ABCD'
    #key_autinput(str)

if __name__ == "__main__":
    image = ImageGrab.grab()
    print(image.size)
    width = image.size[0]
    height = image.size[1]
    box = (int(width / 5 * 2), int(height / 5 * 2), int(width / 5 * 3), int(height / 5 * 4))
    print(box)
    region = image.crop(box)
    region.show()

    """ 你的 APPID AK SK """
    APP_ID = '17455795'
    API_KEY = '2eRyuVgd1ohtNMeszaCpK6jl'
    SECRET_KEY = 'fXIh5POUXAmerYa6t42kQoNmGPIUNuVc'

    output_buffer = BytesIO()
    region.save(output_buffer, format='png')
    binary_data = output_buffer.getvalue()
    binary_data = base64.b64encode(binary_data)


    headers = {'Content-Type':'application/json',
                'charset':'UTF-8'}
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=2eRyuVgd1ohtNMeszaCpK6jl&client_secret=fXIh5POUXAmerYa6t42kQoNmGPIUNuVc'
    res = requests.post(host, headers=headers)
    token = res.json()["access_token"]
    print(token)

    #token = '24.36bd551d0bff8e5a746f670bf04ccac7.2592000.1573054545.282335-17455795'

    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=' + token
    params = {"image": binary_data}
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    res = requests.post(url, headers=headers, params=params)
    print(res.status_code)
    print(res.json())





#import pytesseract
#from PIL import Image

## pytesseract.pytesseract.tesseract_cmd = r"""D:\Program Files (x86)\Tesseract-OCR\tesseract.exe"""
#image = Image.open(r"""C:\Users\yangd\Desktop\temp\1570447874(1).png""")
#print(image.size)
#width = image.size[0]
#height = image.size[1]
#box = (int(width / 3), int(height / 4 * 3), int(width / 3 * 2), height)
#print(box)
#region = image.crop(box)
#region = region.convert('1')
## region.show()

#text = pytesseract.image_to_string(region, lang='chi_sim')

#print(text)


#import os
#import requests
#import json
#import time
#import pickle

#def download_file(url, path):
#    with requests.get(url, stream=True) as r:
#        chunk_size = 1024
#        # content_size = int(r.headers['content-length'])
#        print('下载开始')
#        with open(path, "wb") as f:
#            for chunk in r.iter_content(chunk_size=chunk_size):
#                print("====")
#                f.write(chunk)
 
 
#if __name__ == '__main__':
#    url = """https://cd.phncdn.com/videos/201811/25/193715551/190220_2324_480P_600K_193715551.mp4?l9pCPZr6Ix0h1mbJUgHJRUbfdTePz2AYisCLe6MpmAChXBX-QZBbNnQQObKlnTgf3Pk9E4ZnIFtjrx9qIn9lBCPD771eWf0c1svIQJeCX3z7hGrfK9PL8bZJVTyiG4sh5IYx58TylPHvX50hLp-qTYIyCPSFvqh-8dd4gmqOBSD7MNiU2yxkY4Rci1uGkmVM-FbYVW7SLTT9KUIMG6Ieawb7HX983WkFDyb2hc1Zp1YNNOs_FHHK-DYqBOhZ"""
#    path = 'ph59be5870880ae.mp4'
#    download_file(url, path)

#def save_data(data, block_filename):
#    if not os.path.exists(block_filename):
#        with open(block_filename, 'wb') as f:
#            block_list = []
#            block_list.append(data)
#            pickle.dump(block_list, f)
#    else:
#        with open(block_filename, 'rb') as f:
#            block_list = pickle.load(f)
#        with open(block_filename, 'wb') as f:
#            block_list.append(data)
#            pickle.dump(block_list, f)

#with open("height.data", 'rb') as f:
#    try:
#        height = pickle.load(f)
#    except EOFError as result:
#        print(result)
#        height = 1

#while True:
#    block_filename = "block{}.data".format(int(height / 100000))
#    try:
#        print("height = {}".format(height))
#        res = requests.get(url.format(height))
#        print(res.status_code)
#        if res.status_code == 429:
#            time.sleep(1)
#            continue
        
#        data = res.json()
#        if data['err_no'] != 0:
#            print(data)
#            time.sleep(10)
#            continue

#        print(data)
#        save_data(data, block_filename)
                    
#    except Exception as result:
#        print(result)
#        time.sleep(1)
#        continue
#    time.sleep(0.01)
#    height += 1
#    with open("height.data", 'wb') as f:
#        pickle.dump(height, f)



#a = "你好"
#print("===>1:", a)
#print("===>2:", len(a))
#b = a.encode("utf8")
#print("===>3:", b)
#print("===>4:", len(b))
#c = b.decode("utf8")
#print("===>5:", c)
#print("===>6:", len(c))



## 字典推导式
#DIAL_CODES = [
#    (86, 'China'),
#    (91, 'India'),
#    (1, 'United States'),
#    (62, 'Indonesia'),
#    (55, 'Brazil'),
#    (92, 'Pakistan'),
#    (880, 'Bangladesh'),
#    (234, 'Nigeria'),
#    (7, 'Russia'),
#    (81, 'Japan'),
#]
#country_code = {country: code for code, country in DIAL_CODES}
#print("===>1:", country_code)
#print("===>2:", {code: country.upper() for country, code in country_code.items() if code < 66})

## 字典的构造
#a = dict(one=1, two=2, three=3)
#b = {'one': 1, 'two': 2, 'three': 3}
#c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
#d = dict([('two', 2), ('one', 1), ('three', 3)])
#e = dict({'three': 3, 'one': 1, 'two': 2})
#print(a == b == c == d == e)

#from collections import deque
#dq = deque(range(10), maxlen=10)
#print("===>1:", dq)
#dq.rotate(3)
#print("===>2:", dq)
#dq.rotate(-4)
#print("===>3:", dq)
#dq.appendleft(-1)
#print("===>4:", dq)
#dq.extend([11, 22, 33])
#print("===>5:", dq)
#dq.extendleft([10, 20, 30, 40])
#print("===>6:", dq)


#import numpy
#floats = numpy.loadtxt('floats-10M-lines.txt')
#floats[-3:]
#floats *= .5
#floats[-3:]
#from time import perf_counter as pc
#t0 = pc(); floats /= 3; pc() - t0
#numpy.save('floats-10M', floats)
#floats2 = numpy.load('floats-10M.npy', 'r+')
#floats2 *= 6
#floats2[-3:]

#import numpy
#a = numpy.arange(12)
#print("===>1:", a)
#print("===>2:", type(a))
#print("===>3:", a.shape)
#a.shape = 3, 4
#print("===>4:", a)
#print("===>5:", a[2])
#print("===>6:", a[2, 1])
#print("===>7:", a[:, 1])
#print("===>8:", a.transpose())

#import array

#numbers = array.array('h', [-2, -1, 0, 1, 2])
#memv = memoryview(numbers)
#print(len(memv))
#print(memv[0])
#memv_oct = memv.cast('B')
#print(memv_oct.tolist())
#memv_oct[5] = 1
#print(numbers)

#from array import array
#from random import random
#floats = array('d', (random() for i in range(10**7)))
#print(floats[-1])
#fp = open('floats.bin', 'wb')
#floats.tofile(fp)
#fp.close()
#floats2 = array('d')
#fp = open('floats.bin', 'rb')
#floats2.fromfile(fp, 10**7)
#fp.close()
#print(floats2[-1])
#print(floats2 == floats)

#import bisect
#import random
#SIZE=7
#random.seed(1729)
#my_list = []
#for i in range(SIZE):
#    new_item = random.randrange(SIZE*2)
#    bisect.insort(my_list, new_item)
#    print('%2d ->' % new_item, my_list)

#import bisect
#def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
#    i = bisect.bisect(breakpoints, score)
#    print(i)
#    return grades[i]

#print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])

#import bisect
#import sys
#HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
#NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
#ROW_FMT = '{0:2d} @ {1:2d} {2}{0:<2d}'
#def demo(bisect_fn):
#    for needle in reversed(NEEDLES):
#        position = bisect_fn(HAYSTACK, needle)
#        offset = position * ' |'
#        print(ROW_FMT.format(needle, position, offset))

#if __name__ == '__main__':
#    if sys.argv[-1] == 'left':
#        bisect_fn = bisect.bisect_left
#    else:
#        bisect_fn = bisect.bisect
#    print('DEMO:', bisect_fn.__name__)
#    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
#    demo(bisect_fn)

#l = list(range(10))
#print(l)
#l[2:5] = [20, 30]
#print(l)
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
