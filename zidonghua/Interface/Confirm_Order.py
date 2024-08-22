url1 =("https://staging-gateway.test.lcscm.cn"
       "/zhonghai/trade-center/order-admin-center/1004708/api/trantor/data-source")

url2 =("https://staging-gateway.test.lcscm.cn"
      "/zhonghai/trade-center/order-admin-center/1004708/api/trantor/action/exe")

data1 = {
    "frontendContext": {},
    "singleResult": False,
    "targetModel": "order_GetGoodsOrderPO",
    "sourceModel": "order_GetGoodsOrderPO",
    "searchValues": {
        "code": {
            "type": "One",
            "value": "PO20240103002001001"
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

data2 = {
    "frontendContext": {},
    "actionKey": "order_GetGoodsOrderPO_GetGoodsServerAction::goodsOrderConfirm",
    "context": {
        "record": 'record',
        "modelKey": "order_GetGoodsOrderPO"
    }
}