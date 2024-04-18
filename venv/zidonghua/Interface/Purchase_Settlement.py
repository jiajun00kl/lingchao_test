url1 = ("https://staging-gateway.test.lcscm.cn"
       "/zhonghai/settlement-center/settlement-admin/1004893/api/trantor/action/exe")

data1 = {
    "frontendContext": {},
    "actionKey": "settlement_center_PayableMergePO_PurchaseCheckAction::generateCheck",
    "context": {
        "env": {
            "ids": [
                "PO20240112000011——ORDER",
                "POAZ20240112000007001——GOODS_INSTALL_ACCEPT",
                "PO20240112000011——QUALITY_ASSURANCE",
                "PO20240112000011——SETTLEMENT_ORDER",
                "PR20240112000007001——GOODS_RETURN",
                "POAR20240112000007——GOODS_ARRIVED_ACCEPT",
                "PO20240112000011001——GOODS_GET"
            ],
            "searchData": {
                "payableSourceType": None,
                "payableSourceCode": None,
                "supplier": {
                    "code": None,
                    "name": None
                },
                "contract": {
                    "code": None,
                    "name": None
                },
                "payableMergeStatus": None,
                "protocol": {
                    "name": None
                },
                "taxRateStr": None,
                "project": {
                    "name": None
                },
                "createdAt": None
            }
        },
        "record": [
            {}
        ],
        "modelKey": "settlement_center_PayableMergePO"
    }
}

url2 =("https://staging-gateway.test.lcscm.cn"
       "/zhonghai/settlement-center/settlement-admin/1004893/api/trantor/data-source")

