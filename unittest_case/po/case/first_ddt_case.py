#coding=utf-8
import ddt
#用户名、密码、错误信息定位、错误提示
import os
# import sys
# sys.path.append("/Users/roseboy/Desktop/unittest_case/po")
from business.login_business import LoginBussiness
from selenium import webdriver
import time
import unittest
import HTMLTestRunner
from util.excel_util import ExcelUtil
ex=ExcelUtil()
data=ex.get_data()
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        #因为其他地方也要使用，所以需要把driver变成全局的，前面加self
        self.driver=webdriver.Chrome()
        self.driver.get('http://www.maiziedu.com/')
        time.sleep(3)
        self.driver.find_element_by_link_text('登录').click()
        time.sleep(3)
        self.login_b=LoginBussiness(self.driver)
    def tearDown(self):
        #失败时截图
        for method_name,error in self._outcome.errors:
            if error:
                case_name=self._testMethodName
                file_path=os.path.join(os.getcwd()+"/report/"+case_name+".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()
    #
    @ddt.data(*data)
    def test_login_username_error(self,data):
        #输入一个错误的用户名
        username, password, err_ele, err_code=data
        user_error=self.login_b.login_function(username,password,err_ele,err_code)
        # if user_error==True:
        #     print("注册成功，验证失败")
        # #通过assert判断是否为error
        self.assertFalse(user_error,"case执行")
if __name__ == '__main__':
    file_path = os.path.join(os.getcwd() + "/report" + "/case.html")
    f = open(file_path, 'wb')
    # suit = unittest.TestSuite()
    # suit.addTest(FirstDdtCase('test_login_username_error'))
    suite=unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="麦子", description=u'第一个测试报告', verbosity=2)
    runner.run(suite)