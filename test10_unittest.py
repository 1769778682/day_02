# 获取验证码： http://localhost/index.php?m=Home&c=User&a=verify
# 登录： http://localhost/index.php?m=Home&c=User&a=do_login

import unittest
import requests

session = requests.Session()


class Login(unittest.TestCase):
    """登录接口测试类"""

    def setUp(self):  # 系统自带方法，在方法调用时都会用到的东西
        self.session = requests.Session()
        self.verify = 'http://localhost/index.php?m=Home&c=User&a=verify'
        self.login = 'http://localhost/index.php?m=Home&c=User&a=do_login'
        # response = session.get(self.verify)

    def tearDown(self):   # 系统自带方法，方法调用后都会用到的东西
        self.session.close()

    def test01_success(self, mobile, password, verify_code):
        """登录成功方法"""

        # 发送获取验证码请求
        response = self.session.get(self.verify)
        self.assertEqual(200, response.status_code)  # 断言响应状态码
        self.assertIn("image", response.headers.get("Content-Type"))  # 断言返回是否图片
        login_data = {
            "username": mobile,
            "password": password,
            "verify_code": verify_code
        }
        # 发送请求
        response = self.session.post(url=self.login, data=login_data)
        print(response.json())

        self.assertEqual(200, response.status_code)  # 断言响应状态码
        self.assertEqual(1, response.json().get("status"))  # 断言返回数据
        self.assertIn("登陆成功", response.json().get("msg"))

    def test02_exist(self):
        """账号不存在方法"""

        # 发送获取验证码请求
        response = self.session.get(self.verify)
        self.assertEqual(200, response.status_code)
        self.assertIn("image", response.headers.get("Content-Type"))
        login_data = {
            "username": 13812345699,
            "password": 123456,
            "verify_code": 8888
        }

        response = self.session.post(url=self.login, data=login_data)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(-1, response.json().get("status"))
        self.assertIn("账号不存在", response.json().get("msg"))

    def test03_error(self):
        """密码错误方法"""
        response = self.session.get(self.verify)
        self.assertEqual(200, response.status_code)
        self.assertIn("image", response.headers.get("Content-Type"))
        login_data = {
            "username": 13812345678,
            "password": 123457,
            "verify_code": 8888
        }

        response = self.session.post(url=self.login, data=login_data)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(-2, response.json().get("status"))
        self.assertIn("密码错误", response.json().get("msg"))


