import zidonghua.Common.Cookies
import zidonghua.Common.Requests
import zidonghua.Common.Select_Order
import zidonghua.Interface.Goods_Rejected

def goods_rejected(mobile,so_code):
    cookies = zidonghua.Common.Cookies.get_cookies(mobile)
    so_goods_order, po_goods_order = (
        zidonghua.Common.Select_Order.order(so_code).parana_get_goods_order())
    ordercode = so_goods_order[0]['code']
    orderid = so_goods_order[0]['id']
    so_delivery_order, po_delivery_order =(
        zidonghua.Common.Select_Order.order(so_code).parana_delivery_order())
    for i in range(len(so_delivery_order)):
        if so_delivery_order[i]['GetGoodsOrderPODeliveryOrderPO'] == orderid:
            deliveryId = so_delivery_order[i]['id']
            podeliveryId =po_delivery_order[i]['id']
    zidonghua.Interface.Goods_Rejected.data2['deliveryId'] = deliveryId
    url1 ="https://b2b-mall-uat.test.lcscm.cn/api/front/reverse/apply/'{}'".format(orderid)
    response1 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Goods_Rejected.url1,
         cookies=cookies).get()
    result1 = response1['result']
    response2 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Goods_Rejected.url2,json=zidonghua.Interface.Goods_Rejected.data2,
        cookies=cookies).post()
    result2 = response2.json()['result']
    data3 = zidonghua.Interface.Goods_Rejected.data3
    data3['deliveryOrderId'] = result1['deliveryOrderInfos'][0]['id']
    data3['deliveryOrderCode'] =result1['deliveryOrderInfos'][0]['code']
    data3['reverseItemLineInfos'] =result2['reverseItemLineInfos']
    data3['contactMobile'] = result1['contactMobile']   # 多个商品
    # data3['reverseItemLineInfos'] =result2['reverseItemLineInfos'][0]
    # data3['reverseItemLineInfos'][0]['reverseNum']=1 # 退货数量
    response3 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Goods_Rejected.url3, json=zidonghua.Interface.Goods_Rejected.data3,
        cookies=cookies).post()
    print(response3.json())
    so_reverse_order, po_reverse_order=(
        zidonghua.Common.Select_Order.order(so_code).parana_reverse_order())
    for  i in range(len(parana_reverse_order)):
        if po_reverse_order[i]['get_goods_order_id'] == podeliveryId:
            data4['context']['record'][0]['id'] = po_reverse_order[0]['id']

    response4 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Goods_Rejected.url4, json=zidonghua.Interface.Goods_Rejected.data4,
        cookies=cookies).post()
    print(response4.json())

if __name__ == '__main__':
 print(goods_rejected('18178952878','SO20240222000006'))


