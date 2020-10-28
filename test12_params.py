# 获取验证码： http://localhost/index.php?m=Home&c=User&a=verify
# 登录： http://localhost/index.php?m=Home&c=User&a=do_login
import json
import unittest
import requests
from parameterized import parameterized


def build_data():
    test_data = []
    file = './data/login.json'
    with open(file, encoding='utf-8') as f:
        json_data = json.load(f)
        for case_data in json_data:
            username = case_data.get("username")
            password = case_data.get("password")
            verify_code = case_data.get("verify_code")
            status_code = case_data.get("status_code")
            status = case_data.get("status")
            msg = case_data.get("msg")
            test_data.append((username, password, verify_code, status_code, status, msg))
    # print('test_data=:'.format(username, password, verify_code, status_code, status, msg))
    return test_data


class Login(unittest.TestCase):
    """登录接口测试类"""

    def setUp(self):  # 系统自带方法，在方法调用时都会用到的东西
        self.session = requests.Session()
        self.verify = 'http://localhost/index.php?m=Home&c=User&a=verify'
        self.login = 'http://localhost/index.php?m=Home&c=User&a=do_login'
        # response = session.get(self.verify)

    def tearDown(self):  # 系统自带方法，方法调用后都会用到的东西
        self.session.close()

    @parameterized.expand(build_data())
    def test(self, username, password, verify_code, status_code, status, msg):
        """登录成功方法"""

        # 发送获取验证码请求
        response = self.session.get(self.verify)
        self.assertEqual(200, response.status_code)  # 断言响应状态码
        self.assertIn("image", response.headers.get("Content-Type"))  # 断言返回是否图片
        login_data = {
            "username": username,
            "password": password,
            "verify_code": verify_code
        }
        # 发送请求
        response = self.session.post(url=self.login, data=login_data)
        print(response.json())

        self.assertEqual(status_code, response.status_code)  # 断言响应状态码
        self.assertEqual(status, response.json().get("status"))  # 断言返回数据
        self.assertIn(msg, response.json().get("msg"))
