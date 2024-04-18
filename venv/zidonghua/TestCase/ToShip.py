import json

import zidonghua.Common.Requests
import zidonghua.Interface.To_Ship
import zidonghua.Common.Cookies
import zidonghua.Common.Select_Order

def to_ship(mobile,so_code): # 去审核发货
    cookies = zidonghua.Common.Cookies.get_cookies(mobile)
    so_delivery_order, po_delivery_order = (
        zidonghua.Common.Select_Order.order(so_code).parana_delivery_order())
    zidonghua.Interface.To_Ship.data1['context']['env']['id'] = po_delivery_order[0]['id']
    response = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.To_Ship.url,
        json=zidonghua.Interface.To_Ship.data1, cookies=cookies).post()
    orders = response.json()['res']['data']
    data = zidonghua.Interface.To_Ship.data2['context']['env']
    data['id'] = orders['id']
    data['purchaserName'] = orders['purchaserName']
    data['corporateCompanyName'] = orders['corporateCompanyName']
    data['oaContent'] = orders['oaContent']
    data['deliveryAmount'] = orders['deliveryAmount']
    data['advanceAmount'] = orders['advanceAmount']
    data['advanceInfoList'] = orders['advanceInfoList']
    data['restAmount'] = orders['restAmount']
    data['riskLevel'] = orders['riskLevel']
    data['receiveInfo'] = orders['receiveInfo']
    data['guarantee'] = orders['guarantee']
    data['accountPeriod'] = orders['accountPeriod']
    response = zidonghua.Common.Requests.HttpUtil(
        url = zidonghua.Interface.To_Ship.url,
        json = zidonghua.Interface.To_Ship.data2 , cookies = cookies).post()
    return response.json()

print(to_ship('18520611771','SO20240110000004'))
