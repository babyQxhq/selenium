#coding=utf-8
class FindElement(object):
    def __int__(self,driver):
        self.driver=driver

    def get_element(self,by,value):
        try:
            if by=="id":
                return self.driver.find_element_by_id(value)
            elif by == 'link_text':
                return self.driver.find_element_by_link_text(value)

            elif by == 'class_name':
                 return self.driver.find_elements_by_class_name(value)

            elif by == 'xpath':
                 return self.driver.find_element_by_xpath(value)

            else:
                 return self.driver.find_element_by_css_selector(value)
        except:
            self.driver.save_screenshot('image/%s.png' %value)
            return None