import json
import zidonghua.Common.Requests
import zidonghua.Common.Cookies
import zidonghua.Common.Settlement_Order
import zidonghua.Interface.Generate_Payment

def generate_payment(mobile,so_code):  #生成收款单
    cookies = zidonghua.Common.Cookies.get_cookies(mobile)
    salecheck = zidonghua.Common.Settlement_Order.sale_check(so_code)
    sales_check_id = salecheck[0]['id']
    data = zidonghua.Interface.Generate_Payment.data
    data['context']['record'][0]['id'] = sales_check_id
    response1 = zidonghua.Common.Requests.HttpUtil(
        url = zidonghua.Interface.Generate_Payment.url,
        json = zidonghua.Interface.Generate_Payment.data, cookies=cookies).post()
    return response1.json()

if __name__ == '__main__':
    print(generate_payment('admin','SO20240110000004'))
