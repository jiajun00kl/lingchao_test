import zidonghua.Common.Requests
import zidonghua.Interface.Select_Goods
import zidonghua.Common.Cookies

def select_goods(mobile,goods_name):
    cookies = zidonghua.Common.Cookies.get_cookies(mobile)
    zidonghua.Interface.Select_Goods.data['searchValues']['name']['value'] = goods_name
    response = zidonghua.Common.Requests.HttpUtil(
        url= zidonghua.Interface.Select_Goods.url,
        json=zidonghua.Interface.Select_Goods.data,cookies=cookies).post()
    return response.json()

# print(select_goods('admin','305不锈钢水箱 方形组合式耐高温防锈材质规格 定制加工'))
