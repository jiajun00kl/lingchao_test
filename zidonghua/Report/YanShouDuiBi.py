import time

import zidonghua.Common.Requests
import zidonghua.Conf.Datetime

def login_cookies(mobile,password):
    url = 'https://lcscm.cn/api/user/web/login/identify'
    data = {
        "isApp": False,
        "password": "d6yg5oFTCC4Um3Tj",
        "identify": "16600000000"
    }
    data['identify']=mobile
    data['password'] = password
    response = zidonghua.Common.Requests.HttpUtil(
        url=url,json=data).post()
    cookies = response.cookies.get_dict()
    return cookies

def yanshou(deliveryCode):
    cookies = login_cookies(mobile='16600000000', password='d6yg5oFTCC4Um3Tj')
    url2 = "https://gateway.lcscm.cn/zhonghai/settlement-center/settlement-admin/1004923/api/trantor/data-source"  # 验收单报表
    data2 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "settlement_center_AcceptanceReportVo",
        "queryValues": {
            "source": {
                "type": "One",
                "value": "AcceptanceReportForOperator"
            }
        },
        "searchValues": {
            "salesInvoiceCode": {
                "type": "One",
                "value": deliveryCode
            }
        },
        "dataSource": {
            "actionKey": "settlement_center_AcceptanceReportVo_acceptance_report_list"
        },
        "result": {
            "fields": [
                {
                    "fieldName": "id"
                },
                {
                    "fieldName": "contractLabel"
                },
                {
                    "fieldName": "purchaserName"
                },
                {
                    "fieldName": "corporateCompanyName"
                },
                {
                    "fieldName": "projectName"
                },
                {
                    "fieldName": "salesContractCode"
                },
                {
                    "fieldName": "salesContractName"
                },
                {
                    "fieldName": "purchaseContractName"
                },
                {
                    "fieldName": "brandOwnerName"
                },
                {
                    "fieldName": "dealerName"
                },
                {
                    "fieldName": "salesDemandName"
                },
                {
                    "fieldName": "salesDemandCode"
                },
                {
                    "fieldName": "salesInvoiceCode"
                },
                {
                    "fieldName": "salesArrivalAcceptanceCode"
                },
                {
                    "fieldName": "arrivalAcceptanceDate"
                },
                {
                    "fieldName": "installAcceptanceDate"
                },
                {
                    "fieldName": "itemCode"
                },
                {
                    "fieldName": "itemName"
                },
                {
                    "fieldName": "categoryName"
                },
                {
                    "fieldName": "unit"
                },
                {
                    "fieldName": "thisShipmentNum"
                },
                {
                    "fieldName": "arrivalAcceptedNum"
                },
                {
                    "fieldName": "installAcceptedNum"
                },
                {
                    "fieldName": "salesPrice"
                },
                {
                    "fieldName": "salesDeliveryFee"
                },
                {
                    "fieldName": "salesInstallFee"
                },
                {
                    "fieldName": "salesComprehensiveFee"
                },
                {
                    "fieldName": "salesAdditionalCostAmount"
                },
                {
                    "fieldName": "purchasePrice"
                },
                {
                    "fieldName": "purchaseDeliveryFee"
                },
                {
                    "fieldName": "purchaseInstallFee"
                },
                {
                    "fieldName": "purchaseComprehensiveFee"
                },
                {
                    "fieldName": "purchaseAdditionalCostAmount"
                },
                {
                    "fieldName": "salesAcceptedTotal"
                },
                {
                    "fieldName": "purchaseAcceptedTotal"
                },
                {
                    "fieldName": "salesReconciliationStatus"
                },
                {
                    "fieldName": "salesReconciliationDate"
                },
                {
                    "fieldName": "purchaseReconciliationStatus"
                },
                {
                    "fieldName": "purchaseReconciliationDate"
                },
                {
                    "fieldName": "performanceHeadStr"
                },
                {
                    "fieldName": "salesHeadStr"
                },
                {
                    "fieldName": "signDate"
                }
            ]
        },
        "paging": {
            "no": 1,
            "size": 100
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    response2 = zidonghua.Common.Requests.HttpUtil(url=url2, json=data2, cookies=cookies).post()
    result2 = response2.json()
    shuju2 = result2['res']['data']
    salesAcceptedTotalSum = 0  # 初始化累加器
    for item in shuju2:  # 直接遍历列表中的每个元素
        salesAcceptedTotalSum =round(salesAcceptedTotalSum + item['salesAcceptedTotal'],2)
    return salesAcceptedTotalSum

def duibi(yema,yeshu):
    url1 = "https://gateway.lcscm.cn/zhonghai/trade-center/order-admin-center/1004871/api/trantor/data-source"  # 单据管理
    data1 = {
        "frontendContext": {},
        "singleResult": False,
        "targetModel": "order_AcceptanceOrderPO",
        "sourceModel": "order_AcceptanceOrderPO",
        "dataSource": {
            "actionKey": "order_AcceptanceOrderPO_operator_seller_receipt_acceptance_list"
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
                    "fieldName": "deliveryCode"
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
                            "fieldName": "purchaser",
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
                            "fieldName": "isTranslation"
                        },
                        {
                            "fieldName": "title"
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
                            "fieldName": "project",
                            "fields": [
                                {
                                    "fieldName": "id"
                                },
                                {
                                    "fieldName": "name"
                                },
                                {
                                    "fieldName": "lcName"
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
                                }
                            ]
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
                            "fieldName": "orderRule"
                        }
                    ]
                },
                {
                    "fieldName": "categoryName"
                },
                {
                    "fieldName": "settleStatus"
                },
                {
                    "fieldName": "isInstall"
                },
                {
                    "fieldName": "acceptanceDate"
                },
                {
                    "fieldName": "acceptanceOrderLinePOList",
                    "fields": [
                        {
                            "fieldName": "id"
                        },
                        {
                            "fieldName": "getGoodsOrderLinePO",
                            "fields": [
                                {
                                    "fieldName": "id"
                                },
                                {
                                    "fieldName": "taxPrice"
                                }
                            ]
                        },
                        {
                            "fieldName": "orderLinePO",
                            "fields": [
                                {
                                    "fieldName": "id"
                                },
                                {
                                    "fieldName": "deliveryFee"
                                },
                                {
                                    "fieldName": "installFee"
                                }
                            ]
                        },
                        {
                            "fieldName": "acceptanceNum"
                        }
                    ],
                    "page": {
                        "curPage": 1,
                        "pageSize": 650
                    }
                },
                {
                    "fieldName": "acceptanceAmount"
                },
                {
                    "fieldName": "reverseAmount"
                },
                {
                    "fieldName": "paidAmount"
                },
                {
                    "fieldName": "checkedAmount"
                },
                {
                    "fieldName": "payDate"
                }
            ]
        },
        "paging": {
            "no": yema,
            "size": yeshu
        },
        "order": {
            "by": "updatedAt",
            "isAsc": False
        }
    }
    cookies = login_cookies(mobile='16600000000',password='d6yg5oFTCC4Um3Tj')
    response1 = zidonghua.Common.Requests.HttpUtil(
        url=url1,json=data1, cookies=cookies).post()
    result1 =  response1.json()
    shuju1 = result1['res']['data']
    for shuju in shuju1:
        deliveryCode = shuju['deliveryCode']
        acceptancedate =shuju['acceptanceDate']
        acceptanceAmount = round(shuju['acceptanceAmount'],2)
        salesAcceptedTotalSum = yanshou(deliveryCode)
        if acceptanceAmount != salesAcceptedTotalSum:
            print("发货单号:{}与验收单报表的数据不一致,单据验收金额为:{} ,到货验收报表金额为:{},"
                  "到货验收日期:{}".format(shuju['deliveryCode'],acceptanceAmount,salesAcceptedTotalSum,zidonghua.Conf.Datetime.fan_timestamp(acceptancedate)))
            continue

if __name__ == '__main__':
        duibi(yema= 1,yeshu=200)