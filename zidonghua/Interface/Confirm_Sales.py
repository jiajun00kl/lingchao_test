url1 = ("https://staging-gateway.test.lcscm.cn"
        "/zhonghai/settlement-center/settlement-center/1004893/api/trantor/data-source")
data1 = {
    "frontendContext": {},
    "singleResult": True,
    "targetModel": "settlement_center_SalesCheck",
    "sourceModel": "settlement_center_SalesCheck",
    "queryValues": {
        "id": {
            "type": "One",
            "value": 214004
        }
    },
    "dataSource": {
        "actionKey": "settlement_center_SalesCheck_sales_check_detail"
    },
    "result": {
        "fields": [
            {
                "fieldName": "id"
            },
            {
                "fieldName": "salesCheckCode"
            },
            {
                "fieldName": "salesCheckName"
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
                                        "fieldName": "companyCode"
                                    },
                                    {
                                        "fieldName": "uscc"
                                    },
                                    {
                                        "fieldName": "mobile"
                                    },
                                    {
                                        "fieldName": "address"
                                    },
                                    {
                                        "fieldName": "invoiceInfo",
                                        "fields": [
                                            {
                                                "fieldName": "id"
                                            },
                                            {
                                                "fieldName": "name"
                                            },
                                            {
                                                "fieldName": "invoiceCompany"
                                            },
                                            {
                                                "fieldName": "invoiceBank"
                                            },
                                            {
                                                "fieldName": "invoiceAccount"
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "fieldName": "contractName"
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
                "fieldName": "outlineCheck"
            },
            {
                "fieldName": "payMethod"
            },
            {
                "fieldName": "confirmTime"
            },
            {
                "fieldName": "remark"
            },
            {
                "fieldName": "returnedReason"
            },
            {
                "fieldName": "returnedRemark"
            },
            {
                "fieldName": "salesCheckAttachments",
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
            }
        ]
    }
}

data2 = {
    "frontendContext": {},
    "singleResult": False,
    "targetModel": "settlement_center_SalesCheckLine",
    "dataSource": {
        "actionKey": "settlement_center_SalesCheckLine_SalesCheckLineAdvanceMultiAction",
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
                "fieldName": "receivableSourceType"
            },
            {
                "fieldName": "receivableSourceCode"
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
                    }
                ]
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
                "fieldName": "receivableTotalAmount"
            },
            {
                "fieldName": "adjustTotalAmount"
            },
            {
                "fieldName": "receivedTotalAmount"
            }
        ]
    },
    "related": {
        "field": "id",
        "recordIds": [
            214004
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

data3 = {
    "frontendContext": {},
    "singleResult": False,
    "targetModel": "settlement_center_SalesCheckLine",
    "dataSource": {
        "actionKey": "settlement_center_SalesCheckLine_SalesCheckLineAcceptMultiAction",
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
                "fieldName": "receivableSourceType"
            },
            {
                "fieldName": "receivableSourceCode"
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
                    }
                ]
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
                "fieldName": "receivableTotalAmount"
            },
            {
                "fieldName": "adjustTotalAmount"
            },
            {
                "fieldName": "backTotalAmount"
            },
            {
                "fieldName": "receivedTotalAmount"
            }
        ]
    },
    "related": {
        "field": "id",
        "recordIds": [
            214004
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
    "targetModel": "settlement_center_SalesCheckLine",
    "dataSource": {
        "actionKey": "settlement_center_SalesCheckLine_SalesCheckLineInstallMultiAction",
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
                "fieldName": "receivableSourceType"
            },
            {
                "fieldName": "receivableSourceCode"
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
                    }
                ]
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
                "fieldName": "receivableTotalAmount"
            },
            {
                "fieldName": "adjustTotalAmount"
            },
            {
                "fieldName": "receivedTotalAmount"
            }
        ]
    },
    "related": {
        "field": "id",
        "recordIds": [
            214004
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
    "targetModel": "settlement_center_SalesCheckLine",
    "dataSource": {
        "actionKey": "settlement_center_SalesCheckLine_SalesCheckLineSettleMultiAction",
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
                "fieldName": "receivableSourceType"
            },
            {
                "fieldName": "receivableSourceCode"
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
                    }
                ]
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
                "fieldName": "receivableTotalAmount"
            },
            {
                "fieldName": "adjustTotalAmount"
            },
            {
                "fieldName": "receivedTotalAmount"
            }
        ]
    },
    "related": {
        "field": "id",
        "recordIds": [
            214004
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
    "targetModel": "settlement_center_SalesCheckLine",
    "dataSource": {
        "actionKey": "settlement_center_SalesCheckLine_SalesCheckLineAssuranceMultiAction",
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
                "fieldName": "receivableSourceType"
            },
            {
                "fieldName": "receivableSourceCode"
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
                    }
                ]
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
                "fieldName": "receivableTotalAmount"
            },
            {
                "fieldName": "adjustTotalAmount"
            },
            {
                "fieldName": "receivedTotalAmount"
            }
        ]
    },
    "related": {
        "field": "id",
        "recordIds": [
            214004
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
    "targetModel": "settlement_center_SalesCheckBill",
    "dataSource": {
        "actionKey": "settlement_center_SalesCheckBill_SalesCheckBillInvoiceMultiAction",
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
            214004
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
    "targetModel": "settlement_center_SalesCheckBill",
    "dataSource": {
        "actionKey": "settlement_center_SalesCheckBill_SalesCheckBillMultiAction",
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
            214004
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

data9 ={
    "frontendContext": {},
    "singleResult": False,
    "targetModel": "settlement_center_SalesCheckBill",
    "dataSource": {
        "actionKey": "settlement_center_SalesCheckBill_SalesCheckPrePayBillMultiAction",
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
            }
        ]
    },
    "related": {
        "field": "id",
        "recordIds": [
            214004
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
    "targetModel": "settlement_center_SalesCheckSystemAttachment",
    "dataSource": {
        "actionKey": "settlement_center_SalesCheckSystemAttachment_SalesCheckSystemAttachmentMultiAction",
        "type": "Action"
    },
    "result": {
        "fields": [
            {
                "fieldName": "id"
            },
            {
                "fieldName": "attachName"
            }
        ]
    },
    "related": {
        "field": "id",
        "recordIds": [
            214004
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

url2 =("https://staging-gateway.test.lcscm.cn"
       "/zhonghai/settlement-center/settlement-admin/1004893/api/trantor/action/exe")

data11 = {
    "frontendContext": {},
    "actionKey": "settlement_center_SalesCheck_SalesCheckServerAction::updateStatus",
    "context": {
        "modelKey": "settlement_center_SalesCheck",
        "env": {
            "mode": "confirm"
        },
        "actionLabel": "确认",
        "record": [
            {
                "id": 214004
            }
        ]
    }
}