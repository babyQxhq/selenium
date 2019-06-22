# coding=utf_8
from util.read_ini import ReadIni


class FindElement(object):
    """docstring for FindElement"""

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key):
        read_ini = ReadIni()
        # 返回register_nickname形式数据
        data = read_ini.get_value(key)
        # 以>进行拆分，第一个是查找形式，第二个是查找参数
        by = data.split('>')[0]
        val = data.split('>')[1]
        try:
            if by == 'id':
                element = self.driver.find_element_by_id(val)
                return element
            elif by == 'link_text':
                element = self.driver.find_element_by_link_text(val)
                return element
            elif by == 'class_name':
                element = self.driver.find_elements_by_class_name(val)
                return element
            elif by == 'xpath':
                element = self.driver.find_element_by_xpath(val)
                return element
            else:
                element = self.driver.find_element_by_css_selector(val)
                return element

        except:
            self.driver.save_screenshot('image/%s.png' %val)
            return None

