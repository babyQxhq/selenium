#coding=utf_8
import configparser
class ReadIni(object):

	def __init__(self,file_name=None,node=None):
		if file_name==None:
			file_name="../config/LocalElement.ini"
		if node==None:
			self.node="LoginElement"
		else:
			self.node=node
		self.cf=self.load_ini(file_name)

	#加载文件
	def  load_ini(self,file_name):
		cft=configparser.ConfigParser()
		cft.read(file_name)
		return cft
	#获取value值
	def get_value(self,key):
		data=self.cf.get(self.node,key)
		return data







