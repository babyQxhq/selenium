#coding=utf-8
from selenium import webdriver

import time

driver=webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://mail.126.com/")
time.sleep(3)




driver.find_element_by_id("lbNormal").click()
time.sleep(1)
iframe=driver.find_element_by_xpath('//*[@id="loginDiv"]/iframe')
driver.switch_to.frame(iframe)
driver.find_element_by_xpath('//input[@name="email"]').send_keys("xhq11093")

driver.find_element_by_xpath('//input[@name="password"]').send_keys("xhq11093..")
driver.find_element_by_id("dologin").click()
driver.find_element_by_id("_mail_tabitem_1_4text").click()
time.sleep(1)
# //div[starts-with(@id,'_mail_button_')][1]
driver.find_elements_by_xpath("//div[@id='dvContainer']/div/div/div//section[2]/div/div/span")[0].click()
time.sleep(1)
driver.find_element_by_id('input_N').send_keys("babyQ")
driver.find_element_by_xpath('//*[@id="iaddress_MAIL_wrap"]/dl/dd/div/input').send_keys("981311093@qq.com")
driver.find_element_by_class_name('nui-chk-symbol').click()
driver.find_element_by_xpath("//div[(@id='iaddress_TEL_wrap')]/dl/dd/div/input").send_keys("15210424367")
driver.find_element_by_xpath('//*[@id="contact_edit_main_normal"]/dl[3]/dd/div/textarea').send_keys("babyQ")
driver.find_elements_by_xpath("//div[@class='nui-msgbox-ft-btns']/div")[0].click()



time.sleep(3)


driver.close()
