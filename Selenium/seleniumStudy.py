'''
Selenium是一个自动化测试工具，利用它可以驱动浏览器执行特定的动作，如点击、下拉等操作
同时还可以获取浏览器当前呈现的页面的源代码，做到可见即可爬。

'''

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.wait import  WebDriverWait

""" 一、声明浏览器对象
# 声明浏览器对象，Selenium支持非常多的浏览器，如Chrome、Firefox、Edge，还有手机端的浏览器、也支持无界面浏览器PhantomJS
# 使用以下方式初始化,这样完成了浏览器的初始化并将值赋值给broswer对象，接下来就是调用broswer对象，让其执行各个动作以模拟浏览器操作
# browser = webdriver.Firefox()
# browser = webdriver.Edge()
# browser = webdriver.PhantomJS()
# browser = webdriver.Safari()
"""
browser = webdriver.Chrome()

""" 二、访问页面
# 访问页面，使用get()方法来访问页面，参数传入链接URL，这里使用get()方法访问淘宝，然后打印出源代码
# 打开百度
"""
#browser.get('https://www.taobao.com')
#print(browser.page_source)
#browser.close()



""" 三、获取单个节点
# 所有获取单个节点的方法
# find_element_by_id
# find_element_by_xpath
# find_element_by_name
# find_element_by_link_text
# find_element_by_partial_link_text
# find_element_by_tag_name
# find_element_by_class_name
# find_element_by_css_selector
"""

# input_first = browser.find_element_by_id('q')
# input_second = browser.find_element_by_css_selector('#q')
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first)
# print(input_second)
# print(input_third)


""" 四、获取单个节点的第二个方式 """
# input_fourth = browser.find_element(By.ID,'q')
# print(input_fourth)


""" 五、多个节点
# 如果查找的目标在网页中只有一个，那么完全可以使用find_element()方法，但如果有多个节点
# 再使用find_element()方法查找，就只能得到第一个节点了，如果要查找所有满足条件的节点，需要
# 使用find_elements()方法查找
"""
# 查找淘宝左侧导航条的所有条目
# lis = browser.find_elements_by_css_selector('.service-bd li')
# print(lis)
# browser.close()

""" 六、节点交互
# Selenium可以驱动浏览器来执行一些操作，也就是说可以让浏览器模拟执行一些操作，比较
# 常见的有 输入文字时使用send_keys()方法，清空文字时使用clear()方法，点击按钮时使用click()方法
"""
# input = browser.find_element_by_id('q')
# input.send_keys('iPhone')
# time.sleep(1)
# input.clear()
# input.send_keys('iPad')
# button = browser.find_element_by_class_name('btn-search')
# button.click()

""" 七、动作链
# 在前面的实例中，一些交互动作都是针对某个节点执行的，如输入框、我们就调用他的输入文字和清空文字的方法
# 对于按钮、就调用他的点击的方法，还有一些其他操作，他们没有特定的执行对象，如鼠标拖拽、键盘按键等
# 这些动作用另一种方式来执行，那就是动作链
"""
# 如实现一个节点的拖拽操作，将某个节点从一处拖拽到另外一处
url="https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
browser.get(url)
browser.switch_to.frame('iframeResult')
source=browser.find_element_by_id('draggable')
target=browser.find_element_by_css_selector('#droppable')
actions=ActionChains(browser)
actions.drag_and_drop(source,target)
actions.perform()



# 找到输入框
#input = browser.find_element_by_id('kw')

#在搜索框里输入Python
#input.send_keys('Python')

#input.send_keys(Keys.ENTER)



