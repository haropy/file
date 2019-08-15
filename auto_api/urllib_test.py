#:coding:utf-8
import urllib.request

# 请求百度网页
re = urllib.request.urlopen('http://www.baidu.com', data=None, timeout=10)
print(re.info())
