url1 ="https://staging-gateway.test.lcscm.cn/zhonghai/item-center/itemcenter/1004704/api/trantor/data-source"

data1 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "itemcenter_FrontItemVO",
	"sourceModel": "itemcenter_FrontItemVO",
	"searchValues": {
		"itemCode": {
			"type": "One",
			"value": "110202901050044"
		}
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
				"fieldName": "sourceFrom"
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
				"fieldName": "projectName"
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

data2 = {
	"frontendContext": {},
	"singleResult": True,
	"targetModel": "itemcenter_ItemVO",
	"sourceModel": "itemcenter_ItemVO",
	"queryValues": {
		"itemCode": {
			"type": "One",
			"value": "110202901050044"
		},
		"virtualPrice": {
			"type": "One",
			"value": ""
		},
		"type": {
			"type": "One",
			"value": 1
		},
		"isSpecialItem": {
			"type": "One",
			"value": "1"
		},
		"createdAt": {
			"type": "One",
			"value": 1693811805000
		},
		"sellerId": {
			"type": "One",
			"value": "278001"
		},
		"digitalSyncStatus": {
			"type": "One",
			"value": "default"
		},
		"id": {
			"type": "One",
			"value": 110202901050044
		},
		"updatedAt": {
			"type": "One",
			"value": 1721983272000
		},
		"image": {
			"type": "One",
			"value": "http://lcscm-trantor.oss-cn-shenzhen.aliyuncs.com/images/manage/1000001/20e8febb-28f6-4147-a714-f9b0d68a3972/9325fb26-6aad-44d4-80f6-6e7044aa4b04领潮.jpg"
		},
		"brandName": {
			"type": "One",
			"value": "戴科"
		},
		"version": {
			"type": "One",
			"value": 0
		},
		"name": {
			"type": "One",
			"value": "戴科 WDZBN-KYJY-4*1.5 上海真如境5#地块项目"
		},
		"leadTrendYn": {
			"type": "One",
			"value": "0"
		},
		"status": {
			"type": "One",
			"value": -1
		},
		"itemType": {
			"type": "One",
			"value": "实物商品"
		},
		"skuList": {
			"type": "Collection",
			"values": [
				110202901050044
			]
		},
		"deletable": {
			"type": "One",
			"value": True
		},
		"shopNames": {
			"type": "Collection",
			"values": [
				None
			]
		},
		"itemMarkupRate": {
			"type": "One",
			"value": "2.03%"
		},
		"salePriceRange": {
			"type": "One",
			"value": "¥6.52"
		},
		"shopIds": {
			"type": "Collection",
			"values": [
						None
			]
		},
		"contractName": {
			"type": "One",
			"value": "2024-2025年度电线电缆（戴科）集中采购合同\r\n"
		},
		"quickOrder": {
			"type": "One",
			"value": "0"
		},
		"createdName": {
			"type": "One",
			"value": ""
		},
		"sourceFrom": {
			"type": "One",
			"value": "领潮"
		},
		"editable": {
			"type": "One",
			"value": True
		},
		"isSyncDigital": {
			"type": "One",
			"value": 0
		},
		"updatedByName": {
			"type": "One",
			"value": "谢维"
		},
		"specification": {
			"type": "One",
			"value": "WDZBN-KYJY-4*1.5"
		},
		"userId": {
			"type": "One",
			"value": 10
		},
		"auditStatus": {
			"type": "One",
			"value": 2
		},
		"itemSource": {
			"type": "One",
			"value": "中海发展供应链公司"
		},
		"digitalStatus": {
			"type": "One",
			"value": -1
		},
		"category": {
			"type": "One",
			"value": "电缆(戴科)(5122)"
		},
		"businessType": {
			"type": "One",
			"value": 1
		},
		"costPriceRange": {
			"type": "One",
			"value": "¥6.39"
		}
	},
	"dataSource": {
		"actionKey": "itemcenter_ItemVO_item_update"
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
				"fieldName": "contract",
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
				"fieldName": "itemLevel"
			},
			{
				"fieldName": "districtList"
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
				"fieldName": "projectName"
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
				"fieldName": "digitalStatus"
			},
			{
				"fieldName": "digitalSyncStatus"
			},
			{
				"fieldName": "digitalSyncError"
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
				"fieldName": "version"
			},
			{
				"fieldName": "itemSource"
			}
		]
	}
}

