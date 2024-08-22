
url1 ="https://b2b-mall-uat.test.lcscm.cn/api/front/reverse/apply/238069"

url2 ="https://b2b-mall-uat.test.lcscm.cn/api/front/reverse/returnRefund"
data2 ={"deliveryId":218078,"type":"ORDER_REVERSE"}

url3 = "https://b2b-mall-uat.test.lcscm.cn/api/front/reverse/create"
data3 ={
    "deliveryOrderId": 218078,
    "deliveryOrderCode": "SO20240222000006001001",
    "orderId": None,
    "reverseType": "RETURN_REFUND",
    "type": "ORDER_REVERSE",
    "reverser": "test熊",
    "reasonType": "货物破损",
    "reverseItemLineInfos": [
        {
            "id": None,
            "orderLineId": 218133,
            "itemId": 210204600125009,
            "itemCode": "210204600125009",
            "mainImage": "//lcscm-trantor.oss-cn-shenzhen.aliyuncs.com/trantor/attachments/"
     "1056637d-2af3-4465-bc33-244c16333395.jpg",
            "name": "立邦 环氧地坪 溶剂型 砂面防滑 5.0mm厚 适用于常规地区",
            "brand": "立邦",
            "specification": "立邦地坪漆材料 ：ZF-F951-防静电的环保地坪漆",
            "attribute": None,
            "price": 41.37,
            "canReverseNum": 10,
            "reverseNum": 1,
            "orderRule": "CALCULATED_AT_TAX_INCLUSIVE_PRICE",
            "priceNoTax": 41.37,
            "taxRate": 13
        },
        {
            "id": None,
            "orderLineId": 218134,
            "itemId": 210204601003306,
            "itemCode": "210204601003306",
            "mainImage": "http://lcscm-trantor.oss-cn-shenzhen.aliyuncs.com/images/manage/2046/46a23c6a-07bf-45fc-8d23-078dab8a0855/06a02908-5065-4369-b2e0-58325b5ff515.png",
            "name": "立邦 广角镜",
            "brand": "立邦",
            "specification": "立邦地坪漆材料 ：ZF-F951-防静电的环保地坪漆",
            "attribute": None,
            "price": 59.66,
            "canReverseNum": 10,
            "reverseNum": 1,
            "orderRule": "CALCULATED_AT_TAX_INCLUSIVE_PRICE",
            "priceNoTax": 59.66,
            "taxRate": 13
        }
    ],
    "contactMobile": "18178952878"
}

url4 =("https://staging-gateway.test.lcscm.cn"
       "/zhonghai/trade-center/order-admin-center/1004708/api/trantor/action/exe")
data4 ={"frontendContext":{},"actionKey":"order_ReverseOrderPO_ReverseOrderServerAction::approveReverseOrder",
        "context":{"modelKey":"order_ReverseOrderPO","actionLabel":"确认","record":[{"id":172006}]}}


