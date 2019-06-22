#coding=utf-8
from pageObjects.HomePage import HomePage
from pageObjects.AddressBookPage import AddressBookPage
import traceback
import time
class AddContactPerson(object):
    def __init__(self):
        print("add contact person.")

    @staticmethod
    def add(driver,contactName,contactEmail,isStar,contactPhone,contactComment):
        try:
            #创建主页实例对象
            hp=HomePage(driver)
            #点击通讯录链接
            hp.addressLink().click()
            time.sleep(3)
            #创建添加联系人页实例对象
            abp=AddressBookPage(driver)
            abp.createContactPersonButton().click()
            if contactName:
                #非必填
                abp.contactPersonName().send_keys(contactName)
            #必填项
            abp.contactPersonEmail().send_keys(contactEmail)
            if isStar==u"是":
                abp.starContacts().click()
            if contactPhone:
                abp.contactPersonMobile().send_keys(contactPhone)
            if contactComment:
                abp.contactPersonComment().send_keys(contactComment)
            abp.saveContacePerson().click()
        except Exception as e:
            #打印堆栈异常信息
            print(traceback.print_exc())
            raise e
