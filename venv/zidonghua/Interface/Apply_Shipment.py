url1 = ("https://staging-gateway.test.lcscm.cn"
        "/zhonghai/trade-center/order-admin-center/1004708/api/trantor/data-source")

url2 =("https://staging-gateway.test.lcscm.cn"
       "/zhonghai/trade-center/order-admin-center/1004708/api/trantor/action/exe")
data1 ={
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