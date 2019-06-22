#coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from DataDriverFrameWork.util.ParseExcel import ParseExcel
from config.VarConfig import *
from appModules.AddContactPersonAction import AddContactPerson
from appModules.LoginAction import LoginAction
import traceback
import time
from DataDriverFrameWork.util.Log import *

#设置此次测试的环境编码为utf-8,ptyhon2的写法
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")
#创建解析Excel文件
excelobj=ParseExcel()
#将excel加载到内存
excelobj.loadWorkBook(dataFilePath)

def LaunchBrowser():
    #创建chrome浏览器的一个Options实例对象
    chrome_options=Options()
    #向浏览器中添加金庸跨站插件的设置参数项
    chrome_options.add_argument("--disable--extensions")
    #添加屏蔽--ignore--certificate--errors提示信息的设置参数项
    chrome_options.add_experimental_option("excludeSwitches",["--ignore--certificate--errors"])
    #添加浏览器最大化的设置参数项，一启动就是最大化
    chrome_options.add_argument('--start-maximized')
    #启动带有自定义设置的Chrome浏览器
    driver=webdriver.Chrome("/usr/local/bin/chromedriver",0,chrome_options)
    #访问126邮箱首页
    driver.get("https://mail.126.com/")
    time.sleep(3)
    return driver

def test126MailAddContacts():
    logging.info(u"测试为126邮箱添加联系人执行开始...")
    try:
        #根据sheet名称获取sheet
        userSheet=excelobj.getSheetByName(u"126账号")
        #获取126中的账号是否被执行
        isExecuteUser=excelobj.getColumn(userSheet,account_isExecute)
        #获取126账号sheet中数据表列
        dataBookColumn=excelobj.getColumn(userSheet,account_dataBook)

        #enumerate枚举
        for idx,i in enumerate(isExecuteUser[1:]):
            #循环遍历126账号表中的账号，为需要执行的账号添加联系人
            if i.value == 'y':
                #获取第i行的数据
                userRow=excelobj.getRow(userSheet,idx+2)
                #获取第i行的用户名
                username=userRow[account_username - 1].value
                #获取第i行第密码
                password=str(userRow[account_password - 1 ].value)
                print(username,password)

                #创建浏览器实例对象
                driver=LaunchBrowser()
                logging.info(u"启动浏览器，访问126邮箱主页...")


                #登录126邮箱
                LoginAction.login(driver, username,password)
                time.sleep(3)
                try:
                    #断言登录后的标题是否包含网易邮箱
                    assert u"收件箱" in driver.page_source
                    logging.info(u"用户%s登录后，断言页面关键字'收件箱'成功" %username)

                except AssertionError as e:
                    logging.debug(u"用户%s登录后，断言页面关键字'收件箱'失败"
                                  u"异常信息:%s" %(username,str(traceback.format_exc())))

                #获取为第i行用户添加联系人第数据表sheet名
                dataBookName=dataBookColumn[idx+1].value
                #根据表名获取对应第数据表
                dataSheet=excelobj.getSheetByName(dataBookName)
                # 获取联系人数据表中是否执行列对象
                isExecuteData = excelobj.getColumn(dataSheet, contacts_isExecute)
                #记录添加成功联系人个数
                contactNum=0
                #记录需要被执行联系人个数
                isExecuteNum=0
                for id,data in enumerate(isExecuteData[1:]):
                    #遍历是否执行列
                    if data.value=='y':
                        isExecuteNum+=1
                        #获取整行数据
                        rowContent=excelobj.getRow(dataSheet,id+2)
                        #获取联系人姓名
                        contactPersonName=rowContent[contacts_contactPersonName-1].value
                        #获取联系人邮箱
                        contactPersonEmail = rowContent[contacts_contactPersonEmail - 1].value
                        #获取是否设置为星标联系人
                        isStar=rowContent[contacts_isStar-1].value
                        #获取联系人手机号
                        contactPersonMobile=rowContent[contacts_contactPersonMobile-1].value
                        #获取联系人备注信息
                        contactPersonComment=rowContent[contacts_contactPersonComment-1].value
                        #添加联系人添加成功之后，断言的关键字
                        assertKeyWord=rowContent[contacts_assertKeyWorks-1].value
                        # print(contactPersonName,contactPersonEmail,assertKeyWord)
                        # print(contactPersonMobile,contactPersonComment,isStar)
                        #执行新建联系人操作
                        AddContactPerson.add(driver,contactPersonName,contactPersonEmail,
                                             isStar,contactPersonMobile,contactPersonComment)
                        time.sleep(1)
                        logging.info(u'添加联系人%s成功' % contactPersonEmail)
                        #在联系人工作表中写入添加联系人执行时间
                        excelobj.writeCellCurrentTime(dataSheet,rowNo=id+2,colsNo=contacts_runTime)
                        try:
                            #断言给定的关键字是否出现在页面中
                            assert assertKeyWord in driver.page_source
                        except AssertionError as e:
                            #断言失败，在联系人工作表中写入添加联系人测试失败信息
                            excelobj.writeCell(dataSheet,"faild",rowNo=id+2,colsNo=contacts_testResult,style="red")
                            logging.info(u'断言关键字%s失败' % assertKeyWord)
                        else:
                            excelobj.writeCell(dataSheet, "pass", rowNo=id+2, colsNo=contacts_testResult,style="green")
                            contactNum+=1
                            logging.info(u'断言关键字%s成功' % assertKeyWord)
                    else:
                        logging.info(u'联系人%s被忽略执行' % contactPersonEmail)
                # print("contactNum=%s,isExecuteNum=%s" %(contactNum,isExecuteNum))
                if contactNum==isExecuteNum:
                    #如果想到说明给第i个用户添加联系人第测试用例执行成功，在126账号工作表中写入成功信息，否则写入失败信息
                    excelobj.writeCell(userSheet, "pass", rowNo=idx + 2, colsNo=account_testResult, style='green')
                    # print(u"为用户%s添加%d个联系人，测试通过！" %(username,contactNum))
                else:
                    excelobj.writeCell(userSheet, "faild", rowNo=idx + 2, colsNo=account_testResult, style='red')
                logging.info(u'为用户%s添加%d个联系人，%d个成功\n' % (username,isExecuteNum,contactNum))
            else:
                ignoreUserName=excelobj.getCellOfValue(userSheet,rowNo=idx+2,colsNo=account_username)
                print(u"用户%s被设置为忽略执行！" %ignoreUserName)
            driver.quit()
    except Exception as e:
        logging.debug(u"数据驱动框架主程序发生异常，异常信息为:%s" %str(traceback.format_exc()))
        #打印异常堆栈信息





