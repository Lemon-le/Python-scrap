# requests的cookies与session的用法
# https://www.programcreek.com/python/example/18310/requests.Session
# https://2.python-requests.org//zh_CN/latest/user/advanced.html

import requests
import sys

# 发送请求可能会发生的错误
# 1、网络无法链接，本机无法上网
# 1、网页在服务器不存在
# 2、服务器不存在
# 3、请求链接异常

# 请求链接异常
try:
    r = requests.get("http://www.ythonscraping.com/pages/page002.html")
    print(r.raise_for_status())
    print(r)
except requests.exceptions.HTTPError as e:
    print("b")
except requests.exceptions.ConnectionError:

    print("网络异常, 可能出现的情况如下: \n"
          "1、本机网络异常, 检查本机网络是否可用\n"
          "2、请求地址错误, 检查请求地址的正确性\n"
          "3、请求地址是否需要翻墙\n"
          "4、访问请求地址次数过多, 拒绝访问, 可采用使用代理等方式尝试解决")
    raise
    sys.exit(1)
