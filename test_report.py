# 导包
import time
import unittest
from tools.HTMLTestRunner import HTMLTestRunner
from test_x import TPspLogin
from test12_params import Login
# 封装测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TPspLogin))
suite.addTest(unittest.makeSuite(Login))
# 指定报告路径
report = "./report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
# "./report/report-{}.html"
# 打开文件流
with open(report, "wb") as f:
    # 创建HTMLRunner运行器
    runner = HTMLTestRunner(f, title='接口测试报告')
    # 执行测试套件
    runner.run(suite)

