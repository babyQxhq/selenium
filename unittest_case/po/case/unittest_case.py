#coding=utf-8
import unittest
import HTMLTestRunner
import os
class FirstCase(unittest.TestCase):
    #case必须以test开头
    @classmethod
    def setUpClass(cls) -> None:
        print("001")
    @classmethod
    def tearDownClass(cls) -> None:
        print("002")
    def setUp(self):
        print("这是case的前置条件")
    def tearDown(self):
        print("这是后置条件")
    def test01(self):
        print('case001')
    def test02(self):
        print('case02')
if __name__ == '__main__':
    # unittest.main()
    # suite=unittest.TestSuite()
    # suite.addTest(FirstCase('test01'))
    # unittest.TextTestRunner().run(suite)
    file_path = os.path.join(os.getcwd() + "/report" + "/case.html")
    f = open(file_path, 'wb')
    suit = unittest.TestSuite()
    suit.addTest(FirstCase('test01'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="麦子", description=u'第一个测试报告', verbosity=2)
    runner.run(suit)