url3 ="https://staging-gateway.test.lcscm.cn/zhonghai/item-center/itemcenter/1004704/api/trantor/action/exe"
data3 = {
	"frontendContext": {},
	"actionKey": "itemcenter_ItemVO_ItemAction::update",
	"context": {
		"modelKey": "itemcenter_ItemVO",
		"actionLabel": "提交",
		"record": [
			{
				"category": {
					"id": 5122
				},
				"type": 1,
				"itemCode": "110202901050044",
				"name": "戴科 WDZBN-KYJY-4*1.5 上海真如境5#地块项目",
				"shortName": "戴科",
				"b2bPartnerVO": {
					"code": "P20240726000001S",
					"name": "上海戴科投资集团有限公司",
					"enterpriseId": 278001,
					"id": 264001
				},
				"brand": {
					"updatedBy": "User(super=BaseModel(super=RootModel(id=10, __trantorExtendFields={}), createdAt=None, updatedAt=None, isDeleted=None, createdBy=None, updatedBy=None), username=None, nickname=None, avatar=None, mobile=None, email=None, password=None, pwdExpireAt=None, enabled=None, locked=None)",
					"createdAt": 1617868150000,
					"enName": "Décor",
					"name": "戴科",
					"logo": "//lcscm-trantor-test.oss-cn-shenzhen.aliyuncs.com/trantor/attachments/8a0c8316-8b35-4046-a05e-7d2910a19a77.png",
					"id": 2028,
					"updatedAt": 1721983272000
				},
				"contract": {
					"id": 73,
					"name": "2024-2025年度电线电缆（戴科）集中采购合同"
				},
				"itemLevel": "S",
				"districtList": None,
				"originPlace": None,
				"invoiceCategoryVO": {
					"code": "109040999",
					"name": "其他电线电缆",
					"id": 100000003563
				},
				"taxRate": "13%",
				"supplyCycle": 30,
				"minOrderNumber": 1,
				"deliveryFeeTemplates": None,
				"installFeeTemplates": None,
				"unit": "件",
				"leadTrendYn": "0",
				"specialYn": "0",
				"priceAdjustYn": "0",
				"isSpecialItem": 1,
				"specialSupply": [
					{
						"name": "湖北家家有限公司",
						"id": 138013
					},
					{
						"name": "湖北家家有限公司",
						"id": 4038
					},
					{
						"unifiedSocialCreditCode": "91330100799655058A",
						"code": "CO20230718000004",
						"name": "中国阿里巴巴有限公司",
						"id": 142041
					}
				],
				"projectName": None,
				"videoUrl": None,
				"specification": "WDZBN-KYJY-4*1.5",
				"isSyncDigital": 0,
				"digitalStatus": -1,
				"digitalSyncStatus": "default",
				"digitalSyncError": None,
				"advertise": None,
				"keyword": None,
				"mainImageAttachment": {
					"files": [
						{
							"name": "领潮",
							"type": "jpg",
							"url": "http://lcscm-trantor.oss-cn-shenzhen.aliyuncs.com/images/manage/1000001/20e8febb-28f6-4147-a714-f9b0d68a3972/9325fb26-6aad-44d4-80f6-6e7044aa4b04领潮.jpg"
						}
					]
				},
				"itemChartlet": None,
				"itemModel": None,
				"showVirtualPrice": "NOT",
				"version": 0,
				"itemSource": "中海发展供应链公司",
				"id": 110202901050044,
				"categoryAttributes": [
					{
						"updatedBy": "User(super=BaseModel(super=RootModel(id=10, __trantorExtendFields={}), createdAt=None, updatedAt=None, isDeleted=None, createdBy=None, updatedBy=None), username=None, nickname=None, avatar=None, mobile=None, email=None, password=None, pwdExpireAt=None, enabled=None, locked=None)",
						"values": [
							"电缆"
						],
						"customizable": True,
						"displayable": False,
						"salable": False,
						"searchable": True,
						"required": False,
						"attributeId": 40090,
						"createdAt": 1624987246000,
						"valueType": 0,
						"tenantId": 1,
						"name": "二级分类",
						"valueHolder": "电缆",
						"id": 40090,
						"categoryId": 5122,
						"group": "BASIC",
						"status": 1,
						"updatedAt": 1663812337000
					},
					{
						"updatedBy": "User(super=BaseModel(super=RootModel(id=None, __trantorExtendFields={}), createdAt=None, updatedAt=None, isDeleted=None, createdBy=None, updatedBy=None), username=None, nickname=None, avatar=None, mobile=None, email=None, password=None, pwdExpireAt=None, enabled=None, locked=None)",
						"customizable": True,
						"displayable": True,
						"salable": False,
						"searchable": True,
						"required": False,
						"attributeId": 40091,
						"createdAt": 1624987246000,
						"valueType": 0,
						"tenantId": 1,
						"name": "标称截面积",
						"valueHolder": "",
						"id": 40091,
						"categoryId": 5122,
						"group": "BASIC",
						"status": 1,
						"updatedAt": 1624987246000
					},
					{
						"updatedBy": "User(super=BaseModel(super=RootModel(id=10, __trantorExtendFields={}), createdAt=None, updatedAt=None, isDeleted=None, createdBy=None, updatedBy=None), username=None, nickname=None, avatar=None, mobile=None, email=None, password=None, pwdExpireAt=None, enabled=None, locked=None)",
						"values": [
							"普通",
							"A类阻燃",
							"B类阻燃",
							"C类阻燃",
							"耐火",
							"A类阻燃/耐火",
							"B类阻燃/耐火",
							"C类阻燃/耐火",
							"阻燃/无卤低烟",
							"A类阻燃/无卤低烟",
							"B类阻燃/无卤低烟",
							"C类阻燃/无卤低烟",
							"A类阻燃/耐火/无卤低烟",
							"B类阻燃/耐火/无卤低烟",
							"C类阻燃/耐火/无卤低烟",
							"阻燃/耐火/无卤低烟",
							"铠装",
							"A类阻燃/铠装",
							"B类阻燃/铠装",
							"C类阻燃/铠装",
							"A类阻燃/耐火/铠装",
							"B类阻燃/耐火/铠装",
							"C类阻燃/耐火/铠装",
							"耐火/铠装",
							"A类阻燃/无卤低烟/铠装",
							"B类阻燃/无卤低烟/铠装",
							"C类阻燃/无卤低烟/铠装",
							"C类阻燃/耐火/无卤低烟/铠装",
							"A类阻燃/耐火/无卤低烟/铠装",
							"B类阻燃/耐火/无卤低烟/铠装",
							"屏蔽",
							"防水",
							"矿物",
							"高压",
							"C类阻燃/高压",
							"铠装/高压",
							"C类阻燃/铠装/高压",
							"C类阻燃/无卤低烟/高压",
							"C类阻燃/无卤低烟/铠装/高压",
							"预分支",
							"A类阻燃/预分支",
							"B类阻燃/预分支",
							"C类阻燃/预分支",
							"铠装/预分支",
							"A类阻燃/铠装/预分支",
							"B类阻燃/铠装/预分支",
							"C类阻燃/铠装/预分支",
							"耐火/预分支",
							"A类阻燃/耐火/预分支",
							"B类阻燃/耐火/预分支",
							"C类阻燃/耐火/预分支",
							"耐火/铠装/预分支",
							"A类阻燃/耐火/铠装/预分支",
							"B类阻燃/耐火/铠装/预分支",
							"C类阻燃/耐火/铠装/预分支",
							"A类阻燃/无卤低烟/铠装/预分支",
							"B类阻燃/无卤低烟/铠装/预分支",
							"C类阻燃/无卤低烟/铠装/预分支",
							"A类阻燃/耐火/无卤低烟/铠装/预分支",
							"B类阻燃/耐火/无卤低烟/铠装/预分支",
							"C类阻燃/耐火/无卤低烟/铠装/预分支",
							"预分支/矿物",
							"配件"
						],
						"customizable": True,
						"displayable": False,
						"salable": False,
						"searchable": True,
						"required": False,
						"attributeId": 40092,
						"createdAt": 1624987246000,
						"valueType": 0,
						"tenantId": 1,
						"name": "类别",
						"valueHolder": "普通,A类阻燃,B类阻燃,C类阻燃,耐火,A类阻燃/耐火,B类阻燃/耐火,C类阻燃/耐火,阻燃/无卤低烟,A类阻燃/无卤低烟,B类阻燃/无卤低烟,C类阻燃/无卤低烟,A类阻燃/耐火/无卤低烟,B类阻燃/耐火/无卤低烟,C类阻燃/耐火/无卤低烟,阻燃/耐火/无卤低烟,铠装,A类阻燃/铠装,B类阻燃/铠装,C类阻燃/铠装,A类阻燃/耐火/铠装,B类阻燃/耐火/铠装,C类阻燃/耐火/铠装,耐火/铠装,A类阻燃/无卤低烟/铠装,B类阻燃/无卤低烟/铠装,C类阻燃/无卤低烟/铠装,C类阻燃/耐火/无卤低烟/铠装,A类阻燃/耐火/无卤低烟/铠装,B类阻燃/耐火/无卤低烟/铠装,屏蔽,防水,矿物,高压,C类阻燃/高压,铠装/高压,C类阻燃/铠装/高压,C类阻燃/无卤低烟/高压,C类阻燃/无卤低烟/铠装/高压,预分支,A类阻燃/预分支,B类阻燃/预分支,C类阻燃/预分支,铠装/预分支,A类阻燃/铠装/预分支,B类阻燃/铠装/预分支,C类阻燃/铠装/预分支,耐火/预分支,A类阻燃/耐火/预分支,B类阻燃/耐火/预分支,C类阻燃/耐火/预分支,耐火/铠装/预分支,A类阻燃/耐火/铠装/预分支,B类阻燃/耐火/铠装/预分支,C类阻燃/耐火/铠装/预分支,A类阻燃/无卤低烟/铠装/预分支,B类阻燃/无卤低烟/铠装/预分支,C类阻燃/无卤低烟/铠装/预分支,A类阻燃/耐火/无卤低烟/铠装/预分支,B类阻燃/耐火/无卤低烟/铠装/预分支,C类阻燃/耐火/无卤低烟/铠装/预分支,预分支/矿物,配件",
						"id": 40092,
						"categoryId": 5122,
						"group": "BASIC",
						"status": 1,
						"updatedAt": 1663839605000
					},
					{
						"updatedBy": "User(super=BaseModel(super=RootModel(id=10, __trantorExtendFields={}), createdAt=None, updatedAt=None, isDeleted=None, createdBy=None, updatedBy=None), username=None, nickname=None, avatar=None, mobile=None, email=None, password=None, pwdExpireAt=None, enabled=None, locked=None)",
						"values": [
							"1.347",
							"1.853",
							"2.661",
							"3.682",
							"2.336",
							"3.252",
							"9.416",
							"11.755",
							"15.41",
							"8.324",
							"10.444",
							"13.812",
							"17.268",
							"21.756",
							"0.065",
							"0.105",
							"0.17",
							"0.255",
							"0.435",
							"0.69",
							"1.065",
							"1.485",
							"2.02",
							"2.92",
							"4.065",
							"5.135",
							"6.325",
							"7.915",
							"10.405",
							"13.055",
							"17.265",
							"21.585",
							"27.195",
							"0.47",
							"0.734",
							"0.993",
							"1.433",
							"2.029",
							"2.763",
							"3.41",
							"4.317",
							"5.223",
							"6.82",
							"8.59",
							"11.655",
							"0.077",
							"0.125",
							"0.189",
							"0.315",
							"0.506",
							"0.791",
							"1.049",
							"1.432",
							"2.057",
							"2.848",
							"3.675",
							"4.398",
							"5.583",
							"7.298",
							"9.134",
							"11.957",
							"0.091",
							"0.146",
							"0.224",
							"0.368",
							"0.597",
							"0.928",
							"1.182",
							"1.661",
							"2.371",
							"3.272",
							"4.278",
							"4.984",
							"6.397",
							"8.356",
							"13.554",
							"0.099",
							"0.159",
							"0.241",
							"0.405",
							"0.648",
							"1.008",
							"4.705",
							"5.668",
							"7.2",
							"0.013",
							"0.021",
							"0.034",
							"0.051",
							"0.087",
							"0.138",
							"0.213",
							"0.297",
							"0.404",
							"0.584",
							"0.813",
							"1.027",
							"1.265",
							"1.583",
							"2.081",
							"2.611",
							"3.453",
							"5.439",
							"0.026",
							"0.042",
							"0.068",
							"0.102",
							"0.174",
							"0.276",
							"0.426",
							"0.594",
							"0.808",
							"1.168",
							"1.626",
							"2.054",
							"2.53",
							"3.166",
							"4.162",
							"5.222",
							"6.906",
							"8.634",
							"10.878",
							"0.153",
							"1.752",
							"2.439",
							"6.243",
							"7.833",
							"10.359",
							"12.951",
							"16.317",
							"0.204",
							"0.036",
							"0.176",
							"0.227",
							"0.305",
							"0.392",
							"0.486",
							"0.665",
							"0.887",
							"1.139",
							"1.392",
							"1.652",
							"1.996",
							"2.621",
							"3.188",
							"3.982",
							"0.071",
							"0.335",
							"0.56",
							"0.81",
							"0.975",
							"1.325",
							"1.775",
							"2.275",
							"2.784",
							"0.498",
							"0.375",
							"1.592",
							"2.12",
							"2.769",
							"3.672",
							"4.004",
							"2.649",
							"3.22",
							"3.995",
							"0.46",
							"1.002",
							"1.888",
							"2.461",
							"3.35",
							"4.445",
							"3.53",
							"0.178",
							"0.499",
							"0.781",
							"1.157",
							"1.692",
							"2.269",
							"2.956",
							"5.372",
							"6.96",
							"0.806",
							"1.171",
							"4.627",
							"0.3",
							"0.401",
							"0.612",
							"0.835",
							"1.163",
							"1.452",
							"1.901",
							"2.696",
							"3.555",
							"5.025",
							"0.365",
							"0.742",
							"0.943",
							"1.319",
							"1.727",
							"2.246",
							"3.033",
							"5.91",
							"0.352",
							"0.725",
							"1.424",
							"6.405",
							"3.081",
							"4.108",
							"4.749",
							"6.3320",
							"0.243",
							"0.351",
							"0.567",
							"0.918",
							"1.377",
							"0.333",
							"0.481",
							"0.777",
							"1.258",
							"1.887",
							"0.052",
							"0.084",
							"0.136",
							"0.045",
							"0.063",
							"0.147",
							"0.238",
							"0.357",
							"0.072",
							"0.104",
							"0.168",
							"0.272",
							"0.408",
							"0.09",
							"0.13",
							"0.21",
							"0.34",
							"0.51",
							"0.108",
							"0.156",
							"0.252",
							"0.126",
							"0.182",
							"0.294",
							"0.476",
							"0.714",
							"0.144",
							"0.208",
							"0.336",
							"0.544",
							"0.816",
							"0.171",
							"0.247",
							"0.399",
							"0.646",
							"0.969",
							"0.216",
							"0.312",
							"0.504",
							"1.224",
							"0.27",
							"0.39",
							"0.63",
							"1.02",
							"1.53",
							"0.053",
							"0.08",
							"0.134",
							"0.214",
							"0.027",
							"0.039",
							"0.325",
							"0.452",
							"0.732",
							"1.092",
							"0.432",
							"0.603",
							"0.971",
							"1.46",
							"0.062",
							"0.082",
							"0.073",
							"0.1",
							"0.149",
							"0.231",
							"0.093",
							"0.211",
							"0.15",
							"0.346",
							"0.132",
							"0.196",
							"0.29",
							"0.151",
							"0.223",
							"0.505",
							"0.188",
							"0.387",
							"0.578",
							"0.206",
							"0.287",
							"0.44",
							"0.65",
							"0.24",
							"0.76",
							"0.41",
							"0.662",
							"0.988",
							"0.359",
							"1.21",
							"0.018",
							"0.261",
							"0.348",
							"0.372",
							"0.492",
							"0.668",
							"0.902",
							"1.175",
							"1.443",
							"1.776",
							"2.155",
							"2.754",
							"3.328",
							"4.41",
							"0.318",
							"0.592",
							"0.836",
							"0.107",
							"0.367",
							"0.54",
							"0.771",
							"1.089",
							"0.142",
							"0.453",
							"0.97",
							"0.371",
							"0.899",
							"1.126",
							"1.367",
							"1.695",
							"2.195",
							"2.732",
							"3.486",
							"5.825",
							"1.113",
							"1.995",
							"2.697",
							"3.378",
							"4.101",
							"5.085",
							"6.585",
							"8.196",
							"10.458",
							"13.335",
							"17.475"
						],
						"customizable": True,
						"displayable": True,
						"salable": False,
						"searchable": True,
						"required": False,
						"attributeId": 40093,
						"createdAt": 1624987246000,
						"valueType": 0,
						"tenantId": 1,
						"name": "线密度",
						"valueHolder": "1.347,1.853,2.661,3.682,2.336,3.252,9.416,11.755,15.41,8.324,10.444,13.812,17.268,21.756,0.065,0.105,0.17,0.255,0.435,0.69,1.065,1.485,2.02,2.92,4.065,5.135,6.325,7.915,10.405,13.055,17.265,21.585,27.195,0.47,0.734,0.993,1.433,2.029,2.763,3.41,4.317,5.223,6.82,8.59,11.655,0.077,0.125,0.189,0.315,0.506,0.791,1.049,1.432,2.057,2.848,3.675,4.398,5.583,7.298,9.134,11.957,0.091,0.146,0.224,0.368,0.597,0.928,1.182,1.661,2.371,3.272,4.278,4.984,6.397,8.356,13.554,0.099,0.159,0.241,0.405,0.648,1.008,4.705,5.668,7.2,0.013,0.021,0.034,0.051,0.087,0.138,0.213,0.297,0.404,0.584,0.813,1.027,1.265,1.583,2.081,2.611,3.453,5.439,0.026,0.042,0.068,0.102,0.174,0.276,0.426,0.594,0.808,1.168,1.626,2.054,2.53,3.166,4.162,5.222,6.906,8.634,10.878,0.153,1.752,2.439,6.243,7.833,10.359,12.951,16.317,0.204,0.036,0.176,0.227,0.305,0.392,0.486,0.665,0.887,1.139,1.392,1.652,1.996,2.621,3.188,3.982,0.071,0.335,0.56,0.81,0.975,1.325,1.775,2.275,2.784,0.498,0.375,1.592,2.12,2.769,3.672,4.004,2.649,3.22,3.995,0.46,1.002,1.888,2.461,3.35,4.445,3.53,0.178,0.499,0.781,1.157,1.692,2.269,2.956,5.372,6.96,0.806,1.171,4.627,0.3,0.401,0.612,0.835,1.163,1.452,1.901,2.696,3.555,5.025,0.365,0.742,0.943,1.319,1.727,2.246,3.033,5.91,0.352,0.725,1.424,6.405,3.081,4.108,4.749,6.3320,0.243,0.351,0.567,0.918,1.377,0.333,0.481,0.777,1.258,1.887,0.052,0.084,0.136,0.045,0.063,0.147,0.238,0.357,0.072,0.104,0.168,0.272,0.408,0.09,0.13,0.21,0.34,0.51,0.108,0.156,0.252,0.126,0.182,0.294,0.476,0.714,0.144,0.208,0.336,0.544,0.816,0.171,0.247,0.399,0.646,0.969,0.216,0.312,0.504,1.224,0.27,0.39,0.63,1.02,1.53,0.053,0.08,0.134,0.214,0.027,0.039,0.325,0.452,0.732,1.092,0.432,0.603,0.971,1.46,0.062,0.082,0.073,0.1,0.149,0.231,0.093,0.211,0.15,0.346,0.132,0.196,0.29,0.151,0.223,0.505,0.188,0.387,0.578,0.206,0.287,0.44,0.65,0.24,0.76,0.41,0.662,0.988,0.359,1.21,0.018,0.261,0.348,0.372,0.492,0.668,0.902,1.175,1.443,1.776,2.155,2.754,3.328,4.41,0.318,0.592,0.836,0.107,0.367,0.54,0.771,1.089,0.142,0.453,0.97,0.371,0.899,1.126,1.367,1.695,2.195,2.732,3.486,5.825,1.113,1.995,2.697,3.378,4.101,5.085,6.585,8.196,10.458,13.335,17.475",
						"id": 40093,
						"categoryId": 5122,
						"group": "BASIC",
						"status": 1,
						"updatedAt": 1663838602000
					},
					{
						"updatedBy": "User(super=BaseModel(super=RootModel(id=None, __trantorExtendFields={}), createdAt=None, updatedAt=None, isDeleted=None, createdBy=None, updatedBy=None), username=None, nickname=None, avatar=None, mobile=None, email=None, password=None, pwdExpireAt=None, enabled=None, locked=None)",
						"customizable": True,
						"displayable": True,
						"salable": False,
						"searchable": True,
						"required": False,
						"attributeId": 40094,
						"createdAt": 1624987246000,
						"valueType": 0,
						"tenantId": 1,
						"name": "线芯数量",
						"valueHolder": "",
						"id": 40094,
						"categoryId": 5122,
						"group": "BASIC",
						"status": 1,
						"updatedAt": 1624987246000
					},
					{
						"updatedBy": "User(super=BaseModel(super=RootModel(id=None, __trantorExtendFields={}), createdAt=None, updatedAt=None, isDeleted=None, createdBy=None, updatedBy=None), username=None, nickname=None, avatar=None, mobile=None, email=None, password=None, pwdExpireAt=None, enabled=None, locked=None)",
						"customizable": True,
						"displayable": True,
						"salable": False,
						"searchable": True,
						"required": False,
						"attributeId": 40095,
						"createdAt": 1624987246000,
						"valueType": 0,
						"tenantId": 1,
						"name": "绝缘材料",
						"valueHolder": "",
						"id": 40095,
						"categoryId": 5122,
						"group": "BASIC",
						"status": 1,
						"updatedAt": 1624987246000
					},
					{
						"updatedBy": "User(super=BaseModel(super=RootModel(id=None, __trantorExtendFields={}), createdAt=None, updatedAt=None, isDeleted=None, createdBy=None, updatedBy=None), username=None, nickname=None, avatar=None, mobile=None, email=None, password=None, pwdExpireAt=None, enabled=None, locked=None)",
						"customizable": True,
						"displayable": True,
						"salable": False,
						"searchable": True,
						"required": False,
						"attributeId": 40096,
						"createdAt": 1624987246000,
						"valueType": 0,
						"tenantId": 1,
						"name": "防火等级",
						"valueHolder": "",
						"id": 40096,
						"categoryId": 5122,
						"group": "BASIC",
						"status": 1,
						"updatedAt": 1624987246000
					},
					{
						"updatedBy": "User(super=BaseModel(super=RootModel(id=None, __trantorExtendFields={}), createdAt=None, updatedAt=None, isDeleted=None, createdBy=None, updatedBy=None), username=None, nickname=None, avatar=None, mobile=None, email=None, password=None, pwdExpireAt=None, enabled=None, locked=None)",
						"values": [
							"5.0",
							"5.0",
							"5.0"
						],
						"customizable": False,
						"displayable": False,
						"salable": False,
						"searchable": False,
						"required": False,
						"attributeId": 46104,
						"createdAt": 1634019060000,
						"valueType": 1,
						"tenantId": 1,
						"name": "121",
						"valueHolder": "5.0,5.0,5.0",
						"id": 46104,
						"categoryId": 5122,
						"group": "BASIC",
						"status": 1,
						"updatedAt": 1634019093000
					},
					{
						"updatedBy": "User(super=BaseModel(super=RootModel(id=2001, __trantorExtendFields={}), createdAt=None, updatedAt=None, isDeleted=None, createdBy=None, updatedBy=None), username=None, nickname=None, avatar=None, mobile=None, email=None, password=None, pwdExpireAt=None, enabled=None, locked=None)",
						"values": [
							"1.0"
						],
						"customizable": False,
						"displayable": True,
						"salable": False,
						"searchable": False,
						"required": False,
						"attributeId": 68013,
						"createdAt": 1679472813000,
						"valueType": 1,
						"tenantId": 1,
						"name": "1",
						"valueHolder": "1.0",
						"id": 68013,
						"categoryId": 5122,
						"group": "BASIC",
						"status": 1,
						"updatedAt": 1679472813000
					},
					{
						"updatedBy": "User(super=BaseModel(super=RootModel(id=10, __trantorExtendFields={}), createdAt=None, updatedAt=None, isDeleted=None, createdBy=None, updatedBy=None), username=None, nickname=None, avatar=None, mobile=None, email=None, password=None, pwdExpireAt=None, enabled=None, locked=None)",
						"values": [],
						"customizable": True,
						"displayable": True,
						"salable": False,
						"searchable": False,
						"required": True,
						"attributeId": 128001,
						"createdAt": 1722215732000,
						"valueType": 1,
						"tenantId": 1,
						"name": "52049 线密度(kg/m)",
						"valueHolder": "",
						"id": 128001,
						"categoryId": 4837,
						"group": "BASIC",
						"status": 1,
						"updatedAt": 1722216043000
					}
				],
				"skuAttributes": [],
				"skuList": [
					{
						"originalPrice": 0,
						"increaseRate": "0.1000",
						"createdAt": 1693811805000,
						"itemMarkupRate": 0.05,
						"enable": True,
						"price": 6.73,
						"id": 110202901050044,
						"barcode": "110202901050044",
						"updatedAt": 1693811805000,
						"image": "http://lcscm-trantor.oss-cn-shenzhen.aliyuncs.com/images/manage/1000001/20e8febb-28f6-4147-a714-f9b0d68a3972/9325fb26-6aad-44d4-80f6-6e7044aa4b04领潮.jpg",
						"costPrice": 6.39,
						"oldCostPrice": 6.39,
						"version": 0,
						"taxRate": 13,
						"name": "戴科 WDZBN-KYJY-4*1.5 上海真如境5#地块项目",
						"unitAmount": 1,
						"skuCode": "110202901050044",
						"status": 1,
						"oldItemMarkupRate": "0.0200",
						"salesBenchmarkPrice": 6.5178,
						"standardRaiseRate": 0.1,
						"priceRanges": [
							{
								"useStatus": False,
								"subsidyPrice": None,
								"itemMarkupRate": "0",
								"minOrderNum": None,
								"priceDesc": "",
								"getErrorMessage": {},
								"setErrorMessage": {}
							},
							{
								"useStatus": False,
								"subsidyPrice": None,
								"itemMarkupRate": "0",
								"minOrderNum": None,
								"priceDesc": "",
								"getErrorMessage": {},
								"setErrorMessage": {}
							},
							{
								"useStatus": False,
								"subsidyPrice": None,
								"itemMarkupRate": "0",
								"minOrderNum": None,
								"priceDesc": "",
								"getErrorMessage": {},
								"setErrorMessage": {}
							}
						],
						"priceExclusive": 5.96,
						"errorList": []
					}
				],
				"otherAttributes": [
					{
						"group": "BASIC",
						"otherAttributes": [
							{
								"id": 128001,
								"attrKey": "52049 线密度(kg/m)",
								"group": "BASIC",
								"attrVal": "780001"
							}
						]
					},
					{
						"group": "DEFAULT",
						"otherAttributes": []
					},
					{
						"group": "USER_DEFINED",
						"otherAttributes": []
					}
				]
			}
		]
	}
}

