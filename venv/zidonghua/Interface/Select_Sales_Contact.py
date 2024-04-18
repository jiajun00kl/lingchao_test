url = ('https://staging-gateway.test.lcscm.cn'
       '/zhonghai/contract-center/contract-center-admin/1004703/api/trantor/data-source')

data = {
    "frontendContext": {},
    "singleResult": False,
    "targetModel": "contract_domain_Contract",
    "sourceModel": "contract_domain_Contract",
    "searchValues": {
        "project.name": {
            "type": "One",
            "value": ""
        }
    },
    "dataSource": {
        "actionKey": "contract_domain_Contract_to_pur_sales_contract_list"
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
                "fieldName": "financeSysCode"
            },
            {
                "fieldName": "name"
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
                "fieldName": "corporateCompany",
                "fields": [
                    {
                        "fieldName": "id"
                    },
                    {
                        "fieldName": "companyName"
                    }
                ]
            },
            {
                "fieldName": "partB",
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
                "fieldName": "startDate"
            },
            {
                "fieldName": "endDate"
            },
            {
                "fieldName": "signDate"
            },
            {
                "fieldName": "contractTotalAmount"
            },
            {
                "fieldName": "attn",
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
                "fieldName": "copySignCommonStatus"
            },
            {
                "fieldName": "contractType"
            }
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
