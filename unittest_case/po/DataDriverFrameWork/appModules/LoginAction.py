#coding=utf-8
from pageObjects.LoginPage import LoginPage
class LoginAction(object):
    def __init__(self):
        print("loging..")
    @staticmethod
    def login(driver,username,password):
        try:
            login=LoginPage(driver)
            login.loginWay().click()
            login.switchToFrame()
            login.userNameObj().send_keys(username)
            login.passWordObj().send_keys(password)
            login.loginButton().click()
            login.switchToDefaultFrame()
        except Exception as e:
            raise e
# if __name__ == '__main__':
#     from selenium import webdriver
#     import time
#     driver=webdriver.Chrome()
#     driver.get("https://mail.126.com/")
#     time.sleep(3)
#     LoginAction.login(driver,"xhq11093","xhq11093..")
#     time.sleep(3)
#     driver.quit()