data2 = {
    "frontendContext": {},
    "singleResult": True,
    "targetModel": "settlement_center_PurchaseCheck",
    "sourceModel": "settlement_center_PurchaseCheck",
    "queryValues": {
        "id": {
            "type": "One",
            "value": 126009
        }
    },
    "dataSource": {
        "actionKey": "settlement_center_PurchaseCheck_lc_edit"
    },
    "result": {
        "fields": [
            {
                "fieldName": "id"
            },
            {
                "fieldName": "purchaseCheckCode"
            },
            {
                "fieldName": "purchaseCheckName"
            },
            {
                "fieldName": "contract",
                "fields": [
                    {
                        "fieldName": "id"
                    },
                    {
                        "fieldName": "name"
                    },
                    {
                        "fieldName": "code"
                    },
                    {
                        "fieldName": "payType"
                    }
                ]
            },
            {
                "fieldName": "contractName"
            },
            {
                "fieldName": "protocolName"
            },
            {
                "fieldName": "protocol",
                "fields": [
                    {
                        "fieldName": "id"
                    },
                    {
                        "fieldName": "name"
                    },
                    {
                        "fieldName": "code"
                    }
                ]
            },
            {
                "fieldName": "checkAcceptMonth"
            },
            {
                "fieldName": "taxRate"
            },
            {
                "fieldName": "createdAt"
            },
            {
                "fieldName": "createdBy",
                "fields": [
                    {
                        "fieldName": "id"
                    },
                    {
                        "fieldName": "username"
                    },
                    {
                        "fieldName": "nickname"
                    }
                ]
            },
            {
                "fieldName": "status"
            },
            {
                "fieldName": "contractCompletedTotal"
            },
            {
                "fieldName": "finalTotal"
            },
            {
                "fieldName": "adjustInvoiceTotal"
            },
            {
                "fieldName": "payMethod"
            },
            {
                "fieldName": "remark"
            },
            {
                "fieldName": "supplierName"
            },
            {
                "fieldName": "supplierCode"
            },
            {
                "fieldName": "bank"
            },
            {
                "fieldName": "accountName"
            },
            {
                "fieldName": "bankNo"
            },
            {
                "fieldName": "bankAccount"
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
                        "fieldName": "code"
                    },
                    {
                        "fieldName": "bankType"
                    },
                    {
                        "fieldName": "bankName"
                    },
                    {
                        "fieldName": "cardNo"
                    }
                ]
            },
            {
                "fieldName": "purchaseCheckAdjustList",
                "fields": [
                    {
                        "fieldName": "id"
                    },
                    {
                        "fieldName": "code"
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
                                "fieldName": "supplierName"
                            },
                            {
                                "fieldName": "contractName"
                            }
                        ]
                    },
                    {
                        "fieldName": "adjustType"
                    },
                    {
                        "fieldName": "adjustTotal"
                    },
                    {
                        "fieldName": "remark"
                    }
                ],
                "page": {
                    "curPage": 1,
                    "pageSize": 650
                }
            },
            {
                "fieldName": "purchaseCheckAttachmentList",
                "fields": [
                    {
                        "fieldName": "id"
                    },
                    {
                        "fieldName": "attachment"
                    },
                    {
                        "fieldName": "remark"
                    }
                ],
                "page": {
                    "curPage": 1,
                    "pageSize": 650
                }
            },
            {
                "fieldName": "purchaseCheckSystemAttachments",
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

data3 = {
    "frontendContext": {},
    "singleResult": False,
    "targetModel": "settlement_center_PurchaseCheckLine",
    "dataSource": {
        "actionKey": "settlement_center_PurchaseCheckLine_PurchaseCheckLineAdvanceMultiAction",
        "type": "Action"
    },
    "result": {
        "fields": [
            {
                "fieldName": "id"
            },
            {
                "fieldName": "projectName"
            },
            {
                "fieldName": "payableSourceType"
            },
            {
                "fieldName": "payableSourceCode"
            },
            {
                "fieldName": "payableSourceTotal"
            },
            {
                "fieldName": "createdAt"
            },
            {
                "fieldName": "payPercent"
            },
            {
                "fieldName": "taxRate"
            },
            {
                "fieldName": "adjustTaxRate"
            },
            {
                "fieldName": "payableTotalAmount"
            },
            {
                "fieldName": "adjustTotalAmount"
            },
            {
                "fieldName": "paymentTotal"
            }
        ]
    },
    "related": {
        "field": "id",
        "recordIds": [
            126009
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

data4 ={
    "frontendContext": {},
    "singleResult": False,
    "targetModel": "settlement_center_PurchaseCheckLine",
    "dataSource": {
        "actionKey": "settlement_center_PurchaseCheckLine_PurchaseCheckLineAcceptMultiAction",
        "type": "Action"
    },
    "result": {
        "fields": [
            {
                "fieldName": "id"
            },
            {
                "fieldName": "projectName"
            },
            {
                "fieldName": "payableSourceType"
            },
            {
                "fieldName": "payableSourceCode"
            },
            {
                "fieldName": "payableSourceTotal"
            },
            {
                "fieldName": "createdAt"
            },
            {
                "fieldName": "payPercent"
            },
            {
                "fieldName": "taxRate"
            },
            {
                "fieldName": "adjustTaxRate"
            },
            {
                "fieldName": "payableTotalAmount"
            },
            {
                "fieldName": "adjustTotalAmount"
            },
            {
                "fieldName": "returnBalance"
            },
            {
                "fieldName": "paymentTotal"
            }
        ]
    },
    "related": {
        "field": "id",
        "recordIds": [
            126009
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

data5 = {
    "frontendContext": {},
    "singleResult": False,
    "targetModel": "settlement_center_PurchaseCheckLine",
    "dataSource": {
        "actionKey": "settlement_center_PurchaseCheckLine_PurchaseCheckLineInstallMultiAction",
        "type": "Action"
    },
    "result": {
        "fields": [
            {
                "fieldName": "id"
            },
            {
                "fieldName": "projectName"
            },
            {
                "fieldName": "payableSourceType"
            },
            {
                "fieldName": "payableSourceCode"
            },
            {
                "fieldName": "payableSourceTotal"
            },
            {
                "fieldName": "createdAt"
            },
            {
                "fieldName": "payPercent"
            },
            {
                "fieldName": "taxRate"
            },
            {
                "fieldName": "adjustTaxRate"
            },
            {
                "fieldName": "payableTotalAmount"
            },
            {
                "fieldName": "adjustTotalAmount"
            },
            {
                "fieldName": "paymentTotal"
            }
        ]
    },
    "related": {
        "field": "id",
        "recordIds": [
            126009
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

data6 ={
    "frontendContext": {},
    "singleResult": False,
    "targetModel": "settlement_center_PurchaseCheckLine",
    "dataSource": {
        "actionKey": "settlement_center_PurchaseCheckLine_PurchaseCheckLineSettleMultiAction",
        "type": "Action"
    },
    "result": {
        "fields": [
            {
                "fieldName": "id"
            },
            {
                "fieldName": "projectName"
            },
            {
                "fieldName": "payableSourceType"
            },
            {
                "fieldName": "payableSourceCode"
            },
            {
                "fieldName": "payableSourceTotal"
            },
            {
                "fieldName": "createdAt"
            },
            {
                "fieldName": "payPercent"
            },
            {
                "fieldName": "taxRate"
            },
            {
                "fieldName": "adjustTaxRate"
            },
            {
                "fieldName": "payableTotalAmount"
            },
            {
                "fieldName": "adjustTotalAmount"
            },
            {
                "fieldName": "paymentTotal"
            }
        ]
    },
    "related": {
        "field": "id",
        "recordIds": [
            126009
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

data7 = {
    "frontendContext": {},
    "singleResult": False,
    "targetModel": "settlement_center_PurchaseCheckLine",
    "dataSource": {
        "actionKey": "settlement_center_PurchaseCheckLine_PurchaseCheckLineAssuranceMultiAction",
        "type": "Action"
    },
    "result": {
        "fields": [
            {
                "fieldName": "id"
            },
            {
                "fieldName": "projectName"
            },
            {
                "fieldName": "payableSourceType"
            },
            {
                "fieldName": "payableSourceCode"
            },
            {
                "fieldName": "payableSourceTotal"
            },
            {
                "fieldName": "createdAt"
            },
            {
                "fieldName": "payPercent"
            },
            {
                "fieldName": "taxRate"
            },
            {
                "fieldName": "adjustTaxRate"
            },
            {
                "fieldName": "payableTotalAmount"
            },
            {
                "fieldName": "adjustTotalAmount"
            },
            {
                "fieldName": "paymentTotal"
            }
        ]
    },
    "related": {
        "field": "id",
        "recordIds": [
            126009
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

data8 = {
    "frontendContext": {},
    "singleResult": False,
    "targetModel": "settlement_center_ContractAdditionalCostPO",
    "dataSource": {
        "actionKey": "settlement_center_ContractAdditionalCostPO_PurchaseContractPriceAdjustMultiAction",
        "type": "Action"
    },
    "result": {
        "fields": [
            {
                "fieldName": "id"
            },
            {
                "fieldName": "sourceType"
            },
            {
                "fieldName": "sourceCode"
            },
            {
                "fieldName": "calculateAccountPeriodTimeDesc"
            },
            {
                "fieldName": "contractAdditionCostsAmount"
            },
            {
                "fieldName": "adjustAccountPeriodTimeDesc"
            },
            {
                "fieldName": "adjustAmount"
            }
        ]
    },
    "related": {
        "field": "id",
        "recordIds": [
            126009
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

data9 = {
    "frontendContext": {},
    "singleResult": False,
    "targetModel": "settlement_center_PriceAdjust",
    "dataSource": {
        "actionKey": "settlement_center_PriceAdjust_PriceAdjustPurchaseMultiAction",
        "type": "Action"
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
                "fieldName": "supplierName"
            },
            {
                "fieldName": "purchaseContractName"
            },
            {
                "fieldName": "totalAmount"
            },
            {
                "fieldName": "remark"
            }
        ]
    },
    "related": {
        "field": "id",
        "recordIds": [
            126009
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

data10 = {
    "frontendContext": {},
    "singleResult": False,
    "targetModel": "settlement_center_PurchaseCheckBill",
    "dataSource": {
        "actionKey": "settlement_center_PurchaseCheckBill_PurchaseCheckBillInvoiceMultiAction",
        "type": "Action"
    },
    "result": {
        "fields": [
            {
                "fieldName": "id"
            },
            {
                "fieldName": "attributeCode"
            },
            {
                "fieldName": "computingFormula"
            },
            {
                "fieldName": "attributeFundName"
            },
            {
                "fieldName": "currentTotal"
            },
            {
                "fieldName": "remark"
            }
        ]
    },
    "related": {
        "field": "id",
        "recordIds": [
            126009
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

data11 = {
    "frontendContext": {},
    "singleResult": False,
    "targetModel": "settlement_center_PurchaseCheckBill",
    "dataSource": {
        "actionKey": "settlement_center_PurchaseCheckBill_PurchaseCheckBillMultiAction",
        "type": "Action"
    },
    "result": {
        "fields": [
            {
                "fieldName": "id"
            },
            {
                "fieldName": "attributeCode"
            },
            {
                "fieldName": "computingFormula"
            },
            {
                "fieldName": "attributeFundName"
            },
            {
                "fieldName": "currentTotal"
            }
        ]
    },
    "related": {
        "field": "id",
        "recordIds": [
            126009
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

data12 = {
    "frontendContext": {},
    "singleResult": False,
    "targetModel": "settlement_center_PurchaseCheckBill",
    "dataSource": {
        "actionKey": "settlement_center_PurchaseCheckBill_PurchaseCheckPrePayBillMultiAction",
        "type": "Action"
    },
    "result": {
        "fields": [
            {
                "fieldName": "id"
            },
            {
                "fieldName": "attributeCode"
            },
            {
                "fieldName": "computingFormula"
            },
            {
                "fieldName": "attributeFundName"
            },
            {
                "fieldName": "lastTotal"
            },
            {
                "fieldName": "currentTotal"
            },
            {
                "fieldName": "currentSum"
            },
            {
                "fieldName": "attributeType"
            }
        ]
    },
    "related": {
        "field": "id",
        "recordIds": [
            126009
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

data13 = {
    "frontendContext": {},
    "actionKey": "settlement_center_PurchaseCheck_PurchaseCheckAction::submitPurchaseCheck",
    "context": {
        "record": [
            {
                "purchaseCheckCode": "DZP20240119000001",
                "purchaseCheckName": "哈哈锁智能芯合同-第5次对账",
                "contract": {
                    "id": 128085,
                    "code": "哈哈锁智能芯合同-01"
                },
                "contractName": "哈哈锁智能芯合同",
                "protocolName": None,
                "protocol": {
                    "id": None,
                    "code": None
                },
                "checkAcceptMonth": 1705309809000,
                "taxRate": 13,
                "createdAt": 1705636879000,
                "createdBy": {
                    "id": 10,
                    "nickname": "谢维"
                },
                "status": "UNSUBMIT",
                "contractCompletedTotal": 502.92,
                "finalTotal": 457.2,
                "adjustInvoiceTotal": 457.2,
                "payMethod": None,
                "remark": "验收单截至2024年01月 \r\n本期验收单总额502.92元，上述合计开票金额457.20元；\r\n本期应付457.20元（其中预付款100.58元、到货款150.88元、安装款137.16元、结算款45.72元、质保金45.72元、退货款-22.86元），上述合计实付总额457.20元。\r\n往来款项明细为：\r\n",
                "id": 126009,
                "supplier": {
                    "id": 138017,
                    "name": "深圳哈哈有限公司",
                    "code": "CO20230705000002",
                    "bankType": "建设银行",
                    "bankName": "深圳市龙华区龙华人民路建设银行",
                    "cardNo": "63221877998765353331"
                },
                "bankNo": None,
                "purchaseCheckAdjustList": [],
                "purchaseCheckAttachmentList": [],
                "purchaseCheckSystemAttachments": []
            }
        ],
        "env": {},
        "modelKey": "settlement_center_PurchaseCheck"
    }
}