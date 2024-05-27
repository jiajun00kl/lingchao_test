import zidonghua.Common.Requests
import zidonghua.Interface.Confirm_Order
import zidonghua.Common.Cookies
import zidonghua.Common.Select_Order

def confirm_orders(mobile,so_code):  #供应商确认订单
    cookies = zidonghua.Common.Cookies.get_cookies(mobile)
    so_goods_order,po_goods_order = (
        zidonghua.Common.Select_Order.order(so_code).parana_get_goods_order())
    zidonghua.Interface.Confirm_Order.data1['searchValues']['code']['value'] = po_goods_order[0]['code']
    response = zidonghua.Common.Requests.HttpUtil(
        url = zidonghua.Interface.Confirm_Order.url1,
        json = zidonghua.Interface.Confirm_Order.data1, cookies = cookies).post()
    orders = response.json()
    zidonghua.Interface.Confirm_Order.data2['context']['record'] = orders['res']['data']
    response1 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Confirm_Order.url2,
        json=zidonghua.Interface.Confirm_Order.data2, cookies=cookies).post()
    return response1.json()

if __name__ == '__main__':
 print(confirm_orders('18178952877','SO20240525000003'))
    
    
    