# 导包
import requests

# 发送请求
# response = requests.get("http://www.baidu.com")
urlA = "http://localhost/Home/Goods/search.html"

# 1.字符串
stringA = 'q=iphone'
response = requests.get(url=urlA, params=stringA)

# 2.字典
# dictA = {
#     'q': 'iphone'
# }
# response = requests.get(url=urlA, params=dictA)

# 查看响应
print("设置后响应数据：", response.text)