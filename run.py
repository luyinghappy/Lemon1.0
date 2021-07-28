# @Project:SCB_22
# @Auth:  禾禾
# @Time:  2021/7/19 23:59
# @E-mail:1554152079@qq.com
# @Company:测试

from common.method import read_case,write_result, api_fun

# 完整的接口自动化测试
def execute_fun(filename,sheetname):  # 封装成函数
    cases = read_case(filename, sheetname)  # 定义变量，接收获取测试用例数据
    for case in cases:
        case_id = case['case_id']
        url = case['url']  # 获取url
        data = eval(case['data'])  # 获取data
        expect = eval(case['expect']) # 获取期望expect
        # print(case)
        # print(case_id,data,type(expect))
        # 获取期望code、msg
        expect_code = expect['code']
        expect_msg = expect['msg']
        print('预期结果：code为{}，msg为：{}'.format(expect_code,expect_msg))
        # 调用接口
        real_result = api_fun(url=url,data=data)
        # print(real_result)
        # 获取实际的code、msg
        real_code = real_result['code']
        real_msg = real_result['msg']
        print('实际结果：code为{},msg为{}'.format(real_code,real_msg))

        # 断言
        if expect_code==real_code and expect_msg==real_msg:
            print('第{}条测试用例通过'.format(case_id))
            final_re = 'Passed'
        else:
            print('第{}条测试用例不通过'.format(case_id))
            final_re = 'Failed'
        print('*' * 10)
        # 写入最终的测试结果到excel
        write_result(filename,sheetname,case_id+1,8,final_re)

# 调用execute_fun()函数，对login接口自动化测试
execute_fun('C:\Users\Administrator\.jenkins\workspace\scb22\\test_data\\testcase_api_wuye.xlsx', 'login' )








