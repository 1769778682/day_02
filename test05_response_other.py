# 导包
import requests
# 1). 访问百度首页的接口`http://www.baidu.com`，获取以下响应数据
response = requests.get('http://www.baidu.com')
# 2). 获取响应状态码
print(response.status_code)
# 3). 获取请求URL
print("URL:", response.url)
# 4). 获取响应字符编码
print('相应字符编码：', response.encoding)
response.encoding = 'utf-8'
print('相应字符编码：', response.encoding)
# 5). 获取响应头数据
print('响应头：', response.headers)
print(response.headers.get("Content-Type"))
# 6). 获取响应的cookie数据
print('cookie数据：', response.cookies)
print(response.cookies.get("BDORZ"))
# 7). 获取文本形式的响应内容
print('文本形式内容：', response.text)
# 8). 获取字节形式的响应内容
print("获取字节形式的响应内容", response.content)
print("获取字节形式的响应内容", response.content.decode('utf-8'))
