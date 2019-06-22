#coding=utf-8
#为handle提供页面元素
#调用findelement
from base.find_element import FindElement
class LoginPage(object):
    #拿元素
    def __init__(self,driver):
        self.get_ele=FindElement(driver)
    #获取用户名
    def get_username_element(self):
        return self.get_ele.get_element("user")
    #获取密码
    def get_pass_element(self):
        return self.get_ele.get_element("password")
    #获取错误信息
    def get_error_element(self):
        return self.get_ele.get_element("error")
    #点击登录
    def get_login_button(self):
        return self.get_ele.get_element("button")