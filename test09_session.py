# 获取验证码：http://localhost/index.php?m=Home&c=User&a=verify
# 登录：http://localhost/index.php?m=Home&c=User&a=do_login
# 我的订单：http://localhost/Home/Order/order_list.html
# 导包
import requests
# 创建session
session = requests.Session()
response1 = session.get('http://localhost/index.php?m=Home&c=User&a=verify')

# print(response.cookies)
# PHPSESSID = response.cookies.get("PHPSESSID")
# print(PHPSESSID)

# 登录
login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
login_data = {
    "username": 13812345678,
    "password": 123456,
    "verify_code": 8888
}

# cookies = {
#     "PHPSESSID": PHPSESSID
# }
response2 = session.post(url=login_url, data=login_data)   # cookies=cookies)
print(response2.json())
response3 = session.get('http://localhost/Home/Order/order_list.html')  # cookies=cookies)
print(response3.text)
