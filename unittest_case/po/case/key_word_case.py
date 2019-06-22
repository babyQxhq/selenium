#coding=utf-8
from util.excel_util import ExcelUtil
from key_word.action_Method import ActionMethod
class KeyWordCase:
    def run_main(self):
        self.action_method = ActionMethod()
        handle_excel=ExcelUtil()
        case_lines=handle_excel.get_lines()
        if case_lines:
            for i in range(1,case_lines):
                is_run=handle_excel.get_col_value(i,3)
                if is_run=='yes':
                    method=handle_excel.get_col_value(i,4)
                    send_value=handle_excel.get_col_value(i,5)
                    handle_value=handle_excel.get_col_value(i,6)
                    except_result_method = handle_excel.get_col_value(i,7)
                    except_result = handle_excel.get_col_value(i, 8)

                    self.run_method(method,send_value,handle_value)
                    if except_result!='':
                        except_value=self.get_expect_result_value(except_result)
                        if except_value[0]=='text':
                            result=self.run_method(except_result_method)
                            if except_value[1] in result:
                                handle_excel.write_val(i,'pass')
                            else:
                                handle_excel.write_val(i,'fail')
                        elif except_value[0]=='element':
                            self.run_method(except_result_method,except_value[1])
                            if result:
                                handle_excel.write_val(i,'pass')
                            else:
                                handle_excel.write_val(i,'fail')

                    else:
                        print('预期结果为空')
    #获取预期结果值
    def get_expect_result_value(self,data):
         return data.split('=')
         pass
        #拿到行数
        #循环行数去执行每一行的case
        #是否执行
            #是：拿到执行方法，拿到操作值，拿到输入数据
            #是否有输入数据
                #有：执行方法（输入数据，操作元素）
                #没有：执行方法（操作元素）

    def run_method(self,method,send_value='',handle_value=''):

        method_value=getattr(self.action_method,method)
        # print(method_value)
        if send_value!=''and handle_value!='':
            result=method_value(send_value,handle_value)
        elif send_value=='' and handle_value!='':
            result=method_value(handle_value)
        elif send_value!='' and handle_value=='':
            result=method_value(send_value)
        else:
            result=method_value()
        return result
if __name__ == '__main__':
    kwc=KeyWordCase()
    kwc.run_main()