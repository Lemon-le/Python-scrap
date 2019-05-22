from lxml import etree


#读取HTML文本进行解析
def test1():
    text='''
    <div>
        <ul>
             <li class="item-0"><a href="link1.html">第一个</a></li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0"><a href="link5.html">a属性</a>
         </ul>
     </div>
    '''

    #初始化生成一个XPath解析对象
    html = etree.HTML(text)

    #解析对象输出
    result = etree.tostring(html)
    print(type(html))
    print(type(result))
    print(result.decode('utf-8'))


#读取HTML文件进行解析
def test2():
    #etree.HTMLParse()指定解析器HTMLParse会根据文件修复HTML文件中缺失的信息，如申明信息
    html = etree.parse('test.html',etree.HTMLParser())
    #tostring()方法可输出修正后的HTML代码，但结果是bytes类型，使用decode()方法将其转换成str类型
    result = etree.tostring(html)
    print(type(html))
    print(type(result))
    print(result.decode('utf-8'))

#获取所有的节点
def test3():
    html=etree.parse("test.html",etree.HTMLParser())
    #这里的*代表匹配所有节点，也就是整个HTML文本中的所有节点都会被获取；返回得到的是一个列表
    #每个元素是Element类型，其后跟了节点的名称
    result=html.xpath('//*')
    print(type(result))
    print(type(html))
    print(result)


#获取指定节点名称的节点
def test4():
    html=etree.parse('test.html',etree.HTMLParser())
    result=html.xpath('//li')
    print(result)
    print(result[1])


#获取子节点
def test5():
    html=etree.parse('test.html',etree.HTMLParser())
    result=html.xpath('//li/a')
    print(result)


#获取父节点
#知道了子节点，获取父节点
def test6():
    html=etree.parse('test.html',etree.HTMLParser())
    result=html.xpath('//a[@href="link1.html"]/../@class')
    result1=html.xpath('//a[@href="link1.html"]/parent::*/@class')
    print(result)
    print(result1)

#属性匹配
def test7():
    html=etree.parse('test.html',etree.HTMLParser())
    result=html.xpath('//li[@class="item-0"]')
    print(result)

#文本获取
def test8():
    html=etree.parse('test.html',etree.HTMLParser())
    result=html.xpath('//li[@class="item-0"]//text()')
    print(result)

#属性获取
def test9():
    html=etree.parse('test.html',etree.HTMLParser())
    result=html.xpath('//li/a/@href')
    print(result)

#属性多值匹配
def test10():
    html=etree.parse('test.html',etree.HTMLParser())
    result=html.xpath('//li[contains(@class,"item-2")]/a/text()')
    print(result)

#属性属性匹配
def test10():
    html=etree.parse('test.html',etree.HTMLParser())
    result=html.xpath('//li[contains(@class,"item-2") and @name="aa"]/a/text()')
    print(result)
test10()
