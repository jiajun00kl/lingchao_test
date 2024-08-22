url = ('https://staging-gateway.test.lcscm.cn'
       '/zhonghai/item-center/itemcenter/1004704/api/trantor/data-source')

data = {
    "frontendContext": {},
    "singleResult": False,
    "targetModel": "itemcenter_FrontItemVO",
    "sourceModel": "itemcenter_FrontItemVO",
    "searchValues": {
        "name": {
            "type": "One",
            "value": "305不锈钢水箱 方形组合式耐高温防锈材质规格 定制加工"
        },
#       "itemCode": {
#           "type": "One",
#          "value": ""
#        }   # id查询
    },
    "dataSource": {
        "actionKey": "itemcenter_FrontItemVO_admin_listAll"
    },
    "result": {
        "fields": [
            {
                "fieldName": "id"
            },
            {
                "fieldName": "image"
            },
            {
                "fieldName": "name"
            },
            {
                "fieldName": "itemCode"
            },
            {
                "fieldName": "type"
            },
            {
                "fieldName": "brandName"
            },
            {
                "fieldName": "specification"
            },
            {
                "fieldName": "contractName"
            },
            {
                "fieldName": "category"
            },
            {
                "fieldName": "virtualPrice"
            },
            {
                "fieldName": "costPriceRange"
            },
            {
                "fieldName": "itemMarkupRate"
            },
            {
                "fieldName": "salePriceRange"
            },
            {
                "fieldName": "salePriceExclusiveRange"
            },
            {
                "fieldName": "showPrice"
            },
            {
                "fieldName": "quickOrder"
            },
            {
                "fieldName": "subsidyPriceFirst"
            },
            {
                "fieldName": "minOrderNumFirst"
            },
            {
                "fieldName": "subsidyPriceSecond"
            },
            {
                "fieldName": "minOrderNumSecond"
            },
            {
                "fieldName": "subsidyPriceThird"
            },
            {
                "fieldName": "minOrderNumThird"
            },
            {
                "fieldName": "leadTrendYn"
            },
            {
                "fieldName": "isSyncDigital"
            },
            {
                "fieldName": "digitalSyncStatus"
            },
            {
                "fieldName": "digitalStatus"
            },
            {
                "fieldName": "platformAuditStatus"
            },
            {
                "fieldName": "createdName"
            },
            {
                "fieldName": "createdAt"
            },
            {
                "fieldName": "updatedByName"
            },
            {
                "fieldName": "auditBy",
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
                "fieldName": "itemSource"
            },
            {
                "fieldName": "isSpecialItem"
            },
            {
                "fieldName": "specialSupply"
            },
            {
                "fieldName": "itemType"
            },
            {
                "fieldName": "status"
            },
            {
                "fieldName": "updatedAt"
            },
            {
                "fieldName": "version"
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

