import zidonghua.Common.Requests
import zidonghua.Interface.Order_Goods
import zidonghua.Common.Cookies
import zidonghua.Common.Select_Order

def order_goods(mobile,so_code):   # 采购商订货
    cookies = zidonghua.Common.Cookies.get_cookies(mobile)
    so_id = zidonghua.Common.Select_Order.order(so_code).so_id
    zidonghua.Interface.Order_Goods.data1['queryValues']['id']['value'] = so_id
    response = zidonghua.Common.Requests.HttpUtil(
        url= zidonghua.Interface.Order_Goods.url1,
        json=zidonghua.Interface.Order_Goods.data1,cookies=cookies).post()
    orders = response.json()
    zidonghua.Interface.Order_Goods.data2['context']['record'][0]['orderCode'] = so_code
    zidonghua.Interface.Order_Goods.data2['context']['record'][0]['order'] = (
        orders)['res']['data']['order']
    zidonghua.Interface.Order_Goods.data2['context']['record'][0]['getGoodsOrderLinePOList'] =(
        orders)['res']['data']['getGoodsOrderLinePOList']
    response1 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Order_Goods.url2,
        json=zidonghua.Interface.Order_Goods.data2, cookies=cookies).post()
    return response1.json()

if __name__ == '__main__':
    print(order_goods('18178952878','SO20240428000007'))

