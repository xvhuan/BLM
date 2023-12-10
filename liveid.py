import os

import requests

url = "https://api.live.bilibili.com/room/v1/Area/getList?show_pinyin=1"

headers = {
    'authority': 'api.live.bilibili.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'dnt': '1',
    'origin': 'https://link.bilibili.com',
    'pragma': 'no-cache',
    'referer': 'https://link.bilibili.com/p/center/index',
    'sec-ch-ua': '"Not A(Brand";v="99", "Chromium";v="22"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.9 Safari/537.36'
}

response = requests.request("GET", url, headers=headers)
a = 1
for i in response.json()["data"]:
    print(str(a)+"."+i["name"])
    a+=1
id = int(input("请输入对应序号进行查询"))
os.system("clear")
for i in response.json()["data"][id-1]["list"]:
    print(i["id"]+"."+i["name"])
