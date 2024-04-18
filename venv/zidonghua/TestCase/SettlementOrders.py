import datetime,json
import zidonghua.Common.Requests
import zidonghua.Interface.Settlement_Orders
import zidonghua.Common.Cookies
import zidonghua.Common.Select_Order

def settlement_orders(mobile,so_code): #供应商发起需求单结算
    cookies = zidonghua.Common.Cookies.get_cookies(mobile)
    so_order, po_order = zidonghua.Common.Select_Order.order(so_code).parana_order()
    zidonghua.Interface.Settlement_Orders.data1['context']['record'][0]['id'] = po_order['id']
    response = zidonghua.Common.Requests.HttpUtil(
        url= zidonghua.Interface.Settlement_Orders.url1,
        json= zidonghua.Interface.Settlement_Orders.data1, cookies=cookies).post()
    restult1 = response.json()
    zidonghua.Interface.Settlement_Orders.data2['queryValues']['id']['value'] = po_order['id']
    response1 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Settlement_Orders.url2,
        json=zidonghua.Interface.Settlement_Orders.data2, cookies=cookies).post()
    restult2 = response1.json()['res']['data']
    data = zidonghua.Interface.Settlement_Orders.data3['context']['record'][0]
    data['order'] = restult2['order']
    data['settlementTotal'] = restult2['settlementTotal']
    data['remainedRetentionStart'] = int(datetime.datetime.now().timestamp() * 1000)
    data['remainedRetentionEnd'] = int(datetime.datetime.now().timestamp() * 1000+ 3600000000)
    data['orderSettlementDetailList'] = restult2['orderSettlementDetailList']
    data['orderSettlementAttachList'] = restult2['orderSettlementAttachList']
    response2 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Settlement_Orders.url3,
        json=zidonghua.Interface.Settlement_Orders.data3, cookies=cookies).post()
    return response2.json()
if __name__ == '__main__':
    print(settlement_orders('18178952877','SO20240222000006'))