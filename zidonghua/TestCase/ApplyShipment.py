import zidonghua.Common.Requests
import zidonghua.Interface.Apply_Shipment
import zidonghua.Common.Cookies
import zidonghua.Common.Select_Order

def apply_shipment(mobile,so_code):   # 供应商申请发货
    cookies = zidonghua.Common.Cookies.get_cookies(mobile)
    so_goods_order,po_goods_order = (
        zidonghua.Common.Select_Order.order(so_code).parana_get_goods_order())
    zidonghua.Interface.Apply_Shipment.data1['queryValues']['id']['value'] = po_goods_order[0]['id']
    response = zidonghua.Common.Requests.HttpUtil(
        url = zidonghua.Interface.Apply_Shipment.url1,
        json = zidonghua.Interface.Apply_Shipment.data1, cookies = cookies).post()
    orders = response.json()['res']['data']
    data = zidonghua.Interface.Apply_Shipment.data2
    record = data['context']['record'][0]
    data['context']['env']['getGoodsOrderId'] = orders['getGoodsOrder']['id']
    record['getGoodsOrderCode'] = orders['getGoodsOrderCode']
    record['getGoodsOrder']['id'] = orders['getGoodsOrder']['id']
    record['getGoodsOrder']['siteReceivingContact'] = orders['getGoodsOrder']['siteReceivingContact']
    record['getGoodsOrder']['siteReceivingContactPhone'] = (
        orders)['getGoodsOrder']['siteReceivingContactPhone']
    record['order']['id'] = orders['order']['id']
    record['order']['purchaserName'] = orders['order']['purchaserName']
    record['order']['project'] = orders['order']['project']
    record['order']['dealerContactName'] = orders['order']['dealerContactName']
    record['order']['dealerContactMobile'] = orders['order']['dealerContactMobile']
    record['order']['brandOwnerName'] = orders['order']['brandOwnerName']
    record['lingchaoContact'] = orders['lingchaoContact']
    record['lingchaoMobile'] = orders['lingchaoMobile']
    deliveryOrderLinePOList = []
    for i in range(len(orders['deliveryOrderLinePOList'])):
        dict1 = {}
        dict1['item'] = orders['deliveryOrderLinePOList'][i]['item']
        dict1['itemCode'] = orders['deliveryOrderLinePOList'][i]['itemCode']
        dict1['itemName'] = orders['deliveryOrderLinePOList'][i]['itemName']
        dict1['specification'] = orders['deliveryOrderLinePOList'][i]['specification']
        dict1['unit'] = orders['deliveryOrderLinePOList'][i]['unit']
        dict1['getGoodsOrderLine']=orders['deliveryOrderLinePOList'][i]['getGoodsOrderLine']
        dict1['deliveryNum'] = (
            orders)['deliveryOrderLinePOList'][i]['deliveryNum']
        deliveryOrderLinePOList.append(dict1)
    record['deliveryOrderLinePOList'] = deliveryOrderLinePOList
    response1 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Apply_Shipment.url2,
        json=data, cookies=cookies).post()
    return response1.json()
print(apply_shipment('18178952878','SO20240525000003'))
