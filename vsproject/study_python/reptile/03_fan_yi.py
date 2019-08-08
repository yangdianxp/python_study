import traceback
import sys
import requests

data = {
    "address": "2khEheVH5hqCLEjvMFrvhiovQUHw",
    "coin": "lkl",
}

post_url = "https://api.coints.io/api/data/is_addr"
#url = """https://www.baidu.com"""
get_url = "https://api.coints.io/api/data/is_addr?address=3h1pxo67SAAY7U5S2UULgFatSPhH"

def main(argv):
    # r = requests.post(post_url, data=data)
    r = requests.get(get_url)
    print(r.status_code)
    print(r.content.decode())
    print(r.text)
    
if __name__ == "__main__":
    try:
        main(sys.argv)
    except Exception as result:
        ex_type, ex_val, ex_stack = sys.exc_info()
        print(ex_type)
        print(ex_val)
        for stack in traceback.extract_tb(ex_stack):
            print(stack)
