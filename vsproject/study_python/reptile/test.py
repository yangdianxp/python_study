from splinter import Browser

# "C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe"
# executable_path = {'executable_path':r"""C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe"""}
browser = Browser("chrome")
browser.visit('http://www.baidu.com')
browser.fill('q', 'splinter - python acceptance testing for web applications')
browser.find_by_name('btnG').click()

if browser.is_text_present('splinter.readthedocs.io'):
    print("Yes, the official website was found!")
else:
    print("No, it wasn't found... We need to improve our SEO techniques")

browser.quit()



'''
import requests
import json
# 字典推导式应用
cookies = "BIDUPSID=F8C5081723C7DDD5E0D68A9EC55C2C83; PSTM=1545314080; BD_UPN=12314353; __cfduid=dd9578bc449a9c83acedefb820902535b1552619203; BAIDUID=033137D7E09CE69C4AFC5F92B0BBBF4A:FG=1; BDUSS=jJEZTRaTUdWZXpRV3Z4RjhIa25uRG9SY2RXS3dJWld-VUVYSDhlU0F3NnY1VTlkSVFBQUFBJCQAAAAAAAAAAAEAAAAjFHMsZGl1ZGl1ZGl1bmljZQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK9YKF2vWChdU; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; yjs_js_security_passport=0823cb407687584c26f2ed91cf59da12be47a3be_1564637908_js; H_PS_PSSID=1425_21123_29522_29520_29098_29568_28836_29221_26350_29458; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=6; BD_HOME=1; COOKIE_SESSION=33282_0_7_6_4_7_0_0_6_5_2_0_0_0_0_0_1564544165_0_1564660250%7C9%235313_175_1564043661%7C9"
cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
print(cookies)
'''

'''
# 
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
