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
import re

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

def match_string(find_str, target_str):
    res = bool(re.search(find_str, target_str))
    return res

if __name__ == "__main__":
    #image = ImageGrab.grab()
    #print(image.size)
    #width = image.size[0]
    #height = image.size[1]

    ##box = (int(width / 5 * 2), int(height / 5 * 2), int(width / 5 * 3), int(height / 5 * 4))
    ##print(box)
    ##region = image.crop(box)
    ##region.show()

    #region = image

    #output_buffer = BytesIO()
    #region.save(output_buffer, format='png')
    #binary_data = output_buffer.getvalue()
    #binary_data = base64.b64encode(binary_data)

    f = open(r'C:\Users\Administrator\Desktop\picture\1570447874(1).png', 'rb')
    binary_data = base64.b64encode(f.read())

    """ 你的 APPID AK SK """
    APP_ID = '17455795'
    API_KEY = '2eRyuVgd1ohtNMeszaCpK6jl'
    SECRET_KEY = 'fXIh5POUXAmerYa6t42kQoNmGPIUNuVc'

    headers = {'Content-Type':'application/json',
                'charset':'UTF-8'}
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=2eRyuVgd1ohtNMeszaCpK6jl&client_secret=fXIh5POUXAmerYa6t42kQoNmGPIUNuVc'
    res = requests.post(host, headers=headers)
    token = res.json()["access_token"]
    print(token)

    #token = '24.36bd551d0bff8e5a746f670bf04ccac7.2592000.1573054545.282335-17455795'

    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=' + token
    # url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate?access_token=' + token
    data = {"image": binary_data}
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    res = requests.post(url, headers=headers, data=data)
    print(res.status_code)
    print(res.json())

    #word_location = {}
    #words_result = res.json()['words_result']
    #for w in words_result:
    #    if match_string("邮箱帐号或手机号码", w['words']):
    #        word_location["邮箱帐号或手机号码"] = w["location"]
    #    elif match_string("输入密码", w['words']):
    #        word_location["输入密码"] = w["location"]
    #    elif match_string("免登录", w['words']):
    #        word_location["免登录"] = w["location"] 
    #    elif match_string("登录", w['words']):
    #        word_location["登录"] = w["location"] 

    #print(word_location)

    ## 修饰鼠标点击位置
    #mouse_click_location = {}
    #for w in word_location.keys():
    #    x_pos = int(word_location[w]["left"] + word_location[w]["width"] / 2)
    #    y_pos = int(word_location[w]["top"] + word_location[w]["height"] / 2)
    #    mouse_click_location[w] = (x_pos, y_pos)
    #print(mouse_click_location)
        
    ## 邮箱账号
    #account = "yangdianxp"
    #passwd = "sbaukoige"
    #mouse_click(mouse_click_location["邮箱帐号或手机号码"][0], mouse_click_location["邮箱帐号或手机号码"][1])
    #key_autinput(account)
    #mouse_click(mouse_click_location["输入密码"][0], mouse_click_location["输入密码"][1])
    #key_autinput(passwd)
    #mouse_click(mouse_click_location["免登录"][0], mouse_click_location["免登录"][1])  
    #mouse_click(mouse_click_location["登录"][0], mouse_click_location["登录"][1]) 
