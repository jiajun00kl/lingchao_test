url ='https://staging-gateway.test.lcscm.cn/zhonghai/business-partner/partner-center-admin/1004706/api/trantor/data-source'

data =   {
    "frontendContext": {},
    "singleResult": False,
    "targetModel": "partner_center_Project",
    "sourceModel": "partner_center_Project",
    "searchValues": {
        "name": {
            "type": "One",
            "value": "武汉的项目"
        }
    },
    "dataSource": {
        "actionKey": "partner_center_Project_project_list_all"
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
                "fieldName": "status"
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

