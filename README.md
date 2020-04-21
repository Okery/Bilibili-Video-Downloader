# Bilibili视频下载器

特点：

- 可下载UP主视频, 支持多P下载
- 可下载番剧、电影, 支持多P下载
- 支持多线程下载, 加速多P下载

注意: 本脚本只是帮助使用者下载使用者原本就能观看的视频. 

如果没有提供大会员的Cookie, 将无法下载大会员专享内容.

如果使用者在大陆, 将无法下载港澳台专享内容.

## 使用要求

- python 3
- requests

## 示例

```
python main.py --url https://www.bilibili.com/video/BVxxxxxxxx --page 1 --quality 3
```
常用：
```
--url, -u: 视频url, 必填
--page, -p: 视频的序号. 默认值为1, 表示下载第1个视频. 如果为0, 则下载所有视频.
--quality, -q: 视频的清晰度档次. 默认值为3, 表示下载第三种清晰度, 一般是720P.
```

其它：
```
--max-workers: 线程数, 默认值为当前cpu核心数的一半.
```
