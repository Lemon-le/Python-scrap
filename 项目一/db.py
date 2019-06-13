import pymysql


class DB(object):

    def __init__(self, config):
        self.host = config['host']
        self.port = config['port']
        self.user = config['user']
        self.password = config['password']
        self.db = config['db']
        self.charset = config['charset']

        # 连接数据库
        self.db = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db,
            charset=self.charset
        )

        # 创建一个游标
        self.cursor = self.db.cursor()

    def insert_table(self, sql):
        try:
            result = self.cursor.execute(sql)
            self.db.commit()
            return result
        except Exception as e:
            print(e)

    def delete_table(self,sql):
        try:
            result = self.cursor.execute(sql)
            self.db.commit()
            return result
        except Exception as e:
            print(e)
            self.db.rollback()

    def update_table(self,sql):
        try:
            result = self.cursor.execute(sql)
            self.db.commit()
            return result
        except Exception as e:
            print(e)
            self.db.rollback()

    def select_table(self, sql):
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(e)

    def close(self):
        self.cursor.close()
        self.db.close()



