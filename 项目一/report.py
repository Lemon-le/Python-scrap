#coding = utf8

import matplotlib.pyplot as plt
from db import DB

import pandas as pd

class Report(object):
    def __init__(self, config):
        self.db = DB(config)

    def aero_pie(self, sql, title, save_filename):

        result = self.db.select_table(sql)

        value_list = {}

        for i in result:
            value_list[i[0][:-2]] = i[1]
        print(value_list)

        labels = []
        values = []
        for key, value in value_list.items():
            if value != 0:
                labels.append(key)
                values.append(value)

        plt.tight_layout()
        plt.pie(values, explode=None, colors=None, autopct='%1.2f%%', labels=labels) #pctdistance=1.3  autopct='%1.2f%%',labeldistance=1.1, pctdistance=1.5
        plt.title(title)
        plt.savefig(save_filename)

        self.db.close()

    def top_ten(self, sql, columns):
        result = self.db.select_table(sql)
        row1 = []
        row2 = []
        row3 = []
        row4 = []

        for every_one in result:
            row1.append(every_one[0])
            row2.append(every_one[1])
            row3.append(every_one[2])
            row4.append(every_one[3])

        raw_data = {'columns[0]':row1, 'columns[0]':row2, 'columns[0]':row3, 'columns[0]':row4}
        pd.DataFrame(raw_data, columns=columns)
        print(pd)
        self.db.close()




if __name__ == "__main__":
    config = {
        'host': '18.203.153.3',
        'port': 3306,
        'user': 'lile',
        'password': 'Lile@5201314',
        'db': 'ftx',
        'charset': 'utf8'
    }

    reports = Report(config=config)

    # 区域占比
    sql = "select lp_aero,count(lp_aero) from ld_basic_information where wy_category like ('%住宅%') group by lp_aero"
    title = '区域房源占比（住宅）'
    save_filename = '区域房源占比.png'
    reports.aero_pie(sql=sql, title=title, save_filename=save_filename)

    # # 前10
    # columns = ['区域', '楼盘', '均价', '楼盘地址']
    # sql = "select lp_aero,lp_name,lp_price,lp_adress from gz_basic_information where wy_category like ('%普通住宅%') ORDER BY cast(lp_price as SIGNED) desc  limit 10"
    # reports.top_ten(sql, columns)



# http://www.pythoner.com/200.html 解决乱码问题