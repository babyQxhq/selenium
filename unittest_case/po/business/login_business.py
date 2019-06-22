#coding=utf-8
#封装handle，供case直接调用
from handle.login_handle import LoginHandle
class LoginBussiness(object):
    #执行操作
    def __init__(self,driver):
        self.login_h=LoginHandle(driver)
    def user_base(self,username,password):
        self.login_h.send_username(username)
        self.login_h.send_password(password)
        self.login_h.click_button()
    def login_succes(self):
        if self.login_h.get_login_text()==None:
            return True
        else:
            return False
    def login_user_error(self,username,password):
        self.user_base(username,password)
        if self.login_h.get_error("该账号格式不正确")==None:
            print("用户名校验不成功")
            return True
        else:
            return False
    def login_function(self,username,password,err_ele,err_code):
        self.user_base(username, password)
        if self.login_h.get_error(err_ele,err_code) == None:
            print("用户名校验不成功")
            return True
        else:
            return False

    def login_pass_error(self,username,password):
        self.user_base(username, password)
        if self.login_h.get_error("账号或者密码错误，请重新输入")==None:
            print("密码校验不成功")
            return True
        else:
            return False