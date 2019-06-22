#coding=utf-8
from DataDriverFrameWork.util.ObjectMap import *
from DataDriverFrameWork.util.ParseConfigurationFile import ParserConfigFile
class HomePage(object):
    def __init__(self,driver):
        self.driver=driver
        self.parseCF=ParserConfigFile()

    def addressLink(self):
        try:

            locateType, locatorExpression = self.parseCF.getOptionValue\
                ("126mail_homePage","homePage.adressbook").split('>')
            return getElement(self.driver, locateType, locatorExpression)

        except Exception as e:
            raise e
