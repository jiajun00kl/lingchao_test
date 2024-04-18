url = ('https://staging-gateway.test.lcscm.cn'
       '/zhonghai/item-center/itemcenter/1004704/api/trantor/data-source')

data = {
    "frontendContext": {},
    "singleResult": True,
    "targetModel": "itemcenter_ItemVO",
    "sourceModel": "itemcenter_FrontItemVO",
    "queryValues": {
        "id": {
            "type": "One",
            "value": 113801700281007
        }
    },
    "dataSource": {
        "actionKey": "itemcenter_ItemVO_item_view_list_detail"
    },
    "result": {
        "fields": [
            {
                "fieldName": "id"
            },
            {
                "fieldName": "categoryNameList"
            },
            {
                "fieldName": "category",
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
                "fieldName": "type"
            },
            {
                "fieldName": "itemCode"
            },
            {
                "fieldName": "isCombined"
            },
            {
                "fieldName": "name"
            },
            {
                "fieldName": "shortName"
            },
            {
                "fieldName": "b2bPartnerVO",
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
                "fieldName": "brand",
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
                "fieldName": "contractName"
            },
            {
                "fieldName": "itemLevel"
            },
            {
                "fieldName": "districtNames"
            },
            {
                "fieldName": "originPlace"
            },
            {
                "fieldName": "invoiceCategoryVO",
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
                "fieldName": "taxRate"
            },
            {
                "fieldName": "supplyCycle"
            },
            {
                "fieldName": "minOrderNumber"
            },
            {
                "fieldName": "deliveryFeeTemplates",
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
                "fieldName": "deliveryFeeFactor"
            },
            {
                "fieldName": "installFeeTemplates",
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
                "fieldName": "installFeeFactor"
            },
            {
                "fieldName": "unit"
            },
            {
                "fieldName": "leadTrendYn"
            },
            {
                "fieldName": "specialYn"
            },
            {
                "fieldName": "priceAdjustYn"
            },
            {
                "fieldName": "isSpecialItem"
            },
            {
                "fieldName": "specialSupply",
                "fields": [
                    {
                        "fieldName": "id"
                    },
                    {
                        "fieldName": "name"
                    }
                ],
                "page": {
                    "curPage": 1,
                    "pageSize": 650
                }
            },
            {
                "fieldName": "nipponRelationItemCode"
            },
            {
                "fieldName": "videoUrl"
            },
            {
                "fieldName": "specification"
            },
            {
                "fieldName": "isSyncDigital"
            },
            {
                "fieldName": "advertise"
            },
            {
                "fieldName": "keyword"
            },
            {
                "fieldName": "mainImageAttachment"
            },
            {
                "fieldName": "itemChartlet"
            },
            {
                "fieldName": "itemModel"
            },
            {
                "fieldName": "showVirtualPrice"
            },
            {
                "fieldName": "virtualPrice"
            },
            {
                "fieldName": "version"
            },
            {
                "fieldName": "categoryDiscountPriceList",
                "fields": [
                    {
                        "fieldName": "id"
                    },
                    {
                        "fieldName": "categoryName"
                    },
                    {
                        "fieldName": "grade"
                    },
                    {
                        "fieldName": "discountRate"
                    },
                    {
                        "fieldName": "price"
                    }
                ],
                "page": {
                    "curPage": 1,
                    "pageSize": 650
                }
            },
            {
                "fieldName": "purchaserCategoryPriceList",
                "fields": [
                    {
                        "fieldName": "id"
                    },
                    {
                        "fieldName": "categoryName"
                    },
                    {
                        "fieldName": "purchaserName"
                    },
                    {
                        "fieldName": "grade"
                    },
                    {
                        "fieldName": "discountRate"
                    },
                    {
                        "fieldName": "price"
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