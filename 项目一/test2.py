# #class Parse(object):
#
# def send_request(url):
#     my_headers = [
#         "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
#         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
#         "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
#         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
#         "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
#         'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
#         'Opera/9.25 (Windows NT 5.1; U; en)',
#         'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
#         'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
#         'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
#         'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
#         "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
#         "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
#     ]
# url = "https://gz.newhouse.fang.com/house/s/"
#
# my_headers = [
#     "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
#     "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
#     'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
#     'Opera/9.25 (Windows NT 5.1; U; en)',
#     'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
#     'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
#     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
#     'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
#     "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
#     "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
# ]
#
# headers = {
#     'Referer': "https://gz.newhouse.fang.com/house/s/",
#     "User-Agent": random.choice(my_headers)
# }
#
# proxies = {
#     'http': 'http://5.141.81.65:61853',
#     'http': '188.92.242.180:52048',
#
# }
#
# session = requests.session()
#
# url = "https://yayunchenggz.fang.com/house/2811801062/housedetail.htm"
# result = session.get(url, headers=headers)
# result.encoding = 'gb2312'
#
# selector = etree.HTML(result.text)
#
# #打印编码
# print(result.encoding)
#
#
#
# #基本信息
# #YouHui = selector.xpath('//div[@class="main-left"]/div[1]/h3/text()')
# #销售信息
# #YouHui = selector.xpath('//div[@class="main-left"]/div[1]/ul/li/div[3]/h3/text()')
# #周边设施
# #YouHui = selector.xpath('//div[@class="main-left"]/div[1]/ul/li/div[4]/h3/text()')
# #小区规划
# #YouHui = selector.xpath('//div[@class="main-left"]/div[1]/ul/li/div[5]/h3/text()')
# #价格信息
# #YouHui = selector.xpath('//div[@class="main-left"]/div[1]/ul/li/div[6]/h3/text()')
# # 项目简介
# #YouHui = selector.xpath('//div[@class="main-left"]/div[1]/ul/li/div[7]/h3/text()')

c = []
a = ['1','2']
b = ['3','4']
c.append(a)
c.append(b)
print(c)