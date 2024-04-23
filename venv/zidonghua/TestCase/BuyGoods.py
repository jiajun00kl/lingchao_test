import json
import zidonghua.Common.Mysql_Con
import zidonghua.Common.Requests
import zidonghua.Interface.Buy_Goods
import zidonghua.Common.Cookies
import decimal
import zidonghua.Conf.Settings
from urllib.parse import urlparse   # 使用urllib.parse库中的urlparse函数来解析URL

# zidonghua.Conf.Settings.url =zidonghua.Conf.Settings.dev_url  # 环境切换

class BuyGoods:
    def __init__(self,mobile,password):
        self.mobile = mobile
        self.password = password

    def cha_info(self):
        cookies = zidonghua.Common.Cookies.get_cookies(self.mobile)
        response = zidonghua.Common.Requests.HttpUtil(
            url=zidonghua.Conf.Settings.url+ "/api/partner/b2b/current/info",
            cookies=cookies).get()
        purchaserId = response['result']['enterpriseId']
        return purchaserId


    def Cha_Project(self):
        cookies = zidonghua.Common.Cookies.get_cookies(self.mobile)
        try:
            response1 = zidonghua.Common.Requests.HttpUtil(
                url=zidonghua.Conf.Settings.url+zidonghua.Interface.Buy_Goods.api1 ,
                        params=zidonghua.Interface.Buy_Goods.params1,cookies=cookies).get()
            projectId = response1['result'][3]['id']
            address = response1['result'][3]['address']
            return projectId, address
        except Exception as err:
            return (f"获取项目失败")

    def Add_Goods(self,itermId):
        cookies = zidonghua.Common.Cookies.get_cookies(self.mobile)
        projectId, address = self.Cha_Project()
        zidonghua.Interface.Buy_Goods.params2['path'] = '/items/'+ str(itermId)
        parsed_url = urlparse(zidonghua.Conf.Settings.url)
        zidonghua.Interface.Buy_Goods.params2['host'] = parsed_url.netloc # 获取主机名
        try:
            response2 = zidonghua.Common.Requests.HttpUtil(
            url= zidonghua.Conf.Settings.url+zidonghua.Interface.Buy_Goods.api2,
            params = zidonghua.Interface.Buy_Goods.params2,
                cookies=cookies).get()
            print(response2)
        except Exception as err:
            print("查询商品信息失败"+ err)
        zidonghua.Interface.Buy_Goods.params3['projectId'] = projectId
        zidonghua.Interface.Buy_Goods.params3['lines'][0]['itemId'] = (
            response2)['serviceData']['body_6']['_DATA_']['result']['item']['id']
        zidonghua.Interface.Buy_Goods.params3['lines'][0]['price'] = (
            response2)['serviceData']['body_6']['_DATA_']['result']['skuList'][0]['price']
        zidonghua.Interface.Buy_Goods.params3['lines'][0]['shopId'] = (
            response2)['serviceData']['body_6']['_DATA_']['result']['item']['sellerId']
        zidonghua.Interface.Buy_Goods.params3['lines'][0]['skuId'] = (
            response2)['serviceData']['body_6']['_DATA_']['result']['item']['id']
        zidonghua.Interface.Buy_Goods.params3['lines'][0]['categoryId']= (
            response2)['serviceData']['body_6']['_DATA_']['result']['item']['categoryId']
        try:
            response3 = zidonghua.Common.Requests.HttpUtil(
                url= zidonghua.Conf.Settings.url+zidonghua.Interface.Buy_Goods.api3,
                         json=zidonghua.Interface.Buy_Goods.params3, cookies=cookies).post()
            return response3.json()
        except Exception as err:
            return ("商品加入购物车失败")

    def Cha_Cart(self):
        cookies = zidonghua.Common.Cookies.get_cookies(self.mobile)
        projectId, address = self.Cha_Project()
        divisionIds = address['province']['id'] +','+address['city']['id'] +','+address['region']['id']
        zidonghua.Interface.Buy_Goods.params4['divisionIds'] = divisionIds
        zidonghua.Interface.Buy_Goods.params4['projectId'] = projectId
        try:
            response4 = zidonghua.Common.Requests.HttpUtil(
                url=zidonghua.Conf.Settings.url+zidonghua.Interface.Buy_Goods.api4,
                        params=zidonghua.Interface.Buy_Goods.params4, cookies=cookies).get()
            return response4
        except Exception as err:
            return ("进入购物车失败"+str(err))

    def Cart_Submit(self):
        cookies = zidonghua.Common.Cookies.get_cookies(self.mobile)
        projectId, address = self.Cha_Project()
        sql1 ="SELECT id FROM uc_user WHERE mobile = '{}';".format(self.mobile)
        sellId = zidonghua.Common.Mysql_Con.sql_select(sql1)[0]['id']
        sql2 = ("select a.cart_line_id,a.category_id,a.quantity,a.item_id,a.sku_id,a.shop_id,"
               "b.extra_json from parana_cart_line a left join parana_item b  on a.item_id =b.id"
               " where a.project_id ='{}' and a.`status` ='NORMAL' "
               "and a.buyer_id='{}'").format(projectId, sellId)
        carts = zidonghua.Common.Mysql_Con.sql_select(sql2)
        params5 = zidonghua.Interface.Buy_Goods.params5
        params5['projectId'] = projectId
        params5['address'] = address
        orderLineList1 =[]
        for i in range(len(carts)):
            dict1 = {}
            dict1['itemId'] = carts[i]['item_id']
            dict1['skuId'] = carts[i]['sku_id']
            dict1['quantity'] = int(
                carts[i]['quantity'].quantize(decimal.Decimal('0.00')))
            dict1['skuId'] = carts[i]['sku_id']
            dict1['shopId'] = carts[i]['shop_id']
            dict1['cartLineId'] = carts[i]['cart_line_id']
            dict1['categoryId'] = carts[i]['category_id']
            dict1['categoryIds'] = (
                json.loads((json.loads(carts[i]['extra_json']))['categoryList']))
            orderLineList1.append(dict1)
        params5['orderLineList'] = orderLineList1
        try:
            response5 = zidonghua.Common.Requests.HttpUtil(
                url=zidonghua.Conf.Settings.url+zidonghua.Interface.Buy_Goods.api5,
                json=params5, cookies=cookies).post()
            print(response5.json())
        except Exception as err:
            print("购物车提交订单校验失败" + str(err))
        params6 = zidonghua.Interface.Buy_Goods.params6
        params6['cartLineIds'] = []
        params6['divisionIds'] = (address['province']['id']
                                  + ',' + address['city']['id'] + ',' + address['region']['id'])
        params6['projectId'] = projectId
        params6['detailAddress'] = address['detail']
        orderLineList2 =[]
        for i in range(len(carts)):
            dict2 ={}
            dict2['itemId'] = carts[i]['item_id']
            dict2['skuId'] = carts[i]['sku_id']
            dict2['quantity'] = int(
                carts[i]['quantity'].quantize(decimal.Decimal('0.00')))
            dict2['skuId'] = carts[i]['sku_id']
            dict2['shopId'] = carts[i]['shop_id']
            dict2['cartLineId'] = carts[i]['cart_line_id']
            dict2['categoryId'] = carts[i]['category_id']
            dict2['categoryIds'] = (
                json.loads((json.loads(carts[i]['extra_json']))['categoryList']))
            orderLineList2.append(dict2)
            params6['cartLineIds'].append(carts[i]['cart_line_id'])
        params6['orderLineList'] = orderLineList2
        try:
            response6 = zidonghua.Common.Requests.HttpUtil(
                url=zidonghua.Conf.Settings.url+zidonghua.Interface.Buy_Goods.api6,
                json=params6, cookies=cookies).post()
            return response6.json()
        except Exception as err:
            return ("购物车提交订单失败" + str(err))


    def Submit_Order(self):
        cookies = zidonghua.Common.Cookies.get_cookies(self.mobile)
        purchaserId = self.cha_info()
        result = self.Cart_Submit()['result']
        projectId, address = self.Cha_Project()
        params7 = zidonghua.Interface.Buy_Goods.params7
        params7['projectId'] = result['projectId']
        params7['paymentType'] = 'account'  # account 账期支付 ,offline 线下转账，online 线上支付
        params7['orderTitle'] = result['orderTitle']
        params7['projectName'] = result['projectName']
        params7['orderAddress'] = result['orderAddress']
        params7['address'] = result['address']
        params7['orderUserName'] = result['orderUserName']
        params7['orderPhone'] = result['orderPhone']
        params7['invoice'] = result['invoice']
        params7['projectContactName'] = result['projectContact'][0]['contactName']
        params7['projectContactPhone'] = result['projectContact'][0]['contactPhone']
        params7['orderContactId'] = result['orderUserId']
        params7['salesContractId'] = result['salesContract'][0]['saleId']
        params7['orderList'] = []
        for i in range(len(result['orderList'])):
            params9 = zidonghua.Interface.Buy_Goods.params9
            params9['categoryIds'] = (result['orderList'][i]['activityOrderList'][0]['orderLineGroups']
            [0]['orderLineList'][0]['categoryIds'])
            params9['contractId'] = result['orderList'][i]['salesContract'][0]['saleId']
            params9['requireInstall'] = True
            try:
                response9 = zidonghua.Common.Requests.HttpUtil(
                    url=zidonghua.Conf.Settings.url+zidonghua.Interface.Buy_Goods.api9,
                    json=params9, cookies=cookies).post()
            except Exception as err:
                print("获取付款条件错误" + str(err))
            if response9.json()['result'][0]['id'] is not None:
                print("付款条件id为："+ str(response9.json()['result'][0]['id']))
            else:
                print('没有付款条件')


        for i in range(len(result['orderList'])):
            params10 = zidonghua.Interface.Buy_Goods.params10
            params10['categoryIds'] = (result['orderList'][i]['activityOrderList'][0]
            ['orderLineGroups'][0]['orderLineList'][0]['categoryIds'])
            params10['contractId'] = result['orderList'][i]['salesContract'][0]['saleId']
            params10['provinceId'] = address['province']['id']
            params10['cityId'] =address['city']['id']
            params10['requireInstall'] = False
            params10['mdEnterpriseId'] =  purchaserId
            orderList1 = result['orderList'][i]['activityOrderList'][0]['orderLineGroups'][0]['orderLineList']
            orderlinelist =[]
            for j in range(len(orderList1)):
                dict2 ={}
                dict2['id'] = orderList1[j]['itemId']
                dict2['quality'] = int(orderList1[j]['quantity'])
                orderlinelist.append(dict2)
            params10['orderList'] = orderlinelist
            response10 = zidonghua.Common.Requests.HttpUtil(
                    url=zidonghua.Conf.Settings.url+zidonghua.Interface.Buy_Goods.api10,
                json=params10, cookies=cookies).post()
            result10 =response10.json()
            for a in range(len(orderList1)):
                for k in range(len(result10['result'])):
                    if orderList1[a]['itemId'] == result10['result'][k]['id']:
                        orderList1[a]['colorNumberShow'] = 0
                        orderList1[a]['colorNum'] =''
                        orderList1[a]['defaultRadix'] = result10['result'][k]['defaultRadix']
                        orderList1[a]['purDiscountRate'] = result10['result'][k]['purDiscountRate']
                        orderList1[a]['saleRadix'] = result10['result'][k]['saleRadix']
                        orderList1[a]['taxPriceMoney'] = result10['result'][k]['taxPriceMoney']
                        orderList1[a]['taxPrice'] = result10['result'][k]['taxPrice']
                        orderList1[a]['priceExclusive'] = result10['result'][k]['priceExclusive']
                        orderList1[a]['totalPrice'] = result10['result'][k]['totalPrice']
                        orderList1[a]['totalPriceExclusive'] = result10['result'][k]['totalPriceExclusive']
                        orderList1[a]['subtotal'] = result10['result'][k]['totalPrice']*100
                        orderList1[a]['attribute'] = []
                        del orderList1[a]['extra']
                        del orderList1[a]['summary']
            # print(orderList1)
            dict1 = {}
            dict1['supplierId'] = result['orderList'][i]['supplier'][0]['supplierId']
            dict1['contactName'] = result['orderList'][i]['contactName']
            dict1['contactId'] = result['orderList'][i]['contactId']
            dict1['contactPhone'] = result['orderList'][i]['contactPhone']
            dict1['buyerNote'] = result['orderList'][i]['buyerNote']
            dict1['paymentId'] = (
                result)['orderList'][i]['salesContract'][0]['contractPaymentItermList'][0]['id']
            dict1['paymentRadix'] = (
                result)['orderList'][i]['salesContract'][0]['contractPaymentItermList'][0]['radix']
            if result['orderList'][i]['salesContract'][0]['contractPaymentItermList'][0]['installOption'] == (
                    'SUPPLY_INSTALL'):
                dict1['installation'] = True
            else:
                dict1['installation'] = False
            dict1['orderLineList'] = orderList1
            dict1['orderContactId'] = result['orderUserId']
            dict1['brandOwnerId'] = result['orderList'][i]['supplier'][0]['supplierId']
            dict1['orderAttachment'] = {"files": [] }
            dict1['itemTotalAmount'] =0
            dict1['deliveryTotalAmount'] =0
            dict1['installTotalAmount']=0
            dict1['totalAmount'] =0
            dict1['totalAmountprice'] =0
            dict1['totalAmountPriceExclusive'] =0
            for i in range(len(orderList1)):
                dict1['itemTotalAmount'] += float(orderList1[i]['taxPrice'])*float(orderList1[i]['quantity'])
                if orderList1[i]['deliveryFee'] is not None:
                    dict1['deliveryTotalAmount'] += (
                        float(orderList1[i]['deliveryFee'])*float(orderList1[i]['quantity']))
                if orderList1[i]['installFee'] is not None:
                    dict1['installTotalAmount'] += (
                        float(orderList1[i]['installFee']) * float(orderList1[i]['quantity']))
                dict1['totalAmount'] += orderList1[i]['subtotal']
                dict1['totalAmountprice'] += orderList1[i]['totalPrice']
                dict1['totalAmountPriceExclusive'] += orderList1[i]['totalPriceExclusive']
            params7['orderList'].append(dict1)
        # print(json.dumps(params7,ensure_ascii=False))
        response7 = zidonghua.Common.Requests.HttpUtil(
                    url=zidonghua.Conf.Settings.url+zidonghua.Interface.Buy_Goods.api7,
            json=params7, cookies=cookies).post()
        return response7.json()
        try:
            orderCodes = response7.json()['result']['orderCodes']
            if params7['paymentType'] != 'account':
                zidonghua.Interface.Buy_Goods.params11['orderCodes'] = orderCodes
                zidonghua.Interface.Buy_Goods.params11['projectId'] = projectId
                cookies = zidonghua.Common.Cookies.get_cookies(mobile)
                response11 = zidonghua.Common.Requests.HttpUtil(
                    url= zidonghua.Conf.Settings.url+zidonghua.Interface.Buy_Goods.api11,
                    json=zidonghua.Interface.Buy_Goods.params11, cookies=cookies).post()
            print(response11.json())
        except Exception as e:
            print(e)

if __name__ == '__main__':
    account = BuyGoods('18178952878','a1234567')
    account.Add_Goods('210204601003309')
    account.Add_Goods('110800300376001')
    # print(account.Submit_Order())

