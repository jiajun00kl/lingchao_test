uat_api={
"api1" : "/zhonghai/business-partner/partner-center-admin/1004706/api/trantor/data-source",
"api2" : "/zhonghai/business-partner/partner-center-admin/1004706/api/trantor/action/exe",
"api3" :"/zhonghai/contract-center/contract-center-admin/1004703/api/trantor/action/exe",

}

dev_api={
"api1" : "/zhonghai/business-partner/partner-center-admin/1005739/api/trantor/data-source",
"api2" : "/zhonghai/business-partner/partner-center-admin/1005739/api/trantor/action/exe",
"api3" : "/zhonghai/contract-center/contract-center-admin/1005736/api/trantor/action/exe",

}
api = uat_api

data ={
    "frontendContext": {},
    "singleResult": False,
    "targetModel": "partner_center_CorporateCompany",
    "queryValues": {
        "contractExpand": {
            "type": "One",
            "value": {
                "startDateType": "FIXED_DATE"
            }
        },
        "uuid": {
            "type": "One",
            "value": "1q7fy81715563598531"
        },
        "quotationId": {
            "type": "One",
            "value": {
                "taxedFormula": "销售金额=含税销售单价*数量，运算后四舍五入保留两位小数;\n含税销售单价=未税销售单价*(1+税率) ，运算后四舍五入保留两位小数;",
                "untaxedFormula": "销售金额=未税金额+税款金额;\n税款金额=(未税金额*税率)，运算后四舍五入保留两位小数;\n未税金额=(未税销售单价*数量)，运算后四舍五入保留两位小数;"
            }
        },
        "code": {
            "type": "One",
            "value": "COBSCMMD20240513000004"
        },
        "client": {
            "type": "One",
            "value": "LC"
        },
        "contractOption": {
            "type": "One",
            "value": "ONLINE"
        },
        "partB": {
            "type": "One",
            "value": 70057
        },
        "tips": {
            "type": "One",
            "value": ""
        },
        "isAllCategory": {
            "type": "One",
            "value": False
        },
        "project": {
            "type": "One",
            "value": {}
        },
        "startDate": {
            "type": "One",
            "value": 1715563599007
        },
        "contractType": {
            "type": "One",
            "value": "SALE_CONTRACT"
        },
        "type": {
            "type": "One",
            "value": "SALE_CONTRACT"
        },
        "contractTypeAttribute": {
            "type": "One",
            "value": "COMMODITY_SALES"
        },
        "attn": {
            "type": "One",
            "value": 14064
        },
        "lastUpdateBy": {
            "type": "One",
            "value": 14064
        },
        "syncStatus": {
            "type": "One",
            "value": "TO_BE_PUSHED"
        }
    },
    "dataSource": {
        "actionKey": "partner_center_CorporateCompany_SalesContractCorporateCompanyMultiAction",
        "type": "Action"
    },
    "result": {
        "fields": [
            {
                "fieldName": "id"
            },
            {
                "fieldName": "companyName"
            }
        ]
    },
    "paging": {
        "no": 1,
        "size": 10000
    },
    "order": {
        "by": "updatedAt",
        "isAsc": False
    }
}