data4 ={
	"frontendContext": {},
	"singleResult": True,
	"targetModel": "itemcenter_ItemOnShelfVO",
	"sourceModel": "itemcenter_ItemOnShelfVO",
	"queryValues": {
		"id": {
			"type": "One",
			"value": 110202901050016
		}
	},
	"dataSource": {
		"actionKey": "itemcenter_ItemOnShelfVO_confirmOnShelf"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "autoOffShelfTime"
			}
		]
	}
}

data5 ={
	"frontendContext": {},
	"actionKey": "itemcenter_ItemOnShelfVO_ItemOnShelfAction::onShelf",
	"context": {
		"env": {
			"itemId": 110202901050016,
			"shopId": None,
			"version": 0,
			"autoOffShelfTime": 1753951080000
		},
		"record": [
			{
				"autoOffShelfTime": 1753951080000
			}
		],
		"modelKey": "itemcenter_ItemOnShelfVO"
	}
}

data6 ={
	"frontendContext": {},
	"actionKey": "itemcenter_ItemOnShelfVO_ItemOnShelfAction::auditPass",
	"context": {
		"modelKey": "itemcenter_ItemOnShelfVO",
		"env": {
			"itemId": 110202901050016,
			"shopId": None,
			"version": 1
		},
		"actionLabel": "审核通过",
		"record": [
			{
				"id": 110202901050016
			}
		]
	}
}

