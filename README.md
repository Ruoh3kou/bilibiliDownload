#urllib实现爬B站视频

本来想下载小英雄第二季视频，结果版权问题无法缓存，遂尝试用PYTHON爬一下试试

##思路:
>利用浏览器F12查看B站播放时XHR请求，筛选合适的请求
>保存请求头
>利用urllib.request.urlretrieve进行下载
结果发现目标视频的请求分成了四次。。也就是说要爬下一个完整视频需要爬四次再合并
我实在太懒于是放弃
实现爬一段，以后有精力再折腾~
