import json
import base64
import requests
from urllib import parse
import hashlib
import time
import random

import logging
import os
from logging.handlers import TimedRotatingFileHandler

def set_logger(fname):
    global logger
    fname = os.path.splitext(fname)[0] + ".log"
    logHandler = TimedRotatingFileHandler(fname, when="MIDNIGHT")
    logFormatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    logHandler.setFormatter(logFormatter)
    logger = logging.getLogger(__name__)
    logger.addHandler(logHandler)
    logger.setLevel(logging.INFO)
    return logger

logger = set_logger(__file__)

def get_req_sign(params, appkey):
    logger.info("params:{}".format(params))
    temp = sorted(params.items(), key = lambda x:x[0])
    str = ""
    for t in temp:
        key = t[0]
        value = t[1]
        if value != '':
            str += "{}={}&".format(key, parse.quote(value))
     
    str += "app_key={}".format(appkey)

    logger.info(str)
    sign = hashlib.md5(str.encode('utf8')).hexdigest().upper()
    logger.info(sign)
    return sign

    

if __name__ == "__main__":
    #data = {
    #    'app_id' : "10000",
    #    'time_stamp' : "1493449657",
    #    'nonce_str' : "20e3408a79",
    #    'key1' : "腾讯AI开放平台",
    #    'key2' : "示例仅供参考",
    #    }
    #print(data)
    #data['sign'] = get_req_sign(data, 'a95eceb1ac8c24ee28b70f7dbba912bf')
    #print(data)


    appid = "2122691474"
    appkey = "sOUiS1rZR9cTHoqu"

    f = open(r'C:\Users\Administrator\Desktop\picture\1570447874(1).png', 'rb')
    picture_data = f.read()
    logger.info("picture_data:{}".format(str(picture_data)))
    binary_data = base64.b64encode(picture_data)
    data_temp = {
        'app_id' : appid,
        'image' : binary_data,
        'nonce_str' : "20e3408a79",
        'time_stamp' : str(int(time.time())),
        # 'nonce_str' : str(int(random.random())),
        }
    data = {
        'app_id' : appid,
        'image' : binary_data,
        'nonce_str' : "20e3408a79",
        'time_stamp' : str(int(time.time())),
        'sign' : get_req_sign(data_temp, appkey),
        # 'nonce_str' : str(int(random.random())),
        }
    logger.info(data)

    url = 'https://api.ai.qq.com/fcgi-bin/ocr/ocr_generalocr'
    # headers = {'Content-Type':'application/x-www-form-urlencoded'}
    res = requests.post(url, data = data)
    logger.info(res.status_code)
    logger.info(res.json())
