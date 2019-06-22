#coding=utf-8
from configparser import ConfigParser
from config.VarConfig import pageElementLocatorPath
class ParserConfigFile(object):
    def __init__(self):
        self.cf=ConfigParser()
        self.cf.read(pageElementLocatorPath)

    def getItemsSection(self,sectionName):
        # 读取对应模块下的值，转变成元祖键值对形式
        optionsDict=dict(self.cf.items(sectionName))
        # print(optionsDict)
        return optionsDict
    def getOptionValue(self,sectionName,optionName):
        value = self.cf.get(sectionName,optionName)
        # print(value)
        return value
if __name__ == '__main__':
    pc=ParserConfigFile()
    pc.getItemsSection('126mail_login')
    pc.getOptionValue('126mail_login','loginPage.Way')