import json
import zidonghua.Common.Requests
import zidonghua.Interface.Sales_Check
import zidonghua.Common.Cookies
import zidonghua.Common.Settlement_Order

def sales_check(mobile,so_code):  # 生成对账单
    cookies = zidonghua.Common.Cookies.get_cookies(mobile)
    receivable = zidonghua.Common.Settlement_Order.settlement_receivable(so_code)
    ids = []
    SourceCode = ""  # 确保SourceCode被初始化为空字符串
    for item in receivable:  # 直接遍历列表元素，而不是索引
        ids.append(item['receivable_source_code']+'——'+item['receivable_source_type'])
        if SourceCode:  # 如果SourceCode不为空，即已经有内容，才添加换行符和源代码
            SourceCode += r'\n' + item['receivable_source_code']
        else:  # 如果是第一个元素，直接赋值，不需要加换行符
            SourceCode = item['receivable_source_code']
    data1 = zidonghua.Interface.Sales_Check.data1
    data1['context']['env']['ids'] = ids
    data1['context']['env']['searchData']['receivableSourceCode'] =  SourceCode
    response1 = zidonghua.Common.Requests.HttpUtil(
        url = zidonghua.Interface.Sales_Check.url1,
        json = zidonghua.Interface.Sales_Check.data1, cookies = cookies).post()
    sales_check_id = response1.json()['res']['data']
    data2 = zidonghua.Interface.Sales_Check.data2
    data2['searchValues']['receivableSourceCode']['value'] = SourceCode
    response2 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Sales_Check.url2,
        json=zidonghua.Interface.Sales_Check.data2, cookies=cookies).post()
    result2 = response2.json()
    data3 = zidonghua.Interface.Sales_Check.data3
    data3['queryValues']['id']['value'] = sales_check_id
    response3 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Sales_Check.url2,
        json=zidonghua.Interface.Sales_Check.data3, cookies=cookies).post()
    result3 = response3.json()['res']['data']
    data4 = zidonghua.Interface.Sales_Check.data4
    data4['related']['recordIds'][0] = sales_check_id
    response4 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Sales_Check.url2,
        json=zidonghua.Interface.Sales_Check.data4, cookies=cookies).post()
    result4 = response4.json()
    data5 = zidonghua.Interface.Sales_Check.data5
    data5['related']['recordIds'][0]= sales_check_id
    response5 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Sales_Check.url2,
        json=zidonghua.Interface.Sales_Check.data5, cookies=cookies).post()
    result5 = response5.json()
    data6 = zidonghua.Interface.Sales_Check.data6
    data6['related']['recordIds'][0] = sales_check_id
    response6 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Sales_Check.url2,
        json=zidonghua.Interface.Sales_Check.data6, cookies=cookies).post()
    result6 = response6.json()
    data7 = zidonghua.Interface.Sales_Check.data7
    data7['related']['recordIds'][0] = sales_check_id
    response7 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Sales_Check.url2,
        json=zidonghua.Interface.Sales_Check.data7, cookies=cookies).post()
    result7 = response7.json()
    data8 = zidonghua.Interface.Sales_Check.data8
    data8['related']['recordIds'][0] = sales_check_id
    response8 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Sales_Check.url2,
        json=zidonghua.Interface.Sales_Check.data8, cookies=cookies).post()
    result8 = response8.json()
    data9 = zidonghua.Interface.Sales_Check.data9
    data9['related']['recordIds'][0] = sales_check_id
    response9= zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Sales_Check.url2,
        json=zidonghua.Interface.Sales_Check.data9, cookies=cookies).post()
    result9 = response9.json()
    data10 = zidonghua.Interface.Sales_Check.data10
    data10['related']['recordIds'][0] = sales_check_id
    response10 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Sales_Check.url2,
        json=zidonghua.Interface.Sales_Check.data10, cookies=cookies).post()
    result10 = response10.json()
    data11 = zidonghua.Interface.Sales_Check.data11
    data11['related']['recordIds'][0] = sales_check_id
    response11 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Sales_Check.url2,
        json=zidonghua.Interface.Sales_Check.data11, cookies=cookies).post()
    result11 = response11.json()
    data12 = zidonghua.Interface.Sales_Check.data12
    data12['related']['recordIds'][0] = sales_check_id
    response12 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Sales_Check.url2,
        json=zidonghua.Interface.Sales_Check.data12, cookies=cookies).post()
    result12 = response12.json()
    data13 = zidonghua.Interface.Sales_Check.data13
    data13['related']['recordIds'][0] = sales_check_id
    response13 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Sales_Check.url2,
        json=zidonghua.Interface.Sales_Check.data13, cookies=cookies).post()
    result13 = response13.json()
    record = zidonghua.Interface.Sales_Check.data14['context']['record'][0]
    record['requestFundsInfoUrl'] = result3['requestFundsInfoUrl']
    record['salesCheckCode'] = result3['salesCheckCode']
    record['salesCheckName'] = result3['salesCheckName']
    record['contract']['id'] = result3['contract']['id']
    record['contract']['code'] = result3['contract']['code']
    record['contract']['project']['corporateCompany']['companyCode']= (
        result3)['contract']['project']['corporateCompany']['companyCode']
    record['contract']['project']['corporateCompany']['uscc'] = (
        result3)['contract']['project']['corporateCompany']['uscc']
    record['contract']['project']['corporateCompany']['mobile'] = (
        result3)['contract']['mobile']
    record['contract']['project']['corporateCompany']['address'] = (
        result3)['contract']['project']['corporateCompany']['address']
    record['contract']['project']['corporateCompany']['invoiceInfo']['id'] = (
        result3)['contract']['project']['corporateCompany']['invoiceInfo']['id']
    record['contract']['project']['corporateCompany']['invoiceInfo']['invoiceCompany'] = \
        (result3)['contract']['project']['corporateCompany']['invoiceInfo']['invoiceCompany']
    record['contract']['project']['corporateCompany']['invoiceInfo']['invoiceBank']\
        = (result3)['contract']['project']['corporateCompany']['invoiceInfo']['invoiceBank']
    record['contract']['project']['corporateCompany']['invoiceInfo']['invoiceAccount'] \
        = (result3)['contract']['project']['corporateCompany']['invoiceInfo']['invoiceAccount']
    record['contract']['project']['corporateCompany']['id'] = \
        (result3)['contract']['project']['corporateCompany']['id']
    record['contractName'] = (result3)['contract']['name']
    record['checkAcceptMonth'] = result3['checkAcceptMonth']
    record['taxRate'] = result3['taxRate']
    record['createdAt'] = result3['createdAt']
    record['createdBy'] = result3['createdBy']
    record['status'] = result3['status']
    record['contractCompletedTotal'] = result3['contractCompletedTotal']
    record['finalTotal'] = result3['finalTotal']
    record['adjustInvoiceTotal'] = result3['adjustInvoiceTotal']
    record['outlineCheck'] = result3['outlineCheck']
    record['remark'] = result3['remark']
    record['id'] = result3['id']
    record['salesCheckAdjustList'] = result3['salesCheckAdjustList']
    record['salesCheckAttachments'] = result3['salesCheckAttachments']
    record['salesCheckSystemAttachments'] = result3['salesCheckSystemAttachments']
    response14 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Sales_Check.url1,
        json=zidonghua.Interface.Sales_Check.data14, cookies=cookies).post()
    return response14.json()

if __name__ == '__main__':
    print(sales_check('admin','SO20240228000001'))
