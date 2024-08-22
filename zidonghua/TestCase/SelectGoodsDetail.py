import zidonghua.Common.Requests
import zidonghua.Interface.Select_Goods_Detail
import zidonghua.Common.Cookies

def select_goods_detail(mobile,iterm_id):
    cookies = zidonghua.Common.Cookies.get_cookies(mobile)
    zidonghua.Interface.Select_Goods_Detail.data['queryValues']['id']['value'] = iterm_id
    response = zidonghua.Common.Requests.HttpUtil(
        url= zidonghua.Interface.Select_Goods_Detail.url,
        json=zidonghua.Interface.Select_Goods_Detail.data,cookies=cookies).post()
    return response.json()

# print(select_goods_detail('admin','113801700281007'))