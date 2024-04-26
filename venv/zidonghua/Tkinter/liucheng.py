import requests
import pymysql
from pymysql import MySQLError
import datetime
import time,json

def my_conn(sql, params=None):
    try:
        # 使用连接池（需要预先配置）
        conn = pymysql.connect(db='trantor_workspace_staging', user='mysql',
                passwd='77oELIFI67abMArf', port=3306,host='172.99.227.53',
                               charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        # 或者使用ORM框架如SQLAlchemy，它内置了连接池

        # 假设我们有一个连接池对象 pool
        # conn = pool.get_connection()
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            # 使用参数化查询
            cursor.execute(sql, params)
            result = cursor.fetchall()
        return result
    except pymysql.MySQLError as e:
        # 处理数据库异常
        print(f"Database error: {e}")
        return None
    finally:
        # 确保连接被正确关闭（如果使用连接池，这一步通常由连接池管理）
        # conn.close()
        pass


class order():
    def __init__(self,so_code):
        self.so_code = so_code
        self.so_id = None
        self.po_id = None

    @property
    def po_id(self):
        return self._po_id
    @po_id.setter
    def po_id(self,poId):
        sql= "SELECT *  FROM parana_order WHERE parent_order_code ='{}'; ".format(self.so_code)
        po_order = my_conn(sql)
        self._po_id = po_order[0]['id']

    @property
    def so_id(self):
        return self._so_id
    @so_id.setter
    def so_id(self,soId):
        sql = "SELECT *  FROM parana_order WHERE code ='{}'; ".format(self.so_code)
        so_order = my_conn(sql)
        self._so_id = so_order[0]['id']

    def parana_order(self):  # 需求单
        sql = "SELECT *  FROM parana_order WHERE id= '{}';".format(self.so_id)
        so_order = my_conn(sql)[0]

        sql1 = "SELECT *  FROM parana_order WHERE id ='{}'; ".format(self.po_id)
        po_order = my_conn(sql1)[0]
        return so_order,po_order

    def sup_mobile(self):
        sql = "SELECT *  FROM parana_order WHERE id= '{}';".format(self.so_id)
        enterpriseId = my_conn(sql)[0]['supplier']
        sql2 ="SELECT * FROM md_enterprise WHERE  id= '{}';".format(enterpriseId)
        enterprise = my_conn(sql2)
        return enterprise
    def pur_mobile(self):
        so_order,po_order = self.parana_order()
        buyer =so_order['buyer']
        sql ="SELECT *  FROM uc_user WHERE id= '{}';".format(buyer)
        pur_user = my_conn(sql)[0]
        return pur_user

    def parana_get_goods_order(self):  # 订单
        sql = ("SELECT * FROM parana_get_goods_order "
               "WHERE `order`='{}' ORDER BY `code` DESC;").format(self.so_id)
        so_goods_order = my_conn(sql)

        sql1=("SELECT * FROM parana_get_goods_order "
              "WHERE `order`='{}' ORDER BY `code` DESC;").format(self.po_id)
        po_goods_order = my_conn(sql1)
        return so_goods_order,po_goods_order

    def parana_delivery_order(self): # 发货
        sql = ("SELECT * FROM parana_delivery_order "
               "WHERE `order` ='{}' ORDER BY `code` DESC;").format(self.so_id)
        so_delivery_order = my_conn(sql)

        sql1 = ("SELECT * FROM parana_delivery_order "
                "WHERE `order` ='{}' ORDER BY `code` DESC;").format(self.po_id)
        po_delivery_order = my_conn(sql1)
        return so_delivery_order,po_delivery_order
    def parana_acceptance_order(self):  # 到货安装
        sql = ("SELECT * FROM parana_acceptance_order  "
               "WHERE  `order` ='{}' ORDER BY `code` DESC ;").format(self.so_id)
        so_acceptance_order = my_conn(sql)

        sql1 = ("SELECT * FROM parana_acceptance_order  "
                "WHERE  `order` ='{}' ORDER BY `code` DESC ;").format(self.so_id)
        po_acceptance_order = my_conn(sql1)
        return so_acceptance_order,po_acceptance_order

    def order_settlement(self):
        sql1 = "select * from  order_settlement where `order` ='{}' ;".format(self.so_id)
        so_settlement = my_conn(sql1)
        sql2 = "select * from  order_settlement where `order` ='{}' ;".format(self.po_id)
        po_settlement = my_conn(sql2)
        return so_settlement, po_settlement

    def settlement_receivable(self):
        sql = "select * from  settlement_center__receivable where order_id ='{}' ;".format(self.so_id)
        receivable = my_conn(sql)
        return receivable

    def settlement_payable(self):
        sql1 = ("select payable_source_code,payable_source_type from  settlement_center__payable "
                "where order_id ='{}'GROUP BY payable_source_code,payable_source_type ;").format(self.po_id)
        payable1 = my_conn(sql1)
        sql = ("select * from  settlement_center__payable "
               "where order_id ='{}' ;").format(self.po_id)
        payable = my_conn(sql)
        return payable, payable1

    def SaleCheck(self):
        sql = ("select * from sales_check where id in("
               "SELECT sales_check_id FROM  sales_check_line WHERE `order` ='{}');").format(self.so_id)
        salecheck = my_conn(sql)
        return salecheck

    def sup_login(self,mobile):
        url = "https://b2b-mall-uat.test.lcscm.cn/api/user/web/login/login-by-sms-code"
        data = {"mobile":mobile , "smsCode": "111111", "isApp": False, "prefix": "86"}
        response = requests.post(url=url, json=data, headers={'Content-Type': 'application/json'})
        cookies = response.cookies.get_dict()
        return cookies

    def SupplierAcceptanceOrder(self):   # 供应商接单
        enterprise = self.sup_mobile()
        cookies = self.sup_login(mobile=enterprise[0]['phone'])
        so_order, po_order = self.parana_order()
        url =("https://staging-gateway.test.lcscm.cn/zhonghai/trade-center"
              "/order-admin-center/1004708/api/trantor/data-source")
        data ={
	"frontendContext": {

	},
	"singleResult": False,
	"targetModel": "order_OrderPO",
	"sourceModel": "order_OrderPO",
	"searchValues": {
		"code": {
			"type": "One",
			"fullMatch": True,
			"value": po_order['code']
		}
	},
	"dataSource": {
		"actionKey": "order_OrderPO_order_supplier_orders_to_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "code"
			},
			{
				"fieldName": "title"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "settleStatus"
			},
			{
				"fieldName": "qualityAssuranceStatus"
			},
			{
				"fieldName": "projectReceiverName"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "protocolName"
			},
			{
				"fieldName": "categoryNames"
			},
			{
				"fieldName": "project",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "name"
					}
				]
			},
			{
				"fieldName": "purchaserName"
			},
			{
				"fieldName": "dealerName"
			},
			{
				"fieldName": "brandOwnerName"
			},
			{
				"fieldName": "signStatus"
			},
			{
				"fieldName": "orderDate"
			},
			{
				"fieldName": "takeOrderDate"
			},
			{
				"fieldName": "totalAmount"
			},
			{
				"fieldName": "getGoodsAmount"
			},
			{
				"fieldName": "deliveryAmount"
			},
			{
				"fieldName": "reverseAmount"
			},
			{
				"fieldName": "settledAmount"
			},
			{
				"fieldName": "orderCreateType"
			},
			{
				"fieldName": "payType"
			},
			{
				"fieldName": "contract",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "name"
					}
				]
			},
			{
				"fieldName": "id"
			},
			{
				"fieldName": "supplier",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "name"
					}
				]
			},
			{
				"fieldName": "brandOwner",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "name"
					}
				]
			},
			{
				"fieldName": "assignAble"
			}
		]
	},
	"paging": {
		"no": 1,
		"size": 200
	},
	"order": {
		"by": "createdAt",
		"isAsc": False
	}
}
        response = requests.post(url=url, json=data,cookies=cookies)
        result = response.json()['res']['data']
        url1 =("https://staging-gateway.test.lcscm.cn/zhonghai"
               "/trade-center/order-admin-center/1004708/api/trantor/action/exe")
        data1 ={
    "frontendContext": {},
    "actionKey": "order_GetGoodsOrderPO_GetGoodsServerAction::defaultContact",
    "context": {
        "env": {
            "mdEnterpriseId": enterprise[0]['id']
        },
        "record": [
            result
        ],
        "modelKey": "order_GetGoodsOrderPO"
    }
}
        response1 = requests.post(url=url1, json=data1, cookies=cookies)
        url2 = ('https://staging-gateway.test.lcscm.cn/zhonghai/trade-center/'
           'order-admin-center/1004708/api/trantor/action/exe')
        supplier_data = {
        "id": so_order['supplier'],
        "website": enterprise[0]['website']
    }
        supplier_contact_data = response1.json()['res']['data']['businessContact']
        data2 = {
        "frontendContext": {},
        "actionKey": "order_OrderPO_OrderAction::orderConfirm",
        "context": {
            "env": {
                "datas": {
                    "id": po_order['id'],
                    "supplier": supplier_data,
                    "supplierContact": supplier_contact_data
                }
            },
            "record": [
                {
                    "id": po_order['id'],
                    "supplier": supplier_data,
                    "supplierContact": supplier_contact_data
                }
            ],
            "modelKey": "order_OrderPO"
        }
    }
        if po_order['status'] == 'PENDING_RECEIVE':
            try:
                # Send the POST request and return the JSON response
                response = requests.post(url2, json=data2, cookies=cookies)
                response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
                print(response.json())
            except requests.exceptions.RequestException as e:
                # Handle any request exceptions and return an error message
                print(str(e))
        else:
            # Return a status message if the order doesn't need to be confirmed
            print ("该订单为'{}'，无需操作").format(po_order['status'])

    def order_goods(self,getGoodsNum):
        pur_user = self.pur_mobile()
        cookies = self.sup_login(mobile=pur_user['mobile'])
        url1 = ('https://staging-gateway.test.lcscm.cn/zhonghai/trade-center'
                '/order-admin-center/1004708/api/trantor/data-source')
        data1 = {
            "frontendContext": {},
            "singleResult": True,
            "targetModel": "order_GetGoodsOrderPO",
            "sourceModel": "order_OrderPO",
            "queryValues": {
                "id": {
                    "type": "One",
                    "value": self.so_id
                }
            },
            "dataSource": {
                "actionKey": "order_GetGoodsOrderPO_order_goods_to_create"
            },
            "result": {
                "fields": [
                    {
                        "fieldName": "id"
                    },
                    {
                        "fieldName": "code"
                    },
                    {
                        "fieldName": "orderCode"
                    },
                    {
                        "fieldName": "createdAt"
                    },
                    {
                        "fieldName": "readyToShipLetter"
                    },
                    {
                        "fieldName": "expectedArrivalDate"
                    },
                    {
                        "fieldName": "siteReceivingContact"
                    },
                    {
                        "fieldName": "siteReceivingContactPhone"
                    },
                    {
                        "fieldName": "orderAttachment"
                    },
                    {
                        "fieldName": "getGoodsOrderAttachment"
                    },
                    {
                        "fieldName": "remark"
                    },
                    {
                        "fieldName": "order",
                        "fields": [
                            {
                                "fieldName": "id"
                            },
                            {
                                "fieldName": "code"
                            },
                            {
                                "fieldName": "purchaser",
                                "fields": [
                                    {
                                        "fieldName": "id"
                                    },
                                    {
                                        "fieldName": "name"
                                    }
                                ]
                            },
                            {
                                "fieldName": "corporateCompanyName"
                            },
                            {
                                "fieldName": "project",
                                "fields": [
                                    {
                                        "fieldName": "id"
                                    },
                                    {
                                        "fieldName": "name"
                                    }
                                ]
                            },
                            {
                                "fieldName": "projectReceiverName"
                            },
                            {
                                "fieldName": "projectReceiverPhone"
                            },
                            {
                                "fieldName": "dealerName"
                            },
                            {
                                "fieldName": "dealerContactName"
                            },
                            {
                                "fieldName": "dealerContactMobile"
                            },
                            {
                                "fieldName": "brandOwnerName"
                            },
                            {
                                "fieldName": "lingchaoContact"
                            },
                            {
                                "fieldName": "lingchaoMobile"
                            },
                            {
                                "fieldName": "orderRule"
                            }
                        ]
                    },
                    {
                        "fieldName": "getGoodsOrderLinePOList",
                        "fields": [
                            {
                                "fieldName": "id"
                            },
                            {
                                "fieldName": "item",
                                "fields": [
                                    {
                                        "fieldName": "id"
                                    },
                                    {
                                        "fieldName": "name"
                                    }
                                ]
                            },
                            {
                                "fieldName": "itemCode"
                            },
                            {
                                "fieldName": "itemName"
                            },
                            {
                                "fieldName": "brand",
                                "fields": [
                                    {
                                        "fieldName": "id"
                                    },
                                    {
                                        "fieldName": "name"
                                    }
                                ]
                            },
                            {
                                "fieldName": "specification"
                            },
                            {
                                "fieldName": "attribute"
                            },
                            {
                                "fieldName": "unit"
                            },
                            {
                                "fieldName": "colorNum"
                            },
                            {
                                "fieldName": "priceTax"
                            },
                            {
                                "fieldName": "priceNoTax"
                            },
                            {
                                "fieldName": "taxPrice"
                            },
                            {
                                "fieldName": "price"
                            },
                            {
                                "fieldName": "getGoodsNum"
                            },
                            {
                                "fieldName": "expectedArrivalDate"
                            },
                            {
                                "fieldName": "remark"
                            },
                            {
                                "fieldName": "itemMallUrl"
                            }
                        ],
                        "page": {
                            "curPage": 1,
                            "pageSize": 650
                        }
                    }
                ]
            }
        }
        response = requests.post(url=url1,json=data1, cookies=cookies)
        orders = response.json()
        url2 =("https://staging-gateway.test.lcscm.cn/zhonghai/trade-center"
               "/order-admin-center/1004708/api/trantor/action/exe")
        getGoodsOrderLinePOList = orders['res']['data']['getGoodsOrderLinePOList']
        record =[
            {
                "code": None,
                "orderCode": self.so_code,
                "createdAt": None,
                "readyToShipLetter": None,
                "expectedArrivalDate": None,
                "siteReceivingContact": pur_user['nickname'],
                "siteReceivingContactPhone": pur_user['mobile'],
                "orderAttachment": {
                    "files": []
                },
                "getGoodsOrderAttachment": None,
                "remark": None,
                "order": orders['res']['data']['order'],
                "getGoodsOrderLinePOList": getGoodsOrderLinePOList
            }
        ]
        for i in range(len(getGoodsOrderLinePOList)):
            getGoodsOrderLinePOList[i]['getGoodsNum'] = getGoodsNum
        data2 =    {
        "frontendContext": {},
        "actionKey": "order_GetGoodsOrderPO_GetGoodsServerAction::checkGoodsOrder",
        "context": {
            "record": record,
            "modelKey": "order_GetGoodsOrderPO"
             }
        }
        data3 = {
    "frontendContext": {},
    "actionKey": "order_GetGoodsOrderPO_OrderGoodsAction::submitGoodsOrder",
    "context": {
        "modelKey": "order_GetGoodsOrderPO",
        "actionLabel": "提交",
        "record": record
    }
}

        try :
            response2 = requests.post(url=url2, json=data2, cookies=cookies)
            result1 = response2.json()
            response2.raise_for_status()
            response3 = requests.post(url=url2, json=data3, cookies=cookies)
            result2 = response3.json()
            print(result2)
        except requests.exceptions.RequestException as e:
            # Handle any request exceptions and return an error message
            print(str(e))

    def confirm_orders(self):
        enterprise = self.sup_mobile()
        cookies = self.sup_login(mobile=enterprise[0]['phone'])
        so_goods_order, po_goods_order = self.parana_get_goods_order()
        url1 = ("https://staging-gateway.test.lcscm.cn"
                "/zhonghai/trade-center/order-admin-center/1004708/api/trantor/data-source")

        data1 = {
            "frontendContext": {},
            "singleResult": False,
            "targetModel": "order_GetGoodsOrderPO",
            "sourceModel": "order_GetGoodsOrderPO",
            "searchValues": {
                "code": {
                    "type": "One",
                    "value": None
                },
                "searchEventType": {
                    "type": "One",
                    "value": "SEARCH_GOODS_ORDER_BY_SUPPLIER"
                }
            },
            "dataSource": {
                "actionKey": "order_GetGoodsOrderPO_supplier_get_goods_order_to_list"
            },
            "result": {
                "fields": [
                    {
                        "fieldName": "code"
                    },
                    {
                        "fieldName": "orderCode"
                    },
                    {
                        "fieldName": "order",
                        "fields": [
                            {
                                "fieldName": "id"
                            },
                            {
                                "fieldName": "code"
                            },
                            {
                                "fieldName": "title"
                            },
                            {
                                "fieldName": "purchaserName"
                            },
                            {
                                "fieldName": "buyer",
                                "fields": [
                                    {
                                        "fieldName": "id"
                                    },
                                    {
                                        "fieldName": "username"
                                    }
                                ]
                            },
                            {
                                "fieldName": "projectReceiverPhone"
                            },
                            {
                                "fieldName": "orderCreateType"
                            },
                            {
                                "fieldName": "payType"
                            },
                            {
                                "fieldName": "contract",
                                "fields": [
                                    {
                                        "fieldName": "id"
                                    },
                                    {
                                        "fieldName": "name"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "fieldName": "status"
                    },
                    {
                        "fieldName": "settleStatus"
                    },
                    {
                        "fieldName": "platformAuditStatus"
                    },
                    {
                        "fieldName": "project"
                    },
                    {
                        "fieldName": "getGoodsAmount"
                    },
                    {
                        "fieldName": "deliveryAmount"
                    },
                    {
                        "fieldName": "reverseAmount"
                    },
                    {
                        "fieldName": "createdAt"
                    },
                    {
                        "fieldName": "confirmDate"
                    },
                    {
                        "fieldName": "existReadyToShipmentPrepayment"
                    },
                    {
                        "fieldName": "dealer",
                        "fields": [
                            {
                                "fieldName": "id"
                            },
                            {
                                "fieldName": "name"
                            }
                        ]
                    },
                    {
                        "fieldName": "supplier",
                        "fields": [
                            {
                                "fieldName": "id"
                            },
                            {
                                "fieldName": "name"
                            },
                            {
                                "fieldName": "contactName"
                            },
                            {
                                "fieldName": "contactPhone"
                            }
                        ]
                    },
                    {
                        "fieldName": "id"
                    },
                    {
                        "fieldName": "assignable"
                    },
                    {
                        "fieldName": "remark"
                    }
                ]
            },
            "paging": {
                "no": 1,
                "size": 10
            },
            "order": {
                "by": "updatedAt",
                "isAsc": False
            }
        }
        url2 = ("https://staging-gateway.test.lcscm.cn"
                "/zhonghai/trade-center/order-admin-center/1004708/api/trantor/action/exe")
        data2 = {
            "frontendContext": {},
            "actionKey": "order_GetGoodsOrderPO_GetGoodsServerAction::goodsOrderConfirm",
            "context": {
                "record": None,
                "modelKey": "order_GetGoodsOrderPO"
            }
        }
        for i in range(len(po_goods_order)):
            if po_goods_order[i]['get_goods_status'] =='ORDERED_GOODS':
                data1['searchValues']['code']['value'] = po_goods_order[i]['code']
                try:
                    response1 = requests.post(url=url1, json=data1, cookies=cookies)
                    response1.raise_for_status()
                    orders = response1.json()
                    data2['context']['record'] = orders['res']['data']
                    response2 = requests.post(url=url2, json=data2, cookies=cookies)
                    print(response2.json())
                except requests.exceptions.RequestException as e:
                # Handle any request exceptions and return an error message
                    print(str(e))


    def apply_shipment(self):
        enterprise = self.sup_mobile()
        cookies = self.sup_login(mobile=enterprise[0]['phone'])
        so_goods_order, po_goods_order = self.parana_get_goods_order()
        url1 = ("https://staging-gateway.test.lcscm.cn"
                "/zhonghai/trade-center/order-admin-center/1004708/api/trantor/data-source")

        url2 = ("https://staging-gateway.test.lcscm.cn"
                "/zhonghai/trade-center/order-admin-center/1004708/api/trantor/action/exe")
        data1 = {
            "frontendContext": {},
            "singleResult": True,
            "targetModel": "order_DeliveryOrderPO",
            "sourceModel": "order_DeliveryOrderPO",
            "queryValues": {
                "id": {
                    "type": "One",
                    "value": 224007
                }
            },
            "dataSource": {
                "actionKey": "order_DeliveryOrderPO_delivery_order_to_create"
            },
            "result": {
                "fields": [
                    {
                        "fieldName": "id"
                    },
                    {
                        "fieldName": "code"
                    },
                    {
                        "fieldName": "getGoodsOrderCode"
                    },
                    {
                        "fieldName": "address"
                    },
                    {
                        "fieldName": "sender"
                    },
                    {
                        "fieldName": "contactMobile"
                    },
                    {
                        "fieldName": "deliveryDate"
                    },
                    {
                        "fieldName": "arrivalDate"
                    },
                    {
                        "fieldName": "acceptanceDate"
                    },
                    {
                        "fieldName": "getGoodsOrder",
                        "fields": [
                            {
                                "fieldName": "id"
                            },
                            {
                                "fieldName": "siteReceivingContact"
                            },
                            {
                                "fieldName": "siteReceivingContactPhone"
                            }
                        ]
                    },
                    {
                        "fieldName": "remark"
                    },
                    {
                        "fieldName": "order",
                        "fields": [
                            {
                                "fieldName": "id"
                            },
                            {
                                "fieldName": "code"
                            },
                            {
                                "fieldName": "purchaserName"
                            },
                            {
                                "fieldName": "project",
                                "fields": [
                                    {
                                        "fieldName": "id"
                                    },
                                    {
                                        "fieldName": "name"
                                    }
                                ]
                            },
                            {
                                "fieldName": "projectReceiverName"
                            },
                            {
                                "fieldName": "projectReceiverPhone"
                            },
                            {
                                "fieldName": "dealerName"
                            },
                            {
                                "fieldName": "dealerContactName"
                            },
                            {
                                "fieldName": "dealerContactMobile"
                            },
                            {
                                "fieldName": "brandOwnerName"
                            }
                        ]
                    },
                    {
                        "fieldName": "lingchaoContact"
                    },
                    {
                        "fieldName": "lingchaoMobile"
                    },
                    {
                        "fieldName": "deliveryOrderLinePOList",
                        "fields": [
                            {
                                "fieldName": "id"
                            },
                            {
                                "fieldName": "item",
                                "fields": [
                                    {
                                        "fieldName": "id"
                                    },
                                    {
                                        "fieldName": "name"
                                    },
                                    {
                                        "fieldName": "brandId"
                                    },
                                    {
                                        "fieldName": "brandName"
                                    },
                                    {
                                        "fieldName": "supplyCycle"
                                    }
                                ]
                            },
                            {
                                "fieldName": "itemCode"
                            },
                            {
                                "fieldName": "itemName"
                            },
                            {
                                "fieldName": "specification"
                            },
                            {
                                "fieldName": "attribute"
                            },
                            {
                                "fieldName": "unit"
                            },
                            {
                                "fieldName": "getGoodsOrderLine",
                                "fields": [
                                    {
                                        "fieldName": "id"
                                    },
                                    {
                                        "fieldName": "colorNum"
                                    },
                                    {
                                        "fieldName": "toDeliveryNum"
                                    },
                                    {
                                        "fieldName": "canApplyDeliveryNumber"
                                    }
                                ]
                            },
                            {
                                "fieldName": "deliveryNum"
                            },
                            {
                                "fieldName": "reasonableArrivalDate"
                            }
                        ],
                        "page": {
                            "curPage": 1,
                            "pageSize": 650
                        }
                    }
                ]
            }
        }
        data2 = {
            "frontendContext": {},
            "actionKey": "order_DeliveryOrderPO_DeliveryOrderServerAction::applyDelivery",
            "context": {
                "modelKey": "order_DeliveryOrderPO",
                "env": {
                    "getGoodsOrderId": 224007
                },
                "actionLabel": "提交发货申请",
                "record": [
                    {
                        "code": None,
                        "getGoodsOrderCode": "PO20231220000001001",
                        "address": None,
                        "sender": "test2熊",
                        "contactMobile": "18178952877",
                        "deliveryDate": 1704421614000,
                        "arrivalDate": None,
                        "acceptanceDate": None,
                        "getGoodsOrder": {
                            "id": 224007,
                            "siteReceivingContact": "test1熊",
                            "siteReceivingContactPhone": "13500000011"
                        },
                        "remark": None,
                        "order": {
                            "id": 236032,
                            "purchaserName": "深圳哈哈有限公司",
                            "project": {
                                "id": 110002,
                                "name": "test1采购项目"
                            },
                            "projectReceiverName": None,
                            "projectReceiverPhone": None,
                            "dealerName": None,
                            "dealerContactName": "test2熊",
                            "dealerContactMobile": "18178952877",
                            "brandOwnerName": "深圳哈哈有限公司"
                        },
                        "lingchaoContact": "test1",
                        "lingchaoMobile": "18178952878",
                        "deliveryOrderLinePOList": [
                            {
                                "item": {
                                    "id": 210204601003306,
                                    "brandId": 50001,
                                    "brandName": "立邦"
                                },
                                "itemCode": "210204601003306",
                                "itemName": "立邦 广角镜",
                                "specification": "立邦地坪漆材料 ：ZF-F951-防静电的环保地坪漆",
                                "attribute": "产品分类：交安系统；产品类型：广角镜；产品规格：直径800mm，PC树脂防爆镜面，胀栓支架固定；使用地区：地上或地下车库的交通安全设施；工艺分类：PC树脂",
                                "unit": "个",
                                "getGoodsOrderLine": {
                                    "id": 224009,
                                    "toDeliveryNum": 1,
                                    "canApplyDeliveryNumber": 1
                                },
                                "deliveryNum": 1,
                                "reasonableArrivalDate": None
                            }
                        ]
                    }
                ]
            }
        }
        for i in range(len(po_goods_order)):
            if  po_goods_order[i]['get_goods_status'] =='CONFIRMED':
                data1['queryValues']['id']['value'] = po_goods_order[i]['id']
                try:
                    response = requests.post(url=url1, json=data1, cookies=cookies)
                    response.raise_for_status()
                    orders = response.json()['res']['data']
                except requests.exceptions.RequestException as e:
                    print(str(e))
                record = data2['context']['record'][0]
                data2['context']['env']['getGoodsOrderId'] = orders['getGoodsOrder']['id']
                record['getGoodsOrderCode'] = orders['getGoodsOrderCode']
                record['getGoodsOrder']['id'] = orders['getGoodsOrder']['id']
                record['getGoodsOrder']['siteReceivingContact'] = orders['getGoodsOrder']['siteReceivingContact']
                record['getGoodsOrder']['siteReceivingContactPhone'] = (
                    orders)['getGoodsOrder']['siteReceivingContactPhone']
                record['order']['id'] = orders['order']['id']
                record['order']['purchaserName'] = orders['order']['purchaserName']
                record['order']['project'] = orders['order']['project']
                record['order']['dealerContactName'] = orders['order']['dealerContactName']
                record['order']['dealerContactMobile'] = orders['order']['dealerContactMobile']
                record['order']['brandOwnerName'] = orders['order']['brandOwnerName']
                record['lingchaoContact'] = orders['lingchaoContact']
                record['lingchaoMobile'] = orders['lingchaoMobile']
                deliveryOrderLinePOList = []
                for i in range(len(orders['deliveryOrderLinePOList'])):
                    dict1 = {}
                    dict1['item'] = orders['deliveryOrderLinePOList'][i]['item']
                    dict1['itemCode'] = orders['deliveryOrderLinePOList'][i]['itemCode']
                    dict1['itemName'] = orders['deliveryOrderLinePOList'][i]['itemName']
                    dict1['specification'] = orders['deliveryOrderLinePOList'][i]['specification']
                    dict1['unit'] = orders['deliveryOrderLinePOList'][i]['unit']
                    dict1['getGoodsOrderLine'] = (
                        orders)['deliveryOrderLinePOList'][i]['getGoodsOrderLine']
                    dict1['deliveryNum'] = (
                    orders)['deliveryOrderLinePOList'][i]['deliveryNum']
                    deliveryOrderLinePOList.append(dict1)
                record['deliveryOrderLinePOList'] = deliveryOrderLinePOList
                try:
                    response2 = requests.post(url=url2, json=data2, cookies=cookies)
                    response2.raise_for_status()
                    print(response2.json())
                except requests.exceptions.RequestException as e:
                    print(str(e))

    def to_ship(self):
        cookies = self.sup_login(mobile='18520611771')
        so_delivery_order, po_delivery_order = self.parana_delivery_order()
        url1 = ("https://staging-gateway.test.lcscm.cn"
               "/zhonghai/trade-center/order-admin-center/1004708/api/trantor/action/exe")
        data1 = {
            "frontendContext": {},
            "actionKey": "order_DeliveryApproveVO_DeliveryApproveSingleDataAction::getDeliveryApproveInfo",
            "context": {
                "env": {
                    "id": 204049
                },
                "record": [],
                "modelKey": "order_DeliveryApproveVO"
            }
        }
        data2 = {
            "frontendContext": {},
            "actionKey": "order_DeliveryApproveVO_DeliveryApproveSingleDataAction::submitOA",
            "context": {
                "env": {
                    "id": 204049,
                    "purchaserName": "湖北家家有限公司",
                    "corporateCompanyName": "湖北家家有限公司",
                    "oaContent": "付款方式：预付款20.00%，货款60.00%；应开保函XXX元；\n预付款：本期发生应收预收款11.93元，应收预收款11.93，已收预付款0.00元，预付款未回款；\n保函：应开保函XXX元，已开保函0.00元，保函到期日：；\n账期敞口：合同下往期已发货435,501.68元，本期申请发货59.66元，至本期已发货：435,561.34元，累计已回款375,613.26元，账期敞口：59,948.08元；\n应收未收款：应收未收款33,928.00元；\n\n申请发货，请领导审批。",
                    "deliveryAmount": 59.66,
                    "advanceInfoList": [
                        {
                            "__trantorExtendFields": {},
                            "advanceType": "预收款-需求单",
                            "deliveryAmount": 0,
                            "periodAmount": 5.966,
                            "receivedAmount": 0,
                            "riskLevel": 3,
                            "stateDesc": "预收款未回款"
                        },
                        {
                            "__trantorExtendFields": {},
                            "advanceType": "预收款-订单",
                            "deliveryAmount": 0,
                            "periodAmount": 5.966,
                            "receivedAmount": 0,
                            "riskLevel": 3,
                            "stateDesc": "预收款未回款"
                        }
                    ],
                    "advanceAmount": 11.93,
                    "restAmount": 47.73,
                    "riskLevel": 3,
                    "receiveInfo": {
                        "__trantorExtendFields": {},
                        "periodAmount": 11.93,
                        "receiveType": "应收未收款",
                        "riskLevel": 2,
                        "stateDesc": "有此单外的欠款",
                        "unreceivedAmount": 33928
                    },
                    "guarantee": {
                        "__trantorExtendFields": {},
                        "guaranteeType": "保函",
                        "occupyAmount": 0,
                        "riskLevel": 1,
                        "stateDesc": "无保函"
                    },
                    "accountPeriod": {
                        "__trantorExtendFields": {},
                        "afterPeriodAmount": 59948.08,
                        "periodAmount": 59.66,
                        "periodPercent": 59888.42,
                        "periodType": "账期敞口",
                        "riskLevel": 3,
                        "stateDesc": "保函不可覆盖账期敞口"
                    }
                },
                "record": [],
                "modelKey": "order_DeliveryApproveVO"
            }
        }
        for i in range(len(po_delivery_order)):
            if po_delivery_order[i]['platform_audit_status'] =='DELIVERY_WAIT_AUDIT':
                data1['context']['env']['id'] = po_delivery_order[i]['id']
                response1 = requests.post(url=url1,json=data1, cookies=cookies)
                orders = response1.json()['res']['data']
                data = data2['context']['env']
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
                try:
                    response2 = requests.post(url=url1 ,json=data2, cookies=cookies)
                    response2.raise_for_status()
                    print(response2.json())
                except requests.exceptions.RequestException as e:
                    print(str(e))


    def oa_approver(self):
        url = "https://settlement-admin-uat.test.lcscm.cn/oa/approval/callback"
        data = {
            "auditComments": "审批通过",
            "instanceId": "0aa9b2f4-d5e7-4592-9db6-5a4ea601d993",
            "type": "DELIVERY",
            "status": "APPROVED"
        }
        so_delivery_order, po_delivery_order = self.parana_delivery_order()
        for i in range(len(po_delivery_order)):
            if  (po_delivery_order[i]['platform_audit_status'] =='DELIVERY_WAIT_AUDIT'
                    and po_delivery_order[i]['oa_delivery_status'] =='OA_DELIVERY_WAIT_AUDIT'):
                data['instanceId'] = po_delivery_order[i]['oa_instance_id']
                response = requests.post(url=url,json=data)
                print(response.json(),str(po_delivery_order[i]['id']))


    def order_accept(self):
        pur_user = self.pur_mobile()
        cookies = self.sup_login(mobile=pur_user['mobile'])
        so_delivery_order, po_delivery_order = self.parana_delivery_order()
        url1 = ("https://staging-gateway.test.lcscm.cn"
                "/zhonghai/trade-center/order-admin-center/1004708/api/trantor/data-source")

        data1 = {
            "frontendContext": {},
            "singleResult": True,
            "targetModel": "order_AcceptanceOrderPO",
            "sourceModel": "order_DeliveryOrderPO",
            "queryValues": {
                "id": {
                    "type": "One",
                    "value": 196066
                }
            },
            "dataSource": {
                "actionKey": "order_AcceptanceOrderPO_acceptance_create"
            },
            "result": {
                "fields": [
                    {
                        "fieldName": "id"
                    },
                    {
                        "fieldName": "isInstall"
                    },
                    {
                        "fieldName": "deliveryOrder",
                        "fields": [
                            {
                                "fieldName": "id"
                            }
                        ]
                    },
                    {
                        "fieldName": "parentAcceptanceOrderCode"
                    },
                    {
                        "fieldName": "order",
                        "fields": [
                            {
                                "fieldName": "id"
                            },
                            {
                                "fieldName": "code"
                            },
                            {
                                "fieldName": "purchaserName"
                            },
                            {
                                "fieldName": "project",
                                "fields": [
                                    {
                                        "fieldName": "id"
                                    },
                                    {
                                        "fieldName": "name"
                                    },
                                    {
                                        "fieldName": "corporateCompany",
                                        "fields": [
                                            {
                                                "fieldName": "id"
                                            },
                                            {
                                                "fieldName": "companyName"
                                            },
                                            {
                                                "fieldName": "graphicSealValidPeriodEnd"
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "fieldName": "projectReceiverName"
                            },
                            {
                                "fieldName": "projectReceiverPhone"
                            },
                            {
                                "fieldName": "dealerName"
                            },
                            {
                                "fieldName": "dealerContactName"
                            },
                            {
                                "fieldName": "dealerContactMobile"
                            },
                            {
                                "fieldName": "brandOwnerName"
                            },
                            {
                                "fieldName": "orderRule"
                            }
                        ]
                    },
                    {
                        "fieldName": "code"
                    },
                    {
                        "fieldName": "deliveryCode"
                    },
                    {
                        "fieldName": "address"
                    },
                    {
                        "fieldName": "getGoodsOrder",
                        "fields": [
                            {
                                "fieldName": "id"
                            },
                            {
                                "fieldName": "getGoodsContact",
                                "fields": [
                                    {
                                        "fieldName": "id"
                                    },
                                    {
                                        "fieldName": "username"
                                    },
                                    {
                                        "fieldName": "nickname"
                                    },
                                    {
                                        "fieldName": "mobile"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "fieldName": "sender"
                    },
                    {
                        "fieldName": "contactMobile"
                    },
                    {
                        "fieldName": "deliveryDate"
                    },
                    {
                        "fieldName": "arrivalDate"
                    },
                    {
                        "fieldName": "acceptanceDate"
                    },
                    {
                        "fieldName": "installAcceptanceDate"
                    },
                    {
                        "fieldName": "remark"
                    },
                    {
                        "fieldName": "logistics",
                        "fields": [
                            {
                                "fieldName": "id"
                            },
                            {
                                "fieldName": "companyName"
                            },
                            {
                                "fieldName": "trackingNumber"
                            },
                            {
                                "fieldName": "deliveryStaff"
                            },
                            {
                                "fieldName": "contactMobile"
                            }
                        ]
                    },
                    {
                        "fieldName": "lingchaoContact"
                    },
                    {
                        "fieldName": "lingchaoMobile"
                    },
                    {
                        "fieldName": "acceptanceOrderLinePOList",
                        "fields": [
                            {
                                "fieldName": "id"
                            },
                            {
                                "fieldName": "itemCode"
                            },
                            {
                                "fieldName": "item",
                                "fields": [
                                    {
                                        "fieldName": "id"
                                    },
                                    {
                                        "fieldName": "name"
                                    }
                                ]
                            },
                            {
                                "fieldName": "itemName"
                            },
                            {
                                "fieldName": "brand",
                                "fields": [
                                    {
                                        "fieldName": "id"
                                    },
                                    {
                                        "fieldName": "name"
                                    }
                                ]
                            },
                            {
                                "fieldName": "specification"
                            },
                            {
                                "fieldName": "attribute"
                            },
                            {
                                "fieldName": "unit"
                            },
                            {
                                "fieldName": "getGoodsOrderLinePO",
                                "fields": [
                                    {
                                        "fieldName": "id"
                                    },
                                    {
                                        "fieldName": "colorNum"
                                    }
                                ]
                            },
                            {
                                "fieldName": "deliveryNum"
                            },
                            {
                                "fieldName": "acceptanceNum"
                            },
                            {
                                "fieldName": "remark"
                            },
                            {
                                "fieldName": "orderLinePO",
                                "fields": [
                                    {
                                        "fieldName": "id"
                                    }
                                ]
                            }
                        ],
                        "page": {
                            "curPage": 1,
                            "pageSize": 650
                        }
                    }
                ]
            }
        }
        url2 = ("https://staging-gateway.test.lcscm.cn"
                "/zhonghai/trade-center/order-admin-center/1004708/api/trantor/action/exe")
        data2 ={
    "frontendContext": {},
    "actionKey": "order_AcceptanceOrderPO_AcceptanceOrderServerAction::checkAcceptanceInputError",
    "context": {
        "modelKey": "order_AcceptanceOrderPO",
        "env": {
            "datas": {
                "context": {}
            }
        },
        "record": [
            {
                "context": {}
            }
        ]
    }
}
        data3 = {
            "frontendContext": {},
            "actionKey": "order_AcceptanceOrderPO_AcceptanceOrderServerAction::save",
            "context": {
                "record": [1],
                "modelKey": "order_AcceptanceOrderPO",
                "env": {
                    "datas": {}
                }
            }
        }
        for i in range(len(so_delivery_order)):
            if so_delivery_order[i]['status'] == 'DELIVERY_SHIPPED':
                data1['queryValues']['id']['value'] = so_delivery_order[i]['id']
                response = requests.post(url=url1, json=data1,cookies=cookies)
                response.raise_for_status()
                orders = response.json()['res']['data']
                record = data2['context']['record'][0]['context']
                for i in range(len(orders['acceptanceOrderLinePOList'])):
                    orders['acceptanceOrderLinePOList'][i]['acceptanceNum'] = (
                        orders)['acceptanceOrderLinePOList'][i]['deliveryNum']
                record = orders
                data2['context']['env']['datas']['context'] = record
                response1 = requests.post(url=url2,json=data2, cookies=cookies)
                print(response1.json())
                data3['context']['record'][0] = record
                data3['context']['env']['datas'] = record
                response2 = requests.post(url=url2,json=data3, cookies=cookies)
                print(response2.json())

    def Install_accept(self):
        pur_user = self.pur_mobile()
        cookies = self.sup_login(mobile=pur_user['mobile'])
        so_delivery_order, po_delivery_order = self.parana_delivery_order()
        url1 = ("https://staging-gateway.test.lcscm.cn"
                "/zhonghai/trade-center/order-admin-center/1004708/api/trantor/data-source")
        data1 = {
            "frontendContext": {},
            "singleResult": True,
            "targetModel": "order_AcceptanceOrderPO",
            "sourceModel": "order_DeliveryOrderPO",
            "queryValues": {
                "id": {
                    "type": "One",
                    "value": 204050
                }
            },
            "dataSource": {
                "actionKey": "order_AcceptanceOrderPO_acceptance_install_create"
            },
            "result": {
                "fields": [
                    {
                        "fieldName": "id"
                    },
                    {
                        "fieldName": "isInstall"
                    },
                    {
                        "fieldName": "installCode"
                    },
                    {
                        "fieldName": "deliveryOrder",
                        "fields": [
                            {
                                "fieldName": "id"
                            }
                        ]
                    },
                    {
                        "fieldName": "parentAcceptanceOrderCode"
                    },
                    {
                        "fieldName": "deliveryCode"
                    },
                    {
                        "fieldName": "address"
                    },
                    {
                        "fieldName": "order",
                        "fields": [
                            {
                                "fieldName": "id"
                            },
                            {
                                "fieldName": "code"
                            },
                            {
                                "fieldName": "purchaserName"
                            },
                            {
                                "fieldName": "project",
                                "fields": [
                                    {
                                        "fieldName": "id"
                                    },
                                    {
                                        "fieldName": "name"
                                    },
                                    {
                                        "fieldName": "corporateCompany",
                                        "fields": [
                                            {
                                                "fieldName": "id"
                                            },
                                            {
                                                "fieldName": "companyName"
                                            },
                                            {
                                                "fieldName": "graphicSealValidPeriodEnd"
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "fieldName": "projectReceiverName"
                            },
                            {
                                "fieldName": "projectReceiverPhone"
                            },
                            {
                                "fieldName": "dealerName"
                            },
                            {
                                "fieldName": "dealerContactName"
                            },
                            {
                                "fieldName": "dealerContactMobile"
                            },
                            {
                                "fieldName": "brandOwnerName"
                            },
                            {
                                "fieldName": "orderRule"
                            }
                        ]
                    },
                    {
                        "fieldName": "getGoodsOrder",
                        "fields": [
                            {
                                "fieldName": "id"
                            },
                            {
                                "fieldName": "getGoodsContact",
                                "fields": [
                                    {
                                        "fieldName": "id"
                                    },
                                    {
                                        "fieldName": "username"
                                    },
                                    {
                                        "fieldName": "nickname"
                                    },
                                    {
                                        "fieldName": "mobile"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "fieldName": "sender"
                    },
                    {
                        "fieldName": "contactMobile"
                    },
                    {
                        "fieldName": "deliveryDate"
                    },
                    {
                        "fieldName": "arrivalDate"
                    },
                    {
                        "fieldName": "acceptanceDate"
                    },
                    {
                        "fieldName": "installAcceptanceDate"
                    },
                    {
                        "fieldName": "remark"
                    },
                    {
                        "fieldName": "lingchaoContact"
                    },
                    {
                        "fieldName": "lingchaoMobile"
                    },
                    {
                        "fieldName": "acceptanceOrderLinePOList",
                        "fields": [
                            {
                                "fieldName": "id"
                            },
                            {
                                "fieldName": "itemCode"
                            },
                            {
                                "fieldName": "item",
                                "fields": [
                                    {
                                        "fieldName": "id"
                                    },
                                    {
                                        "fieldName": "name"
                                    }
                                ]
                            },
                            {
                                "fieldName": "itemName"
                            },
                            {
                                "fieldName": "brand",
                                "fields": [
                                    {
                                        "fieldName": "id"
                                    },
                                    {
                                        "fieldName": "name"
                                    }
                                ]
                            },
                            {
                                "fieldName": "specification"
                            },
                            {
                                "fieldName": "attribute"
                            },
                            {
                                "fieldName": "unit"
                            },
                            {
                                "fieldName": "getGoodsOrderLinePO",
                                "fields": [
                                    {
                                        "fieldName": "id"
                                    },
                                    {
                                        "fieldName": "colorNum"
                                    }
                                ]
                            },
                            {
                                "fieldName": "deliveryNum"
                            },
                            {
                                "fieldName": "acceptanceNum"
                            },
                            {
                                "fieldName": "reverseNum"
                            },
                            {
                                "fieldName": "installAcceptanceNum"
                            },
                            {
                                "fieldName": "orderLinePO",
                                "fields": [
                                    {
                                        "fieldName": "id"
                                    }
                                ]
                            }
                        ],
                        "page": {
                            "curPage": 1,
                            "pageSize": 650
                        }
                    }
                ]
            }
        }

        url2 = ("https://staging-gateway.test.lcscm.cn"
                "/zhonghai/trade-center/order-admin-center/1004708/api/trantor/action/exe")

        data2 = {
            "frontendContext": {},
            "actionKey": "order_AcceptanceOrderPO_AcceptanceOrderServerAction::checkAcceptanceInstallInputError",
            "context": {
                "modelKey": "order_AcceptanceOrderPO",
                "env": {
                    "deliveryOrderId": 204050
                },
                "record": [{}]
            }
        }

        data3 = {
            "frontendContext": {},
            "actionKey": "order_AcceptanceOrderPO_AcceptanceOrderServerAction::saveInstallOrder",
            "context": {
                "record": [{}],
                "modelKey": "order_AcceptanceOrderPO",
                "env": {
                    "datas": {}
                }
            }
        }
        for i in range(len(so_delivery_order)):
            if so_delivery_order[i]['status'] == "DELIVERY_RECEIVED":
                data1['queryValues']['id']['value'] = so_delivery_order[i]['id']
                response = requests.post(url=url1,json=data1, cookies=cookies)
                orders = response.json()['res']['data']
                data = data2['context']
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
                response1 = requests.post(url=url2,json=data2, cookies=cookies)
                print(response1.json())
                data3['context']['record'][0] = orders
                data3['context']['env']['datas'] = orders
                response2 = requests.post(url=url2, json=data3, cookies=cookies)
                print(response2.json())



def getdelivery(order_code):
    sql ="SELECT * FROM parana_get_goods_order WHERE `code`='{}';".format(order_code)
    data = my_conn(sql)[0]
    pur_user = order(data['order_code']).pur_mobile()
    cookies1 = order(data['order_code']).sup_login(mobile=pur_user['mobile'])
    url1 = "https://b2b-mall-uat.test.lcscm.cn/api/front/reverse/apply/{}".format(data['id'])
    try :
        response1 =requests.get(url=url1,cookies=cookies1)
        response1.raise_for_status()
        result1 = response1.json().get('result',{}).get('deliveryOrderInfos',{})
        return result1
    except requests.exceptions.RequestException as e:
        return e

def reverseItem(order_code,delivercode):
    sql = "SELECT * FROM parana_get_goods_order WHERE `code`='{}';".format(order_code)
    data = my_conn(sql)[0]
    pur_user = order(data['order_code']).pur_mobile()
    cookies1 = order(data['order_code']).sup_login(mobile=pur_user['mobile'])
    result1 = getdelivery(order_code)
    for i in range(len(result1)):
        if delivercode == result1[i]['code']:
            deliverid =result1[i]['id']
    url2 = "https://b2b-mall-uat.test.lcscm.cn/api/front/reverse/returnRefund"
    data2 = {"deliveryId": deliverid, "type": "ORDER_REVERSE"}
    try:
        result2 =  requests.post(url=url2,json=data2,cookies=cookies1)
        result2.raise_for_status()
        result2.json().get('result',{})
        return result2.json()['result']
    except requests.exceptions.RequestException as e:
        return str(e)

def goods_rejected(order_code,delivercode,item,num):
    sql = "SELECT * FROM parana_get_goods_order WHERE `code`='{}';".format(order_code)
    data = my_conn(sql)[0]
    pur_user = order(data['order_code']).pur_mobile()
    cookies1 = order(data['order_code']).sup_login(mobile=pur_user['mobile'])
    enterprise = order(data['order_code']).sup_mobile()
    cookies2 = order(data['order_code']).sup_login(mobile=enterprise[0]['phone'])
    url1 = "https://b2b-mall-uat.test.lcscm.cn/api/front/reverse/apply/{}".format(data['id'])
    response1 = requests.get(url=url1, cookies=cookies1)
    result1 = response1.json().get('result',{})
    for i in range(len(result1['deliveryOrderInfos'])):
        if delivercode == result1['deliveryOrderInfos'][i]['code']:
            deliverid = result1['deliveryOrderInfos'][i]['id']
    result2 = reverseItem(order_code,delivercode)
    items = item.split(',')
    nums = num.split(',')
    list1 = []
    for i in range(len(items)):
        dict1 = {}
        for j in range(len(result2)):
            if items[i] == str(result2[j]['itemId']):
                result2[j]['reverseNum'] = nums[i]
                dict1 = result2[j]
                list1.append(dict1)
    url3 = "https://b2b-mall-uat.test.lcscm.cn/api/front/reverse/create"
    data3 = {
        "deliveryOrderId": deliverid,
        "deliveryOrderCode": delivercode,
        "orderId": None,
        "reverseType": "RETURN_REFUND",
        "type": "ORDER_REVERSE",
        "reverser": result1['reverser'],
        "reasonType": "货物破损",
        "reverseItemLineInfos": list1,
        "contactMobile": result1['contactMobile']
    }
    response3 = requests.post(url=url3, json=data3,cookies=cookies1)
    print(response3.json())

    sql1 = ("select * from parana_reverse_order WHERE "
            "delivery_order_code =(SELECT id FROM parana_delivery_order "
            "WHERE `code`='PO20240222000007001001') and "
            "`status` ='ORDER_WAITING'").format(delivercode.replace('SO','PO'))
    record_id = my_conn(sql1)[0]['id']
    url4 = ("https://staging-gateway.test.lcscm.cn"
            "/zhonghai/trade-center/order-admin-center/1004708/api/trantor/action/exe")
    data4 = {"frontendContext": {},
             "actionKey": "order_ReverseOrderPO_ReverseOrderServerAction::approveReverseOrder",
             "context": {"modelKey": "order_ReverseOrderPO", "actionLabel": "确认",
                         "record": [{"id":record_id}]}}
    response4 = requests.post(url=url4, json=data4,cookies=cookies2)
    print(response4.json())

def settlement_orders(so_code):
    order1 = order(so_code)
    enterprise = order1.sup_mobile()
    cookies = order1.sup_login(mobile=enterprise[0]['phone'])
    so_order, po_order = order1.parana_order()
    url1 = ("https://staging-gateway.test.lcscm.cn"
            "/zhonghai/trade-center/order-admin-center/1004708/api/trantor/action/exe")

    data1 = {
        "frontendContext": {},
        "actionKey": "order_admin_center_OrderSettlementVO_OrderSettleAction::toCreateCheck",
        "context": {
            "record": [
                {
                    "id": po_order['id']
                }
            ],
            "modelKey": "order_admin_center_OrderSettlementVO"
        }
    }
    response = requests.post(url=url1,json=data1, cookies=cookies)
    restult1 = response.json()
    url2 = ("https://staging-gateway.test.lcscm.cn"
            "/zhonghai/trade-center/order-admin-center/1004708/api/trantor/data-source")

    data2 = {
        "frontendContext": {},
        "singleResult": True,
        "targetModel": "order_admin_center_OrderSettlementVO",
        "sourceModel": "order_admin_center_OrderSettlementVO",
        "queryValues": {
            "id": {
                "type": "One",
                "value": po_order['id']
            }
        },
        "dataSource": {
            "actionKey": "order_admin_center_OrderSettlementVO_order_settle_create"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "order",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "code"
                        },
                        {
                            "fieldName": "title"
                        },
                        {
                            "fieldName": "contractName"
                        },
                        {
                            "fieldName": "project",
                            "fields": [
                                {
                                    "fieldName": "id"
                                },
                                {
                                    "fieldName": "name"
                                }
                            ]
                        },
                        {
                            "fieldName": "purchaserName"
                        },
                        {
                            "fieldName": "totalAmount"
                        }
                    ]
                },
                {
                    "fieldName": "settlementTotal"
                },
                {
                    "fieldName": "remainedRetentionStart"
                },
                {
                    "fieldName": "remainedRetentionEnd"
                },
                {
                    "fieldName": "attachment"
                },
                {
                    "fieldName": "settlementDesc"
                },
                {
                    "fieldName": "orderSettlementDetailList",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "orderLinePO",
                            "fields": [
                                {
                                    "fieldName": "id"
                                },
                                {
                                    "fieldName": "itemCode"
                                },
                                {
                                    "fieldName": "itemName"
                                },
                                {
                                    "fieldName": "brand",
                                    "fields": [
                                        {
                                            "fieldName": "id"
                                        },
                                        {
                                            "fieldName": "name"
                                        }
                                    ]
                                },
                                {
                                    "fieldName": "specification"
                                },
                                {
                                    "fieldName": "attribute"
                                },
                                {
                                    "fieldName": "unit"
                                },
                                {
                                    "fieldName": "deliveryFee"
                                },
                                {
                                    "fieldName": "installFee"
                                }
                            ]
                        },
                        {
                            "fieldName": "getGoodsOrderLinePO",
                            "fields": [
                                {
                                    "fieldName": "id"
                                },
                                {
                                    "fieldName": "taxPrice"
                                },
                                {
                                    "fieldName": "getGoodsNum"
                                },
                                {
                                    "fieldName": "price"
                                }
                            ]
                        },
                        {
                            "fieldName": "settlementCount"
                        },
                        {
                            "fieldName": "settlementTotal"
                        }
                    ],
                    "page": {
                        "curPage": 1,
                        "pageSize": 650
                    }
                },
                {
                    "fieldName": "orderSettlementAttachList",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "attachName"
                        }
                    ],
                    "page": {
                        "curPage": 1,
                        "pageSize": 650
                    }
                }
            ]
        }
    }
    response1 = requests.post(url=url2,json=data2, cookies=cookies)
    restult2 = response1.json()['res']['data']
    url3 = ("https://staging-gateway.test.lcscm.cn"
            "/zhonghai/trade-center/order-admin-center/1004708/api/trantor/action/exe")

    data3 = {
        "frontendContext": {},
        "actionKey": "order_admin_center_OrderSettlementVO_OrderSettleAction::create",
        "context": {
            "modelKey": "order_admin_center_OrderSettlementVO",
            "actionLabel": "提交",
            "record": [
                {
                    "order": restult2['order'],
                    "settlementTotal":restult2['settlementTotal'],
                    "remainedRetentionStart": int(datetime.datetime.now().timestamp() * 1000),
                    "remainedRetentionEnd": int(datetime.datetime.now().timestamp() * 1000+ 3600000000),
                    "attachment": {
                        "files": [
                            {
                                "name": "0476.jpg_wh1200.jpg",
                                "url": "//lcscm-trantor-test.oss-cn-shenzhen.aliyuncs.com/trantor/attachments/48de6848-d864-4be8-a1e9-69456d8c66ea.jpg",
                                "type": "jpg",
                                "size": 187140
                            }
                        ]
                    },
                    "settlementDesc": "111222",
                    "orderSettlementDetailList": restult2['orderSettlementDetailList'],
                    "orderSettlementAttachList": restult2['orderSettlementAttachList']
                }
            ]
        }
    }
    response2 = requests.post(url=url3,json=data3, cookies=cookies)
    return response2.json()

def settlement_confirmation(so_code):
    order1 = order(so_code)
    pur_user = order1.pur_mobile()
    cookies = order1.sup_login(mobile=pur_user['mobile'])
    so_settlement, po_settlement = order1.order_settlement()
    url1 = ("https://staging-gateway.test.lcscm.cn"
            "/zhonghai/settlement-center/settlement-admin/1004893/api/trantor/data-source")

    data1 = {
        "frontendContext": {},
        "singleResult": True,
        "targetModel": "settlement_center_OrderSettlement",
        "sourceModel": "settlement_center_OrderSettlement",
        "queryValues": {
            "id": {
                "type": "One",
                "value": so_settlement[0]['id']
            }
        },
        "dataSource": {
            "actionKey": "settlement_center_OrderSettlement_purchaser_settlement_confirm"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "order",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "code"
                        },
                        {
                            "fieldName": "title"
                        },
                        {
                            "fieldName": "contractName"
                        },
                        {
                            "fieldName": "project",
                            "fields": [
                                {
                                    "fieldName": "id"
                                },
                                {
                                    "fieldName": "name"
                                }
                            ]
                        },
                        {
                            "fieldName": "corporateCompany",
                            "fields": [
                                {
                                    "fieldName": "id"
                                },
                                {
                                    "fieldName": "companyName"
                                }
                            ]
                        },
                        {
                            "fieldName": "dealerName"
                        },
                        {
                            "fieldName": "supplierName"
                        },
                        {
                            "fieldName": "totalAmount"
                        },
                        {
                            "fieldName": "orderRule"
                        }
                    ]
                },
                {
                    "fieldName": "settlementTotal"
                },
                {
                    "fieldName": "remainedRetentionStart"
                },
                {
                    "fieldName": "remainedRetentionEnd"
                },
                {
                    "fieldName": "attachment"
                },
                {
                    "fieldName": "settlementDesc"
                },
                {
                    "fieldName": "orderSettlementDetailList",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "orderLinePO",
                            "fields": [
                                {
                                    "fieldName": "id"
                                },
                                {
                                    "fieldName": "itemCode"
                                },
                                {
                                    "fieldName": "itemName"
                                },
                                {
                                    "fieldName": "brand",
                                    "fields": [
                                        {
                                            "fieldName": "id"
                                        },
                                        {
                                            "fieldName": "name"
                                        }
                                    ]
                                },
                                {
                                    "fieldName": "specification"
                                },
                                {
                                    "fieldName": "attribute"
                                },
                                {
                                    "fieldName": "unit"
                                },
                                {
                                    "fieldName": "deliveryFee"
                                },
                                {
                                    "fieldName": "installFee"
                                }
                            ]
                        },
                        {
                            "fieldName": "getGoodsOrderLinePO",
                            "fields": [
                                {
                                    "fieldName": "id"
                                },
                                {
                                    "fieldName": "priceTax"
                                },
                                {
                                    "fieldName": "priceNoTax"
                                },
                                {
                                    "fieldName": "getGoodsNum"
                                }
                            ]
                        },
                        {
                            "fieldName": "getGoodsOrderTotal"
                        },
                        {
                            "fieldName": "settlementCount"
                        },
                        {
                            "fieldName": "settlementTotal"
                        }
                    ],
                    "page": {
                        "curPage": 1,
                        "pageSize": 650
                    }
                },
                {
                    "fieldName": "orderSettlementAttachList",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "attachName"
                        }
                    ],
                    "page": {
                        "curPage": 1,
                        "pageSize": 650
                    }
                }
            ]
        }
    }
    response1 = requests.post(url=url1,json=data1, cookies=cookies)
    print(response1.json())
    result = response1.json()['res']['data']
    url2 = ("https://staging-gateway.test.lcscm.cn"
            "/zhonghai/settlement-center/settlement-admin/1004893/api/trantor/action/exe")

    data2 = {
        "frontendContext": {},
        "actionKey": "settlement_center_OrderSettlement_OrderSettlementAction::submit",
        "context": {
            "modelKey": "settlement_center_OrderSettlement",
            "actionLabel": "确认",
            "record": [
                {
                    "id": so_settlement[0]['id']
                }
            ]
        }
    }
    response2 =requests.post(url=url2,json=data2, cookies=cookies)
    return response2.json()

def sales_check(so_code):
    order1 = order(so_code)
    enterprise = order1.sup_mobile()
    cookies = order1.sup_login(mobile='18520611771')
    receivable = order1.settlement_receivable()
    ids = []
    SourceCode = ""
    for item in receivable:
        ids.append(item['receivable_source_code']+'——'+item['receivable_source_type'])
        if SourceCode:
            SourceCode += r'\n' + item['receivable_source_code']
        else:
            SourceCode = item['receivable_source_code']
    url1 = ("https://staging-gateway.test.lcscm.cn"
            "/zhonghai/settlement-center/settlement-admin/1004893/api/trantor/action/exe")
    data1 = {
  "frontendContext": {},
  "actionKey": "settlement_center_Receivable_SalesCheckServerAction::generateSalesCheck",
  "context": {
    "env": {
      "ids": ids,
      "searchData": {
        "contractName": None,
        "contract": {
          "contractLabel": None
        },
        "purchaseName": None,
        "receivableSourceType": None,
        "receivableSourceCode": SourceCode,
        "taxRateForView": None,
        "project": {
          "name": None,
          "performanceHeadStr": None
        },
        "createdAt": None,
        "usedStatus": "UNUSED"
      }
    },
    "record": [
      {}
    ],
    "modelKey": "settlement_center_Receivable"
  }
}
    response1 = requests.post(url=url1,json=data1, cookies=cookies)
    print(response1.json())
    sales_check_id = response1.json()['res']['data']
    url2 = ("https://staging-gateway.test.lcscm.cn"
            "/zhonghai/settlement-center/settlement-admin/1004893/api/trantor/data-source")

    data2 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_Receivable",
        "sourceModel": "settlement_center_SalesCheck",
        "searchValues": {
            "receivableSourceCode": {
                "type": "One",
                "value": SourceCode
            },
            "usedStatus": {
                "type": "One",
                "value": "UNUSED"
            }
        },
        "dataSource": {
            "actionKey": "settlement_center_Receivable_receivable_create_check"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "receivableCode"
                },
                {
                    "fieldName": "purchaseName"
                },
                {
                    "fieldName": "contractName"
                },
                {
                    "fieldName": "contract",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "name"
                        },
                        {
                            "fieldName": "contractLabel"
                        }
                    ]
                },
                {
                    "fieldName": "projectName"
                },
                {
                    "fieldName": "receivableSourceType"
                },
                {
                    "fieldName": "receivableSourceCode"
                },
                {
                    "fieldName": "receivableType"
                },
                {
                    "fieldName": "paymentStatus"
                },
                {
                    "fieldName": "categoryName"
                },
                {
                    "fieldName": "itemName"
                },
                {
                    "fieldName": "project",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "name"
                        },
                        {
                            "fieldName": "performanceHeadStr"
                        }
                    ]
                },
                {
                    "fieldName": "countAmountSUM"
                },
                {
                    "fieldName": "receivableRate"
                },
                {
                    "fieldName": "taxRate"
                },
                {
                    "fieldName": "totalAmount"
                },
                {
                    "fieldName": "createdAt"
                }
            ]
        },
        "paging": {
            "no": 1,
            "size": 20
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response2 =requests.post(url=url2,json=data2, cookies=cookies)
    result2 = response2.json()
    data3 = {
        "frontendContext": {},
        "singleResult": True,
        "targetModel": "settlement_center_SalesCheck",
        "sourceModel": "settlement_center_SalesCheck",
        "queryValues": {
            "id": {
                "type": "One",
                "value": sales_check_id
            }
        },
        "dataSource": {
            "actionKey": "settlement_center_SalesCheck_lc_sales_check_edit"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "requestFundsInfoUrl"
                },
                {
                    "fieldName": "salesCheckCode"
                },
                {
                    "fieldName": "salesCheckName"
                },
                {
                    "fieldName": "contract",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "name"
                        },
                        {
                            "fieldName": "code"
                        },
                        {
                            "fieldName": "payType"
                        },
                        {
                            "fieldName": "project",
                            "fields": [
                                {
                                    "fieldName": "id"
                                },
                                {
                                    "fieldName": "name"
                                },
                                {
                                    "fieldName": "corporateCompany",
                                    "fields": [
                                        {
                                            "fieldName": "id"
                                        },
                                        {
                                            "fieldName": "companyName"
                                        },
                                        {
                                            "fieldName": "companyCode"
                                        },
                                        {
                                            "fieldName": "uscc"
                                        },
                                        {
                                            "fieldName": "mobile"
                                        },
                                        {
                                            "fieldName": "address"
                                        },
                                        {
                                            "fieldName": "invoiceInfo",
                                            "fields": [
                                                {
                                                    "fieldName": "id"
                                                },
                                                {
                                                    "fieldName": "name"
                                                },
                                                {
                                                    "fieldName": "invoiceCompany"
                                                },
                                                {
                                                    "fieldName": "invoiceBank"
                                                },
                                                {
                                                    "fieldName": "invoiceAccount"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "fieldName": "contractName"
                },
                {
                    "fieldName": "checkAcceptMonth"
                },
                {
                    "fieldName": "taxRate"
                },
                {
                    "fieldName": "createdAt"
                },
                {
                    "fieldName": "createdBy",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "username"
                        },
                        {
                            "fieldName": "nickname"
                        }
                    ]
                },
                {
                    "fieldName": "status"
                },
                {
                    "fieldName": "contractCompletedTotal"
                },
                {
                    "fieldName": "finalTotal"
                },
                {
                    "fieldName": "adjustInvoiceTotal"
                },
                {
                    "fieldName": "outlineCheck"
                },
                {
                    "fieldName": "payMethod"
                },
                {
                    "fieldName": "remark"
                },
                {
                    "fieldName": "salesCheckAdjustList",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "code"
                        },
                        {
                            "fieldName": "order",
                            "fields": [
                                {
                                    "fieldName": "id"
                                },
                                {
                                    "fieldName": "code"
                                },
                                {
                                    "fieldName": "purchaserName"
                                },
                                {
                                    "fieldName": "contractName"
                                }
                            ]
                        },
                        {
                            "fieldName": "adjustType"
                        },
                        {
                            "fieldName": "adjustTotal"
                        },
                        {
                            "fieldName": "remark"
                        }
                    ],
                    "page": {
                        "curPage": 1,
                        "pageSize": 650
                    }
                },
                {
                    "fieldName": "salesCheckAttachments",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "attachment"
                        },
                        {
                            "fieldName": "remark"
                        }
                    ],
                    "page": {
                        "curPage": 1,
                        "pageSize": 650
                    }
                },
                {
                    "fieldName": "salesCheckSystemAttachments",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "attachName"
                        }
                    ],
                    "page": {
                        "curPage": 1,
                        "pageSize": 650
                    }
                }
            ]
        }
    }
    response3 = requests.post(url=url2, json=data3, cookies=cookies)
    result3 = response3.json()['res']['data']
    data4 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_SalesCheckLine",
        "dataSource": {
            "actionKey": "settlement_center_SalesCheckLine_SalesCheckLineAdvanceMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "projectName"
                },
                {
                    "fieldName": "receivableSourceType"
                },
                {
                    "fieldName": "receivableSourceCode"
                },
                {
                    "fieldName": "order",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "code"
                        },
                        {
                            "fieldName": "title"
                        }
                    ]
                },
                {
                    "fieldName": "createdAt"
                },
                {
                    "fieldName": "payPercent"
                },
                {
                    "fieldName": "taxRate"
                },
                {
                    "fieldName": "adjustTaxRate"
                },
                {
                    "fieldName": "receivableTotalAmount"
                },
                {
                    "fieldName": "adjustTotalAmount"
                },
                {
                    "fieldName": "receivedTotalAmount"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                sales_check_id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response4= requests.post(url=url2, json=data4, cookies=cookies)
    result4 = response4.json()
    data5 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_SalesCheckLine",
        "dataSource": {
            "actionKey": "settlement_center_SalesCheckLine_SalesCheckLineAcceptMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "projectName"
                },
                {
                    "fieldName": "receivableSourceType"
                },
                {
                    "fieldName": "receivableSourceCode"
                },
                {
                    "fieldName": "order",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "code"
                        },
                        {
                            "fieldName": "title"
                        }
                    ]
                },
                {
                    "fieldName": "createdAt"
                },
                {
                    "fieldName": "payPercent"
                },
                {
                    "fieldName": "taxRate"
                },
                {
                    "fieldName": "adjustTaxRate"
                },
                {
                    "fieldName": "receivableTotalAmount"
                },
                {
                    "fieldName": "adjustTotalAmount"
                },
                {
                    "fieldName": "backTotalAmount"
                },
                {
                    "fieldName": "receivedTotalAmount"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                sales_check_id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response5 = requests.post(url=url2, json=data5, cookies=cookies)
    result5 = response5.json()
    data6 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_SalesCheckLine",
        "dataSource": {
            "actionKey": "settlement_center_SalesCheckLine_SalesCheckLineInstallMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "projectName"
                },
                {
                    "fieldName": "receivableSourceType"
                },
                {
                    "fieldName": "receivableSourceCode"
                },
                {
                    "fieldName": "order",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "code"
                        },
                        {
                            "fieldName": "title"
                        }
                    ]
                },
                {
                    "fieldName": "createdAt"
                },
                {
                    "fieldName": "payPercent"
                },
                {
                    "fieldName": "taxRate"
                },
                {
                    "fieldName": "adjustTaxRate"
                },
                {
                    "fieldName": "receivableTotalAmount"
                },
                {
                    "fieldName": "adjustTotalAmount"
                },
                {
                    "fieldName": "receivedTotalAmount"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                sales_check_id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response6 = requests.post(url=url2, json=data6, cookies=cookies)
    result6 = response6.json()
    data7 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_SalesCheckLine",
        "dataSource": {
            "actionKey": "settlement_center_SalesCheckLine_SalesCheckLineSettleMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "projectName"
                },
                {
                    "fieldName": "receivableSourceType"
                },
                {
                    "fieldName": "receivableSourceCode"
                },
                {
                    "fieldName": "order",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "code"
                        },
                        {
                            "fieldName": "title"
                        }
                    ]
                },
                {
                    "fieldName": "createdAt"
                },
                {
                    "fieldName": "payPercent"
                },
                {
                    "fieldName": "taxRate"
                },
                {
                    "fieldName": "adjustTaxRate"
                },
                {
                    "fieldName": "receivableTotalAmount"
                },
                {
                    "fieldName": "adjustTotalAmount"
                },
                {
                    "fieldName": "receivedTotalAmount"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                sales_check_id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response7 = requests.post(url=url2, json=data7, cookies=cookies)
    result7 = response7.json()
    data8 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_SalesCheckLine",
        "dataSource": {
            "actionKey": "settlement_center_SalesCheckLine_SalesCheckLineAssuranceMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "projectName"
                },
                {
                    "fieldName": "receivableSourceType"
                },
                {
                    "fieldName": "receivableSourceCode"
                },
                {
                    "fieldName": "order",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "code"
                        },
                        {
                            "fieldName": "title"
                        }
                    ]
                },
                {
                    "fieldName": "createdAt"
                },
                {
                    "fieldName": "payPercent"
                },
                {
                    "fieldName": "taxRate"
                },
                {
                    "fieldName": "adjustTaxRate"
                },
                {
                    "fieldName": "receivableTotalAmount"
                },
                {
                    "fieldName": "adjustTotalAmount"
                },
                {
                    "fieldName": "receivedTotalAmount"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                sales_check_id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response8 = requests.post(url=url2, json=data8, cookies=cookies)
    result8 = response8.json()
    data9 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_ContractAdditionalCostPO",
        "dataSource": {
            "actionKey": "settlement_center_ContractAdditionalCostPO_SalesContractPriceAdjustMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "sourceType"
                },
                {
                    "fieldName": "sourceCode"
                },
                {
                    "fieldName": "calculateAccountPeriodTimeDesc"
                },
                {
                    "fieldName": "contractAdditionCostsAmount"
                },
                {
                    "fieldName": "adjustAccountPeriodTimeDesc"
                },
                {
                    "fieldName": "adjustAmount"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                sales_check_id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response9 = requests.post(url=url2, json=data9, cookies=cookies)
    result9 = response9.json()
    data10 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_PriceAdjust",
        "dataSource": {
            "actionKey": "settlement_center_PriceAdjust_PriceAdjustSalesMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "code"
                },
                {
                    "fieldName": "purchaserName"
                },
                {
                    "fieldName": "contractName"
                },
                {
                    "fieldName": "totalAmount"
                },
                {
                    "fieldName": "remark"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                sales_check_id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response10 = requests.post(url=url2, json=data10, cookies=cookies)
    result10 = response10.json()
    data11 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_SalesCheckBill",
        "dataSource": {
            "actionKey": "settlement_center_SalesCheckBill_SalesCheckBillInvoiceMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "attributeCode"
                },
                {
                    "fieldName": "computingFormula"
                },
                {
                    "fieldName": "attributeFundName"
                },
                {
                    "fieldName": "currentTotal"
                },
                {
                    "fieldName": "remark"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                sales_check_id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response11 = requests.post(url=url2, json=data11, cookies=cookies)
    result11 = response11.json()
    data12 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_SalesCheckBill",
        "dataSource": {
            "actionKey": "settlement_center_SalesCheckBill_SalesCheckBillMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "attributeCode"
                },
                {
                    "fieldName": "computingFormula"
                },
                {
                    "fieldName": "attributeFundName"
                },
                {
                    "fieldName": "currentTotal"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                sales_check_id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response12 = requests.post(url=url2, json=data12, cookies=cookies)
    result12 = response12.json()
    data13 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_SalesCheckBill",
        "dataSource": {
            "actionKey": "settlement_center_SalesCheckBill_SalesCheckPrePayBillMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "attributeCode"
                },
                {
                    "fieldName": "computingFormula"
                },
                {
                    "fieldName": "attributeFundName"
                },
                {
                    "fieldName": "lastTotal"
                },
                {
                    "fieldName": "currentTotal"
                },
                {
                    "fieldName": "currentSum"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                sales_check_id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response13 = requests.post(url=url2, json=data13, cookies=cookies)
    result13 = response13.json()
    data14 = {
        "frontendContext": {},
        "actionKey": "settlement_center_SalesCheck_SalesCheckServerAction::submitSalesCheck",
        "context": {
            "record": [
                record
            ],
            "modelKey": "settlement_center_SalesCheck"
        }
    }
    record['requestFundsInfoUrl'] = result3['requestFundsInfoUrl']
    record['salesCheckCode'] = result3['salesCheckCode']
    record['salesCheckName'] = result3['salesCheckName']
    record['contract']['id'] = result3['contract']['id']
    record['contract']['code'] = result3['contract']['code']
    record['contract']['project']['corporateCompany']['companyCode'] = (
        result3)['contract']['project']['corporateCompany']['companyCode']
    record['contract']['project']['corporateCompany']['uscc'] = (
        result3)['contract']['project']['corporateCompany']['uscc']
    record['contract']['project']['corporateCompany']['mobile'] = (
        result3)['contract']['mobile']
    record['contract']['project']['corporateCompany']['address'] = (
        result3)['contract']['project']['corporateCompany']['address']
    record['contract']['project']['corporateCompany']['invoiceInfo']['id'] = (
        result3)['contract']['project']['corporateCompany']['invoiceInfo']['id']
    record['contract']['project']['corporateCompany']['invoiceInfo']['invoiceCompany'] = \
        (result3)['contract']['project']['corporateCompany']['invoiceInfo']['invoiceCompany']
    record['contract']['project']['corporateCompany']['invoiceInfo']['invoiceBank'] \
        = (result3)['contract']['project']['corporateCompany']['invoiceInfo']['invoiceBank']
    record['contract']['project']['corporateCompany']['invoiceInfo']['invoiceAccount'] \
        = (result3)['contract']['project']['corporateCompany']['invoiceInfo']['invoiceAccount']
    record['contract']['project']['corporateCompany']['id'] = \
        (result3)['contract']['project']['corporateCompany']['id']
    record['contractName'] = (result3)['contract']['name']
    record['checkAcceptMonth'] = result3['checkAcceptMonth']
    record['taxRate'] = result3['taxRate']
    record['createdAt'] = result3['createdAt']
    record['createdBy'] = result3['createdBy']
    record['status'] = result3['status']
    record['contractCompletedTotal'] = result3['contractCompletedTotal']
    record['finalTotal'] = result3['finalTotal']
    record['adjustInvoiceTotal'] = result3['adjustInvoiceTotal']
    record['outlineCheck'] = result3['outlineCheck']
    record['remark'] = result3['remark']
    record['id'] = result3['id']
    record['salesCheckAdjustList'] = result3['salesCheckAdjustList']
    record['salesCheckAttachments'] = result3['salesCheckAttachments']
    record['salesCheckSystemAttachments'] = result3['salesCheckSystemAttachments']
    response14 = requests.post(url=url1, json=data14, cookies=cookies)
    return response14.json()

def TestConfirmSales(so_code):
    order1 = order(so_code)
    pur_user = order1.pur_mobile()
    cookies = order1.sup_login(mobile=pur_user['mobile'])
    salecheck =order1.SaleCheck()
    sales_check_id = salecheck[0]['id']
    url1 = ("https://staging-gateway.test.lcscm.cn"
            "/zhonghai/settlement-center/settlement-center/1004893/api/trantor/data-source")
    data1 = {
        "frontendContext": {},
        "singleResult": True,
        "targetModel": "settlement_center_SalesCheck",
        "sourceModel": "settlement_center_SalesCheck",
        "queryValues": {
            "id": {
                "type": "One",
                "value": sales_check_id
            }
        },
        "dataSource": {
            "actionKey": "settlement_center_SalesCheck_sales_check_detail"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "salesCheckCode"
                },
                {
                    "fieldName": "salesCheckName"
                },
                {
                    "fieldName": "contract",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "name"
                        },
                        {
                            "fieldName": "code"
                        },
                        {
                            "fieldName": "project",
                            "fields": [
                                {
                                    "fieldName": "id"
                                },
                                {
                                    "fieldName": "name"
                                },
                                {
                                    "fieldName": "corporateCompany",
                                    "fields": [
                                        {
                                            "fieldName": "id"
                                        },
                                        {
                                            "fieldName": "companyName"
                                        },
                                        {
                                            "fieldName": "companyCode"
                                        },
                                        {
                                            "fieldName": "uscc"
                                        },
                                        {
                                            "fieldName": "mobile"
                                        },
                                        {
                                            "fieldName": "address"
                                        },
                                        {
                                            "fieldName": "invoiceInfo",
                                            "fields": [
                                                {
                                                    "fieldName": "id"
                                                },
                                                {
                                                    "fieldName": "name"
                                                },
                                                {
                                                    "fieldName": "invoiceCompany"
                                                },
                                                {
                                                    "fieldName": "invoiceBank"
                                                },
                                                {
                                                    "fieldName": "invoiceAccount"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "fieldName": "contractName"
                },
                {
                    "fieldName": "checkAcceptMonth"
                },
                {
                    "fieldName": "taxRate"
                },
                {
                    "fieldName": "createdAt"
                },
                {
                    "fieldName": "createdBy",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "username"
                        },
                        {
                            "fieldName": "nickname"
                        }
                    ]
                },
                {
                    "fieldName": "status"
                },
                {
                    "fieldName": "contractCompletedTotal"
                },
                {
                    "fieldName": "finalTotal"
                },
                {
                    "fieldName": "adjustInvoiceTotal"
                },
                {
                    "fieldName": "outlineCheck"
                },
                {
                    "fieldName": "payMethod"
                },
                {
                    "fieldName": "confirmTime"
                },
                {
                    "fieldName": "remark"
                },
                {
                    "fieldName": "returnedReason"
                },
                {
                    "fieldName": "returnedRemark"
                },
                {
                    "fieldName": "salesCheckAttachments",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "attachment"
                        },
                        {
                            "fieldName": "remark"
                        }
                    ],
                    "page": {
                        "curPage": 1,
                        "pageSize": 650
                    }
                }
            ]
        }
    }
    response1 = requests.post(url=url1,json=data1, cookies=cookies)
    result1 = response1.json()
    data2 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_SalesCheckLine",
        "dataSource": {
            "actionKey": "settlement_center_SalesCheckLine_SalesCheckLineAdvanceMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "projectName"
                },
                {
                    "fieldName": "receivableSourceType"
                },
                {
                    "fieldName": "receivableSourceCode"
                },
                {
                    "fieldName": "order",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "code"
                        },
                        {
                            "fieldName": "title"
                        }
                    ]
                },
                {
                    "fieldName": "createdAt"
                },
                {
                    "fieldName": "payPercent"
                },
                {
                    "fieldName": "taxRate"
                },
                {
                    "fieldName": "adjustTaxRate"
                },
                {
                    "fieldName": "receivableTotalAmount"
                },
                {
                    "fieldName": "adjustTotalAmount"
                },
                {
                    "fieldName": "receivedTotalAmount"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                sales_check_id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response2 = requests.post(url=url1, json=data2, cookies=cookies)
    result2= response2.json()
    data3 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_SalesCheckLine",
        "dataSource": {
            "actionKey": "settlement_center_SalesCheckLine_SalesCheckLineAcceptMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "projectName"
                },
                {
                    "fieldName": "receivableSourceType"
                },
                {
                    "fieldName": "receivableSourceCode"
                },
                {
                    "fieldName": "order",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "code"
                        },
                        {
                            "fieldName": "title"
                        }
                    ]
                },
                {
                    "fieldName": "createdAt"
                },
                {
                    "fieldName": "payPercent"
                },
                {
                    "fieldName": "taxRate"
                },
                {
                    "fieldName": "adjustTaxRate"
                },
                {
                    "fieldName": "receivableTotalAmount"
                },
                {
                    "fieldName": "adjustTotalAmount"
                },
                {
                    "fieldName": "backTotalAmount"
                },
                {
                    "fieldName": "receivedTotalAmount"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                sales_check_id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response3 = requests.post(url=url1, json=data3, cookies=cookies)
    result3 = response3.json()
    data4 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_SalesCheckLine",
        "dataSource": {
            "actionKey": "settlement_center_SalesCheckLine_SalesCheckLineInstallMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "projectName"
                },
                {
                    "fieldName": "receivableSourceType"
                },
                {
                    "fieldName": "receivableSourceCode"
                },
                {
                    "fieldName": "order",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "code"
                        },
                        {
                            "fieldName": "title"
                        }
                    ]
                },
                {
                    "fieldName": "createdAt"
                },
                {
                    "fieldName": "payPercent"
                },
                {
                    "fieldName": "taxRate"
                },
                {
                    "fieldName": "adjustTaxRate"
                },
                {
                    "fieldName": "receivableTotalAmount"
                },
                {
                    "fieldName": "adjustTotalAmount"
                },
                {
                    "fieldName": "receivedTotalAmount"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                sales_check_id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response4 = requests.post(url=url1, json=data4, cookies=cookies)
    result4 = response4.json()
    data5 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_SalesCheckLine",
        "dataSource": {
            "actionKey": "settlement_center_SalesCheckLine_SalesCheckLineSettleMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "projectName"
                },
                {
                    "fieldName": "receivableSourceType"
                },
                {
                    "fieldName": "receivableSourceCode"
                },
                {
                    "fieldName": "order",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "code"
                        },
                        {
                            "fieldName": "title"
                        }
                    ]
                },
                {
                    "fieldName": "createdAt"
                },
                {
                    "fieldName": "payPercent"
                },
                {
                    "fieldName": "taxRate"
                },
                {
                    "fieldName": "adjustTaxRate"
                },
                {
                    "fieldName": "receivableTotalAmount"
                },
                {
                    "fieldName": "adjustTotalAmount"
                },
                {
                    "fieldName": "receivedTotalAmount"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                sales_check_id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response5 = requests.post(url=url1, json=data5, cookies=cookies)
    result5 = response5.json()
    data6 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_SalesCheckLine",
        "dataSource": {
            "actionKey": "settlement_center_SalesCheckLine_SalesCheckLineAssuranceMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "projectName"
                },
                {
                    "fieldName": "receivableSourceType"
                },
                {
                    "fieldName": "receivableSourceCode"
                },
                {
                    "fieldName": "order",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "code"
                        },
                        {
                            "fieldName": "title"
                        }
                    ]
                },
                {
                    "fieldName": "createdAt"
                },
                {
                    "fieldName": "payPercent"
                },
                {
                    "fieldName": "taxRate"
                },
                {
                    "fieldName": "adjustTaxRate"
                },
                {
                    "fieldName": "receivableTotalAmount"
                },
                {
                    "fieldName": "adjustTotalAmount"
                },
                {
                    "fieldName": "receivedTotalAmount"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                sales_check_id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response6 = requests.post(url=url1, json=data6, cookies=cookies)
    result6 = response6.json()
    data7 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_SalesCheckBill",
        "dataSource": {
            "actionKey": "settlement_center_SalesCheckBill_SalesCheckBillInvoiceMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "attributeCode"
                },
                {
                    "fieldName": "computingFormula"
                },
                {
                    "fieldName": "attributeFundName"
                },
                {
                    "fieldName": "currentTotal"
                },
                {
                    "fieldName": "remark"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                sales_check_id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response7 = requests.post(url=url1, json=data7, cookies=cookies)
    result7 = response7.json()
    data8 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_SalesCheckBill",
        "dataSource": {
            "actionKey": "settlement_center_SalesCheckBill_SalesCheckBillMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "attributeCode"
                },
                {
                    "fieldName": "computingFormula"
                },
                {
                    "fieldName": "attributeFundName"
                },
                {
                    "fieldName": "currentTotal"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                sales_check_id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response8 = requests.post(url=url1, json=data8, cookies=cookies)
    result8 = response8.json()
    data9 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_SalesCheckBill",
        "dataSource": {
            "actionKey": "settlement_center_SalesCheckBill_SalesCheckPrePayBillMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "attributeCode"
                },
                {
                    "fieldName": "computingFormula"
                },
                {
                    "fieldName": "attributeFundName"
                },
                {
                    "fieldName": "lastTotal"
                },
                {
                    "fieldName": "currentTotal"
                },
                {
                    "fieldName": "currentSum"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                sales_check_id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response9 = requests.post(url=url1, json=data9, cookies=cookies)
    result9 = response9.json()
    data10 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_SalesCheckSystemAttachment",
        "dataSource": {
            "actionKey": "settlement_center_SalesCheckSystemAttachment_SalesCheckSystemAttachmentMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "attachName"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                sales_check_id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response10 = requests.post(url=url1, json=data10, cookies=cookies)
    result10 = response10.json()
    url2 = ("https://staging-gateway.test.lcscm.cn"
            "/zhonghai/settlement-center/settlement-admin/1004893/api/trantor/action/exe")
    data11 = {
        "frontendContext": {},
        "actionKey": "settlement_center_SalesCheck_SalesCheckServerAction::updateStatus",
        "context": {
            "modelKey": "settlement_center_SalesCheck",
            "env": {
                "mode": "confirm"
            },
            "actionLabel": "确认",
            "record": [
                {
                    "id": sales_check_id
                }
            ]
        }
    }
    response11 = requests.post(url=url2, json=data11, cookies=cookies)
    return response11.json()

def generate_payment(so_code):
    order1 = order(so_code)
    cookies = order1.sup_login(mobile='18520611771')
    salecheck = order1.SaleCheck()
    sales_check_id = salecheck[0]['id']
    url1 = ("https://staging-gateway.test.lcscm.cn"
           "/zhonghai/settlement-center/settlement-admin/1004893/api/trantor/action/exe")
    data1 = {
        "frontendContext": {},
        "actionKey": "settlement_center_SalesCheck_SalesRequestReceiveAction::create",
        "context": {
            "modelKey": "settlement_center_SalesCheck",
            "actionLabel": "生成收款单",
            "record": [
                {
                    "id": sales_check_id
                }
            ]
        }
    }
    response1 = requests.post(url=url1, json=data1, cookies=cookies)
    return  response1.json()

def purchase_settlement(so_code):
    order1 = order(so_code)
    cookies = order1.sup_login(mobile='18520611771')
    payable, payable1 = order1.settlement_payable()
    ids = []
    for i in range(len(payable1)):
        ids.append(payable1[i]['payable_source_code'] + '——' + payable1[i]['payable_source_type'])
    url1 = ("https://staging-gateway.test.lcscm.cn"
            "/zhonghai/settlement-center/settlement-admin/1004893/api/trantor/action/exe")
    data1 = {
        "frontendContext": {},
        "actionKey": "settlement_center_PayableMergePO_PurchaseCheckAction::generateCheck",
        "context": {
            "env": {
                "ids": ids,
                "searchData": {
                    "payableSourceType": None,
                    "payableSourceCode": None,
                    "supplier": {
                        "code": None,
                        "name": None
                    },
                    "contract": {
                        "code": None,
                        "name": None
                    },
                    "payableMergeStatus": None,
                    "protocol": {
                        "name": None
                    },
                    "taxRateStr": None,
                    "project": {
                        "name": None
                    },
                    "createdAt": None
                }
            },
            "record": [
                {}
            ],
            "modelKey": "settlement_center_PayableMergePO"
        }
    }
    response1 = requests.post(url=url1, json=data1, cookies=cookies)
    result1 = response1.json()
    print(result1)
    id = result1['res']['data']
    url2 = ("https://staging-gateway.test.lcscm.cn"
            "/zhonghai/settlement-center/settlement-admin/1004893/api/trantor/data-source")

    data2 = {
        "frontendContext": {},
        "singleResult": True,
        "targetModel": "settlement_center_PurchaseCheck",
        "sourceModel": "settlement_center_PurchaseCheck",
        "queryValues": {
            "id": {
                "type": "One",
                "value": id
            }
        },
        "dataSource": {
            "actionKey": "settlement_center_PurchaseCheck_lc_edit"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "purchaseCheckCode"
                },
                {
                    "fieldName": "purchaseCheckName"
                },
                {
                    "fieldName": "contract",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "name"
                        },
                        {
                            "fieldName": "code"
                        },
                        {
                            "fieldName": "payType"
                        }
                    ]
                },
                {
                    "fieldName": "contractName"
                },
                {
                    "fieldName": "protocolName"
                },
                {
                    "fieldName": "protocol",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "name"
                        },
                        {
                            "fieldName": "code"
                        }
                    ]
                },
                {
                    "fieldName": "checkAcceptMonth"
                },
                {
                    "fieldName": "taxRate"
                },
                {
                    "fieldName": "createdAt"
                },
                {
                    "fieldName": "createdBy",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "username"
                        },
                        {
                            "fieldName": "nickname"
                        }
                    ]
                },
                {
                    "fieldName": "status"
                },
                {
                    "fieldName": "contractCompletedTotal"
                },
                {
                    "fieldName": "finalTotal"
                },
                {
                    "fieldName": "adjustInvoiceTotal"
                },
                {
                    "fieldName": "payMethod"
                },
                {
                    "fieldName": "remark"
                },
                {
                    "fieldName": "supplierName"
                },
                {
                    "fieldName": "supplierCode"
                },
                {
                    "fieldName": "bank"
                },
                {
                    "fieldName": "accountName"
                },
                {
                    "fieldName": "bankNo"
                },
                {
                    "fieldName": "bankAccount"
                },
                {
                    "fieldName": "supplier",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "name"
                        },
                        {
                            "fieldName": "code"
                        },
                        {
                            "fieldName": "bankType"
                        },
                        {
                            "fieldName": "bankName"
                        },
                        {
                            "fieldName": "cardNo"
                        }
                    ]
                },
                {
                    "fieldName": "purchaseCheckAdjustList",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "code"
                        },
                        {
                            "fieldName": "order",
                            "fields": [
                                {
                                    "fieldName": "id"
                                },
                                {
                                    "fieldName": "code"
                                },
                                {
                                    "fieldName": "supplierName"
                                },
                                {
                                    "fieldName": "contractName"
                                }
                            ]
                        },
                        {
                            "fieldName": "adjustType"
                        },
                        {
                            "fieldName": "adjustTotal"
                        },
                        {
                            "fieldName": "remark"
                        }
                    ],
                    "page": {
                        "curPage": 1,
                        "pageSize": 650
                    }
                },
                {
                    "fieldName": "purchaseCheckAttachmentList",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "attachment"
                        },
                        {
                            "fieldName": "remark"
                        }
                    ],
                    "page": {
                        "curPage": 1,
                        "pageSize": 650
                    }
                },
                {
                    "fieldName": "purchaseCheckSystemAttachments",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "attachName"
                        }
                    ],
                    "page": {
                        "curPage": 1,
                        "pageSize": 650
                    }
                }
            ]
        }
    }
    response2 = requests.post(url=url2, json=data2, cookies=cookies)
    result2 = response2.json()
    print(result2)
    data3 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_PurchaseCheckLine",
        "dataSource": {
            "actionKey": "settlement_center_PurchaseCheckLine_PurchaseCheckLineAdvanceMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "projectName"
                },
                {
                    "fieldName": "payableSourceType"
                },
                {
                    "fieldName": "payableSourceCode"
                },
                {
                    "fieldName": "payableSourceTotal"
                },
                {
                    "fieldName": "createdAt"
                },
                {
                    "fieldName": "payPercent"
                },
                {
                    "fieldName": "taxRate"
                },
                {
                    "fieldName": "adjustTaxRate"
                },
                {
                    "fieldName": "payableTotalAmount"
                },
                {
                    "fieldName": "adjustTotalAmount"
                },
                {
                    "fieldName": "paymentTotal"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response3 = requests.post(url=url2, json=data3, cookies=cookies)
    result3 = response3.json()
    print(result3)
    data4 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_PurchaseCheckLine",
        "dataSource": {
            "actionKey": "settlement_center_PurchaseCheckLine_PurchaseCheckLineAcceptMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "projectName"
                },
                {
                    "fieldName": "payableSourceType"
                },
                {
                    "fieldName": "payableSourceCode"
                },
                {
                    "fieldName": "payableSourceTotal"
                },
                {
                    "fieldName": "createdAt"
                },
                {
                    "fieldName": "payPercent"
                },
                {
                    "fieldName": "taxRate"
                },
                {
                    "fieldName": "adjustTaxRate"
                },
                {
                    "fieldName": "payableTotalAmount"
                },
                {
                    "fieldName": "adjustTotalAmount"
                },
                {
                    "fieldName": "returnBalance"
                },
                {
                    "fieldName": "paymentTotal"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response4 = requests.post(url=url2, json=data4, cookies=cookies)
    result4 = response4.json()
    print(result4)
    data5 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_PurchaseCheckLine",
        "dataSource": {
            "actionKey": "settlement_center_PurchaseCheckLine_PurchaseCheckLineInstallMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "projectName"
                },
                {
                    "fieldName": "payableSourceType"
                },
                {
                    "fieldName": "payableSourceCode"
                },
                {
                    "fieldName": "payableSourceTotal"
                },
                {
                    "fieldName": "createdAt"
                },
                {
                    "fieldName": "payPercent"
                },
                {
                    "fieldName": "taxRate"
                },
                {
                    "fieldName": "adjustTaxRate"
                },
                {
                    "fieldName": "payableTotalAmount"
                },
                {
                    "fieldName": "adjustTotalAmount"
                },
                {
                    "fieldName": "paymentTotal"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response5 = requests.post(url=url2, json=data5, cookies=cookies)
    result5 = response5.json()
    print(result5)
    data6 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_PurchaseCheckLine",
        "dataSource": {
            "actionKey": "settlement_center_PurchaseCheckLine_PurchaseCheckLineSettleMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "projectName"
                },
                {
                    "fieldName": "payableSourceType"
                },
                {
                    "fieldName": "payableSourceCode"
                },
                {
                    "fieldName": "payableSourceTotal"
                },
                {
                    "fieldName": "createdAt"
                },
                {
                    "fieldName": "payPercent"
                },
                {
                    "fieldName": "taxRate"
                },
                {
                    "fieldName": "adjustTaxRate"
                },
                {
                    "fieldName": "payableTotalAmount"
                },
                {
                    "fieldName": "adjustTotalAmount"
                },
                {
                    "fieldName": "paymentTotal"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response6 = requests.post(url=url2, json=data6, cookies=cookies)
    result6 = response6.json()
    print(result6)
    data7 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_PurchaseCheckLine",
        "dataSource": {
            "actionKey": "settlement_center_PurchaseCheckLine_PurchaseCheckLineAssuranceMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "projectName"
                },
                {
                    "fieldName": "payableSourceType"
                },
                {
                    "fieldName": "payableSourceCode"
                },
                {
                    "fieldName": "payableSourceTotal"
                },
                {
                    "fieldName": "createdAt"
                },
                {
                    "fieldName": "payPercent"
                },
                {
                    "fieldName": "taxRate"
                },
                {
                    "fieldName": "adjustTaxRate"
                },
                {
                    "fieldName": "payableTotalAmount"
                },
                {
                    "fieldName": "adjustTotalAmount"
                },
                {
                    "fieldName": "paymentTotal"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response7 = requests.post(url=url2, json=data7, cookies=cookies)
    result7 = response7.json()
    print(result7)
    data8 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_ContractAdditionalCostPO",
        "dataSource": {
            "actionKey": "settlement_center_ContractAdditionalCostPO_PurchaseContractPriceAdjustMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "sourceType"
                },
                {
                    "fieldName": "sourceCode"
                },
                {
                    "fieldName": "calculateAccountPeriodTimeDesc"
                },
                {
                    "fieldName": "contractAdditionCostsAmount"
                },
                {
                    "fieldName": "adjustAccountPeriodTimeDesc"
                },
                {
                    "fieldName": "adjustAmount"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response8 = requests.post(url=url2, json=data8, cookies=cookies)
    result8 = response8.json()
    print(result8)
    data9 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_PriceAdjust",
        "dataSource": {
            "actionKey": "settlement_center_PriceAdjust_PriceAdjustPurchaseMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "code"
                },
                {
                    "fieldName": "supplierName"
                },
                {
                    "fieldName": "purchaseContractName"
                },
                {
                    "fieldName": "totalAmount"
                },
                {
                    "fieldName": "remark"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response9 = requests.post(url=url2, json=data9, cookies=cookies)
    result9 = response9.json()
    print(result9)
    data10 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_PurchaseCheckBill",
        "dataSource": {
            "actionKey": "settlement_center_PurchaseCheckBill_PurchaseCheckBillInvoiceMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "attributeCode"
                },
                {
                    "fieldName": "computingFormula"
                },
                {
                    "fieldName": "attributeFundName"
                },
                {
                    "fieldName": "currentTotal"
                },
                {
                    "fieldName": "remark"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response10 = requests.post(url=url2, json=data10, cookies=cookies)
    result10 = response10.json()
    print(result10)
    data11 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_PurchaseCheckBill",
        "dataSource": {
            "actionKey": "settlement_center_PurchaseCheckBill_PurchaseCheckBillMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "attributeCode"
                },
                {
                    "fieldName": "computingFormula"
                },
                {
                    "fieldName": "attributeFundName"
                },
                {
                    "fieldName": "currentTotal"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response11 = requests.post(url=url2, json=data11, cookies=cookies)
    result11 = response11.json()
    print(result11)
    data12 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_PurchaseCheckBill",
        "dataSource": {
            "actionKey": "settlement_center_PurchaseCheckBill_PurchaseCheckPrePayBillMultiAction",
            "type": "Action"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "attributeCode"
                },
                {
                    "fieldName": "computingFormula"
                },
                {
                    "fieldName": "attributeFundName"
                },
                {
                    "fieldName": "lastTotal"
                },
                {
                    "fieldName": "currentTotal"
                },
                {
                    "fieldName": "currentSum"
                },
                {
                    "fieldName": "attributeType"
                }
            ]
        },
        "related": {
            "field": "id",
            "recordIds": [
                id
            ]
        },
        "paging": {
            "no": 1,
            "size": 10
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response12 = requests.post(url=url2, json=data12, cookies=cookies)
    result12 = response12.json()
    print(result12)
    data13 = {
        "frontendContext": {},
        "actionKey": "settlement_center_PurchaseCheck_PurchaseCheckAction::submitPurchaseCheck",
        "context": {
            "record": [
                {
                    "purchaseCheckCode": result2['res']['data']['purchaseCheckCode'],
                    "purchaseCheckName": result2['res']['data']['purchaseCheckName'],
                    "contract": {
                        "id": result2['res']['data']['contract']['id'],
                        "code": result2['res']['data']['contract']['code']
                    },
                    "contractName": result2['res']['data']['contractName'],
                    "protocolName": None,
                    "protocol": {
                        "id": None,
                        "code": None
                    },
                    "checkAcceptMonth": int(time.time()) * 1000,
                    "taxRate": result2['res']['data']['taxRate'],
                    "createdAt": result2['res']['data']['createdAt'],
                    "createdBy": {
                        "id": result2['res']['data']['createdBy']['id'],
                        "nickname": result2['res']['data']['createdBy']['nickname']
                    },
                    "status": result2['res']['data']['status'],
                    "contractCompletedTotal": result2['res']['data']['contractCompletedTotal'],
                    "finalTotal": result2['res']['data']['finalTotal'],
                    "adjustInvoiceTotal": result2['res']['data']['adjustInvoiceTotal'],
                    "payMethod": None,
                    "remark": result2['res']['data']['remark'],
                    "id": result2['res']['data']['id'],
                    "supplier": result2['res']['data']['supplier'],
                    "bankNo": None,
                    "purchaseCheckAdjustList": result2['res']['data']['purchaseCheckAdjustList'],
                    "purchaseCheckAttachmentList": result2['res']['data']['purchaseCheckAttachmentList'],
                    "purchaseCheckSystemAttachments": result2['res']['data']['purchaseCheckSystemAttachments']
                }
            ],
            "env": {},
            "modelKey": "settlement_center_PurchaseCheck"
        }
    }
    response13 = requests.post(url=url1, json=data13, cookies=cookies)
    return  response13.json()










if __name__ == '__main__':
    # goods_rejected('SO20240222000007001')
    # print(reverseItem('SO20240222000007001','SO20240222000007001002'))
    print(order('SO20240415000001').SupplierAcceptanceOrder())












