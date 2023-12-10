# BLM——B站直播监控

### 0x1.食材准备

​	1.`pip install -r requirement.txt`

​	2.添加`cookie`文件，你可以选择执行`login.py`扫码登陆，或在同级目录下新建ck.txt，手动添加cookie文件

​	3.在登录过程中，如果出现二维码无法扫描的场景，可以打开生成的`qrcode.png`进行扫描

​	4.修改直播分区，如果你知道你的直播分区ID，可以直接修改`live.py`中liveid。在不知道分类ID的情况下，可以在终端执行`liveid.py`，选择对应主分区，找到你的分区ID。

### 0x2.食用方法

​	1.请将本项目放在`kplayer`的目录下，确保项目目录为`./kplayer/BLM/live.py`

​	2.如果你使用了宝塔面板或青龙面板，请在面板处添加定时任务

​	3.`crontab`添加定时任务

​		 `crontab -e` 

​		`* * * * * /usr/bin/python3 /path/to/your/live.py`

#### 0x3.遗言

v我50
