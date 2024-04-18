import zidonghua.Common.Requests
import zidonghua.Interface.Install_Accept
import zidonghua.Common.Cookies
import zidonghua.Common.Select_Order

def InstallAccept(mobile,so_code):
    cookies = zidonghua.Common.Cookies.get_cookies(mobile)
    so_delivery_order, po_delivery_order = (
        zidonghua.Common.Select_Order.order(so_code).parana_delivery_order())
    zidonghua.Interface.Install_Accept.data1['queryValues']['id']['value'] = so_delivery_order[0]['id']
    response = zidonghua.Common.Requests.HttpUtil(
        url = zidonghua.Interface.Install_Accept.url1,
        json = zidonghua.Interface.Install_Accept.data1, cookies=cookies).post()
    orders = response.json()['res']['data']
    data = zidonghua.Interface.Install_Accept.data2['context']
    data['env']['deliveryOrderId'] = orders['deliveryOrder']['id']
    data['record'][0]['isInstall'] = orders['isInstall']
    data['record'][0]['deliveryOrder'] = orders['deliveryOrder']
    data['record'][0]['parentAcceptanceOrderCode'] = orders['parentAcceptanceOrderCode']
    data['record'][0]['deliveryCode'] = orders['deliveryCode']
    data['record'][0]['order'] = orders['order']
    data['record'][0]['getGoodsOrder'] = orders['getGoodsOrder']
    data['record'][0]['sender'] = orders['sender']
    data['record'][0]['contactMobile'] = orders['contactMobile']
    data['record'][0]['deliveryDate'] = orders['deliveryDate']
    data['record'][0]['arrivalDate'] = orders['arrivalDate']
    data['record'][0]['acceptanceDate'] = orders['acceptanceDate']
    data['record'][0]['lingchaoContact'] = orders['lingchaoContact']
    data['record'][0]['acceptanceOrderLinePOList'] = orders['acceptanceOrderLinePOList']
    data['record'][0]['acceptanceOrderLinePOList'] = orders['lingchaoMobile']
    response1 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Install_Accept.url2,
        json=zidonghua.Interface.Install_Accept.data2, cookies=cookies).post()
    print(response1.json())
    data11 = zidonghua.Interface.Install_Accept.data3
    data11['context']['record'][0] = orders
    data11['context']['env']['datas'] = orders
    response2 = zidonghua.Common.Requests.HttpUtil(
        url = zidonghua.Interface.Install_Accept.url2,
        json = zidonghua.Interface.Install_Accept.data3, cookies=cookies).post()
    return response2.json()

print(InstallAccept('18178952878','SO20240110000003'))
