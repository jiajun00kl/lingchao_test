url1 =("https://staging-gateway.test.lcscm.cn"
       "/zhonghai/settlement-center/settlement-admin/1004893/api/trantor/data-source")

data1 = {
    "frontendContext": {},
    "singleResult": True,
    "targetModel": "settlement_center_OrderSettlement",
    "sourceModel": "settlement_center_OrderSettlement",
    "queryValues": {
        "id": {
            "type": "One",
            "value": 116004
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

url2= ("https://staging-gateway.test.lcscm.cn"
       "/zhonghai/settlement-center/settlement-admin/1004893/api/trantor/action/exe")

data2 = {
    "frontendContext": {},
    "actionKey": "settlement_center_OrderSettlement_OrderSettlementAction::submit",
    "context": {
        "modelKey": "settlement_center_OrderSettlement",
        "actionLabel": "确认",
        "record": [
            {
                "id": 116004
            }
        ]
    }
}