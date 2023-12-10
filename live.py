import json
import re
import subprocess

import psutil
import requests

liveid = '624'  # 填写直播分类id
roomid = '7681777' #填写房间号

def is_process_running(process_name):
    """
    判断指定名称的进程是否存在
    """
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return True
    return False


urlStatus = f"https://api.live.bilibili.com/xlive/web-room/v1/index/getRoomBaseInfo?room_ids={roomid}&req_biz=link-center"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.9 '
                  'Safari/537.36'
}
response = requests.request("GET", urlStatus, headers=headers)

result = json.loads(response.text)
roomid = result['data']["by_room_ids"]
index, value = next(iter(roomid.items()))
status = value["live_status"]
if status == 2:
    with open("ck.txt", "r") as f:
        ck = f.read()
    pattern = r'bili_jct=([^;]+)'
    matches = re.findall(pattern, ck)
    bili_jct = matches[0]
    urlStart = "https://api.live.bilibili.com/room/v1/Room/startLive"
    payload = f"room_id={index}&platform=pc&area_v2={liveid}&backup_stream=0&csrf_token={bili_jct}&csrf={bili_jct}"
    headers = {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': ck,
        'origin': 'https://link.bilibili.com',
        'referer': 'https://link.bilibili.com/p/center/index',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.9 Safari/537.36'
    }
    requests.request("POST", urlStart, headers=headers, data=payload)

    # 调用函数检查进程是否存在
    if is_process_running('kplayer'):
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == 'kplayer':
                try:
                    # 使用terminate方法终止进程
                    psutil.Process(process.info['pid']).terminate()
                except Exception as e:
                    print(f"无法终止进程: {e}")

    command = "../kplayer play start --daemon"

    subprocess.Popen(command, shell=True)

    exit("我滴任务完成辣")