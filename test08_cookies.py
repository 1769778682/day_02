# 获取验证码：http://localhost/index.php?m=Home&c=User&a=verify
# 登录：http://localhost/index.php?m=Home&c=User&a=do_login
# 我的订单：http://localhost/Home/Order/order_list.html

import requests

response = requests.get('http://localhost/index.php?m=Home&c=User&a=verify')

print(response.cookies)
PHPSESSID = response.cookies.get("PHPSESSID")
print(PHPSESSID)

# 登录
login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
login_data = {
    "username": 13812345678,
    "password": 123456,
    "verify_code": 8888
}

cookies = {
    "PHPSESSID": PHPSESSID
}
response = requests.post(url=login_url, data=login_data, cookies=cookies)
print(response.json())
response = requests.get('http://localhost/Home/Order/order_list.html', cookies=cookies)
print(response.text)