import requests
requests.packages.urllib3.disable_warnings()
headers={
'Host': 'common-mini.okaoyan.com',
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-N960F Build/JLS36C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 MicroMessenger/7.0.12.1620(0x27000C50) Process/appbrand0 NetType/WIFI Language/zh_CN ABI/arm32',
'charset': 'utf-8',
'x-tag': 'flyio',
'authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI5OTAgMTU4NjE4NjU2NjM2NCJ9.lR-p40HA7vycsLqs-9KqI69sdbfMNqJ39rJQfA5CbkE',
'Accept-Encoding': 'gzip,compress,br,deflate',
'content-type': 'application/json'
}
base_url='https://common-mini.okaoyan.com/api/adjust/info/list?province_name=&university_name=&major_name=&learn_style=&page_num=2&page_size=20&year=2020'
req_url ='https://common-mini.okaoyan.com/api/adjust/info/list?province_name=&university_name=&major_name=&learn_style=&page_num=2&page_size=20&year=2020'

# https://customer.okaoyan.com/api/v1/wechat_nos/random?channel_id=4
# https://common-mini.okaoyan.com/api/adjust/info/244768

req_url2='https://common-mini.okaoyan.com/api/adjust/info/244811'
resp = requests.get(url=req_url2,headers=headers,verify=False)
# print(resp.status_code)
# print(resp.text)
