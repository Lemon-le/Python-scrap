import requests
from lxml import etree
import random


url = "https://gz.newhouse.fang.com/house/s/"

my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]

headers = {
    'Referer': "https://gz.newhouse.fang.com/house/s/",
    "User-Agent": random.choice(my_headers)
}

proxies = {
    'http': 'http://5.141.81.65:61853',
    'http': '188.92.242.180:52048',
}

session = requests.session()

url = "https://yayunchenggz.fang.com/house/2811801062/housedetail.htm"
result = session.get(url, headers=headers)

# 当requests请求时只会简单的从服务器返回的Content-Type去获取编码，如果有Charset才能正确识别编码，否则就使用默认的ISO-8859-1，
# 这样某些不规范的服务器返回就会乱码了

# 打印返回结果的编码 为ISO-8859-1，说明没有在Content-Type识别到Charset
print(result.encoding)

# 通过requests.utils.get_encodings_from_content函数通过返回的结果获取真正的编码，这里得到结果为gb2312
actually_code = requests.utils.get_encodings_from_content(result.text)
print(actually_code)

# 从上面知道了真正的编码为gb2312，那么直接对requests请求返回的结果进行正确的编码
result.encoding = 'gb2312'

selector = etree.HTML(result.text)

# 价格
price = selector.xpath('//div[@class="main-info-price"]//em/text()')
price_act = price[0].replace('\t','')

print(price_act)
