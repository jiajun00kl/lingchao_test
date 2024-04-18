import json
import zidonghua.Common.Requests
import zidonghua.Interface.Order_Accept
import zidonghua.Common.Cookies
import zidonghua.Common.Select_Order

def order_accept(mobile,so_code): # 订单到货验收
    cookies = zidonghua.Common.Cookies.get_cookies(mobile)
    so_delivery_order, po_delivery_order = (
        zidonghua.Common.Select_Order.order(so_code).parana_delivery_order())
    zidonghua.Interface.Order_Accept.data1['queryValues']['id']['value'] = so_delivery_order[1]['id']
    response = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Order_Accept.url1,
        json=zidonghua.Interface.Order_Accept.data1, cookies = cookies).post()
    orders = response.json()['res']['data']
    data = zidonghua.Interface.Order_Accept.data2
    record = data['context']['record'][0]['context']
    for i in range(len(orders['acceptanceOrderLinePOList'])):
        orders['acceptanceOrderLinePOList'][i]['acceptanceNum'] = (
            orders)['acceptanceOrderLinePOList'][i]['deliveryNum']
    record = orders
    '''
    
    record['isInstall'] = orders['isInstall']
    record['deliveryOrder'] = orders['deliveryOrder']
    record['parentAcceptanceOrderCode'] = orders['parentAcceptanceOrderCode']
    record['order'] = orders['order']
    record['deliveryCode'] = orders['deliveryCode']
    record['getGoodsOrder'] = orders['getGoodsOrder']
    record['sender'] = orders['sender']
    record['contactMobile'] = orders['contactMobile']
    record['deliveryDate'] = orders['deliveryDate']
    record['lingchaoContact'] = orders['lingchaoContact']
    record['lingchaoMobile'] = orders['lingchaoMobile']
    record['acceptanceOrderLinePOList'][0]['itemCode'] = (
        orders)['acceptanceOrderLinePOList'][0]['itemCode']
    record['acceptanceOrderLinePOList'][0]['item'] = (
        orders)['acceptanceOrderLinePOList'][0]['item']
    record['acceptanceOrderLinePOList'][0]['itemName'] = (
        orders)['acceptanceOrderLinePOList'][0]['itemName']
    record['acceptanceOrderLinePOList'][0]['brand'] = (
        orders)['acceptanceOrderLinePOList'][0]['brand']
    record['acceptanceOrderLinePOList'][0]['specification'] = (
        orders)['acceptanceOrderLinePOList'][0]['specification']
    record['acceptanceOrderLinePOList'][0]['unit'] = (
        orders)['acceptanceOrderLinePOList'][0]['unit']
    record['acceptanceOrderLinePOList'][0]['getGoodsOrderLinePO'] = (
        orders)['acceptanceOrderLinePOList'][0]['getGoodsOrderLinePO']
    record['acceptanceOrderLinePOList'][0]['deliveryNum'] = (
        orders)['acceptanceOrderLinePOList'][0]['deliveryNum']
    record['acceptanceOrderLinePOList'][0]['acceptanceNum'] = (
        orders)['acceptanceOrderLinePOList'][0]['deliveryNum']
    record['payStatus'] = orders['payStatus']
    '''
    data['context']['env']['datas']['context'] = record
    response1 = zidonghua.Common.Requests.HttpUtil(
        url = zidonghua.Interface.Order_Accept.url2,
        json = data, cookies = cookies).post()
    print(response1.json())
    data1 = zidonghua.Interface.Order_Accept.data3
    data1['context']['record'][0] = record
    data1['context']['env']['datas'] = record
    response2 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Order_Accept.url2,
        json= data1, cookies=cookies).post()
    return response2.json()
print(order_accept('18178952878','SO20240326000009'))

