#coding=utf-8
from selenium import webdriver
from util.find_element import FindElement
import time
class ActionMethod:
    def __int__(self):
        pass
    #打开浏览器
    def open_browser(self,browser):
        if browser=='chrome':
            self.driver=webdriver.Chrome()
        elif browser=='firefox':
            self.driver=webdriver.Firefox()
        else:
            self.driver=webdriver.Safari()
    def get_url(self,url):
        self.driver.get(url)
    #定位元素
    def get_element(self,key):
        find_element=FindElement(self.driver)
        element=find_element.get_element(key)
        return element
    #输入元素
    def element_send_keys(self,value,key):
        element=self.get_element(key)
        print(key,value,element)
        time.sleep(3)
        element.send_keys(value)
    #点击元素
    def click_element(self,key):
        self.get_element(key).click()
    #等待
    def sleep_time(self,itime):
        time.sleep(3)
    #关闭浏览器
    def close_browser(self):
        self.driver.close()
    #获取title
    def get_title(self):
        return self.driver.title
