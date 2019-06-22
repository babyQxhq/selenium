#coding=utf-8
from xlutils.copy import copy
import xlrd
import time
class ExcelUtil:
    def __init__(self,file_path=None,index=None):
        if file_path==None:
            self.file_path="../config/key_word.xls"
        else:
            self.file_path=file_path
        if index==None:
            index=0
        self.data=xlrd.open_workbook(self.file_path)
        self.table=self.data.sheets()[index]
        #把数据组织成字符序列
        #行数

    def get_data(self):
        result=[]
        rows=self.get_lines()
        if rows!=None:
            for i in range(rows):
                col=self.table.row_values(i)
                result.append(col)
            return (result)
        return None
    #获取行数
    def get_lines(self):
        rows = self.table.nrows
        if rows>=1:
            return rows
        return None
    #获取单元格数据
    def get_col_value(self,row,col):
        if self.get_lines()>row:
            data=self.table.cell(row,col).value
            return data

    #写入数据
    def write_val(self,row,value):
        read_value=xlrd.open_workbook(self.file_path)
        print(read_value)
        write_data=copy(read_value)
        write_data.get_sheet(0).write(row,9,value)
        write_data.save(self.file_path)
        time.sleep(1)
if __name__ == '__main__':
    eu=ExcelUtil()
    eu.write_val(1,"pass")
    w=eu.get_col_value(1,1)
    print(w)