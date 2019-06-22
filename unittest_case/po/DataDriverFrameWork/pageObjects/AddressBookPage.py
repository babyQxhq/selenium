#coding=utf-8
from DataDriverFrameWork.util.ObjectMap import *
from DataDriverFrameWork.util.ParseConfigurationFile import ParserConfigFile
class AddressBookPage(object):
    def __init__(self,driver):
        self.driver=driver
        self.parseCF = ParserConfigFile()
        self.addContactsOptions = self.parseCF.getItemsSection('126main_addContactPage')
        # print(self.addContactsOptions)

    def createContactPersonButton(self):
        try:
            locateType, locatorExpression = self.addContactsOptions["addContactPage.createContactsBtn".lower()].split('>')
            # return self.driver.find_element_by_id("lbNormal")
            return getElement(self.driver,locateType,locatorExpression)
        except Exception as e:
            raise e

    def contactPersonName(self):
        try:
            locateType, locatorExpression = self.addContactsOptions["addContactPage.contactPersonName".lower()].split('>')
            # return self.driver.find_element_by_id("lbNormal")
            return getElement(self.driver, locateType, locatorExpression)
        except Exception as e:
            raise e

    def contactPersonEmail(self):
        try:
            locateType, locatorExpression = self.addContactsOptions["addContactPage.contactPersonEmail".lower()].split('>')
            # return self.driver.find_element_by_id("lbNormal")
            return getElement(self.driver, locateType, locatorExpression)
        except Exception as e:
            raise e

    def starContacts(self):
        try:
            locateType, locatorExpression = self.addContactsOptions["addContactPage.starContacts".lower()].split('>')
            # return self.driver.find_element_by_id("lbNormal")
            return getElement(self.driver, locateType, locatorExpression)
        except Exception as e:
            raise e

    def contactPersonMobile(self):
        try:
            locateType, locatorExpression = self.addContactsOptions["addContactPage.contactPersonMobile".lower()].split('>')
            # return self.driver.find_element_by_id("lbNormal")
            return getElement(self.driver, locateType, locatorExpression)
        except Exception as e:
            raise e

    def contactPersonComment(self):
        try:
            locateType, locatorExpression = self.addContactsOptions["addContactPage.contactPersonComment".lower()].split('>')
            # return self.driver.find_element_by_id("lbNormal")
            return getElement(self.driver, locateType, locatorExpression)
        except Exception as e:
            raise e
    def saveContacePerson(self):
        try:
            locateType, locatorExpression = self.addContactsOptions["addContactPage.saveContactPerson".lower()].split('>')
            return getElement(self.driver, locateType, locatorExpression)
        except Exception as e:
            raise e
