#coding=utf-8
from DataDriverFrameWork.util.ObjectMap import *
from DataDriverFrameWork.util.ParseConfigurationFile import ParserConfigFile
class LoginPage(object):
    def __init__(self,driver):
        self.driver=driver
        self.parseCF=ParserConfigFile()
        self.loginOptions=self.parseCF.getItemsSection('126mail_login')
        # print(self.loginOptions)


    def loginWay(self):
        try:
            locateType, locatorExpression = self.loginOptions["loginPage.Way".lower()].split('>')
            # return self.driver.find_element_by_id("lbNormal")
            return getElement(self.driver,locateType,locatorExpression)
        except Exception as e:
            raise e


    def switchToFrame(self):
        # iframe = self.driver.find_elements_by_tag_name("iframe")[0]
        try:
            locateType, locatorExpression = self.loginOptions["loginPage.frame".lower()].split('>')
            elementObj = getElement(self.driver, locateType, locatorExpression)
            self.driver.switch_to.frame(elementObj)
        except Exception as e:
            raise e


    #切换到主界面
    def switchToDefaultFrame(self):
        self.driver.switch_to.default_content()


    def userNameObj(self):
        try:
            locateType,locatorExpression=self.loginOptions["loginPage.username".lower()].split('>')
            elementObj=getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e
    def passWordObj(self):
        try:
            locateType, locatorExpression = self.loginOptions["loginPage.password".lower()].split('>')
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e
    def loginButton(self):
        try:
            locateType, locatorExpression = self.loginOptions["loginPage.loginbutton".lower()].split('>')
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e
# if __name__ == '__main__':
#     from selenium import webdriver
#     driver=webdriver.Chrome()
#     driver.get("https://mail.126.com/")
#     import time
#     time.sleep(5)
#     login=LoginPage(driver)
#     login.loginWay().click()
#     time.sleep(1)
#     login.switchToFrame()
#     login.userNameObj().send_keys("xhq11093")
#     login.passWordObj().send_keys("xhq11093..")
#     login.loginButton().click()
#     login.switchToDefaultFrame()
#     assert u"未读邮件" in driver.page_source
#
#     driver.quit()

