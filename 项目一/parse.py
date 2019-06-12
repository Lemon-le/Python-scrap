# coding=utf-8

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
        # print(self.selector)

    # 基本信息
    def basic_information(self):

        basic = []
        # 楼盘区域
        #aero = self.selector.xpath('//div[@class="topcrumbs"]/a[3]/text()')
        aero = self.selector.xpath('//div[@class="topcrumbs"]/a[3]/text()')
        print(aero)
        if not aero:
            aero.append('暂无')
        aero_act = aero[0]
        basic.append(aero_act)

        # 楼盘名称
        name = self.selector.xpath('//div//a[@class="ts_linear"]/text()')
        # print(name[0])
        name_act = name[0]
        print(name_act)
        basic.append(name_act)

        # 1、价格
        price = self.selector.xpath('//div[@class="main-info-price"]//em/text()')
        price_act = price[0].replace('\t','').replace(' ','').replace('\n','')
        # print(price_act)
        basic.append(price_act)

        # 2、物业类别
        property_type = self.selector.xpath('//div[@class="main-left"]/div[1]/ul[@class="list clearfix"]/li[1]/div[2]/text()')
        if not property_type:
            property_type = ['暂无']
        property_type_act = property_type[0].replace('\t','').replace('\n','').replace(' ','')
        # print(property_type_act)
        basic.append(property_type_act)

        # 3、项目特色
        project_feture = self.selector.xpath('//div[@class="main-left"]/div[1]/ul[@class="list clearfix"]/li[2]/div[2]/span/text()')
        if not project_feture:
            project_feture = ['暂无']

        project_feture_act = ''
        for i in project_feture:
             project_feture_act = project_feture_act + i + " "
        # (project_feture_act)
        basic.append(project_feture_act)


        # 4、建筑类别
        building_category = self.selector.xpath('//div[@class="main-left"]/div[1]/ul[@class="list clearfix"]//span[@class="bulid-type"]/text()')
        if not building_category:
            building_category = ['暂无']
        building_category_act = building_category[0].replace('\t','').replace('\n','')
        # print(building_category_act)
        basic.append(building_category_act)

        # 5、装修状态
        zhuangxiu = self.selector.xpath('//div[@class="main-left"]/div[1]/ul[@class="list clearfix"]/li[2]/div[2]/li[2]/div[2]/text()')
        if not zhuangxiu:
            zhuangxiu = ['暂无']
        zhuangxiu_act = zhuangxiu[0].replace('\t', '').replace('\n','')
        #print(zhuangxiu_act)
        basic.append(zhuangxiu_act)

        # 6、产权年限
        chanquanyear = self.selector.xpath('//div[@class="main-left"]/div[1]/ul[@class="list clearfix"]/li[2]/div[2]/li[3]/div[2]//text()')

        if not chanquanyear:
            chanquanyear = ['暂无']

        chanquanyear_act = ''
        for i in chanquanyear:
            chanquanyear_act = chanquanyear_act + i + ' '
        # print(chanquanyear_act.replace('\t','').replace('\n','').replace(' ',''))
        chanquanyear_act = chanquanyear_act.replace('\t', '').replace('\n', '').replace(' ', '')
        basic.append(chanquanyear_act)

        # 7、环线位置
        huanxian_position = self.selector.xpath('//div[@class="main-left"]/div[1]/ul[@class="list clearfix"]/li[2]/div[2]/li[4]/div[2]/text()')
        if not huanxian_position:
            huanxian_position = ['暂无']

        huanxian_position_act = huanxian_position[0].replace('\t','').replace('\n','').replace(' ','')
        # print(huanxian_position_act)
        basic.append(huanxian_position_act)


        # 8、开发商
        kaifa = self.selector.xpath('//div[@class="main-left"]/div[1]/ul[@class="list clearfix"]/li[2]/div[2]/li[5]/div/a/text()')
        if not kaifa:
            kaifa = ['暂无']


        kaifa_act = kaifa[0]
        # print(kaifa_act)
        basic.append(kaifa_act)

        # 9、楼盘地址
        lpaddress = self.selector.xpath('//div[@class="main-left"]/div[1]/ul[@class="list clearfix"]/li[2]/div[2]/li[6]/div[2]/text()')
        if not lpaddress:
            lpaddress = ['暂无']
        lpaddress_act = lpaddress[0]
        # print(lpaddress_act)
        basic.append(lpaddress_act)
        return basic

    # 销售信息
    def sale_information(self):

        sale = []

        # 1、销售状态
        sale_status = self.selector.xpath('//div[@class="main-left"]/div[1]/ul/li/div[3]/ul/li[1]/div[2]/text()')
        if not sale_status:
            sale_status.append('暂无')
        sale_status_act = sale_status[0].replace('\n', '').replace('\t', '').replace(' ', '')
        sale.append(sale_status_act)

        # 2、优惠信息
        youhui = self.selector.xpath('//div[@class="main-left"]/div[1]/ul/li/div[3]/ul/li[2]/div[2]/text()')
        if not youhui:
            youhui.append('暂无')
        youhui_act = youhui[0].replace('\n', '').replace('\t', '').replace(' ', '')
        sale.append(youhui_act)

        # 3、开盘时间
        KaiPan = self.selector.xpath('//div[@class="main-left"]/div[1]/ul/li/div[3]/ul/li[3]/div[2]/text()')
        if not KaiPan:
            KaiPan.append('暂无')
        KaiPan_act = KaiPan[0].replace('\n', '').replace('\t', '').replace(' ', '')
        sale.append(KaiPan_act)

        # 4、交房时间
        jiaofang = self.selector.xpath('//div[@class="main-left"]/div[1]/ul/li/div[3]/ul/li[4]/div[2]/text()')
        if not jiaofang:
            jiaofang.append('暂无')
        jiaofang_act = jiaofang[0].replace('\n', '').replace('\t', '').replace(' ', '')

        sale.append(jiaofang_act)


        # 5、售楼地址
        sale_address = self.selector.xpath('//div[@class="main-left"]/div[1]/ul/li/div[3]/ul/li[5]/div[2]/text()')
        if not sale_address:
            sale_address.append('暂无')
        sale_address_act = sale_address[0].replace('\n', '').replace('\t', '').replace(' ', '')
        sale.append(sale_address_act)


        # 6、咨询电话
        ZiXun_phone = self.selector.xpath('//div[@class="main-left"]/div[1]/ul/li/div[3]/ul/li[6]/div[2]/text()')
        if not ZiXun_phone:
            ZiXun_phone.append('暂无')
        ZiXun_phone_act = ZiXun_phone[0].replace('\n', '').replace('\t', '').replace(' ', '')
        sale.append(ZiXun_phone_act)



        # 7、主力户型
        HuXing = self.selector.xpath('//div[@class="main-left"]/div[1]/ul/li/div[3]/ul/li[7]/div[@class="list-right-text"]//text()')
        HuXing_act = ''
        for i in HuXing:
            i = i.replace('\n','').replace('\t','').replace('\n\t','')
            HuXing_act = HuXing_act + i
        #print(JiaoFang_Act)
        sale.append(HuXing_act)

        return sale

    # 小区规划
    def Xiaoqu(self):

        xiaoqu = []

        # 占地面积
        zhandi = self.selector.xpath('//div[@class="main-left"]/div[1]/ul/li/div[5]/ul/li[1]/div[@class="list-right"]/text()')

        if not zhandi:
            zhandi = ['暂无']
        zhandi_act = zhandi[0]
        xiaoqu.append(zhandi_act)

        # 建筑面积
        jianzhu = self.selector.xpath('//div[@class="main-left"]/div[1]/ul/li/div[5]/ul/li[2]/div[@class="list-right"]/text()')
        if not jianzhu:
            jianzhu = ['暂无']
        jianzhu_act = jianzhu[0]
        xiaoqu.append(jianzhu_act)

        # 容积率
        rongjilv = self.selector.xpath('//div[@class="main-left"]/div[1]/ul/li/div[5]/ul/li[3]/div[@class="list-right"]/text()')
        if not rongjilv:
            rongjilv = ['暂无']
        xiaoqu.append(rongjilv[0])

        # 绿化率
        lvhua = self.selector.xpath('//div[@class="main-left"]/div[1]/ul/li/div[5]/ul/li[4]/div[@class="list-right"]/text()')
        if not lvhua:
            lvhua = ['暂无']
        xiaoqu.append(lvhua[0])

        # 停车位
        car_stop = self.selector.xpath(
            '//div[@class="main-left"]/div[1]/ul/li/div[5]/ul/li[5]/div[@class="list-right"]/text()')
        if not car_stop:
            car_stop = ['暂无']
        xiaoqu.append(car_stop[0])

        # 楼栋总数：
        loudong_count = self.selector.xpath(
            '//div[@class="main-left"]/div[1]/ul/li/div[5]/ul/li[6]/div[@class="list-right"]/text()')
        if not loudong_count:
            loudong_count = ['暂无']
        xiaoqu.append(loudong_count[0])

        # 总户数：
        all_house = self.selector.xpath(
            '//div[@class="main-left"]/div[1]/ul/li/div[5]/ul/li[7]/div[@class="list-right"]/text()')
        if not all_house:
            all_house = ['暂无']
        xiaoqu.append(all_house[0])

        # 物业公司：
        wy_company = self.selector.xpath(
            '//div[@class="main-left"]/div[1]/ul/li/div[5]/ul/li[8]/div[@class="list-right"]/a/text()')
        if not wy_company:
            wy_company = ['暂无']
        xiaoqu.append(wy_company[0])

        # 物业费：
        wy_cost = self.selector.xpath(
            '//div[@class="main-left"]/div[1]/ul/li/div[5]/ul/li[9]/div[@class="list-right"]/text()')
        if not wy_cost:
            wy_cost = ['暂无']
        xiaoqu.append(wy_cost[0])

        # 物业费描述：
        wy_cost_descri = self.selector.xpath(
            '//div[@class="main-left"]/div[1]/ul/li/div[5]/ul/li[10]/div[@class="list-right-floor"]/text()')
        if not wy_cost_descri:
            wy_cost_descri = ['暂无']
        xiaoqu.append(wy_cost_descri[0])

        # 楼层状况：
        lc_descri = self.selector.xpath(
            '//div[@class="main-left"]/div[1]/ul/li/div[5]/ul/li[11]/div[@class="list-right-floor"]/text()')
        if not lc_descri:
            lc_descri = ['暂无']
        xiaoqu.append(lc_descri[0])

        return xiaoqu

    # 项目简介
    def project_intro(self):
        intro_all = ''
        intro_act = []
        intros = self.selector.xpath('//div[@class="main-item"]//p[@class="intro"]//text()')
        for i in intros:
            intro = i.replace('\t','').replace(' ','')
            intro_all = intro_all + intro
        intro_act.append(intro_all)
        #print(intro_act)
        return intro_act

parse = Parse('https://hengbangyifeng.fang.com/house/2810135144/housedetail.htm')
parse.basic_information()