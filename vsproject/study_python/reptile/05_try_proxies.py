import traceback
import sys
import requests


proxies = {"http": "http://182.34.35.5:14992"}

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        }

def main(argv):
    r = requests.post("http://www.baidu.com", proxies=proxies, headers=headers)
    print(r.status_code)
    # print(r.content.decode())
    
if __name__ == "__main__":
    try:
        main(sys.argv)
    except Exception as result:
        ex_type, ex_val, ex_stack = sys.exc_info()
        print(ex_type)
        print(ex_val)
        for stack in traceback.extract_tb(ex_stack):
            print(stack)

