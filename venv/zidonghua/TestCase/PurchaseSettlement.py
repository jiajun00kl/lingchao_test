import json,time
import zidonghua.Common.Requests
import zidonghua.Interface.Purchase_Settlement
import zidonghua.Common.Cookies
import zidonghua.Common.Settlement_Order

def purchase_settlement(mobile,so_code):   # 采购结算，生成对账单并提交
    cookies = zidonghua.Common.Cookies.get_cookies(mobile)
    data1 = zidonghua.Interface.Purchase_Settlement.data1
    payable,payable1 = zidonghua.Common.Settlement_Order.settlement_payable(so_code)
    ids = []
    for i in range(len(payable1)):
        ids.append(payable1[i]['payable_source_code']+'——'+payable1[i]['payable_source_type'])
    data1['context']['env']['ids'] = ids
    response1 = zidonghua.Common.Requests.HttpUtil(
        url = zidonghua.Interface.Purchase_Settlement.url1,
        json= zidonghua.Interface.Purchase_Settlement.data1, cookies=cookies).post()
    result1 = response1.json()
    id = result1['res']['data']
    data2 = zidonghua.Interface.Purchase_Settlement.data2
    data2['queryValues']['id']['value'] = id
    response2 = zidonghua.Common.Requests.HttpUtil(
        url = zidonghua.Interface.Purchase_Settlement.url2,
        json= zidonghua.Interface.Purchase_Settlement.data2, cookies=cookies).post()
    result2 = response2.json()
    data3 = zidonghua.Interface.Purchase_Settlement.data3
    data3['related']['recordIds'][0] = id
    response3 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Purchase_Settlement.url2,
        json=zidonghua.Interface.Purchase_Settlement.data3, cookies=cookies).post()
    result3 = response3.json()
    data4 = zidonghua.Interface.Purchase_Settlement.data4
    data4['related']['recordIds'][0] = id
    response4 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Purchase_Settlement.url2,
        json=zidonghua.Interface.Purchase_Settlement.data4, cookies=cookies).post()
    result4 = response4.json()
    data5 = zidonghua.Interface.Purchase_Settlement.data5
    data5['related']['recordIds'][0] = id
    response5 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Purchase_Settlement.url2,
        json=zidonghua.Interface.Purchase_Settlement.data5, cookies=cookies).post()
    result5 = response5.json()
    data6 = zidonghua.Interface.Purchase_Settlement.data6
    data6['related']['recordIds'][0] = id
    response6 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Purchase_Settlement.url2,
        json=zidonghua.Interface.Purchase_Settlement.data6, cookies=cookies).post()
    result6 = response6.json()
    data7 = zidonghua.Interface.Purchase_Settlement.data7
    data7['related']['recordIds'][0] = id
    response7 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Purchase_Settlement.url2,
        json=zidonghua.Interface.Purchase_Settlement.data7, cookies=cookies).post()
    result7 = response7.json()
    data8 = zidonghua.Interface.Purchase_Settlement.data8
    data8['related']['recordIds'][0] = id
    response8 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Purchase_Settlement.url2,
        json=zidonghua.Interface.Purchase_Settlement.data8, cookies=cookies).post()
    result8 = response8.json()
    data9 = zidonghua.Interface.Purchase_Settlement.data9
    data9['related']['recordIds'][0] = id
    response9 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Purchase_Settlement.url2,
        json=zidonghua.Interface.Purchase_Settlement.data9 ,cookies=cookies).post()
    result9 = response9.json()
    data10 = zidonghua.Interface.Purchase_Settlement.data10
    data10['related']['recordIds'][0] = id
    response10 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Purchase_Settlement.url2,
        json=zidonghua.Interface.Purchase_Settlement.data10, cookies=cookies).post()
    result10 = response10.json()
    data11 = zidonghua.Interface.Purchase_Settlement.data11
    data11['related']['recordIds'][0] = id
    response11 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Purchase_Settlement.url2,
        json=zidonghua.Interface.Purchase_Settlement.data11, cookies=cookies).post()
    result11 = response11.json()
    data12 = zidonghua.Interface.Purchase_Settlement.data12
    data12['related']['recordIds'][0] = id
    response12 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Purchase_Settlement.url2,
        json=zidonghua.Interface.Purchase_Settlement.data12, cookies=cookies).post()
    result12 = response12.json()
    data13 = zidonghua.Interface.Purchase_Settlement.data13
    # print(result2['res']['data'])
    data13['context']['record'][0]['purchaseCheckCode'] = result2['res']['data']['purchaseCheckCode']
    data13['context']['record'][0]['purchaseCheckName'] = result2['res']['data']['purchaseCheckName']
    data13['context']['record'][0]['contract']['id'] = result2['res']['data']['contract']['id']
    data13['context']['record'][0]['contract']['code'] = result2['res']['data']['contract']['code']
    data13['context']['record'][0]['contractName'] = result2['res']['data']['contractName']
    data13['context']['record'][0]['checkAcceptMonth'] = int(time.time()) * 1000
    data13['context']['record'][0]['taxRate'] = result2['res']['data']['taxRate']
    data13['context']['record'][0]['createdAt'] = result2['res']['data']['createdAt']
    data13['context']['record'][0]['createdBy']['id'] = result2['res']['data']['createdBy']['id']
    data13['context']['record'][0]['createdBy']['nickname'] = (
        result2)['res']['data']['createdBy']['nickname']
    data13['context']['record'][0]['status'] = result2['res']['data']['status']
    data13['context']['record'][0]['contractCompletedTotal'] = (
        result2)['res']['data']['contractCompletedTotal']
    data13['context']['record'][0]['finalTotal'] = result2['res']['data']['finalTotal']
    data13['context']['record'][0]['adjustInvoiceTotal'] = (
        result2)['res']['data']['adjustInvoiceTotal']
    data13['context']['record'][0]['remark'] = result2['res']['data']['remark']
    data13['context']['record'][0]['id'] = result2['res']['data']['id']
    data13['context']['record'][0]['supplier'] = result2['res']['data']['supplier']
    data13['context']['record'][0]['purchaseCheckAdjustList'] = (
        result2)['res']['data']['purchaseCheckAdjustList']
    data13['context']['record'][0]['purchaseCheckAttachmentList'] = (
        result2)['res']['data']['purchaseCheckAttachmentList']
    data13['context']['record'][0]['purchaseCheckSystemAttachments'] = (
        result2)['res']['data']['purchaseCheckSystemAttachments']
    response13 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Purchase_Settlement.url1,
        json=zidonghua.Interface.Purchase_Settlement.data13, cookies=cookies).post()
    result13 = response13.json()
    return result13


if __name__ == '__main__':
    print(purchase_settlement('18178952878','SO20231225000001'))



