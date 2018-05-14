import sys
import ssl
import urllib.request

#利用浏览器，播放视频，查看network，捕获到请求，保留requests-headers
"""
GET /upgcxcode/98/96/38759698/38759698-1-64.flv?e=ig8euxZM2rNcNbNMhWKVhoMMnwN3hwdEto8g5X10ugNcXBlqNxHxNEVE5XREto8KqJZHUa6m5J0SqE85tZvEuENvNC8xNEVE9EKE9IMvXBvE2ENvNCImNEVEK9GVqJIwqa80WXIekXRE9IB5QK==&deadline=1526313999&dynamic=1&gen=playurl&hfb=Yjk5ZmZjM2M1YzY4ZjAwYTMzMTIzYmIyNWY4ODJkNWI=&oi=3664420200&os=ks3&platform=pc&rate=241400&trid=0e8b3355fd9645cfb07049de59375484&uipk=5&uipv=5&um_deadline=1526313999&um_sign=4b6210edb469dbb140c3953cfe4d8a7d&upsig=ff46a3e50dcf7ce977e03a6344f0f71d HTTP/1.1
Host: upos-hz-mirrorks3.acgvideo.com
Connection: keep-alive
Origin: https://www.bilibili.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36
Accept: */*
Referer: https://www.bilibili.com/bangumi/play/ep205865/?t=1431
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Range: bytes=2726-
"""

def report(count, blockSize, total):
    #显示进度
    Sizeed = count * blockSize
    percent = int(Sizeed * 100 / total)
    sys.stdout.write(
        f"\r 下载中………… 视频大小: {total} bytes, 进度 {percent} % ")
    sys.stdout.flush()


if __name__ == '__main__':
    # SSL证书
    ssl._create_default_https_context = ssl._create_unverified_context
    # Request URL
    url = 'https://upos-hz-mirrorks3.acgvideo.com/upgcxcode/98/96/38759698/38759698-1-64.flv?e=ig8euxZM2rNcNbNMhWKVhoMMnwN3hwdEto8g5X10ugNcXBlqNxHxNEVE5XREto8KqJZHUa6m5J0SqE85tZvEuENvNC8xNEVE9EKE9IMvXBvE2ENvNCImNEVEK9GVqJIwqa80WXIekXRE9IB5QK==&deadline=1526313999&dynamic=1&gen=playurl&hfb=Yjk5ZmZjM2M1YzY4ZjAwYTMzMTIzYmIyNWY4ODJkNWI=&oi=3664420200&os=ks3&platform=pc&rate=241400&trid=0e8b3355fd9645cfb07049de59375484&uipk=5&uipv=5&um_deadline=1526313999&um_sign=4b6210edb469dbb140c3953cfe4d8a7d&upsig=ff46a3e50dcf7ce977e03a6344f0f71d'

    opener = urllib.request.build_opener()
    #请求头
    opener.addheaders = [
        ('Host', 'upos-hz-mirrorks3.acgvideo.com'),
        ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'),
        ('Accept', '*/*'),
        ('Accept-Language', 'zh-CN,zh;q=0.9'),
        ('Accept-Encoding', 'gzip, deflate, br'),
        ('Range', 'bytes=0-'), 
        ('Referer', 'https://www.bilibili.com/bangumi/play/ep205865/?t=1431'),
        ('Origin', 'https://www.bilibili.com'),
        ('Connection', 'keep-alive'),
    ]
    urllib.request.install_opener(opener)

    urllib.request.urlretrieve(url, filename='小英雄第一集.flv', reporthook=report)
