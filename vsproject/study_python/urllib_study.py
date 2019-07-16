import urllib.request

url_request="http://192.168.0.13:8000"

header_selfdefine = {
    "Content-Type": "application/json"
    }

post_data="{\"id\": 1, \"method\": \"eth_getTransactionByHash\", \"params\": [\"0x9e2c5c5c1a75e82e892d11d1c0f1b50fe43a4b9011192a03d3ca3d537f775a88\"]}\n"
post_data=post_data.encode('utf-8')

request_obj=urllib.request.Request(url=url_request,data=post_data, headers=header_selfdefine)
response_obj=urllib.request.urlopen(request_obj)
html_code=response_obj.read().decode('utf-8')
print(html_code)
