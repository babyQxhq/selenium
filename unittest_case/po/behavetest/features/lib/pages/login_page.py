#coding=utf-8
from features.lib.pages.base_page import BasePage
from selenium.webdriver.common.by import By
#继承BasePage
class LoginPage(BasePage):
    def __int__(self,context):
        #因为需要driver，driver在context里面，所以直接传递context上下文进来

        # super(LoginPage,self).__init__(context.driver)
        super().__init__(context.driver)


    def send_username(self,username):
        self.find_element(By.ID,'user').send_keys(username)

    def send_password(self,password):
        self.find_element(By.ID,'password').send_keys(password)


    def click_login_button(self):
        self.find_element(By.ID,'button').click()
    # def login_get_title(self):
    #     self.get_title()
    def get_error(self):
        return self.find_element(By.ID,'error').text