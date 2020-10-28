# 2、请使用requests模块编写代码访问员工管理模块用户资料查询接口，并输出该接口返回响应数据中
# 的url，encoding，cookies，headers，以及响应数据
# 导包
import requests
session = requests.Session()
login_url = 'http://ihrm-test.itheima.net/api/sys/login'

login_data = {"mobile": "13800000002", "password": "123456"}
login_header = {"Content-Type": "application/json"}

# 发送登陆请求
response = session.post(url=login_url,
                        json=login_data, headers=login_header)
# 查看登陆响应
print(response.json())
print("-" * 30)
pro_url = 'http://ihrm-test.itheima.net/api/sys/profile'
# 发送查询请求
token = response.json().get("data")
pro_header = {"Content-Type": "application/json",
              "Authorization": "Bearer " + token}
response1 = session.post(url=pro_url, headers=pro_header)
# 查看查询响应
print(response1.json())
print("-" * 30)
print("返回的url是：", response1.url)
print("-" * 30)
print('encoding是：', response1.encoding)
print("-" * 30)
print('cookies是：', response1.cookies)
print("-" * 30)
print('headers是：', response1.headers)

