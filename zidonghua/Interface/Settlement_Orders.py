url1 =("https://staging-gateway.test.lcscm.cn"
      "/zhonghai/trade-center/order-admin-center/1004708/api/trantor/action/exe")

data1 = {
    "frontendContext": {},
    "actionKey": "order_admin_center_OrderSettlementVO_OrderSettleAction::toCreateCheck",
    "context": {
        "record": [
            {
                "id": 244171
            }
        ],
        "modelKey": "order_admin_center_OrderSettlementVO"
    }
}

url2 =("https://staging-gateway.test.lcscm.cn"
       "/zhonghai/trade-center/order-admin-center/1004708/api/trantor/data-source")

data2 ={
    "frontendContext": {},
    "singleResult": True,
    "targetModel": "order_admin_center_OrderSettlementVO",
    "sourceModel": "order_admin_center_OrderSettlementVO",
    "queryValues": {
        "id": {
            "type": "One",
            "value": 244171
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

url3 =("https://staging-gateway.test.lcscm.cn"
       "/zhonghai/trade-center/order-admin-center/1004708/api/trantor/action/exe")

data3 = {
    "frontendContext": {},
    "actionKey": "order_admin_center_OrderSettlementVO_OrderSettleAction::create",
    "context": {
        "modelKey": "order_admin_center_OrderSettlementVO",
        "actionLabel": "提交",
        "record": [
            {
                "order": {
                    "id": 244153,
                    "code": "PO20240110000004",
                    "title": "20240110湖北家家有限公司test1采购项目立邦",
                    "contractName": "哈哈-立邦-合同01号",
                    "project": {
                        "id": 100023,
                        "name": "test1采购项目"
                    },
                    "purchaserName": "湖北家家有限公司",
                    "totalAmount": 5.65
                },
                "settlementTotal": 5.65,
                "remainedRetentionStart": 1704816000000,
                "remainedRetentionEnd": 1706630400000,
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
                "orderSettlementDetailList": [
                    {
                        "orderLinePO": {
                            "installFee": 0,
                            "saleRadix": 100,
                            "itemCode": "210204601003308",
                            "createdAt": 1704867316000,
                            "itemName": "立邦 铸铝道钉",
                            "isDeleted": False,
                            "id": 246205,
                            "brand": {
                                "code": "BD20230710000001",
                                "updatedBy": {
                                    "id": 10
                                },
                                "createdAt": 1688973526000,
                                "isDeleted": False,
                                "createdBy": {
                                    "id": 2001
                                },
                                "name": "立邦",
                                "digitalSyncStatus": "default",
                                "logo": "//lcscm-trantor-test.oss-cn-shenzhen.aliyuncs.com/trantor/attachments/8df10ec2-4c29-4fb7-a2f4-6d8082228987.jpg",
                                "id": 50001,
                                "shortName": "lb",
                                "updatedAt": 1703492952000
                            },
                            "costPriceTax": 0,
                            "updatedAt": 1704878990000,
                            "purchaserMaterialCode": "",
                            "costPriceNoTax": 0,
                            "taxNotAmount": 0,
                            "updatedBy": {
                                "id": 132016
                            },
                            "colorNum": "",
                            "toDeliveryNum": 0,
                            "costPrice": 0,
                            "specification": "立邦地坪漆材料 ：ZF-F951-防静电的环保地坪漆",
                            "purDiscountRate": 1,
                            "taxRateAmount": 0,
                            "taxRate": 13,
                            "unit": "个",
                            "deliveryFee": 0,
                            "createdBy": {
                                "id": 132016
                            },
                            "priceNoTax": 0,
                            "taxPrice": 5.65,
                            "purchaseNum": 1,
                            "priceTax": 0,
                            "taxAmount": 5.65,
                            "toGetGoodsNum": 0,
                            "defaultRadix": 100
                        },
                        "settlementCount": 1,
                        "settlementTotal": 5.65,
                        "getGoodsOrderLinePO": {
                            "itemCode": "210204601003308",
                            "price": 5.65,
                            "id": 224169,
                            "getGoodsNum": 1,
                            "taxRate": 13,
                            "priceNoTax": 0,
                            "taxPrice": 5.65,
                            "priceTax": 5.65
                        }
                    }
                ],
                "orderSettlementAttachList": [
                    {
                        "attachType": "ACCEPTANCE",
                        "attachName": "验收单汇总",
                        "id": 172011
                    },
                    {
                        "attachType": "ACCEPTANCE_DETAIL",
                        "attachName": "验收单明细",
                        "id": 172012
                    },
                    {
                        "attachType": "REVERSE",
                        "attachName": "退货单汇总",
                        "id": 172013
                    },
                    {
                        "attachType": "REVERSE_DETAIL",
                        "attachName": "退货单明细",
                        "id": 172014
                    },
                    {
                        "attachType": "GOODS",
                        "attachName": "物资管理台账",
                        "id": 172015
                    }
                ]
            }
        ]
    }
}
