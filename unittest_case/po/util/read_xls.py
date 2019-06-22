#coding=utf-8
import xlrd
class ReadXls(object):


    def read_xls(self,file_name=None):
        if file_name==None:
            file_name="config/user.xls"
        xl=xlrd.open_workbook(file_name)
        table=xl.sheets()[0]
        row=table.row_values(1)
        # col=table.col_values(0)
        # print(row[2],row[3])
        return row
