# 获取验证码： http://localhost/index.php?m=Home&c=User&a=verify
# 登录： http://localhost/index.php?m=Home&c=User&a=do_login
# 导包
import requests
import unittest


class TPspLogin(unittest.TestCase):
    """定义登录接口测试类"""

    def setUp(self):
        self.session = requests.Session()
        self.verify = 'http://localhost/index.php?m=Home&c=User&a=verify'
        self.login = 'http://localhost/index.php?m=Home&c=User&a=do_login'

    def tearDown(self):
        self.session.close()

    def test_success(self):
        response = self.session.get(self.verify)
        self.assertEqual(200, response.status_code)
        self.assertIn("image", response.headers.get("Content-Type"))
        login_data = {
            "username": 13812345678,
            "password": 123456,
            "verify_code": 8888
        }
        response = self.session.post(url=self.login, data=login_data)
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json().get("status"))
        self.assertIn("登陆成功", response.json().get("msg"))

    def test_exist(self):
        response = self.session.get(self.verify)
        self.assertEqual(200, response.status_code)
        self.assertIn("image", response.headers.get("Content-Type"))
        login_data = {
            "username": 13812345699,
            "password": 123456,
            "verify_code": 8888
        }
        response = self.session.post(url=self.login, data=login_data)
        self.assertEqual(200, response.status_code)
        self.assertEqual(-1, response.json().get("status"))
        self.assertIn("账号不存在", response.json().get("msg"))

    def test_error(self):
        response = self.session.get(self.verify)
        self.assertEqual(200, response.status_code)
        self.assertIn("image", response.headers.get("Content-Type"))
        login_data = {
            "username": 13812345678,
            "password": 123457,
            "verify_code": 8888
        }
        response = self.session.post(url=self.login, data=login_data)
        self.assertEqual(200, response.status_code)
        self.assertEqual(-2, response.json().get("status"))
        self.assertIn("密码错误", response.json().get("msg"))
