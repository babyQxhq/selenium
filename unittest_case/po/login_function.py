#coding=utf-8

from find_element import FindElement
from selenium import webdriver
import time
from util.read_xls import ReadXls
class LoginFunction(object):
    def __init__(self,url,i):
        self.driver=self.get_driver(url,i)
    #获取driver并且打开url
    def get_driver(self,url,i):
        #模拟多个浏览器跑case
        if i==0:
            driver=webdriver.Chrome()
        elif i==1:
            driver=webdriver.Chrome()
        else:
            driver=webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver
    #输入用户信息data
    def send_user_info(self,key,data):
        self.get_user_element(key).send_keys(data)
    #定位用户信息，获取element
    def get_user_element(self,key):
        find_ele=FindElement(self.driver)
        user_element=find_ele.get_element(key)
        return user_element
    def read_user_xls(self):
        read_user_xls = ReadXls()
        user_list=read_user_xls.read_xls()
        return user_list
    def main(self):
        # try:
            read_user_xls=ReadXls()
            useres=read_user_xls.read_xls("config/user.xls")
            username=useres[2]
            password=useres[3]
            print(username,password)
            self.get_user_element('login').click()
            time.sleep(5)
            self.send_user_info('user',username)
            self.send_user_info('password',password)
            self.get_user_element('button').click()
            login_error=self.get_user_element('error')
            if login_error==None:
                print("登录成功")
            else:
                self.driver.save_screenshot("image/error.png")

        # except Exception:
        #     print(Exception)
            time.sleep(1)
            self.driver.close()

if __name__ == '__main__':
    #多浏览器循环
    for i in range(3):
        login_function=LoginFunction('http://www.maiziedu.com/',i)
        login_function.main()