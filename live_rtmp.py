import requests, json, re
"""
author: 季博达
English: jjbig
QQ: 1205871479
有问题找他！
"""
def get_live_rtmp_url():
    url = 'https://api.live.bilibili.com/xlive/app-blink/v1/live/FetchWebUpStreamAddr' # 查询直播间推流码
    with open("ck.txt", "r") as f:
        ck = f.read()
    headers = {
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': ck,
            'origin': 'https://link.bilibili.com',
            'referer': 'https://link.bilibili.com/p/center/index',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.9 Safari/537.36'
        }
    pattern = r'bili_jct=([^;]+)'
    matches = re.findall(pattern, ck)
    bili_jct = matches[0]
    data = f'platform=pc&backup_stream=0&csrf_token={bili_jct}&csrf={bili_jct}'
    res = requests.post(url=url,headers=headers,data=data)
    res_data = res.json()
    # 获取addr和code的值
    addr = res_data['data']['addr']['addr']
    code = res_data['data']['addr']['code']
    # 拼接addr和code的值
    url = addr + code
    # 输出拼接后的结果
    #print(url)
    with open('../config.json', 'r') as f:
        config = json.load(f)

    rtmp_url = config['output']['lists'][0]['path']

    config['output']['lists'][0]['path'] = url

    # 将更新后的内容写回到config.json文件中
    with open('../config.json', 'w') as f:
        json.dump(config, f, indent=4)
