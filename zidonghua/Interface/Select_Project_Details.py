url = ('https://staging-gateway.test.lcscm.cn'
       '/zhonghai/business-partner/partner-center-admin/1004706/api/trantor/data-source')

data = {
    "frontendContext": {},
    "singleResult": True,
    "targetModel": "partner_center_Project",
    "sourceModel": "partner_center_Project",
    "queryValues": {
        "id": {
            "type": "One",
            "value": 102004
        }
    },
    "dataSource": {
        "actionKey": "partner_center_Project_to_project_detail"
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
                "fieldName": "name"
            },
            {
                "fieldName": "lcName"
            },
            {
                "fieldName": "status"
            },
            {
                "fieldName": "quotationHead",
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
                ],
                "page": {
                    "curPage": 1,
                    "pageSize": 650
                }
            },
            {
                "fieldName": "performanceHead",
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
                ],
                "page": {
                    "curPage": 1,
                    "pageSize": 650
                }
            },
            {
                "fieldName": "salesHead",
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
                ],
                "page": {
                    "curPage": 1,
                    "pageSize": 650
                }
            },
            {
                "fieldName": "salesSupport",
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
                ],
                "page": {
                    "curPage": 1,
                    "pageSize": 650
                }
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
                "fieldName": "createdAt"
            },
            {
                "fieldName": "remark"
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
                                "fieldName": "taxpayerCode"
                            },
                            {
                                "fieldName": "invoiceAddress"
                            },
                            {
                                "fieldName": "invoiceMobile"
                            },
                            {
                                "fieldName": "invoiceType"
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
            },
            {
                "fieldName": "invoiceRemark"
            },
            {
                "fieldName": "userExtList",
                "fields": [
                    {
                        "fieldName": "id"
                    },
                    {
                        "fieldName": "username"
                    },
                    {
                        "fieldName": "phone"
                    },
                    {
                        "fieldName": "email"
                    },
                    {
                        "fieldName": "roleType"
                    },
                    {
                        "fieldName": "isContractor"
                    }
                ],
                "page": {
                    "curPage": 1,
                    "pageSize": 650
                }
            },
            {
                "fieldName": "projectAddressList",
                "fields": [
                    {
                        "fieldName": "id"
                    },
                    {
                        "fieldName": "code"
                    },
                    {
                        "fieldName": "address"
                    },
                    {
                        "fieldName": "type"
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

