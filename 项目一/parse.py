import requests
from lxml import etree
import random

class Parse(object):

    def __init__(self,url):


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
        self.url = url
        self.result = session.get(url, headers=headers)
        self.result.encoding = 'gb2312'

        self.selector = etree.HTML(self.result.text)
        #print(self.selector)





    # 基本信息
    def basic_information(self):

        basic = []

        # 楼盘名称
        name = self.selector.xpath('//div//a[@class="ts_linear"]/text()')
        # print(name[0])
        name_act = name[0]
        basic.append(name_act)

        # 1、价格
        price = self.selector.xpath('//div[@class="main-info-price"]//em/text()')
        price_act = price[0].replace('\t','').replace(' ','').replace('\n','')
        # print(price_act)
        basic.append(price_act)

        # 2、物业类别
        property_type = self.selector.xpath('//div[@class="main-left"]/div[1]/ul[@class="list clearfix"]/li[1]/div[2]/text()')
        property_type_act = property_type[0].replace('\t','').replace('\n','').replace(' ','')
        # print(property_type_act)
        basic.append(property_type_act)

        # 3、项目特色
        project_feture = self.selector.xpath('//div[@class="main-left"]/div[1]/ul[@class="list clearfix"]/li[2]/div[2]/span/text()')
        project_feture_act = ''
        for i in project_feture:
             project_feture_act = project_feture_act + i + " "
        # (project_feture_act)
        basic.append(project_feture_act)


        # 4、建筑类别
        building_category = self.selector.xpath('//div[@class="main-left"]/div[1]/ul[@class="list clearfix"]//span[@class="bulid-type"]/text()')
        building_category_act = building_category[0].replace('\t','').replace('\n','')
        # print(building_category_act)
        basic.append(building_category_act)

        # 5、装修状态
        zhuangxiu = self.selector.xpath('//div[@class="main-left"]/div[1]/ul[@class="list clearfix"]/li[2]/div[2]/li[2]/div[2]/text()')
        zhuangxiu_act = zhuangxiu[0].replace('\t', '').replace('\n','')
        #print(zhuangxiu_act)
        basic.append(zhuangxiu_act)

        # 6、产权年限
        chanquanyear = self.selector.xpath('//div[@class="main-left"]/div[1]/ul[@class="list clearfix"]/li[2]/div[2]/li[3]/div[2]//text()')
        chanquanyear_act = ''
        for i in chanquanyear:
            chanquanyear_act = chanquanyear_act + i + ' '
        # print(chanquanyear_act.replace('\t','').replace('\n','').replace(' ',''))
        chanquanyear_act = chanquanyear_act.replace('\t', '').replace('\n', '').replace(' ', '')
        basic.append(chanquanyear_act)

        # 7、环线位置
        huanxian_position = self.selector.xpath('//div[@class="main-left"]/div[1]/ul[@class="list clearfix"]/li[2]/div[2]/li[4]/div[2]/text()')
        huanxian_position_act = huanxian_position[0].replace('\t','').replace('\n','').replace(' ','')
        # print(huanxian_position_act)
        basic.append(huanxian_position_act)


        # 8、开发商
        kaifa = self.selector.xpath('//div[@class="main-left"]/div[1]/ul[@class="list clearfix"]/li[2]/div[2]/li[5]/div/a/text()')
        kaifa_act = kaifa[0]
        # print(kaifa_act)
        basic.append(kaifa_act)

        # 9、楼盘地址
        lpaddress = self.selector.xpath('//div[@class="main-left"]/div[1]/ul[@class="list clearfix"]/li[2]/div[2]/li[6]/div[2]/text()')
        lpaddress_act = lpaddress[0]
        # print(lpaddress_act)
        basic.append(lpaddress_act)

        return basic

    # 销售信息

    def SaleInformation(self):

        sale = []

        #1、销售状态,优惠信息,开盘时间,交房时间,售楼地址,咨询电话,主力户型
        JiaoFang = self.selector.xpath('//div[@class="main-left"]/div[1]/ul/li/div[3]/ul/*')

        for i in range(1,len(JiaoFang)-1):
           # print(self.selector.xpath('//div[@class="main-left"]/div[1]/ul/li/div[3]/ul/li[' + str(i) + ']/div[2]/text()')[0].replace('\n', '').replace('\t', '').replace(' ', ''))
            result = self.selector.xpath('//div[@class="main-left"]/div[1]/ul/li/div[3]/ul/li[' + str(i) + ']/div[2]/text()')
            if not result:
                result = [' ']
            sale.append(result[0].replace('\n', '').replace('\t', '').replace(' ', ''))


        #主力户型
        JiaoFang = self.selector.xpath('//div[@class="main-left"]/div[1]/ul/li/div[3]/ul/li[7]/div[@class="list-right-text"]//text()')
        JiaoFang_Act = ''
        for i in JiaoFang:
            i = i.replace('\n','').replace('\t','').replace('\n\t','')
            JiaoFang_Act = JiaoFang_Act + i
        #print(JiaoFang_Act)
        sale.append(JiaoFang_Act)

        #print(sale)
        return sale

    #小区规划

    def Xiaoqu(self):

        xiaoqu = []

        XiaoQu = self.selector.xpath('//div[@class="main-left"]/div[1]/ul/li/div[5]/ul/li/div[2]//text()')

        if len(XiaoQu) != 11:
            for i in XiaoQu:
                if not i:
                    i = ' '
                xiaoqu.append(i)

        print(xiaoqu)
        # return xiaoqu

    # 项目简介
    def project_intro(self):
        intro_all = ''
        intro_act = []
        intros = self.selector.xpath('//div[@class="main-item"]//p[@class="intro"]//text()')
        for i in intros:
            intro = i.replace('\t','').replace(' ','')
            intro_all = intro_all + intro
        intro_act.append(intro_all)
        # print(intro_act)
        return intro_act

#
parse = Parse('https://dazhuangmingcheng.fang.com/house/2811173750/housedetail.htm')
parse.Xiaoqu()