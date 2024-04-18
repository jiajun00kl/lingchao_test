url1 =("https://staging-gateway.test.lcscm.cn"
       "/zhonghai/settlement-center/settlement-admin/1004893/api/trantor/action/exe")
data1 = {
  "frontendContext": {},
  "actionKey": "settlement_center_Receivable_SalesCheckServerAction::generateSalesCheck",
  "context": {
    "env": {
      "ids": [
        "SO20240228000001——SETTLEMENT_ORDER",
        "SOAZ20240228000001001——GOODS_INSTALL_ACCEPT",
        "SOAR20240228000001——GOODS_ARRIVED_ACCEPT",
        "SO20240228000001001——GOODS_GET"
      ],
      "searchData": {
        "contractName": None,
        "contract": {
          "contractLabel": None
        },
        "purchaseName": None,
        "receivableSourceType": None,
        "receivableSourceCode": "SO20240228000001\nSO20240228000001001\nSOAR20240228000001\nSOAZ20240228000001001\nSO20240228000001\n",
        "taxRateForView": None,
        "project": {
          "name": None,
          "performanceHeadStr": None
        },
        "createdAt": None,
        "usedStatus": "UNUSED"
      }
    },
    "record": [
      {}
    ],
    "modelKey": "settlement_center_Receivable"
  }
}

url2=("https://staging-gateway.test.lcscm.cn"
      "/zhonghai/settlement-center/settlement-admin/1004893/api/trantor/data-source")

data2 = {
    "frontendContext": {},
    "singleResult": False,
    "targetModel": "settlement_center_Receivable",
    "sourceModel": "settlement_center_SalesCheck",
    "searchValues": {
        "receivableSourceCode": {
            "type": "One",
            "value": "SO20240110000003\nSO20240110000003001\nSOAR20240110000013\nSOAZ20240110000013001\nSO20240110000003"
        },
        "usedStatus": {
            "type": "One",
            "value": "UNUSED"
        }
    },
    "dataSource": {
        "actionKey": "settlement_center_Receivable_receivable_create_check"
    },
    "result": {
        "fields": [
            {
                "fieldName": "id"
            },
            {
                "fieldName": "receivableCode"
            },
            {
                "fieldName": "purchaseName"
            },
            {
                "fieldName": "contractName"
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
                        "fieldName": "contractLabel"
                    }
                ]
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
                "fieldName": "receivableType"
            },
            {
                "fieldName": "paymentStatus"
            },
            {
                "fieldName": "categoryName"
            },
            {
                "fieldName": "itemName"
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
                        "fieldName": "performanceHeadStr"
                    }
                ]
            },
            {
                "fieldName": "countAmountSUM"
            },
            {
                "fieldName": "receivableRate"
            },
            {
                "fieldName": "taxRate"
            },
            {
                "fieldName": "totalAmount"
            },
            {
                "fieldName": "createdAt"
            }
        ]
    },
    "paging": {
        "no": 1,
        "size": 20
    },
    "order": {
        "by": "updatedAt",
        "isAsc": False
    }
}

data3 = {
    "frontendContext": {},
    "singleResult": True,
    "targetModel": "settlement_center_SalesCheck",
    "sourceModel": "settlement_center_SalesCheck",
    "queryValues": {
        "id": {
            "type": "One",
            "value": 212004
        }
    },
    "dataSource": {
        "actionKey": "settlement_center_SalesCheck_lc_sales_check_edit"
    },
    "result": {
        "fields": [
            {
                "fieldName": "id"
            },
            {
                "fieldName": "requestFundsInfoUrl"
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
                        "fieldName": "payType"
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
                "fieldName": "remark"
            },
            {
                "fieldName": "salesCheckAdjustList",
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
                                "fieldName": "purchaserName"
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
            },
            {
                "fieldName": "salesCheckSystemAttachments",
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

data4 = {
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
            212004
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
            212004
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
            212004
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
            212004
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
            212004
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
    "targetModel": "settlement_center_ContractAdditionalCostPO",
    "dataSource": {
        "actionKey": "settlement_center_ContractAdditionalCostPO_SalesContractPriceAdjustMultiAction",
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
            212004
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
    "targetModel": "settlement_center_PriceAdjust",
    "dataSource": {
        "actionKey": "settlement_center_PriceAdjust_PriceAdjustSalesMultiAction",
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
                "fieldName": "purchaserName"
            },
            {
                "fieldName": "contractName"
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
            212004
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
            212004
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
            212004
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
            212004
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

data14 = {
    "frontendContext": {},
    "actionKey": "settlement_center_SalesCheck_SalesCheckServerAction::submitSalesCheck",
    "context": {
        "record": [
            {
                "requestFundsInfoUrl": "https://performance-uat.lcscm.cn/#/casLoginIframe?token=MTAtMjAyNDAxMTE=&client=lcscm&redirectUrl=PleaseGenerateList?code=DZS20240111002004",
                "salesCheckCode": "DZS20240111002004",
                "salesCheckName": "合作意向签约-第72次对账",
                "contract": {
                    "id": 124057,
                    "code": "QZhetong12345678",
                    "project": {
                        "corporateCompany": {
                            "companyCode": "CO20230703000001",
                            "companyName": "湖北家家有限公司",
                            "uscc": "914200001776058818",
                            "mobile": None,
                            "address": "湖北武汉",
                            "invoiceInfo": {
                                "id": 226002,
                                "invoiceCompany": "湖北家家有限公司",
                                "invoiceBank": "中国邮政深圳分行龙华支行",
                                "invoiceAccount": "622878272262673834223"
                            },
                            "id": 108009
                        }
                    }
                },
                "contractName": "合作意向签约",
                "checkAcceptMonth": 1704879044000,
                "taxRate": 13,
                "createdAt": 1704959656000,
                "createdBy": {
                    "id": 10,
                    "nickname": "谢维"
                },
                "status": "UNSUBMIT",
                "contractCompletedTotal": 6.22,
                "finalTotal": 5.6,
                "adjustInvoiceTotal": 6.22,
                "outlineCheck": "NO",
                "payMethod": None,
                "remark": "验收单截至2024年01月 \r\n本期验收单总额6.22元，上述合计开票金额6.22元；\r\n本期应付5.60元（其中预付款1.24元、到货款1.87元、安装款1.87元、结算款0.62元），上述合计实付总额5.60元。\r\n往来款项明细为：\r\n1、扣【20240110湖北家家有限公司test1采购项目立邦】【-0.62】保修金\r\n",
                "id": 212004,
                "salesCheckAdjustList": [],
                "salesCheckAttachments": [],
                "salesCheckSystemAttachments": []
            }
        ],
        "modelKey": "settlement_center_SalesCheck"
    }
}