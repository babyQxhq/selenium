#coding=utf-8
#命令切换到该目录下，输入behave命令
from behave import *
from features.lib.pages.login_page import LoginPage
#使用正则表达式
use_step_matcher('re')

@when('I open the login website  "http://www.maiziedu.com/" ')
def step_login(context):
    LoginPage(context).get_url("http://www.maiziedu.com/")

# @when('I open the login website  "([^"]*)" ')
# def step_login(context,url):
#     LoginPage(context).get_url(url)
#
# #([^"]*) 匹配 非双引号字符组成的字符串
# @then('I expect that the title is "([^"]*)"')
# def step_login1(context,title_name):
#     title=LoginPage(context).get_title()
#     assert title_name in title

# @when('I set with username "([^"]*)"')
# def step_login(context,username):
#     LoginPage(context).send_username(username)
#
# @when('I set with password "([^"]*)"')
# def step_login(context,password):
#     LoginPage(context).send_username(password)
#
# @when('I click with login')
# def step_login(context):
#     LoginPage(context).click_login_button()
#
# @then('I except that text "([^"]*)"')
# def step_login(context,error_text):
#     text=LoginPage(context).get_error()
#     assert error_text in text