data7 ={
	"frontendContext": {},
	"singleResult": True,
	"targetModel": "itemcenter_ItemVO",
	"sourceModel": "itemcenter_ItemVO",
	"queryValues": {
		"category": {
			"type": "One",
			"value": 5128
		},
		"type": {
			"type": "One",
			"value": 1
		}
	},
	"dataSource": {
		"actionKey": "itemcenter_ItemVO_item_create"
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
				"fieldName": "contract",
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
				"fieldName": "itemLevel"
			},
			{
				"fieldName": "districtList"
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
				"fieldName": "projectName"
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
				"fieldName": "version"
			}
		]
	}
}

url8 =("https://staging-gateway.test.lcscm.cn"
	   "/zhonghai/business-partner/partner-center-admin/1004706/api/trantor/data-source")
data8 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "itemcenter_B2bPartnerVO",
	"queryValues": {
		"type": {
			"type": "One",
			"value": 1
		},
		"categoryNameList": {
			"type": "One",
			"value": "土建类/管线类/电线电缆/电缆/电缆(戴科)"
		},
		"categoryAttributes": {
			"type": "Collection",
			"values": [
				40090,
				40091,
				40092,
				40093,
				40094,
				40095,
				40096,
				46104,
				68013,
				128001
			]
		},
		"specialRelationEnterpriseId": {
			"type": "One",
			"value": 132012
		},
		"useWMS": {
			"type": "One",
			"value": True
		},
		"category": {
			"type": "One",
			"value": 5122
		},
		"isCombined": {
			"type": "One",
			"value": False
		},
		"isSpecialItem": {
			"type": "One",
			"value": 0
		},
		"isSyncDigital": {
			"type": "One",
			"value": 0
		}
	},
	"dataSource": {
		"actionKey": "partner_center_admin_B2bPartnerVO_B2bItemPurchaserMultiAction",
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
				"fieldName": "name"
			},
			{
				"fieldName": "enterpriseId"
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
	},
	"fuzzyValue": "深圳哈哈"
}

