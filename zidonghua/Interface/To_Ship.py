url =("https://staging-gateway.test.lcscm.cn"
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
