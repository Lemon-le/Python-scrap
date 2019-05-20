import requests
from lxml import etree


class Login(object):
    def __init__(self):
        """ Referer: 当浏览器向web服务器发送请求的时候，一般都会带上Referer，告诉服务器我是从哪个页面链接过来的，服务器借此可以获得
            一些信息用于处理，如统计访问量，防外链。
            User-Agent: 模拟浏览器，可以通过在浏览器里输入“chrome://version/”获得用户代理信息
        """
        self.headers = {
            'Referer': 'https://github.com/',
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/74.0.3729.157 Safari/537.36',
            'Host': 'github.com'
        }

        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/session'

        # requests帮助我们维持一个会话，而且可以自动处理Cookies
        self.session = requests.session()

        """ 会话与Cookies
            会话：会话在服务端，也就是网址的服务器，用来保存用户的会话信息；
            Cookies：Cookies在客户端，也可以理解为浏览器端，有了Cookies，浏览器在下次访问网页时会自动附上它发送给服务器；
                     服务器通过识别Cookies并鉴定出是哪个用户，然后再判断用户是否是登录状态，然后返回对应的响应；
                     
                     我们可以理解Cookies里保存了登录的凭证，有了它，只需要在下次请求携带Cookies发送请求而不必重新输入用户名，
                     密码等信息重新登陆了
             
            会话维持：
                   当客户端第一次请求服务器时，服务器会返回一个请求头中带有Set-Cookie字段的响应给客户端，用来标记是哪一个用户，
                   客户端浏览器会把Cookies保存起来。当浏览器下一次请求该网站时，浏览器会把此cookie放到请求头一起提交给服务器，
                   Cookies携带会话ID信息，服务器检查该Cookies即可找到对应的会话是什么，然后再判断会话来以此辨认用户状态。
        """

        # 获取authenticity_token
    def token(self):
        response = self.session.get(self.login_url,headers=self.headers)
        selector = etree.HTML(response.text)
        # token = selector.xpath('//div/input[2]/@value')[0]
        tokens = selector.xpath('//input[2]/@value')
        return tokens

    def login(self,email,password):
        post_data = {
            'commit': 'Sign+in',
            'utf8': '✓',
            'authenticity_token': self.token(),
            'login': email,
            'password': password
        }

        response = self.session.post(self.post_url,data=post_data,headers=self.headers)
        print(response.text)


if __name__ == "__main__":
    login = Login()
    login.login(email="xxxx@qq.com",password="xxxx")

