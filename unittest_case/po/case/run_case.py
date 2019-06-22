#coding=utf-8
#运行所以case
import HTMLTestRunner
import unittest
import os
class RunCase(unittest.TestCase):
    def test_case01(self):
        #获取当前路径
        case_path=os.path.join(os.getcwd(),'case')
        unittest.defaultTestLoader.discover(case_path,'unittest_*.py')
        unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    unittest.main()