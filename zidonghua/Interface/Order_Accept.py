url1 =("https://staging-gateway.test.lcscm.cn"
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

data2 = {
    "frontendContext": {},
    "actionKey": "order_AcceptanceOrderPO_AcceptanceOrderServerAction::checkAcceptanceInputError",
    "context": {
        "modelKey": "order_AcceptanceOrderPO",
        "env": {
            "datas": {
                "context": None
            }
        },
        "record": [
            {
                "context": None
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
            "datas": None
        }
    }
}
