import requests
from lxml import etree
from pyquery import PyQuery

url = "https://gz.newhouse.fang.com/house/s/"

headers = {
            'Referer': 'https://gz.newhouse.fang.com',
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/74.0.3729.157 Safari/537.36',
            'Host': 'gz.newhouse.fang.com'
}

response = requests.get(url,headers)

#对返回的信息进行初始化，构造一个XPath解析对象
selector = etree.HTML(response.text)

result = selector.xpath('//div[@class="nlcd_name"]//a')

print(result)




#find_all(id="sjina_C22_02")