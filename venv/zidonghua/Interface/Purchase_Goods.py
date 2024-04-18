
api ='/api/trade/order/web/create'

data = {
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


api1 ="/api/trade/order/web/create-pay-order"

data1 = {"orderCodes":["SO20240115000011"],"projectId":100023}



