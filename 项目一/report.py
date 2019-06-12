#coding = utf8

import matplotlib.pyplot as plt
from db import DB

config = {
    'host': '18.203.153.3',
    'port': 3306,
    'user': 'lile',
    'password': 'Lile@5201314',
    'db': 'ftx',
    'charset': 'utf8'
}
db = DB(config)

sql = "select lp_aero,count(lp_aero) from gz_basic_information where wy_category like ('%住宅%') group by lp_aero"
result = db.select_table(sql)
print(result)


#     result[1][1]: result[1][1],
#     "IO": result[2][1],
#     "memory": result[3][1],
#     "processor": result[4][1],
#     "system": result[5][1],
#     "custom": result[6][1],
#     "custom": result[7][1],
#     "custom": result[8][1],
#     "custom": result[9][1],
#     "custom": result[10][1],
#     "custom": result[11][1],
#     "custom": result[12][1],
#     "custom": result[13][1],
#     "custom": result[14][1],
# }
value_list = {}

for i in result:
    value_list[i[0]] = i[1]
print(value_list)

labels = []
values = []
for key, value in value_list.items():
    if value != 0:
        labels.append(key)
        values.append(value)

colors = ["pink", "coral", "yellow", "orange"]
plt.pie(values, explode=None, colors=None, autopct='%1.2f%%', labels=labels)
plt.title('各区住宅楼盘所占比')
plt.savefig('1.png')

db.close()
