#coding=utf-8
import os
#当前文件所在目录对绝对路径:工程路径
prentDirPath=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#获取ini文件对绝对路径
pageElementLocatorPath=prentDirPath+u"/config/PageElementLocator.ini"

#获取数据存放的绝对路径
dataFilePath=prentDirPath+u"/testData/126邮箱联系人.xlsx"

#126账号工作表中，每列对应是数字序号
account_username=2
account_password=3
account_dataBook=4
account_isExecute=5
account_testResult=6
#联系人工作表中，每列对应的数字序号
contacts_contactPersonName=2
contacts_contactPersonEmail=3
contacts_isStar=4
contacts_contactPersonMobile=5
contacts_contactPersonComment=6
contacts_assertKeyWorks=7
contacts_isExecute=8
contacts_runTime=9
contacts_testResult=10

