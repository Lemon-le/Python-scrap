'''
urillib是Python内置的Http请求库，包含以下四个模块
1) request: 它是基本的HTTP请求模块，可以用来模拟发送请求
2) error: 异常处理模块，如果出现请求错误，我们可以捕获这些异常，然后进行重试或者其他操作以保证程序不会意外终止
3) parse: 工具模块，提供了许多URL处理方法，如拆分、解析、合并
4) robotparser: 用来识别网站的robots.txt文件，然后判断哪些网站可以爬，哪些不可以爬

'''



from urllib import request,parse
import socket


def urlopenTest():
    ''' urllib的request模块，可以方便的实现请求的发送并得到响应'''
    response = request.urlopen('https://www.python.org')
    #print(response.read().decode('utf-8'))

    #打印响应的类型
    print(type(response))
    '''可以发现他是一个HTTPResponse类型的对象，主要包含read()、readinto()、gatheader(name)、getheaders()、fileno()等方法
       以及msg、version、status、reason、debuglevel、closed等属性
    '''

    #调用read()方法得到返回的网页内容
    print(response.read())

    #调用status属性得到返回结果的状态码
    print(response.status)

    #调用getheaders()方法得到响应的头信息
    print(response.getheaders())

    #调用getheader()方法得到响应头里的某个值
    print(response.getheader('Server'))


def urlopenTimeout():
   '''urllib.request.urlopen()除了传递url后，还可以传递其他的参数，如data、timeout等;
    timeout如果超时了，会抛出一个URLError的错误
      可以通过设置这个超时时间来控制一个网页如果长时间未响应，就跳过他的抓取，可以使用try except语句来实现
   '''

   try:
       response = request.urlopen('https://wwl.com',timeout=1)
   except request.error.URLError as e:
       #isinstance() 如果参数1的类型是参数二的类型
       if isinstance(e.reason,socket.timeout):
           print('Time out')


def RequestTest():
    '''利用urlopen()方法可以实现最基本请求的发起，但这个简单的参数并不足以构建一个完整的请求，如果请求中需要加入Headers信息，就可以使用更强大的Request类来构建'''
    requests = request.Request('https://python.org')
    response = request.urlopen(request)
    print(response.read().decode('utf-8'))

'''添加请求头最常用的方法就是通过修改User-Agent来伪装浏览器，默认的User-Agent是Python-urllib，可以通过修改他来伪装浏览器'''

def RequestTests():
    url = 'https://baidu.com/post'
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE S. S; Windows NT)',
      #  'Host': 'python.org'
    }
    dict = {
        'name':'lile'
    }

    data = bytes(parse.urlencode(dict),encoding='utf8')
    req = request.Request(url=url,data=data,headers=headers,method='POST')
    response=request.urlopen(req)
    print(response.read().decode('utf-8'))

RequestTests()





