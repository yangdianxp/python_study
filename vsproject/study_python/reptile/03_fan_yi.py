import traceback
import sys
import requests

headers = {
    "User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36",
        }

data = {
    "from": "zh",
    "to": "en",
    "query": "你好世界",
}

post_url = "http://fanyi.baidu.com/basetrans"


def main(argv):
    r = requests.post(post_url, data=data, headers=headers)
    print(r.content.decode())
    
if __name__ == "__main__":
    try:
        main(sys.argv)
    except Exception as result:
        ex_type, ex_val, ex_stack = sys.exc_info()
        print(ex_type)
        print(ex_val)
        for stack in traceback.extract_tb(ex_stack):
            print(stack)
