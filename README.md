# Bilibili视频下载器

特点：

- 可下载UP主视频, 番剧 & 电影
- 支持多P下载
- 支持多线程下载
- 可随时停止下载

注意: 本脚本只是帮助使用者下载使用者原本就能观看的视频. 

如果没有提供大会员的 Cookie, 将无法下载大会员专享内容.

如果使用者在大陆, 将无法下载港澳台专享内容.

## 使用要求

- python 3
- requests

## 使用示例

使用前在```main.py```中指定下载路径, 并提供 Cookie:
```
# ---------------下载路径 & Cookie-----------------
DIRNAME = 'E:/downloads'
COOKIE = 'SESSDATA=3f5081db%2C1b02652790%2C8c420*41' # 每月更新一次
# --------------------------------------------------
```

在命令行中, 下载某视频的第 1 部分(1080P):
```
python main.py --url https://www.bilibili.com/video/BVxxxxxxxx --page 1 --quality 4
```

## 参数说明

常用：
```
--url, -u: 视频 url, 必填.
--page, -p: 视频的序号. 默认值为 1, 表示下载第 1 个视频. 如果为 0, 则下载所有视频.
--quality, -q: 视频的清晰度档次. 默认值为 3, 表示下载第三种清晰度, 一般是 720P.
```

高级：
```
--max-workers: 线程数, 默认值为当前 CPU 核心数的一半.
--mode: 模式, 控制脚本行为.
```

## 其它

本 Repo 只是为了学习交流之用, 请勿用于其它途径.

如有问题, 欢迎提 issue.
