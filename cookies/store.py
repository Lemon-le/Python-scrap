import random
import redis

class RedisClient(object):
    # 初始化redis连接
    def __init__(self,type,website,host=REDIS_HOST,port=REDIS_PORT,password=redis_password):
        """
        type: 表示Key组成的一部分
        website: 表示Key组成的第二部分
        host: 地址
        port: 端口
        password: 密码
        """
        # redis.StrictRedis()方法表示与redis建立连接
        self.db = redis.StrictRedis(host=host,port=port,password=password,decode_responses=True)
        self.type = type
        self.website = website

    #获取Hash的名称
    def name(self):
        """ str.format() 格式化字符串，可以快速处理各种字符串
            "my name is {name}".format(name="lile")    output==>  my name is lile
            "my name is {}".format('lile')             output==>  my name is lile
        """
        return "{type}:{website}".format(type=self.type,website=self.website)

    #根据键名获取键值
    def get(self,username):
        return self.db.hget(self.name(),username)

    #根据键名删除键值对
    def delete(self,username):
        return self.db.hdel(self.name(),username)

    #获取数目
    def count(self):
        return self.db.hlen(self.name())

    #随机得到键值，用于随机Cookies获取
    def random(self):
        # hvals()获取指定域的所有值
        return random.choice(self.db.hvals(self.name()))

    #获取所有用户信息
    def usernames(self):
        return self.db.hkeys(self.name())

    #获取所有键值对
    def all(self):
        return self.db.hgetall(self.name())





