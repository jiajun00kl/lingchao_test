url1 = ('https://staging-gateway.test.lcscm.cn/zhonghai/trade-center'
       '/order-admin-center/1004708/api/trantor/data-source')
url2=("https://staging-gateway.test.lcscm.cn"
      "/zhonghai/trade-center/order-admin-center/1004708/api/trantor/action/exe?")

data1 = {
    "frontendContext": {},
    "singleResult": True,
    "targetModel": "order_GetGoodsOrderPO",
    "sourceModel": "order_OrderPO",
    "queryValues": {
        "id": {
            "type": "One",
            "value": 234057
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

data2 ={
    "frontendContext": {},
    "actionKey": "order_GetGoodsOrderPO_OrderGoodsAction::submitGoodsOrder",
    "context": {
        "modelKey": "order_GetGoodsOrderPO",
        "actionLabel": "提交",
        "record": [
            {
                "code": None,
                "orderCode": "SO20240103002001",
                "createdAt": None,
                "readyToShipLetter": None,
                "expectedArrivalDate": 1704297600000,
                "siteReceivingContact": "test1熊",
                "siteReceivingContactPhone": "13500000011",
                "orderAttachment": {
                    "files": []
                },
                "getGoodsOrderAttachment": None,
                "remark": None,
                "order": {
                    "takeOrderDate": 1704353566000,
                    "type": "SO",
                    "invoiceRemark": "444444444444444444444444444444444444444444444444444",
                    "performanceType": "BRAND_SUPPLIER",
                    "payType": "account",
                    "brandOwnerName": "深圳哈哈有限公司",
                    "supplier": {
                        "id": 138017,
                        "website": "11",
                        "name": "深圳哈哈有限公司"
                    },
                    "isTranslation": False,
                    "id": 242001,
                    "isAgentOrder": "NO",
                    "receiveAddress": "北京北京市北京市1111111111111",
                    "deliveryTotalAmount": 0,
                    "buyer": {
                        "mobile": "18878934566",
                        "nickname": "vic",
                        "id": 124057
                    },
                    "orderLockType": "GET_GOODS_ORDER",
                    "orderCreateType": "order_company",
                    "status": "RECEIVED",
                    "needInstall": False,
                    "settleStatus": "NOT_SETTLEMENT",
                    "isQuickGetOrder": False,
                    "corporateCompanyName": "湖北家家有限公司",
                    "projectReceiverPhone": "18178952878",
                    "isDeleted": False,
                    "installTotalAmount": 0,
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
                        "city": {
                            "id": "110100",
                            "name": "北京市"
                        },
                        "detail": "1111111111111",
                        "province": {
                            "id": "110000",
                            "name": "北京"
                        },
                        "region": {
                            "id": "110102",
                            "name": "西城区"
                        }
                    },
                    "copySignStatus": "SIGNING",
                    "orderLinePOList": [
                        {
                            "installFee": 0,
                            "saleRadix": 100,
                            "itemCode": "210204601003306",
                            "itemName": "立邦 广角镜",
                            "id": 244001,
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
                            "costPriceTax": 54.24,
                            "costPriceNoTax": 0,
                            "item": {
                                "itemCode": "210204601003306",
                                "type": 1,
                                "isSpecialItem": 0,
                                "createdAt": 1678672512000,
                                "sellerId": 138017,
                                "digitalSyncStatus": "default",
                                "minOrderNumber": 1,
                                "id": 210204601003306,
                                "updatedAt": 1692606190000,
                                "brandName": "立邦",
                                "updatedBy": {
                                    "id": 36068
                                },
                                "priceAdjustYn": 0,
                                "version": 0,
                                "unit": "个",
                                "purchaserId": 0,
                                "invoiceCategoryName": "立邦",
                                "brandId": 50001,
                                "name": "立邦 广角镜",
                                "leadTrendYn": 1,
                                "preOverdueDate": 1703987760000,
                                "shortName": "立邦",
                                "status": 1,
                                "sellerName": "深圳哈哈有限公司",
                                "specialYn": 0,
                                "isDeleted": False,
                                "contractName": "哈哈-立邦-合同01号",
                                "quickOrder": 1,
                                "showVirtualPrice": "NOT",
                                "overdueDate": 1725012300000,
                                "invoiceCategoryCode": "107020801",
                                "platformAuditStatus": "AGREE",
                                "isSyncDigital": 0,
                                "specification": "立邦地坪漆材料 ：ZF-F951-防静电的环保地坪漆",
                                "mainImage": "http://lcscm-trantor.oss-cn-shenzhen.aliyuncs.com/images/manage/2046/46a23c6a-07bf-45fc-8d23-078dab8a0855/06a02908-5065-4369-b2e0-58325b5ff515.png",
                                "supplyCycle": 10,
                                "bitTag": 0,
                                "md5Info": "948ecbc72bbbfb41494f23d109cb211b",
                                "createdBy": {
                                    "id": 24040
                                },
                                "tenantId": 1,
                                "itemSource": "深圳哈哈有限公司",
                                "extraJson": "{\"taxRate\":\"13\",\"mainImage\":\"{\\\"files\\\":[{\\\"name\\\":\\\"广角镜封面图 1\\\",\\\"type\\\":\\\"jpg\\\",\\\"url\\\":\\\"http://lcscm-trantor.oss-cn-shenzhen.aliyuncs.com/images/manage/2046/46a23c6a-07bf-45fc-8d23-078dab8a0855/06a02908-5065-4369-b2e0-58325b5ff515.png\\\"},{\\\"name\\\":\\\"广角镜封面图 2\\\",\\\"type\\\":\\\"jpg\\\",\\\"url\\\":\\\"http://lcscm-trantor.oss-cn-shenzhen.aliyuncs.com/images/manage/2046/46a23c6a-07bf-45fc-8d23-078dab8a0855/7a3f9bb5-f526-4bf5-826c-915aaa4bf2b6.png\\\"},{\\\"name\\\":\\\"广角镜封面图 3\\\",\\\"type\\\":\\\"jpg\\\",\\\"url\\\":\\\"http://lcscm-trantor.oss-cn-shenzhen.aliyuncs.com/images/manage/2046/46a23c6a-07bf-45fc-8d23-078dab8a0855/784b4626-e468-42ab-b707-1d20d327a964.jpg\\\"}]}\",\"supplyPurchaser\":\"[0]\",\"categoryList\":\"[4797,4804,4839,4949,5147]\"}",
                                "businessType": 1,
                                "digitalStatus": -1,
                                "contractCode": "f0cdc16c581d1",
                                "categoryId": 5147,
                                "overdueStatus": "UNEXPIRED",
                                "itemLevel": "S",
                                "extra": {
                                    "taxRate": "13",
                                    "mainImage": "{\"files\":[{\"name\":\"广角镜封面图 1\",\"type\":\"jpg\",\"url\":\"http://lcscm-trantor.oss-cn-shenzhen.aliyuncs.com/images/manage/2046/46a23c6a-07bf-45fc-8d23-078dab8a0855/06a02908-5065-4369-b2e0-58325b5ff515.png\"},{\"name\":\"广角镜封面图 2\",\"type\":\"jpg\",\"url\":\"http://lcscm-trantor.oss-cn-shenzhen.aliyuncs.com/images/manage/2046/46a23c6a-07bf-45fc-8d23-078dab8a0855/7a3f9bb5-f526-4bf5-826c-915aaa4bf2b6.png\"},{\"name\":\"广角镜封面图 3\",\"type\":\"jpg\",\"url\":\"http://lcscm-trantor.oss-cn-shenzhen.aliyuncs.com/images/manage/2046/46a23c6a-07bf-45fc-8d23-078dab8a0855/784b4626-e468-42ab-b707-1d20d327a964.jpg\"}]}",
                                    "supplyPurchaser": "[0]",
                                    "categoryList": "[4797,4804,4839,4949,5147]"
                                }
                            },
                            "colorNum": "",
                            "specification": "立邦地坪漆材料 ：ZF-F951-防静电的环保地坪漆",
                            "purDiscountRate": 1,
                            "itemSnapshotPOList": [],
                            "taxRate": 13,
                            "unit": "个",
                            "deliveryFee": 0,
                            "priceNoTax": 0,
                            "taxPrice": 59.66,
                            "priceTax": 59.66,
                            "toGetGoodsNum": 1,
                            "defaultRadix": 100
                        }
                    ],
                    "brandOwner": {
                        "id": 138017,
                        "website": "11",
                        "unifiedSocialCreditCode": "9144010173971356XX",
                        "name": "深圳哈哈有限公司"
                    },
                    "contractPaymentIterm": {
                        "updatedBy": {
                            "id": 10
                        },
                        "installOption": "SUPPLY_INSTALL",
                        "code": "PI20230905000002",
                        "isDefaultCreate": False,
                        "sort": 171,
                        "type": "SALE",
                        "radix": 100,
                        "createdAt": 1703578234000,
                        "isDeleted": False,
                        "createdBy": {
                            "id": 10
                        },
                        "name": "test专用",
                        "originPaymentItermId": 54002,
                        "comment": "test专用-接口专用",
                        "originPaymentGroupId": 44002,
                        "id": 224552,
                        "describe": "需求单/订单/到货/安装/结算/质保 (10.00/10.00/30.00/30.00/10.00/10.00)",
                        "status": "ENABLE",
                        "updatedAt": 1703578234000
                    },
                    "dealerContactMobile": "18178952877",
                    "invoiceHeaderType": "COMPANY",
                    "invoiceId": 218003,
                    "contractCode": "QZhetong12345678",
                    "lingchaoContact": "呵呵呵呵",
                    "project": {
                        "corporateCompany": {
                            "companyName": "湖北家家有限公司",
                            "id": 108009,
                            "files": "11",
                            "template": "11"
                        },
                        "id": 100023,
                        "purchaserId": 138013,
                        "name": "test1采购项目"
                    },
                    "invoiceAddress": "123@136.com",
                    "createdAt": 1704266411000,
                    "invoiceType": "ALL_ELE_SPECIAL",
                    "updatedAt": 1704353569000,
                    "updatedBy": {
                        "id": 132030
                    },
                    "purchaser": {
                        "id": 138013,
                        "website": "11",
                        "name": "湖北家家有限公司"
                    },
                    "invoiceTaker": "李四测试",
                    "purchaserName": "湖北家家有限公司",
                    "totalAmount": 59.66,
                    "totalTaxAmount": 0,
                    "orderDate": 1704266409000,
                    "orderRule": "CALCULATED_AT_TAX_INCLUSIVE_PRICE",
                    "code": "SO20240103002001",
                    "signStatus": "WAITTING_LC",
                    "title": "20240103湖北家家有限公司test1采购项目立邦",
                    "dealerContactName": "test2熊",
                    "categoryNames": "地坪漆材料(立邦)",
                    "invoiceMobile": "18178952878",
                    "invoiceUscc": "914200001776058818",
                    "projectReceiverName": "test熊",
                    "contractName": "合作意向签约",
                    "orderAttachment": {
                        "files": []
                    },
                    "supplierName": "深圳哈哈有限公司",
                    "itemTotalAmount": 59.66,
                    "invoiceHeader": "湖北家家有限公司",
                    "needInvoice": True,
                    "createdBy": {
                        "id": 132016
                    },
                    "qualityAssuranceStatus": "NOT_CLEAR",
                    "lingchaoMobile": "18178952878",
                    "payStatus": "UN_PAID"
                },
                "getGoodsOrderLinePOList": [
                    {
                        "id": None,
                        "item": {
                            "itemCode": "210204601003306",
                            "type": 1,
                            "isSpecialItem": 0,
                            "createdAt": 1678672512000,
                            "sellerId": 138017,
                            "digitalSyncStatus": "default",
                            "minOrderNumber": 1,
                            "id": 210204601003306,
                            "updatedAt": 1692606190000,
                            "brandName": "立邦",
                            "updatedBy": {
                                "id": 36068
                            },
                            "priceAdjustYn": 0,
                            "version": 0,
                            "unit": "个",
                            "purchaserId": 0,
                            "invoiceCategoryName": "立邦",
                            "brandId": 50001,
                            "name": "立邦 广角镜",
                            "leadTrendYn": 1,
                            "preOverdueDate": 1703987760000,
                            "shortName": "立邦",
                            "status": 1,
                            "sellerName": "深圳哈哈有限公司",
                            "specialYn": 0,
                            "isDeleted": False,
                            "contractName": "哈哈-立邦-合同01号",
                            "quickOrder": 1,
                            "showVirtualPrice": "NOT",
                            "overdueDate": 1725012300000,
                            "invoiceCategoryCode": "107020801",
                            "platformAuditStatus": "AGREE",
                            "isSyncDigital": 0,
                            "specification": "立邦地坪漆材料 ：ZF-F951-防静电的环保地坪漆",
                            "mainImage": "http://lcscm-trantor.oss-cn-shenzhen.aliyuncs.com/images/manage/2046/46a23c6a-07bf-45fc-8d23-078dab8a0855/06a02908-5065-4369-b2e0-58325b5ff515.png",
                            "supplyCycle": 10,
                            "bitTag": 0,
                            "md5Info": "948ecbc72bbbfb41494f23d109cb211b",
                            "createdBy": {
                                "id": 24040
                            },
                            "tenantId": 1,
                            "itemSource": "深圳哈哈有限公司",
                            "extraJson": "{\"taxRate\":\"13\",\"mainImage\":\"{\\\"files\\\":[{\\\"name\\\":\\\"广角镜封面图 1\\\",\\\"type\\\":\\\"jpg\\\",\\\"url\\\":\\\"http://lcscm-trantor.oss-cn-shenzhen.aliyuncs.com/images/manage/2046/46a23c6a-07bf-45fc-8d23-078dab8a0855/06a02908-5065-4369-b2e0-58325b5ff515.png\\\"},{\\\"name\\\":\\\"广角镜封面图 2\\\",\\\"type\\\":\\\"jpg\\\",\\\"url\\\":\\\"http://lcscm-trantor.oss-cn-shenzhen.aliyuncs.com/images/manage/2046/46a23c6a-07bf-45fc-8d23-078dab8a0855/7a3f9bb5-f526-4bf5-826c-915aaa4bf2b6.png\\\"},{\\\"name\\\":\\\"广角镜封面图 3\\\",\\\"type\\\":\\\"jpg\\\",\\\"url\\\":\\\"http://lcscm-trantor.oss-cn-shenzhen.aliyuncs.com/images/manage/2046/46a23c6a-07bf-45fc-8d23-078dab8a0855/784b4626-e468-42ab-b707-1d20d327a964.jpg\\\"}]}\",\"supplyPurchaser\":\"[0]\",\"categoryList\":\"[4797,4804,4839,4949,5147]\"}",
                            "businessType": 1,
                            "digitalStatus": -1,
                            "contractCode": "f0cdc16c581d1",
                            "categoryId": 5147,
                            "overdueStatus": "UNEXPIRED",
                            "itemLevel": "S",
                            "extra": {
                                "taxRate": "13",
                                "mainImage": "{\"files\":[{\"name\":\"广角镜封面图 1\",\"type\":\"jpg\",\"url\":\"http://lcscm-trantor.oss-cn-shenzhen.aliyuncs.com/images/manage/2046/46a23c6a-07bf-45fc-8d23-078dab8a0855/06a02908-5065-4369-b2e0-58325b5ff515.png\"},{\"name\":\"广角镜封面图 2\",\"type\":\"jpg\",\"url\":\"http://lcscm-trantor.oss-cn-shenzhen.aliyuncs.com/images/manage/2046/46a23c6a-07bf-45fc-8d23-078dab8a0855/7a3f9bb5-f526-4bf5-826c-915aaa4bf2b6.png\"},{\"name\":\"广角镜封面图 3\",\"type\":\"jpg\",\"url\":\"http://lcscm-trantor.oss-cn-shenzhen.aliyuncs.com/images/manage/2046/46a23c6a-07bf-45fc-8d23-078dab8a0855/784b4626-e468-42ab-b707-1d20d327a964.jpg\"}]}",
                                "supplyPurchaser": "[0]",
                                "categoryList": "[4797,4804,4839,4949,5147]"
                            }
                        },
                        "itemCode": "210204601003306",
                        "itemName": "立邦 广角镜",
                        "brand": {
                            "id": 50001,
                            "name": "立邦"
                        },
                        "specification": "立邦地坪漆材料 ：ZF-F951-防静电的环保地坪漆",
                        "attribute": None,
                        "unit": "个",
                        "priceTax": 59.66,
                        "priceNoTax": None,
                        "getGoodsNum": 1,
                        "expectedArrivalDate": 1704297600000,
                        "remark": None
                    }
                ]
            }
        ]
    }
}



