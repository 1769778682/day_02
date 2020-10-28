# 导包
import requests

# 发送请求
response = requests.get("http://www.baidu.com")

# 查看响应
print("原始的数据编码格式为：", response.encoding)
print("设置前响应数据：", response.text)
response.encoding = "utf-8"
print("设置后的数据编码格式为：", response.encoding)
print("设置后响应数据：", response.text)