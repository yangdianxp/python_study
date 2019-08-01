import requests
import json

#api = "eth_getBalance"
#ps = ["0xc71ae22339efa121c3018fdbe788631432da27f2", "latest"]
#url = """https://blockscout.com/etc/mainnet/api?module=account&action=balance&address=0x3bf46a2267b940d4b8b1eac0a8a17528e46135b8"""
#r = requests.post(url, timeout=20)
#res = r.json()
#print(res)

ps = {"module":"account", "action":"balance", "address":"0x3bf46a2267b940d4b8b1eac0a8a17528e46135b8"}
url = """https://blockscout.com/etc/mainnet/api?"""
r = requests.get(url, params=ps, timeout=20)
res = r.json()
print(res)



'''
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
p = {"wd":"flask"}
url_temp = "https://www.baidu.com/s?"

response = requests.get(url_temp, headers=headers, params=p)
print(response.status_code)
print(response.headers)
#print(response.content.decode())
'''

'''
# 以太坊请求交易信息
url_request="http://192.168.0.13:8000"

header_selfdefine = {
    "Content-Type": "application/json"
    }

post_data="{\"id\": 1, \"method\": \"eth_getTransactionByHash\", \"params\": [\"0x9e2c5c5c1a75e82e892d11d1c0f1b50fe43a4b9011192a03d3ca3d537f775a88\"]}\n"
post_data=post_data.encode('utf-8')

response = requests.get(url=url_request,data=post_data, headers=header_selfdefine)
print(response.status_code)
print(response.headers)
print(response.content.decode())
'''
