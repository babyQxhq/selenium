#coding=utf-8
from selenium import webdriver
from iutil.find_element import FindElement
import time

class Login():
    def __int__(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://mail.126.com/")
        time.sleep(3)



    def login(self):
        self.get_ele = FindElement(self.driver)
        FindElement(self.driver).get_element('id','lbNormal').click()
        time.sleep(3)
        self.driver.close()

if __name__ == '__main__':
    login_page=Login()
    login_page.login()