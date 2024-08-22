import json
import zidonghua.Common.Requests
import zidonghua.Interface.Settlement_Confirmation
import zidonghua.Common.Cookies
import zidonghua.Common.Settlement_Order

def settlement_confirmation(mobile,so_code):  #采购商对账单确认
    cookies = zidonghua.Common.Cookies.get_cookies(mobile)
    so_settlement, po_settlement = zidonghua.Common.Settlement_Order.order_settlement(so_code)
    zidonghua.Interface.Settlement_Confirmation.data1['queryValues']['id']['value'] =\
        so_settlement[0]['id']
    response1 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Settlement_Confirmation.url1,
        json = zidonghua.Interface.Settlement_Confirmation.data1, cookies = cookies).post()
    result =response1.json()['res']['data']
    zidonghua.Interface.Settlement_Confirmation.data2['context']['record'][0]['id'] = (
        so_settlement)[0]['id']
    response2 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Settlement_Confirmation.url2,
        json=zidonghua.Interface.Settlement_Confirmation.data2, cookies=cookies).post()
    return response2.json()



if __name__ == '__main__':
    print(settlement_confirmation('18178952878','SO20240112000008'))








