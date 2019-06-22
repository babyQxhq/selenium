#coding=utf—8
from selenium.webdriver.common.by import By
class BasePage:
    def __int__(self,driver):
        self.driver=driver

    #打开页面
    def get_url(self,url):
        self.driver.get(url)

    #获取title
    def get_title(self):
        return self.driver.title

    #定位元素
    def find_element(self,*loc):
        return self.driver.find_element(*loc)



