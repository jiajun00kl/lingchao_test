import json
import zidonghua.Common.Requests
import zidonghua.Common.Cookies
import zidonghua.Common.Settlement_Order
import zidonghua.Interface.Confirm_Sales

def TestConfirmSales(mobile,so_code):  # 确认对账单
    cookies = zidonghua.Common.Cookies.get_cookies(mobile)
    salecheck = zidonghua.Common.Settlement_Order.sale_check(so_code)
    sales_check_id =salecheck[0]['id']
    print(sales_check_id)
    data1 = zidonghua.Interface.Confirm_Sales.data1
    data1['queryValues']['id']['value'] = sales_check_id
    response1 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Confirm_Sales.url1,
        json=zidonghua.Interface.Confirm_Sales.data1, cookies=cookies).post()
    result1 = response1.json()
    data2 = zidonghua.Interface.Confirm_Sales.data2
    data2['related']['recordIds'][0] = sales_check_id
    response2 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Confirm_Sales.url1,
        json=zidonghua.Interface.Confirm_Sales.data2, cookies=cookies).post()
    result2 = response2.json()
    data3 = zidonghua.Interface.Confirm_Sales.data3
    data3['related']['recordIds'][0] = sales_check_id
    response3 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Confirm_Sales.url1,
        json=zidonghua.Interface.Confirm_Sales.data3, cookies=cookies).post()
    result3= response3.json()
    data4 = zidonghua.Interface.Confirm_Sales.data4
    data4['related']['recordIds'][0] = sales_check_id
    response4 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Confirm_Sales.url1,
        json=zidonghua.Interface.Confirm_Sales.data4, cookies=cookies).post()
    result4 = response4.json()
    data5 = zidonghua.Interface.Confirm_Sales.data5
    data5['related']['recordIds'][0] = sales_check_id
    response5 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Confirm_Sales.url1,
        json=zidonghua.Interface.Confirm_Sales.data5, cookies=cookies).post()
    result5 = response5.json()
    data6 = zidonghua.Interface.Confirm_Sales.data6
    data6['related']['recordIds'][0] = sales_check_id
    response6 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Confirm_Sales.url1,
        json=zidonghua.Interface.Confirm_Sales.data6, cookies=cookies).post()
    result6 = response6.json()
    data7 = zidonghua.Interface.Confirm_Sales.data2
    data7['related']['recordIds'][0] = sales_check_id
    response7 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Confirm_Sales.url1,
        json=zidonghua.Interface.Confirm_Sales.data7, cookies=cookies).post()
    result7 = response7.json()
    data8 = zidonghua.Interface.Confirm_Sales.data8
    data8['related']['recordIds'][0] = sales_check_id
    response8 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Confirm_Sales.url1,
        json=zidonghua.Interface.Confirm_Sales.data8, cookies=cookies).post()
    result8 = response8.json()
    data9 = zidonghua.Interface.Confirm_Sales.data9
    data9['related']['recordIds'][0] = sales_check_id
    response9 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Confirm_Sales.url1,
        json=zidonghua.Interface.Confirm_Sales.data9, cookies=cookies).post()
    result9 = response9.json()
    data10 = zidonghua.Interface.Confirm_Sales.data10
    data10['related']['recordIds'][0] = sales_check_id
    response10 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Confirm_Sales.url1,
        json=zidonghua.Interface.Confirm_Sales.data10, cookies=cookies).post()
    result10 = response10.json()
    data11 = zidonghua.Interface.Confirm_Sales.data11
    data11['context']['record'][0]['id'] = sales_check_id
    response11 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Confirm_Sales.url2,
        json=zidonghua.Interface.Confirm_Sales.data11, cookies=cookies).post()
    return response11.json()

if __name__ == '__main__':
    print(TestConfirmSales('18178952878','SO20240527000007'))