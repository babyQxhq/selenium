#coding=utf-8
#操作层、定义输入，，login页操作流程,被bussiness封装起来后被case调用
from page.login_page import LoginPage
class LoginHandle(object):
    #需要想办法获取元素、读取page
    def __init__(self,driver):
        self.login_p=LoginPage(driver)
    # 输入用户名
    def send_username(self,username):
        self.login_p.get_username_element().send_keys(username)
    #输入密码
    def send_password(self,password):
        self.login_p.get_pass_element().send_keys(password)
    #获取错误信息、
    def get_error(self,user_info):
        text=self.login_p.get_error_element().text
        return text
    #点击注册按钮
    def click_button(self):
        self.login_p.get_login_button().click()
    #获取注册按钮文字、
    def get_login_text(self):
       return self.login_p.get_login_button().text