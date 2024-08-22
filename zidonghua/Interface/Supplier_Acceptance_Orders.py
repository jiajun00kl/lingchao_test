url =('https://staging-gateway.test.lcscm.cn/zhonghai/trade-center/'
      'order-admin-center/1004708/api/trantor/action/exe')
# url ="https://dev-gateway.test.lcscm.cn/zhonghai/trade-center/order-admin-center/1005740/api/trantor/action/exe"
data = {
    "frontendContext": {},
    "actionKey": "order_OrderPO_OrderAction::orderConfirm",
    "context": {
        "env": {
            "datas": {
                "id": 234052,
                "supplier": {
                    "id": 138017,
                    "website": "11"
                },
                "supplierContact": {
                    "__trantorExtendFields": {},
                    "id": 132030,
                    "mobile": "18178952877",
                    "nickname": "test2熊"
                }
            }
        },
        "record": [
            {
                "id": 234052,
                "supplier": {
                    "id": 138017,
                    "website": "11"
                },
                "supplierContact": {
                    "__trantorExtendFields": {},
                    "id": 132030,
                    "mobile": "18178952877",
                    "nickname": "test2熊"
                }
            }
        ],
        "modelKey": "order_OrderPO"
    }
}