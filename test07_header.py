# 导包
import requests

login_url = "http://ihrm-test.itheima.net/api/sys/login"
login_data = {"mobile": 13800000002, "password": 123456}
login_header = {
    "Content-Type": "application/json"
}
# 发送请求
response = requests.post(url=login_url, json=login_data, headers=login_header)
# 查看响应
print(response.json())