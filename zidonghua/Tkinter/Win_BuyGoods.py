import requests
import json
import pymysql
import decimal



class Win_User:
    def __init__(self,identify,password):
        self.identify = identify
        self.password =password

    def my_conn(self,sql):
        conn = pymysql.connect(db='trantor_workspace_staging', user='mysql', passwd='77oELIFI67abMArf',
                port=3306,host='172.99.227.53', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        conn.close()
        return cursor.fetchall()

    def cha_info(self):
        cookies = self.get_cookies()
        try:
            response = requests.get(
                url="https://b2b-mall-uat.test.lcscm.cn/api/partner/b2b/current/info", cookies=cookies)
            response.raise_for_status()
            data = response.json()
            purchaserId = data.get('result', {}).get('enterpriseId', {})
            return purchaserId
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")


    def get_cookies(self):
        url = 'https://b2b-mall-uat.test.lcscm.cn/api/user/web/login/identify'
        data = {
            "isApp": False,
            "password": "a1234567",
            "identify": "18178952877"
        }
        data['identify'] = self.identify
        data['password'] = self.password
        response = requests.post(url=url, json=data , headers={'Content-Type': 'application/json'})
        cookies = response.cookies.get_dict()
        return cookies
    def Cha_Project(self):
        url1 = "https://b2b-mall-uat.test.lcscm.cn/api/partner/admin/project/userId"
        params1 = ''
        cookies = self.get_cookies()
        response1 = requests.get(url=url1,params=params1,cookies=cookies)
        result = response1.json()['result']
        projectsname =[]
        for i  in range(len(result)):
            projectsname.append(result[i]['name'])
        return projectsname

    def select_project(self, projectname):
        url1 = "https://b2b-mall-uat.test.lcscm.cn/api/partner/admin/project/userId"
        params1 = {}  # 使用字典而不是空字符串来传递参数
        cookies = self.get_cookies()

        try:
            response1 = requests.get(url=url1, params=params1, cookies=cookies)
            response1.raise_for_status()  # 检查响应状态码，如果不是200则引发HTTPError
            result = response1.json().get('result', [])  # 使用get方法来避免KeyError，并提供一个空列表作为默认值
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None, None  # 或者你可以选择抛出异常

        for item in result:
            if projectname == item.get('name', ''):  # 使用get方法来避免KeyError，并提供一个空字符串作为默认值
                return item.get('id', None), item.get('address', None)  # 同样使用get方法并提供默认值
        return None, None  # 如果没有找到匹配的项目，返回两个None

    def jia_cart(self, itemIds, projectname):
        Ids = itemIds.split(',')
        cookies = self.get_cookies()
        projectId, address = self.select_project(projectname)  # 假设这个方法能返回正确的projectId
        url2 = "https://b2b-mall-uat.test.lcscm.cn/api/design/page/design-data"
        url3 = "https://b2b-mall-uat.test.lcscm.cn/api/trade/cart/add"

        for itemId in Ids:  # 直接迭代Ids中的每个itemId，无需额外的列表推导
            params2 = {
                'release': 1,
                'host': 'b2b-mall-uat.test.lcscm.cn',
                'appType': 'pc',
                'path': f'/items/{itemId}',  # 使用f-string格式化字符串
                'parts': '[{"partKey":"header","scope":"site"},{"partKey":"body"},{"partKey":"footer","scope":"site"}]'
            }
            response2 = requests.get(url=url2, params=params2, cookies=cookies)
            if response2.status_code == 200:  # 检查响应状态码是否为200
                data1 = response2.json()
                item_data = data1.get('serviceData', {}).get('body_6', {}).get('_DATA_', {}).get('result', {}).get(
                    'item', {})
                sku_data = \
                data1.get('serviceData', {}).get('body_6', {}).get('_DATA_', {}).get('result', {}).get('skuList', [{}])[
                    0]

                params3 = {
                    "projectId": projectId,
                    "cartType": "cart_normal",
                    "clientType": "PC",
                    "lines": [
                        {
                            "itemId": item_data.get('id', ''),
                            "price": sku_data.get('price', 0),
                            "quantity": item_data.get('minOrderNumber', 1) * 10,  # 假设最小订单数量存在，并乘以10
                            "shopId": item_data.get('sellerId', ''),
                            "skuId": item_data.get('id', ''),  # 假设skuId与itemId相同
                            "categoryId": item_data.get('categoryId', ''),
                        }
                    ]
                }
                try:
                    response3 = requests.post(url=url3, json=params3, cookies=cookies)  # 注意这里应该使用json参数，而不是params
                    if response3.status_code == 200:  # 检查POST请求是否成功
                        print(f"商品 {itemId} 已成功添加到购物车。")
                    else:
                        print(f"添加商品 {itemId} 到购物车失败，状态码：{response3.status_code}。")
                except requests.exceptions.RequestException as e:
                    print(f"发送POST请求时出错：{e}")
            else:
                print(f"获取商品 {itemId} 详情失败，状态码：{response2.status_code}。")

    def Cha_Cart(self,projectname):
        cookies = self.get_cookies()
        projectId, address = self.select_project(projectname)
        url4 = "https://b2b-mall-uat.test.lcscm.cn/api/trade/cart/query/render"
        params4 = {'cartType': 'cart_normal', 'clientType': 'PC',
                   'divisionIds': '110000,110100,110102', 'projectId': '100022'}
        divisionIds = address['province']['id'] + ',' + address['city']['id'] + ',' + address['region']['id']
        params4['divisionIds'] = divisionIds
        params4['projectId'] = projectId
        response4 = requests.get(url=url4,params=params4, cookies=cookies)
        return response4.json()

    def Cart_Submit(self,projectname):
        cookies = self.get_cookies()
        projectId, address = self.select_project(projectname)
        sql1 = "SELECT id FROM uc_user WHERE mobile = '{}';".format(self.identify)
        sellId = self.my_conn(sql1)[0]['id']
        sql2 = ("select a.cart_line_id,a.category_id,a.quantity,a.item_id,a.sku_id,a.shop_id,"
                "b.extra_json from parana_cart_line a left join parana_item b  on a.item_id =b.id"
                " where a.project_id ='{}' and a.`status` ='NORMAL' "
                "and a.buyer_id='{}'").format(projectId, sellId)
        carts = self.my_conn(sql2)
        url5 = "https://b2b-mall-uat.test.lcscm.cn/api/trade/buy/check-render"
        params5 = {
            "projectId": 100022,
            "orderLineList": [
                {
                    "itemId": 210204601003308,
                    "skuId": 210204601003308,
                    "quantity": 1,
                    "shopId": 132016,
                    "categoryIds": 5147,
                    "cartLineId": 'C1751858721534836736',
                    "categoryId": [4797, 4804, 4839, 4949, 5147]
                }
            ],
            "address": {"address": [{"id": "110000", "name": "北京"}, {"id": "110100", "name": "北京市"},
                                    {"id": "110102", "name": "西城区"}], "city": {"id": "110100", "name": "北京市"},
                        "detail": "社呵呵急急急1",
                        "province": {"id": "110000", "name": "北京"}, "region": {"id": "110102", "name": "西城区"}}
        }
        params5['projectId'] = projectId
        params5['address'] = address
        orderLineList1 = []
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
            response5 = requests.post(url=url5, json=params5, cookies=cookies)
            print(response5.json())
        except Exception as err:
            print("购物车提交订单校验失败" + str(err))
        params6 = {"orderSource": "cart_normal",
                   "cartLineIds": ["C1751858721534836736", "C1751859532339937280"],
                   "divisionIds": "110000,110100,110102",
                   "orderLineList": [{"itemId": "210204601003308", "skuId": "210204601003308",
                                      "quantity": 2, "shopId": "138017", "categoryIds": [4797, 4804, 4839, 4949, 5147],
                                      "cartLineId": "C1751858721534836736", "categoryId": 5147},
                                     {"itemId": "113801700240002", "skuId": "113801700240002", "quantity": 1,
                                      "shopId": "138017",
                                      "categoryIds": [4797, 4805, 4842, 4953, 5155],
                                      "cartLineId": "C1751859532339937280", "categoryId": 5155}], "projectId": 100022,
                   "detailAddress": "社呵呵急急急1",
                   "deviceSource": "PC",
                   "buyConfig": {"lineGrouped": True, "multipleCoupon": True}, "couponParams": [], "benefitParams": []}
        url6 = "https://b2b-mall-uat.test.lcscm.cn/api/trade/buy/render-order"
        params6['cartLineIds'] = []
        params6['divisionIds'] = (address['province']['id']
                                  + ',' + address['city']['id'] + ',' + address['region']['id'])
        params6['projectId'] = projectId
        params6['detailAddress'] = address['detail']
        orderLineList2 = []
        for i in range(len(carts)):
            dict2 = {}
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
            response6 = requests.post(url=url6, json=params6, cookies=cookies)
            return response6.json()
        except Exception as err:
            return ("购物车提交订单失败" + str(err))

    def buyGoods(self,projectname,contractname,paymentType,requireInstall):
        cookies = self.get_cookies()
        purchaserId = self.cha_info()
        result = self.Cart_Submit(projectname)['result']
        projectId, address = self.select_project(projectname)
        for i in range(len(result['salesContract'])):
            if contractname == result['salesContract'][i]['saleName']:
                contractId = result['salesContract'][i]['saleId']
                paymentId = result['salesContract'][i]['contractPaymentItermList'][0]['id']
                paymentRadix = result['salesContract'][i]['contractPaymentItermList'][0]['radix']
        url7 = 'https://b2b-mall-uat.test.lcscm.cn/api/trade/order/web/create'
        params7 = {
            "projectId": 100023,
            "paymentType": "account",
            "isQuickGetOrder": False,
            "orderTitle": "20231213湖北家家有限公司test1采购项目",
            "projectName": "test1采购项目",
            "orderAddress": "北京北京市西城区1111111111111",
            "address": {
                "address": [
                    {
                        "id": "110000",
                        "name": "北京"
                    },
                    {
                        "id": "110100",
                        "name": "北京市"
                    },
                    {
                        "id": "110102",
                        "name": "西城区"
                    }
                ],
                "postcode": None,
                "detail": "1111111111111",
                "region": {
                    "id": "110102",
                    "name": "西城区"
                },
                "province": {
                    "id": "110000",
                    "name": "北京"
                },
                "city": {
                    "id": "110100",
                    "name": "北京市"
                },
                "street": None,
                "community": None
            },
            "orderUserName": "test熊",
            "orderPhone": "18178952878",
            "invoice": {
                "id": None,
                "invoiceType": "ALL_ELE_SPECIAL",
                "titleType": "COMPANY",
                "invoiceCompany": "湖北家家有限公司",
                "invoicePersonal": None,
                "title": "湖北家家有限公司",
                "taxpayerCode": "914200001776058818",
                "uscc": "914200001776058818",
                "invoiceBank": "中国邮政深圳分行龙华支行",
                "invoiceAccount": "622878272262673834223",
                "recipientName": "李四测试",
                "recipientPhone": "18178952878",
                "recipientAddress": "123@136.com",
                "invoiceRemark": "444444444444444444444444444444444444444444444444444",
                "invoiceAddress": "深圳宝安区宝安大道108号哈哈锁厂",
                "invoiceMobile": "18178952878",
                "needInvoice": True,
                "isRequired": True
            },
            "projectContactName": "test熊",
            "projectContactPhone": "18178952878",
            "salesContractId": 124057,
            "orderContactId": 132016,
            "orderList": [
                {
                    "supplierId": 138017,
                    "installation": False,
                    "contactName": None,
                    "contactId": None,
                    "contactPhone": None,
                    "paymentId": 178016,
                    "paymentRadix": 100,
                    "buyerNote": None,
                    "itemTotalAmount": 59.66,
                    "deliveryTotalAmount": 0,
                    "installTotalAmount": 0,
                    "totalAmount": 5966,
                    "totalAmountprice": 59.66,
                    "totalAmountPriceExclusive": 7.76,
                    "orderLineList": [
                        {
                            "itemId": 210204601003306,
                            "skuId": 210204601003306,
                            "skuCode": "210204601003306",
                            "minOrderNum": 1,
                            "bundleId": None,
                            "quantity": 1,
                            "campaignId": None,
                            "campaignName": None,
                            "campaignSubType": None,
                            "preSellMethod": None,
                            "campaignSubId": None,
                            "shopCampaignId": None,
                            "shopPiscesBenefitId": None,
                            "platformCampaignId": None,
                            "platformPiscesBenefitId": None,
                            "extraParam": None,
                            "promotionTag": None,
                            "shopId": 138017,
                            "lineId": "210204601003306",
                            "categoryId": 5147,
                            "skuName": "立邦 广角镜",
                            "attrs": None,
                            "mainImage": "http://lcscm-trantor.oss-cn-shenzhen.aliyuncs.com/images/manage/2046/46a23c6a-07bf-45fc-8d23-078dab8a0855/06a02908-5065-4369-b2e0-58325b5ff515.png",
                            "outerSkuCode": None,
                            "status": 1,
                            "salePrice": 59.66,
                            "itemCode": "210204601003306",
                            "contractId": 158001,
                            "shopName": "深圳哈哈有限公司",
                            "installFee": None,
                            "deliveryFee": None,
                            "categoryIds": [
                                4797,
                                4804,
                                4839,
                                4949,
                                5147
                            ],
                            "brandId": 50001,
                            "brandName": "立邦",
                            "specification": "立邦地坪漆材料 ：ZF-F951-防静电的环保地坪漆",
                            "deliveryFeeTempId": None,
                            "installFeeTempId": None,
                            "name": "立邦 广角镜",
                            "lowPrice": None,
                            "highPrice": None,
                            "isOnShelf": True,
                            "unitWeight": None,
                            "unit": "个",
                            "taxRate": "13",
                            "itemMarkupRate": None,
                            "otherAttributes": [],
                            "preferSalePrice": 5966,
                            "bizCode": "normal_1",
                            "bomId": None,
                            "priceRanges": [
                                {
                                    "id": None,
                                    "__trantorExtendFields": {},
                                    "createdAt": None,
                                    "updatedAt": None,
                                    "isDeleted": None,
                                    "createdBy": None,
                                    "updatedBy": None,
                                    "subsidyPrice": 117.5,
                                    "itemMarkupRate": "1.1663",
                                    "minOrderNum": 10,
                                    "useStatus": True,
                                    "priceDesc": None,
                                    "_fields": {}
                                }
                            ],
                            "colorNumberShow": "0",
                            "colorNum": "",
                            "defaultRadix": 100,
                            "purDiscountRate": 1,
                            "saleRadix": None,
                            "taxPriceMoney": 59.66,
                            "taxPrice": 59.66,
                            "priceExclusive": 0,
                            "totalPrice": 59.66,
                            "totalPriceExclusive": 7.76,
                            "attribute": [],
                            "subtotal": 5966
                        }
                    ],
                    "orderContactId": 132016,
                    "brandOwnerId": 138017,
                    "orderAttachment": {
                        "files": []
                    }
                }
            ]
        }
        params7['projectId'] = result['projectId']
        params7['paymentType'] = paymentType  # account 账期支付 ,offline 线下转账，online 线上支付
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
        params7['salesContractId'] = contractId
        params7['orderList'] = []
        for i in range(len(result['orderList'])):
            url9 = "https://b2b-mall-uat.test.lcscm.cn/api/item/get-payment-list-new"
            params9 = {"contractId": 124054, "requireInstall": True, "categoryIds": [4797, 4805, 4842, 4953, 5156]}
            params9['categoryIds'] = (result['orderList'][i]['activityOrderList'][0]['orderLineGroups']
            [0]['orderLineList'][0]['categoryIds'])
            params9['contractId'] = contractId
            params9['requireInstall'] = True
            try:
                response9 = requests.post(
                    url=url9, json=params9, cookies=cookies)
            except Exception as err:
                print("获取付款条件错误" + str(err))
            if response9.json()['result'][0]['id'] is not None:
                print("付款条件id为："+ str(response9.json()['result'][0]['id']))
            else:
                print('没有付款条件')

        for i in range(len(result['orderList'])):
            url10 = "https://b2b-mall-uat.test.lcscm.cn/api/item/payment/shop-price"
            params10 = {"contractId": 124054, "provinceId": "110000", "cityId": "110100",
                        "orderList": [{"id": 113801700241001, "quality": 10}], "mdEnterpriseId": 138013,
                        "saleRadix": 100, "requireInstall": False}
            params10['categoryIds'] = (result['orderList'][i]['activityOrderList'][0]
            ['orderLineGroups'][0]['orderLineList'][0]['categoryIds'])
            params10['contractId'] = contractId
            params10['provinceId'] = address['province']['id']
            params10['cityId'] =address['city']['id']
            params10['requireInstall'] = True
            params10['mdEnterpriseId'] =  purchaserId
            orderList1 = result['orderList'][i]['activityOrderList'][0]['orderLineGroups'][0]['orderLineList']
            orderlinelist =[]
            for j in range(len(orderList1)):
                dict2 ={}
                dict2['id'] = orderList1[j]['itemId']
                dict2['quality'] = int(orderList1[j]['quantity'])
                orderlinelist.append(dict2)
            params10['orderList'] = orderlinelist
            response10 = requests.post(
                    url=url10, json=params10, cookies=cookies)
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
            dict1['paymentId'] = paymentId
            dict1['paymentRadix'] = paymentRadix
            dict1['installation'] = requireInstall
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
        response7 = requests.post(
                    url=url7, json=params7, cookies=cookies)
        print(response7.json())
        return response7.json()
        try:
            orderCodes = response7.json()['result']['orderCodes']
            if params7['paymentType'] =='offline':
                url11 = "https://b2b-mall-uat.test.lcscm.cn/api/trade/order/web/create-pay-order"
                params11 = {"orderCodes": ["SO20240115000011"], "projectId": 100023}
                params11['orderCodes'] = orderCodes
                params11['projectId'] = projectId
                response11 = requests.post(
                    url= url11,json=params11, cookies=cookies)
            print(response11.json())
        except Exception as e:
            print(e)




if __name__ == '__main__':
    user =Win_User('18178952878','a1234567')
    # print(user.select_project('test1采购项目'))
    # user.jia_cart('210204601003304,210204601003306','深圳市#家家20240109#1111#')
    # print(json.dumps(user.Cart_Submit('深圳市#家家20240109#1111#')['result'],ensure_ascii=False))
    # print(user.cha_info())
    # print(user.buyGoods('test1采购项目','合作意向签约','account',True))
