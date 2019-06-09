import xlwt


class Excel(object):

    # 创建excel
    @staticmethod
    def create_excel(path, row0, list_data):

        # path: 创建excel路径
        # row0: excel表头行
        # list_data: 将要写入的数据，列表里嵌入列表

        # 创建工作簿
        workbook = xlwt.Workbook(encoding='utf-8')

        # 创建sheet
        data_sheet = workbook.add_sheet('广州')

        # 创建表头行
        for i in range(len(row0)):
            data_sheet.write(0, i, row0[i])

        j = 1

        for list_ele in list_data:
            print(list_ele)
            for i in range(len(list_ele)):
                data_sheet.write(j, i, list_ele[i])
            j = j + 1
        workbook.save(path)



# if __name__ == '__main__':
#     write_fang = Excel()
#     write_fang.write_excel('E:\scrap_data\HousePrice.xls')

 # row0 = [
    #     u'楼盘名称', u'价格', u'物业类别', u'项目特色', u'建筑类别', u'装修状态', u'产权年限', u'环线位置', u'开发商', u'楼盘地址',
    #     u'销售状态', u'优惠信息', u'开盘时间', u'交房时间', u'售楼地址', u'咨询电话', u'主力户型',
    #     u'占地面积', u'建筑面积', u'容积率', u'绿化率', u'停车位', u'楼栋总数', u'总户数', u'物业公司', u'物业费',
    #     u'物业费描述', u'楼层状况', u'项目简介'
    # ]
    # path = 'E:\scrap_data\HousePrice.xls'
    # Excel.create_excel(path, row0, all_result)