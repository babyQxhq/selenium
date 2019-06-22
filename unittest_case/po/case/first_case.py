#coding=utf-8
import os
# import sys
# sys.path.append("/Users/roseboy/Desktop/unittest_case/po")
from business.login_business import LoginBussiness
from selenium import webdriver
import time
import unittest
import HTMLTestRunner
class FirstCase(unittest.TestCase):
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
    #case名字要清晰，别人能看懂
    def test_login_username_error(self):
        #输入一个错误的用户名

        user_error=self.login_b.login_user_error('126789345','111')
        # if user_error==True:
        #     print("注册成功，验证失败")
        # #通过assert判断是否为error
        self.assertFalse(user_error,"case执行")

    def test_login_password_error(self):

        pass_error = self.login_b.login_pass_error('15210424367','123456789')
        # if pass_error == True:
        #     print("注册成功，验证失败")
        self.assertFalse(pass_error)
    def test_login_success(self):

        success=self.login_b.login_succes('15210424367','12345678')
        if success == True:
            print("注册成功！")
# def main():
#     #unittest不需要main也能自动执行
#     first_case = FirstCase()
#     first_case.test_login_username_error()
#     first_case.test_login_password_error()
#     first_case.test_login_success()/;
#     # webdriver.close()
#
if __name__ == '__main__':
    file_path=os.path.join(os.getcwd()+"/report"+"/case.html")
    f=open(file_path,'wb')
    suit=unittest.TestSuite()
    suit.addTest(FirstCase('test_login_username_error'))
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,title="麦子",description=u'第一个测试报告',verbosity=2)
    runner.run(suit)