data1={
    "frontendContext": {},
    "actionKey": "contract_domain_Contract_ContractAction::editAndSubmitSaleContract",   #编辑提交合同
    "context": {
        "record": [
            {
                "id": 258015,
                "tempField": '[{"id":4842,"name":"电子锁"},{"id":4804,"name":"涂料类"}]',
                "isEdit": False,
                "isAllCategory": False,
                "projectCode": "ZH20230610000001",
                "client": "LC",
                "code": "COBSCMMD20240603000002",
                "name": "20240603000001test02合同",
                "corporateCompany": {
                    "businessLicense": {
                        "files": [
                            {
                                "name": "微信截图_20230703102935.png",
                                "type": "png",
                                "url": "//lcscm-trantor-test.oss-cn-shenzhen.aliyuncs.com/trantor/attachments/6686762b-71cd-4639-89ca-a054c2bd74de.png"
                            }
                        ]
                    },
                    "travellingTraderBankStatus": "NOT_CREATED",
                    "crmStatus": "NOT_SETTLED",
                    "companyName": "湖北家家有限公司",
                    "isManualEdit": False,
                    "source": "PURCHASER",
                    "authorization": [
                        "authorization"
                    ],
                    "createdAt": 1688378589000,
                    "id": 108009,
                    "updatedAt": 1717144014000,
                    "companyCode": "CO20230703000001",
                    "contactMobile": "18178952878",
                    "updatedBy": {
                        "id": 10
                    },
                    "contactName": "李四测试",
                    "graphicSealValidPeriodStart": 1688378589000,
                    "isEffective": True,
                    "defaultCreateType": "DEFAULT_CREATE_ENTERPRICE",
                    "files": "11",
                    "dataSource": "LC",
                    "status": "APPROVED",
                    "template": "11",
                    "isAvailable": True,
                    "isReEdit": False,
                    "travellingTraderStatus": "NOT_CREATED",
                    "legalRepresentativeName": "李四测试",
                    "uscc": "914200001776058818",
                    "isDeleted": False,
                    "enterpriseName": "湖北家家有限公司",
                    "invoiceInfo": {
                        "titleType": "COMPANY",
                        "recipientPhone": "18178952878",
                        "updatedBy": {
                            "id": 10
                        },
                        "uscc": "914200001776058818",
                        "invoiceAccount": "622878272262673834223",
                        "invoiceAddress": "深圳宝安区宝安大道108号哈哈锁厂",
                        "title": "湖北家家有限公司",
                        "invoiceCompany": "湖北家家有限公司",
                        "invoiceMobile": "18178952878",
                        "createdAt": 1716793812000,
                        "isDeleted": False,
                        "createdBy": {},
                        "needInvoice": False,
                        "invoiceType": "ALL_ELE_SPECIAL",
                        "recipientName": "李四测试",
                        "id": 274437,
                        "recipientAddress": "123@136.com",
                        "taxpayerCode": "914200001776058818",
                        "updatedAt": 1717144014000,
                        "invoiceBank": "中国邮政深圳分行龙华支行"
                    },
                    "address": "湖北武汉",
                    "batchNum": "c77251bf4f96443bb111a6bc117f0d14",
                    "graphicSealValidPeriodEnd": 32503564800000,
                    "createdBy": {
                        "id": 132016
                    },
                    "enterpriseId": 138013,
                    "graphicSeal": {
                        "files": [
                            {
                                "name": "微信截图_20230703102935.png",
                                "type": "png",
                                "url": "//lcscm-trantor-test.oss-cn-shenzhen.aliyuncs.com/trantor/attachments/00ff564d-e88b-44cd-a17e-96a57350be90.png"
                            }
                        ]
                    }
                },
                "partB": {
                    "businessLicense": {
                        "files": []
                    },
                    "creditReport": {
                        "files": []
                    },
                    "idRelationUnit": False,
                    "contactAddress": "深圳市福田区福华路399号中海大厦3楼",
                    "id": 1000001,
                    "adminUserId": 8118,
                    "registrationInformation": "",
                    "phone": "13545185285",
                    "legalRepresentativeName": "陈柯羽",
                    "longTerm": False,
                    "isCorporateCompany": False,
                    "contactDepart": "市场部",
                    "isDeleted": False,
                    "registeredCapital": 0,
                    "currency": "CNY",
                    "bankCode": "",
                    "website": "11",
                    "parentId": 0,
                    "contactPhone": "13545185285",
                    "country": "China",
                    "legalPosition": "",
                    "unifiedSocialCreditCode": "91440300MA5GB6F453",
                    "registrationTaxAccess": {
                        "files": []
                    },
                    "electronicSignatureAttorney": {
                        "files": []
                    },
                    "isMonopolyUnit": False,
                    "isManualEdit": False,
                    "source": "INTERNAL",
                    "createdAt": 1626076388000,
                    "taxpayerType": "general",
                    "foundAt": 1596643200000,
                    "updatedAt": 1717149573000,
                    "updatedBy": {
                        "id": 10
                    },
                    "contactName": "陈柯羽",
                    "businessScope": "",
                    "name": "深圳领潮供应链管理有限公司",
                    "architectureDiagram": {
                        "files": []
                    },
                    "dataSource": "LC",
                    "code": "CO20210629100000",
                    "qualificationCertificate": {
                        "files": []
                    },
                    "auditComments": "",
                    "certificateRepresentative": {
                        "files": []
                    },
                    "financialStatements": {
                        "files": []
                    },
                    "powerAttorney": {
                        "files": []
                    },
                    "introduction": "",
                    "contactEmail": "1171136297@qq.com",
                    "companyType": "I",
                    "creditReportDate": 1626076388000,
                    "taxpayer": "深圳领潮供应链管理有限公司",
                    "enterpriseType": "PC",
                    "createdBy": {},
                    "taxpayerCode": "91440300MA5GB6F453"
                },
                "project": {
                    "source": "MALL_CREATE",
                    "salesHead": [],
                    "createdAt": 1716974277000,
                    "id": 234002,
                    "performanceProjectStatus": "DISCLOSED",
                    "updatedAt": 1717379039000,
                    "purchaserIsVisible": True,
                    "updatedBy": {
                        "id": 10
                    },
                    "performanceHead": [
                        {
                            "nickname": "胡梦云",
                            "id": 270065
                        }
                    ],
                    "purchaserId": 138013,
                    "defaultCreateType": "NOT_DEFAULT",
                    "name": "0529合同测试新建项目001@湖北家家有限公司#深圳非CRM同步的",
                    "status": "ENABLED",
                    "isAvailable": True,
                    "code": "ZH20240529002002",
                    "isDeleted": False,
                    "quotationHeadStr": "王明华",
                    "paymentRequest": 1,
                    "customerPaymentCycle": 30,
                    "salesSupport": [
                        {
                            "nickname": "胡耀东",
                            "id": 270070
                        }
                    ],
                    "performanceHeadStr": "胡梦云",
                    "salesSupportStr": "胡耀东",
                    "address": {
                        "address": [
                            {
                                "id": "120000",
                                "name": "天津"
                            },
                            {
                                "id": "120100",
                                "name": "天津市"
                            },
                            {
                                "id": "120102",
                                "name": "河东区"
                            }
                        ],
                        "city": {
                            "id": "120100",
                            "name": "天津市"
                        },
                        "detail": "没有详细地址",
                        "province": {
                            "id": "120000",
                            "name": "天津"
                        },
                        "region": {
                            "id": "120102",
                            "name": "河东区"
                        }
                    },
                    "createdBy": {
                        "id": 132016
                    },
                    "quotationHead": [
                        {
                            "nickname": "王明华",
                            "id": 270038
                        }
                    ]
                },
                "contractExpand": {
                    "id": 30,
                    "startDateType": "SIGNED_START",
                    "signCommonType": "COMPANY_LEGAL_PERSON",
                    "signCommonFileNumber": 1,
                    "otherSealAttachment": None,
                    "invoiceInfo": {
                        "id": 278041,
                        "invoiceCompany": "湖北家家有限公司",
                        "taxpayerCode": "914200001776058818",
                        "invoiceAddress": "深圳宝安区宝安大道108号哈哈锁厂",
                        "invoiceMobile": "18178952878",
                        "invoiceType": "ALL_ELE_SPECIAL",
                        "invoiceBank": "中国邮政深圳分行龙华支行",
                        "invoiceAccount": "622878272262673834223"
                    },
                    "invoiceRemark": None,
                    "oneQuarterRevenuePlan": None,
                    "twoQuarterRevenuePlan": None,
                    "threeQuarterRevenuePlan": None,
                    "fourQuarterRevenuePlan": None
                },
                "endDate": 1719676800000,
                "signDate": None,
                "contractType": "SALE_CONTRACT",
                "type": "SALE_CONTRACT",
                "contractTypeAttribute": "COMMODITY_SALES",
                "payTypesOnView": [
                    "FACTORING",
                    "CREDIT_CERT",
                    "COMMERCIAL_TICKET",
                    "CASH",
                    "SILVER_TICKET"
                ],
                "contractTotalAmount": 333333,
                "contractTaxRateSale": 9,
                "contractAmountExcludingTax": 305810.09,
                "contractTax": 27522.91,
                "attn": {
                    "id": 10,
                    "nickname": "谢维"
                },
                "lastUpdateBy": {
                    "id": 10,
                    "nickname": "谢维"
                },
                "financeAttn": {
                    "updatedBy": {
                        "id": 10
                    },
                    "mobile": "18620791665",
                    "pwdExpireAt": 3535545600000,
                    "enabled": True,
                    "createdAt": 1624283748000,
                    "password": "73b8@92204e05e90d65220a17",
                    "isDeleted": False,
                    "createdBy": {},
                    "nickname": "巩固",
                    "id": 2014,
                    "locked": False,
                    "email": "gonggu01@cohl.com",
                    "updatedAt": 1717351213000,
                    "username": "gonggu01"
                },
                "contractLabel": "Outside Customer_small",
                "askPriceId": None,
                "isframeworkAgreement": "NO",
                "frameworkAgreement": {
                    "endDate": 1727711999000,
                    "contractType": "SALE_CONTRACT",
                    "type": "SALE_CONTRACT",
                    "payType": [
                        "FACTORING",
                        "CREDIT_CERT",
                        "COMMERCIAL_TICKET",
                        "CASH",
                        "SILVER_TICKET"
                    ],
                    "isContractAdditionalCosts": False,
                    "partAContactMobile": "13345678965",
                    "isStandardTerms": "NO",
                    "isTranslation": False,
                    "id": 144004,
                    "partyEditable": True,
                    "deliveryApprove": True,
                    "canRenew": False,
                    "partBContactName": "test2",
                    "partAName": "深圳哈哈有限公司",
                    "system": "SRM",
                    "partAContactName": "test1",
                    "defaultCreateType": "NOT_DEFAULT",
                    "contractLockType": "GET_GOODS_ORDER",
                    "startDate": 1693843200000,
                    "syncStatus": "TO_BE_PUSHED",
                    "authorizedPerson": "NO",
                    "status": "ENABLE",
                    "template": False,
                    "authorizedRepresentative": "",
                    "pushOa": True,
                    "instanceId": "044edd05-4f44-4e47-8f23-439010a27fea",
                    "isDeleted": False,
                    "contractTemplateFileType": "5A75CE1A-447F-44DE-B93E-45380AC1AC80",
                    "contractTax": 47619.05,
                    "partBName": "深圳领潮供应链管理有限公司",
                    "renewalMethod": "ORIGINAL",
                    "contractLabel": "0688",
                    "accessories": {
                        "files": [
                            {
                                "name": "0476.jpg_wh1200.jpg",
                                "type": "jpg",
                                "url": "//lcscm-trantor-test.oss-cn-shenzhen.aliyuncs.com/trantor/attachments/09a88ec2-f19a-4f2a-a60a-e0ff3032a3c1.jpg"
                            }
                        ]
                    },
                    "attachmentLetter": {},
                    "oaStatus": "OA_SUCCESS",
                    "contractTaxRate": 5,
                    "paymentGroupName": "test专用_合同编号000001",
                    "salesSingFile": {
                        "files": [
                            {
                                "name": "YN.docx",
                                "type": "docx",
                                "url": "//lcscm-trantor-test.oss-cn-shenzhen.aliyuncs.com/trantor/attachments/1ef5cdc7-ec31-4d1d-a2b1-f802f60c816a.docx"
                            }
                        ]
                    },
                    "signDate": 1693843200000,
                    "contractTypeAttribute": "COMMODITY_SALES",
                    "createdAt": 1693906234000,
                    "copySignCommonStatus": "VOIDING",
                    "updatedAt": 1716971917000,
                    "contractAmountExcludingTax": 952380.95,
                    "isframeworkAgreement": "YES",
                    "updatedBy": {
                        "id": 126047
                    },
                    "isOnlinePushOa": True,
                    "isNonstandard": "NO",
                    "name": "test采购项目合同",
                    "isRemind": "OFF",
                    "partBContactEmail": "13345678966@qq.com",
                    "partAContactEmail": "13345678965@qq.com",
                    "isAvailable": True,
                    "code": "合同编号000001",
                    "remark": "test2哈哈哈",
                    "contractTotalAmount": 1000000,
                    "partBContactMobile": "13345678966",
                    "attachment": {
                        "files": [
                            {
                                "name": "0476.jpg_wh1200.jpg",
                                "type": "jpg",
                                "url": "//lcscm-trantor-test.oss-cn-shenzhen.aliyuncs.com/trantor/attachments/06d83062-7418-40d1-a522-fb19af265947.jpg"
                            },
                            {
                                "name": "0476.jpg_wh1200.jpg",
                                "type": "jpg",
                                "url": "//lcscm-trantor-test.oss-cn-shenzhen.aliyuncs.com/trantor/attachments/bb14bf96-46f0-4cdc-9b5a-7cf458a9b545.jpg"
                            }
                        ]
                    },
                    "contractDataType": "PROJECT_CONTRACT",
                    "firstEffectiveDate": 1702266518000,
                    "contractOption": "ONLINE",
                    "mobile": "",
                    "createdBy": {
                        "id": 10
                    },
                    "isOaOption": True,
                    "signCommonStatus": "VOIDING",
                    "overdueStatus": "UNEXPIRED"
                },
                "remark": "【合作事项描述】：\n1、 湖北家家有限公司为0529合同测试新建项目001@湖北家家有限公司#深圳非CRM同步的开发商，通过领潮供平台采购涂料类、电子锁，合同暂定含税总金额333,333元;\n2、 付款方式：test专用+23%支付保函\n3、 合同版本：使用我方合同模板，客户修改部分标黄\n4、 例外情况：无\n5、 项目所在地：天津天津市河东区没有详细地址\n6、 特别说明：无",
                "quotationId": {
                    "quotationFilingSonId": [
                        {
                            "code": "BJD20230524000001",
                            "id": 1,
                            "quotationType": "ASK_PRICE"
                        },
                        {
                            "code": "BJD20230525000012",
                            "id": 18,
                            "quotationType": "ASK_PRICE"
                        }
                    ],
                    "rule": "CALCULATED_AT_UNTAXED_PRICE",
                    "untaxedFormula": "销售金额=未税金额+税款金额;\n税款金额=(未税金额*税率)，运算后四舍五入保留两位小数;\n未税金额=(未税销售单价*数量)，运算后四舍五入保留两位小数;",
                    "id": 98012
                },
                "depositId": {
                    "isDeposit": "YES_DEPOSIT",
                    "paymentStr": "AFTER_SIGNING_THE_CONTRACT",
                    "billPeriod": 3,
                    "paymentContractType": "FIXED",
                    "paymentFixed": 133,
                    "id": 124010
                },
                "letterOfGuaranteeId": {
                    "isGuarantee": "YES_GUARANTEE",
                    "ofIssuance": "TAKE_ORDER_DATE",
                    "billPeriod": 7,
                    "paymentGuaranteeType": "CONTRACT_AMOUNT",
                    "paymentGuarantee": 23,
                    "id": 124010
                },
                "oaStatus": "TO_DO_SUBMIT",
                "contractOption": "ONLINE",
                "contractTemplateFileTypeId": {
                    "updatedBy": {
                        "id": 10
                    },
                    "contractType": "SALE_CONTRACT",
                    "isPartAAppoint": "NO",
                    "templateId": "7799E892-4EF4-4DDC-9416-4B0A8DA1DBDB",
                    "createdAt": 1703309692000,
                    "isStandard": "YES",
                    "annexListShow": "YES",
                    "isDeleted": False,
                    "createdBy": {
                        "id": 0
                    },
                    "contractDataType": "PROJECT_CONTRACT",
                    "name": "销售合同标准模板",
                    "id": 1,
                    "updatedAt": 1717144015000
                },
                "salesSingFile": None,
                "accessories": None,
                "contractFileAttachment": {
                    "id": None,
                    "attachmentOne": None,
                    "attachmentTwo": None,
                    "attachmentThree": None,
                    "attachmentFour": None,
                    "attachmentFive": None,
                    "attachmentSix": None,
                    "attachmentSeven": None,
                    "attachmentEight": None,
                    "attachmentNine": None,
                    "attachmentTen": None,
                    "attachmentEleven": None
                },
                "contractSignOption": "ONLINE_SIGN",
                "isOaOption": True,
                "authorizedPerson": "NO",
                "attachment": None,
                "designatedDistributor": [
                    {
                        "protocolCode": "测试合同001",
                        "protocolName": "测试合同001",
                        "supplierId": "138017",
                        "supplierCode": "CO20230705000002",
                        "supplierName": "深圳哈哈有限公司",
                        "supplierType": "pps",
                        "id": "1380173"
                    },
                    {
                        "protocolCode": "LC20240515002",
                        "protocolName": "LC20240515002",
                        "supplierId": "138017",
                        "supplierCode": "CO20230705000002",
                        "supplierName": "深圳哈哈有限公司",
                        "supplierType": "pps",
                        "id": "1380174"
                    },
                    {
                        "protocolCode": "CG2024051101111",
                        "protocolName": "上下游回写测试-订、到货、结算40/40/40",
                        "supplierId": "138017",
                        "supplierCode": "CO20230705000002",
                        "supplierName": "深圳哈哈有限公司",
                        "supplierType": "pps",
                        "id": "1380176"
                    },
                    {
                        "protocolCode": "CG202405110000022",
                        "protocolName": "上下游回写测试到货/结算/质保80/15/5",
                        "supplierId": "138017",
                        "supplierCode": "CO20230705000002",
                        "supplierName": "深圳哈哈有限公司",
                        "supplierType": "pps",
                        "id": "1380175"
                    },
                    {
                        "protocolCode": "ht202408234",
                        "protocolName": "测试线上签署撤回",
                        "supplierId": "138017",
                        "supplierCode": "CO20230705000002",
                        "supplierName": "深圳哈哈有限公司",
                        "supplierType": "pps",
                        "id": "1380178"
                    },
                    {
                        "protocolCode": "2024022900001",
                        "protocolName": "2024022900001采购合同",
                        "supplierId": "138017",
                        "supplierCode": "CO20230705000002",
                        "supplierName": "深圳哈哈有限公司",
                        "supplierType": "pps",
                        "id": "1380177"
                    },
                    {
                        "protocolCode": "HT202402291735",
                        "protocolName": "测试线上合同撤回及合同文件",
                        "supplierId": "138017",
                        "supplierCode": "CO20230705000002",
                        "supplierName": "深圳哈哈有限公司",
                        "supplierType": "pps",
                        "id": "1380179"
                    },
                    {
                        "protocolCode": "哈哈哈纯净水合同001",
                        "protocolName": "哈哈哈纯净水合同001",
                        "supplierId": "138017",
                        "supplierCode": "CO20230705000002",
                        "supplierName": "深圳哈哈有限公司",
                        "supplierType": "pps",
                        "id": "13801710"
                    },
                    {
                        "protocolCode": "HT202401250001",
                        "protocolName": "哈哈采购娃哈哈办公用水合同",
                        "supplierId": "138017",
                        "supplierCode": "CO20230705000002",
                        "supplierName": "深圳哈哈有限公司",
                        "supplierType": "pps",
                        "id": "13801711"
                    },
                    {
                        "protocolCode": "f0cdc16c581d1",
                        "protocolName": "哈哈-立邦-合同01号",
                        "supplierId": "138017",
                        "supplierCode": "CO20230705000002",
                        "supplierName": "深圳哈哈有限公司",
                        "supplierType": "pps",
                        "id": "1380170"
                    },
                    {
                        "protocolCode": "哈哈锁智能芯合同-01",
                        "protocolName": "哈哈锁智能芯合同",
                        "supplierId": "138017",
                        "supplierCode": "CO20230705000002",
                        "supplierName": "深圳哈哈有限公司",
                        "supplierType": "pps",
                        "id": "1380171"
                    },
                    {
                        "protocolCode": "hahahetong001",
                        "protocolName": "哈哈智能电子锁合同",
                        "supplierId": "138017",
                        "supplierCode": "CO20230705000002",
                        "supplierName": "深圳哈哈有限公司",
                        "supplierType": "pps",
                        "id": "1380172"
                    }
                ],
                "partAContactName": "甲方联系人",
                "partAContactMobile": "133111111111",
                "partAContactEmail": None,
                "partBContactName": "乙方联系人",
                "partBContactMobile": "133111111112",
                "partBContactEmail": None,
                "isTranslation": False,
                "translationSupplier": [],
                "isContractAdditionalCosts": False,
                "additionalCostConfigList": [
                    {
                        "uuid": "7dbe2640-1d04-401b-bfdc-891d7be41b04",
                        "configDetailList": [
                            {
                                "uuid": "fb0858c7-9660-48de-8e7e-93dbf1b3fe80",
                                "calculateBase": "ARRIVAL",
                                "calculateTimeType": "CHECK_CONFIRM",
                                "calculateTimeDay": 0,
                                "calculateTimeCustom": None,
                                "calculateAccountPeriodTime": 0,
                                "calculateAccountPeriodType": "MONTH",
                                "interestRateType": "MONTH",
                                "interestRate": 0,
                                "calculateFormula": "MONTH_MONTH"
                            }
                        ],
                        "configToSupplier": None,
                        "category": None,
                        "categoryList": None
                    }
                ],
                "contractPaymentItermList": [
                    {
                        "__trantorExtendFields": {},
                        "code": "PI20230905000002",
                        "comment": "test专用-接口专用",
                        "contractPaymentConditionList": [
                            {
                                "__trantorExtendFields": {},
                                "createdAt": 1717379037000,
                                "createdBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                },
                                "invoicing": 10,
                                "isDeleted": False,
                                "node": "ORDER_PREPAYMENT",
                                "originPaymentConditionId": 54007,
                                "paymenType": "NATURE_DAY",
                                "paymentDay": 0,
                                "percent": 10,
                                "startingDate": "ORDER_AFTER",
                                "updatedAt": 1717379037000,
                                "updatedBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                }
                            },
                            {
                                "__trantorExtendFields": {},
                                "createdAt": 1717379037000,
                                "createdBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                },
                                "invoicing": 10,
                                "isDeleted": False,
                                "node": "GET_GOODS_PREPAYMENT",
                                "originPaymentConditionId": 54008,
                                "paymenType": "NATURE_DAY",
                                "paymentDay": 0,
                                "percent": 10,
                                "startingDate": "GET_GOODS_ORDER_AFTER",
                                "updatedAt": 1717379037000,
                                "updatedBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                }
                            },
                            {
                                "__trantorExtendFields": {},
                                "createdAt": 1717379037000,
                                "createdBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                },
                                "invoicing": 30,
                                "isDeleted": False,
                                "node": "ARRIVAL_ACCEPT_PAYMENT",
                                "originPaymentConditionId": 54009,
                                "paymenType": "NATURE_DAY",
                                "paymentDay": 0,
                                "percent": 30,
                                "startingDate": "ACCEPTANCE_AFTER",
                                "updatedAt": 1717379037000,
                                "updatedBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                }
                            },
                            {
                                "__trantorExtendFields": {},
                                "createdAt": 1717379037000,
                                "createdBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                },
                                "invoicing": 30,
                                "isDeleted": False,
                                "node": "INSTALL_ACCEPT_PAYMENT",
                                "originPaymentConditionId": 54010,
                                "paymenType": "NATURE_DAY",
                                "paymentDay": 0,
                                "percent": 30,
                                "startingDate": "INSTALLATION_ACCEPTANCE_AFTER",
                                "updatedAt": 1717379037000,
                                "updatedBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                }
                            },
                            {
                                "__trantorExtendFields": {},
                                "createdAt": 1717379037000,
                                "createdBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                },
                                "invoicing": 10,
                                "isDeleted": False,
                                "node": "SETTLEMENT_PAYMENT",
                                "originPaymentConditionId": 54011,
                                "paymenType": "NATURE_DAY",
                                "paymentDay": 0,
                                "percent": 10,
                                "startingDate": "AFTER_PROJECT_AFTER",
                                "updatedAt": 1717379037000,
                                "updatedBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                }
                            },
                            {
                                "__trantorExtendFields": {},
                                "createdAt": 1717379037000,
                                "createdBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                },
                                "invoicing": 10,
                                "isDeleted": False,
                                "node": "RETENTION_MONEY",
                                "originPaymentConditionId": 54012,
                                "paymenType": "NATURE_DAY",
                                "paymentDay": 0,
                                "percent": 10,
                                "startingDate": "WARRANTY_CLEARING_AFTER",
                                "updatedAt": 1717379037000,
                                "updatedBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                }
                            }
                        ],
                        "createdAt": 1717379037000,
                        "createdBy": {
                            "__trantorExtendFields": {},
                            "id": 10
                        },
                        "describe": "需求单/订单/到货/安装/结算/质保 (10.00/10.00/30.00/30.00/10.00/10.00)",
                        "installOption": "ONLY_SUPPLY",
                        "invoicingDescribe": "需求单/订单/到货/安装/结算/质保 (10.00/10.00/30.00/30.00/10.00/10.00/",
                        "isDefaultCreate": False,
                        "isDeleted": False,
                        "mdCategory": {
                            "__trantorExtendFields": {},
                            "extraJson": {},
                            "id": 4842,
                            "name": "电子锁"
                        },
                        "name": "test专用",
                        "originPaymentGroupId": 44002,
                        "originPaymentItermId": 54002,
                        "paymentItermUuid": "35ace3ff-1e46-11ef-b404-6ae8f00e13cc",
                        "radix": 100,
                        "sort": 171,
                        "status": "ENABLE",
                        "type": "SALE",
                        "updatedAt": 1717379037000,
                        "updatedBy": {
                            "__trantorExtendFields": {},
                            "id": 10
                        }
                    },
                    {
                        "__trantorExtendFields": {},
                        "code": "PI20230905000002",
                        "comment": "test专用-接口专用",
                        "contractPaymentConditionList": [
                            {
                                "__trantorExtendFields": {},
                                "createdAt": 1717379037000,
                                "createdBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                },
                                "invoicing": 10,
                                "isDeleted": False,
                                "node": "ORDER_PREPAYMENT",
                                "originPaymentConditionId": 54007,
                                "paymenType": "NATURE_DAY",
                                "paymentDay": 0,
                                "percent": 10,
                                "startingDate": "ORDER_AFTER",
                                "updatedAt": 1717379037000,
                                "updatedBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                }
                            },
                            {
                                "__trantorExtendFields": {},
                                "createdAt": 1717379037000,
                                "createdBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                },
                                "invoicing": 10,
                                "isDeleted": False,
                                "node": "GET_GOODS_PREPAYMENT",
                                "originPaymentConditionId": 54008,
                                "paymenType": "NATURE_DAY",
                                "paymentDay": 0,
                                "percent": 10,
                                "startingDate": "GET_GOODS_ORDER_AFTER",
                                "updatedAt": 1717379037000,
                                "updatedBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                }
                            },
                            {
                                "__trantorExtendFields": {},
                                "createdAt": 1717379037000,
                                "createdBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                },
                                "invoicing": 30,
                                "isDeleted": False,
                                "node": "ARRIVAL_ACCEPT_PAYMENT",
                                "originPaymentConditionId": 54009,
                                "paymenType": "NATURE_DAY",
                                "paymentDay": 0,
                                "percent": 30,
                                "startingDate": "ACCEPTANCE_AFTER",
                                "updatedAt": 1717379037000,
                                "updatedBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                }
                            },
                            {
                                "__trantorExtendFields": {},
                                "createdAt": 1717379037000,
                                "createdBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                },
                                "invoicing": 30,
                                "isDeleted": False,
                                "node": "INSTALL_ACCEPT_PAYMENT",
                                "originPaymentConditionId": 54010,
                                "paymenType": "NATURE_DAY",
                                "paymentDay": 0,
                                "percent": 30,
                                "startingDate": "INSTALLATION_ACCEPTANCE_AFTER",
                                "updatedAt": 1717379037000,
                                "updatedBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                }
                            },
                            {
                                "__trantorExtendFields": {},
                                "createdAt": 1717379037000,
                                "createdBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                },
                                "invoicing": 10,
                                "isDeleted": False,
                                "node": "SETTLEMENT_PAYMENT",
                                "originPaymentConditionId": 54011,
                                "paymenType": "NATURE_DAY",
                                "paymentDay": 0,
                                "percent": 10,
                                "startingDate": "AFTER_PROJECT_AFTER",
                                "updatedAt": 1717379037000,
                                "updatedBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                }
                            },
                            {
                                "__trantorExtendFields": {},
                                "createdAt": 1717379037000,
                                "createdBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                },
                                "invoicing": 10,
                                "isDeleted": False,
                                "node": "RETENTION_MONEY",
                                "originPaymentConditionId": 54012,
                                "paymenType": "NATURE_DAY",
                                "paymentDay": 0,
                                "percent": 10,
                                "startingDate": "WARRANTY_CLEARING_AFTER",
                                "updatedAt": 1717379037000,
                                "updatedBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                }
                            }
                        ],
                        "createdAt": 1717379037000,
                        "createdBy": {
                            "__trantorExtendFields": {},
                            "id": 10
                        },
                        "describe": "需求单/订单/到货/安装/结算/质保 (10.00/10.00/30.00/30.00/10.00/10.00)",
                        "installOption": "SUPPLY_INSTALL",
                        "invoicingDescribe": "需求单/订单/到货/安装/结算/质保 (10.00/10.00/30.00/30.00/10.00/10.00/",
                        "isDefaultCreate": False,
                        "isDeleted": False,
                        "mdCategory": {
                            "__trantorExtendFields": {},
                            "extraJson": {},
                            "id": 4842,
                            "name": "电子锁"
                        },
                        "name": "test专用",
                        "originPaymentGroupId": 44002,
                        "originPaymentItermId": 54002,
                        "paymentItermUuid": "35ace4b9-1e46-11ef-b404-6ae8f00e13cc",
                        "radix": 100,
                        "sort": 171,
                        "status": "ENABLE",
                        "type": "SALE",
                        "updatedAt": 1717379037000,
                        "updatedBy": {
                            "__trantorExtendFields": {},
                            "id": 10
                        }
                    },
                    {
                        "__trantorExtendFields": {},
                        "code": "PI20210628000001",
                        "comment": "订单预付100%",
                        "contractPaymentConditionList": [
                            {
                                "__trantorExtendFields": {},
                                "createdAt": 1717379037000,
                                "createdBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                },
                                "invoicing": 0,
                                "isDeleted": False,
                                "node": "ORDER_PREPAYMENT",
                                "originPaymentConditionId": 1,
                                "paymenType": "NATURE_DAY",
                                "paymentDay": 0,
                                "percent": 0,
                                "startingDate": "ORDER_AFTER",
                                "updatedAt": 1717379037000,
                                "updatedBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                }
                            },
                            {
                                "__trantorExtendFields": {},
                                "createdAt": 1717379037000,
                                "createdBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                },
                                "invoicing": 100,
                                "isDeleted": False,
                                "node": "GET_GOODS_PREPAYMENT",
                                "originPaymentConditionId": 2,
                                "paymenType": "NATURE_DAY",
                                "paymentDay": 0,
                                "percent": 100,
                                "startingDate": "GET_GOODS_ORDER_AFTER",
                                "updatedAt": 1717379037000,
                                "updatedBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                }
                            },
                            {
                                "__trantorExtendFields": {},
                                "createdAt": 1717379037000,
                                "createdBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                },
                                "invoicing": 0,
                                "isDeleted": False,
                                "node": "ARRIVAL_ACCEPT_PAYMENT",
                                "originPaymentConditionId": 4,
                                "paymenType": "NATURE_DAY",
                                "paymentDay": 0,
                                "percent": 0,
                                "startingDate": "ACCEPTANCE_AFTER",
                                "updatedAt": 1717379037000,
                                "updatedBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                }
                            },
                            {
                                "__trantorExtendFields": {},
                                "createdAt": 1717379037000,
                                "createdBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                },
                                "invoicing": 0,
                                "isDeleted": False,
                                "node": "INSTALL_ACCEPT_PAYMENT",
                                "originPaymentConditionId": 5,
                                "paymenType": "NATURE_DAY",
                                "paymentDay": 0,
                                "percent": 0,
                                "startingDate": "INSTALLATION_ACCEPTANCE_AFTER",
                                "updatedAt": 1717379037000,
                                "updatedBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                }
                            },
                            {
                                "__trantorExtendFields": {},
                                "createdAt": 1717379037000,
                                "createdBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                },
                                "invoicing": 0,
                                "isDeleted": False,
                                "node": "SETTLEMENT_PAYMENT",
                                "originPaymentConditionId": 6,
                                "paymenType": "NATURE_DAY",
                                "paymentDay": 0,
                                "percent": 0,
                                "startingDate": "AFTER_PROJECT_AFTER",
                                "updatedAt": 1717379037000,
                                "updatedBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                }
                            },
                            {
                                "__trantorExtendFields": {},
                                "createdAt": 1717379037000,
                                "createdBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                },
                                "invoicing": 0,
                                "isDeleted": False,
                                "node": "RETENTION_MONEY",
                                "originPaymentConditionId": 7,
                                "paymenType": "NATURE_DAY",
                                "paymentDay": 0,
                                "percent": 0,
                                "startingDate": "WARRANTY_CLEARING_AFTER",
                                "updatedAt": 1717379037000,
                                "updatedBy": {
                                    "__trantorExtendFields": {},
                                    "id": 10
                                }
                            }
                        ],
                        "createdAt": 1717379037000,
                        "createdBy": {
                            "__trantorExtendFields": {},
                            "id": 10
                        },
                        "describe": "需求单/订单/到货/安装/结算/质保 (0.00/100.00/0.00/0.00/0.00/0.00)",
                        "installOption": "ONLY_SUPPLY",
                        "invoicingDescribe": "需求单/订单/到货/安装/结算/质保 (0.00/100.00/0.00/0.00/0.00/0.00/",
                        "isDefaultCreate": False,
                        "isDeleted": False,
                        "mdCategory": {
                            "__trantorExtendFields": {},
                            "extraJson": {},
                            "id": 4804,
                            "name": "涂料类"
                        },
                        "name": "【PSL销售】订单预付100%",
                        "originPaymentItermId": 1,
                        "paymentItermUuid": "35ace6f6-1e46-11ef-b404-6ae8f00e13cc",
                        "radix": 100,
                        "sort": 2,
                        "status": "ENABLE",
                        "type": "SALE",
                        "updatedAt": 1717379037000,
                        "updatedBy": {
                            "__trantorExtendFields": {},
                            "id": 10
                        }
                    }
                ],
                "submitHandle": True
            }
        ],
        "modelKey": "contract_domain_Contract"
    }
}

data2 ={
    "frontendContext": {},
    "actionKey": "partner_center_Project_ProjectSingleDataAction::getProjectDetail",
    "context": {
        "env": {
            "projectId": 52004
        },
        "record": [
            {
                "projectId": 52004
            }
        ],
        "modelKey": "partner_center_Project"
    }
}
