import json

import qrcode
import requests

codeUrl = "https://passport.bilibili.com/x/passport-login/web/qrcode/generate"  # 二维码
checkUrl = "https://passport.bilibili.com/x/passport-login/web/qrcode/poll"  # 获取cookie

header = {
    "user-agent": "'Mozilla/5.0 (Linux; Android 20; MI 8 SE Build/PKQ1.181121.001; wv) AppleWebKit/537.36 (KHTML, "
                  "like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36'", }

#  获取二维码直链和验证码
codeUrlRequest = requests.get(codeUrl, headers=header).text
jsonRequest = json.loads(codeUrlRequest)
jsonCodeUrl = jsonRequest["data"]["url"]
jsonOauthKey = jsonRequest["data"]["qrcode_key"]

#  来，展示！
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=1,
    border=0,
)
qr.add_data(jsonCodeUrl)
qr.make(fit=True)
qr.make_image(fill_color="black", back_color="white")
qr.print_ascii(invert=True)

#  获取返回信息
input("扫码后回车")
requestContext = requests.get(checkUrl, headers=header,
                              params={"qrcode_key": jsonOauthKey}).text
jsonRequestContext = json.loads(requestContext)
if jsonRequestContext["data"]["code"] == 0:
    requestCookie = jsonRequestContext["data"]["url"]
    cookieStr = requestCookie[requestCookie.rfind("?") + 1:]
    cookieList = cookieStr.split("&")
    print(cookieList[0], ";", cookieList[1], ";", cookieList[3], ";", cookieList[4], sep='')
    open("ck.txt", "a+").write(cookieList[0] + ";" + cookieList[1] + ";" + cookieList[3] + ";" + cookieList[4])
    print("已存储")
print(jsonRequestContext["data"]["message"])