url9 =("https://staging-gateway.test.lcscm.cn"
	   "/zhonghai/master-data/master-data-admin/1005691/api/trantor/data-source")
data9 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "itemcenter_BrandVO",
	"queryValues": {
		"enterpriseId": {
			"type": "One",
			"value": 138017
		}
	},
	"dataSource": {
		"actionKey": "master_data_admin_MDBrandVO_MDBrandMultiAction",
		"type": "Action"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "name"
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

url10 ="https://staging-gateway.test.lcscm.cn/zhonghai/contract-center/contract-domain/1004703/api/trantor/data-source"
data10 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "contract_domain_Contract",
	"queryValues": {
		"type": {
			"type": "One",
			"value": 1
		},
		"categoryNameList": {
			"type": "One",
			"value": "土建类/管线类/电线电缆/电线/电线(戴科)"
		},
		"categoryAttributes": {
			"type": "Collection",
			"values": [
				40114,
				40115,
				40116,
				40117,
				40118,
				40119,
				44002,
				46110,
				68019,
				128001
			]
		},
		"specialRelationEnterpriseId": {
			"type": "One",
			"value": 132012
		},
		"useWMS": {
			"type": "One",
			"value": True
		},
		"category": {
			"type": "One",
			"value": 5128
		},
		"isCombined": {
			"type": "One",
			"value": False
		},
		"b2bPartnerVO": {
			"type": "One",
			"value": 124016
		},
		"brand": {
			"type": "One",
			"value": 72002
		},
		"isSpecialItem": {
			"type": "One",
			"value": 0
		},
		"isSyncDigital": {
			"type": "One",
			"value": 0
		},
		"mainImageAttachment": {
			"type": "One",
			"value": {
				"files": []
			}
		},
		"itemChartlet": {
			"type": "One",
			"value": {
				"files": []
			}
		}
	},
	"dataSource": {
		"condition": "partB.id == 138017&& contractType=='PURCHASE_CONTRACT' && status == 'ENABLE'",
		"type": "DataStore"
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
				"fieldName": "partAName"
			},
			{
				"fieldName": "partBName"
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

url11="https://staging-gateway.test.lcscm.cn/zhonghai/master-data/master-data-admin/1005691/api/trantor/data-source"
data11={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "itemcenter_MDInvoiceCategoryVO",
	"queryValues": {
		"type": {
			"type": "One",
			"value": 1
		},
		"categoryNameList": {
			"type": "One",
			"value": "土建类/管线类/电线电缆/电线/电线(戴科)"
		},
		"categoryAttributes": {
			"type": "Collection",
			"values": [
				40114,
				40115,
				40116,
				40117,
				40118,
				40119,
				44002,
				46110,
				68019,
				128001
			]
		},
		"specialRelationEnterpriseId": {
			"type": "One",
			"value": 132012
		},
		"useWMS": {
			"type": "One",
			"value": True
		},
		"category": {
			"type": "One",
			"value": 5128
		},
		"isCombined": {
			"type": "One",
			"value": False
		},
		"name": {
			"type": "One",
			"value": ""
		},
		"shortName": {
			"type": "One",
			"value": ""
		},
		"b2bPartnerVO": {
			"type": "One",
			"value": 124016
		},
		"brand": {
			"type": "One",
			"value": 72002
		},
		"contract": {
			"type": "One",
			"value": 256070
		},
		"isSpecialItem": {
			"type": "One",
			"value": 0
		},
		"isSyncDigital": {
			"type": "One",
			"value": 0
		},
		"mainImageAttachment": {
			"type": "One",
			"value": {
				"files": []
			}
		},
		"itemChartlet": {
			"type": "One",
			"value": {
				"files": []
			}
		}
	},
	"dataSource": {
		"actionKey": "master_data_admin_MDInvoiceCategoryVO_MDInvoiceCategoryItemMultiAction",
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
				"fieldName": "name"
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
	},
	"fuzzyValue": "立邦"
}




