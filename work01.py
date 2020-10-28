# 1、请使用python的requests模块编写对百度进行搜索的代码，搜索关键字：接口测试
# 域名：www.baidu.com
# 协议：http
# 接口：/S
# 请求方式：Get
# 请求参数：wd=xxx
# 导包
import requests


url = 'http://www.baidu.com/S'
string = 'wd=接口测试'
# 发送请求
response = requests.get(url=url, params=string)
# 查看响应
print(response.text)