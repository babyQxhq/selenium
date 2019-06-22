#coding=utf-8
#初始化环境
from selenium import webdriver
#前
#context承上启下左右，可以理解为超级全局变量
def before_all(context):
    context.driver=webdriver.Chrome()
#后
def after_all(context):
    context.driver.close()