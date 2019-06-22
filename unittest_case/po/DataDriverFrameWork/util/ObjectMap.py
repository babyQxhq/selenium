#coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
# class FindElement(object):
#     def __int__(self,driver):
#         self.driver=driver

def getElement(driver,locateType,locatorExpression):
    try:
        #lambda为匿名函数
        element=WebDriverWait(driver,30).until\
            (lambda x:x.find_element(by=locateType,value=locatorExpression))
        return element
    except Exception as e:
        raise e


def getElements(driver,locateType,locatorExpression):

    try:
        #lambda为匿名函数
        element=WebDriverWait(driver,30).until\
            (lambda x:x.find_elements(by=locateType,value=locatorExpression))
        return element
    except Exception as e:
        raise e

if __name__ == '__main__':
    from selenium import webdriver
    import time
    driver=webdriver.Chrome()
    driver.get("http://baidu.com/")



    searchBox=get_Element(driver,"id","kw")
    searchBox.send_keys("111")
    print(searchBox.tag_name)
    time.sleep(3)
    aList=get_Elements(driver,"tag name","a")
    print(len(aList))
    time.sleep(3)
    driver.quit()

    # if by=="id":
    #     return self.driver.find_element_by_id(value)
    # elif by == 'link_text':
    #     return self.driver.find_element_by_link_text(value)
    #
    # elif by == 'class_name':
    #      return self.driver.find_elements_by_class_name(value)
    #
    # elif by == 'xpath':
    #      return self.driver.find_element_by_xpath(value)
    #
    # else:
    #      return self.driver.find_element_by_css_selector(value)
    # # except:
    # #     self.driver.save_screenshot('image/%s.png' %value)
    # #     return None