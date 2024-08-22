# 平台通知管理
url1='https://staging-gateway.test.lcscm.cn/zhonghai/master-data/master-data-admin/1005691/api/trantor/data-source'
pro_url1='https://gateway.lcscm.cn/zhonghai/master-data/master-data-admin/1004013/api/trantor/data-source'
data1 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_MessageCenter",
	"sourceModel": "master_data_server_MessageCenter",
	"dataSource": {
		"actionKey": "master_data_server_MessageCenter_give_notice_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "title"
			},
			{
				"fieldName": "sinkObjectType"
			},
			{
				"fieldName": "sinkObject"
			},
			{
				"fieldName": "keyword"
			},
			{
				"fieldName": "initiator",
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
				"fieldName": "dispatchType"
			},
			{
				"fieldName": "sendStatus"
			},
			{
				"fieldName": "toDate"
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
# 平台提醒
data2 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_MDDeliveryRemindVO",
	"sourceModel": "master_data_server_MDDeliveryRemindVO",
	"dataSource": {
		"actionKey": "master_data_server_MDDeliveryRemindVO_delivery_message_remind_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "name"
			},
			{
				"fieldName": "messagesContent"
			},
			{
				"fieldName": "remindCrowd"
			},
			{
				"fieldName": "remindIntervalTime"
			},
			{
				"fieldName": "status"
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
data3 = {
	"frontendContext": {},
	"singleResult": True,
	"targetModel": "master_data_server_MDInvoiceRemindPO",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "master_data_server_MDInvoiceRemindPO_invoiced_reminder_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "remindCondition"
			},
			{
				"fieldName": "remindCrowd"
			},
			{
				"fieldName": "sendTime"
			},
			{
				"fieldName": "messagesSign"
			},
			{
				"fieldName": "messagesContent"
			}
		]
	}
}
data4 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_admin_MDPerformanceRemindVO",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "master_data_admin_MDPerformanceRemindVO_performance_reminder_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "performanceMsgType"
			},
			{
				"fieldName": "pushTag"
			},
			{
				"fieldName": "pushRule"
			},
			{
				"fieldName": "receivePostStr"
			},
			{
				"fieldName": "status"
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
# 个人中心
url2 ='https://staging-gateway.test.lcscm.cn/zhonghai/trantor-workspace/meta-store/1004799/api/trantor/data-source'
pro_url2='https://gateway.lcscm.cn/zhonghai/trantor-workspace/meta-store/1004017/api/trantor/data-source'
data5 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "base_Notice",
	"sourceModel": "base_Notice",
	"dataSource": {
		"actionKey": "base_Notice_listAll"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "content"
			},
			{
				"fieldName": "createdAt"
			},
			{
				"fieldName": "recordId"
			},
			{
				"fieldName": "modelKey"
			},
			{
				"fieldName": "viewActionKey"
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
url3 ='https://staging-gateway.test.lcscm.cn/zhonghai/item-center/itemcenter-server/1004704/api/trantor/data-source'
pro_url3 = 'https://gateway.lcscm.cn/zhonghai/item-center/itemcenter-server/1004019/api/trantor/data-source'
data6 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "itemcenter_server_ExportTask",
	"sourceModel": "itemcenter_server_ExportTask",
	"dataSource": {
		"actionKey": "itemcenter_server_ExportTask_ConsoleExportTaskList"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "createdAt"
			},
			{
				"fieldName": "jobDesc"
			},
			{
				"fieldName": "size"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "url"
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
# 采购商名册管理
url4 ='https://staging-gateway.test.lcscm.cn/zhonghai/master-data/master-data-server/1005691/api/trantor/data-source'
pro_url4 = 'https://gateway.lcscm.cn/zhonghai/master-data/master-data-server/1004013/api/trantor/data-source'
data7 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_MDEnterprise",
	"sourceModel": "master_data_server_MDEnterprise",
	"dataSource": {
		"actionKey": "master_data_server_MDEnterprise_enterprise_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "auditStatus"
			},
			{
				"fieldName": "code"
			},
			{
				"fieldName": "name"
			},
			{
				"fieldName": "unifiedSocialCreditCode"
			},
			{
				"fieldName": "contactName"
			},
			{
				"fieldName": "contactPhone"
			},
			{
				"fieldName": "b2bPartner",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "name"
					},
					{
						"fieldName": "status"
					},
					{
						"fieldName": "auditStatus"
					},
					{
						"fieldName": "roleType"
					}
				]
			},
			{
				"fieldName": "riskScore"
			},
			{
				"fieldName": "riskLevel"
			},
			{
				"fieldName": "rater"
			},
			{
				"fieldName": "grade"
			},
			{
				"fieldName": "expandAuditStatus"
			},
			{
				"fieldName": "enterpriseExpand",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "crmStatus"
					},
					{
						"fieldName": "defaultCreateType"
					}
				]
			},
			{
				"fieldName": "displayExpandType"
			},
			{
				"fieldName": "createdAt"
			},
			{
				"fieldName": "updatedAt"
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
data8 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_MDEnterprise",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "master_data_server_MDEnterprise_not_settled_enterprise_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "auditStatus"
			},
			{
				"fieldName": "code"
			},
			{
				"fieldName": "name"
			},
			{
				"fieldName": "unifiedSocialCreditCode"
			},
			{
				"fieldName": "contactName"
			},
			{
				"fieldName": "contactPhone"
			},
			{
				"fieldName": "b2bPartner",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "name"
					},
					{
						"fieldName": "status"
					},
					{
						"fieldName": "auditStatus"
					},
					{
						"fieldName": "roleType"
					}
				]
			},
			{
				"fieldName": "riskScore"
			},
			{
				"fieldName": "riskLevel"
			},
			{
				"fieldName": "rater"
			},
			{
				"fieldName": "smsSendCount"
			},
			{
				"fieldName": "smsSendTime"
			},
			{
				"fieldName": "grade"
			},
			{
				"fieldName": "expandAuditStatus"
			},
			{
				"fieldName": "enterpriseExpand",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "crmStatus"
					},
					{
						"fieldName": "defaultCreateType"
					}
				]
			},
			{
				"fieldName": "displayExpandType"
			},
			{
				"fieldName": "createdAt"
			},
			{
				"fieldName": "updatedAt"
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
data9= {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_MDEnterprise",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "master_data_server_MDEnterprise_not_certified_enterprise_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "auditStatus"
			},
			{
				"fieldName": "code"
			},
			{
				"fieldName": "name"
			},
			{
				"fieldName": "unifiedSocialCreditCode"
			},
			{
				"fieldName": "contactName"
			},
			{
				"fieldName": "contactPhone"
			},
			{
				"fieldName": "b2bPartner",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "name"
					},
					{
						"fieldName": "status"
					},
					{
						"fieldName": "auditStatus"
					},
					{
						"fieldName": "roleType"
					}
				]
			},
			{
				"fieldName": "riskScore"
			},
			{
				"fieldName": "riskLevel"
			},
			{
				"fieldName": "rater"
			},
			{
				"fieldName": "grade"
			},
			{
				"fieldName": "expandAuditStatus"
			},
			{
				"fieldName": "enterpriseExpand",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "crmStatus"
					},
					{
						"fieldName": "defaultCreateType"
					}
				]
			},
			{
				"fieldName": "displayExpandType"
			},
			{
				"fieldName": "createdAt"
			},
			{
				"fieldName": "updatedAt"
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
# 采购商信息变更
data10 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_MDEnterpriseChangeLog",
	"sourceModel": "master_data_server_MDEnterpriseChangeLog",
	"dataSource": {
		"actionKey": "master_data_server_MDEnterpriseChangeLog_purchaser_changelog_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "afterChange",
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
						"fieldName": "unifiedSocialCreditCode"
					},
					{
						"fieldName": "b2bPartner",
						"fields": [
							{
								"fieldName": "id"
							},
							{
								"fieldName": "name"
							},
							{
								"fieldName": "roleType"
							}
						]
					},
					{
						"fieldName": "auditStatus"
					},
					{
						"fieldName": "editType"
					}
				]
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
				"fieldName": "approvalBy",
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
				"fieldName": "approvalAt"
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
# 项目公司管理
url5 ='https://staging-gateway.test.lcscm.cn/zhonghai/business-partner/partner-center-admin/1004706/api/trantor/data-source'
pro_url5 = 'https://gateway.lcscm.cn/zhonghai/business-partner/partner-center-admin/1004014/api/trantor/data-source'
data11 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "partner_center_CorporateCompany",
	"sourceModel": "partner_center_CorporateCompany",
	"dataSource": {
		"actionKey": "partner_center_CorporateCompany_to_corporate_company_operate_list_view"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "companyCode"
			},
			{
				"fieldName": "companyName"
			},
			{
				"fieldName": "enterpriseName"
			},
			{
				"fieldName": "uscc"
			},
			{
				"fieldName": "contactName"
			},
			{
				"fieldName": "contactMobile"
			},
			{
				"fieldName": "travellingTraderStatus"
			},
			{
				"fieldName": "travellingTraderBankStatus"
			},
			{
				"fieldName": "riskScore"
			},
			{
				"fieldName": "riskLevel"
			},
			{
				"fieldName": "rater"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "auditUser",
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
				"fieldName": "crmStatus"
			},
			{
				"fieldName": "certificationMessageStatus"
			},
			{
				"fieldName": "createdAt"
			},
			{
				"fieldName": "defaultCreateType"
			}
		]
	},
	"paging": {
		"no": 1,
		"size": 10
	},
	"order": {
		"by": "createdAt",
		"isAsc": False
	}
}
data12 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "partner_center_CorporateCompany",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "partner_center_CorporateCompany_to_corporate_company_operate_list_view_personal"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "companyCode"
			},
			{
				"fieldName": "companyName"
			},
			{
				"fieldName": "enterpriseName"
			},
			{
				"fieldName": "uscc"
			},
			{
				"fieldName": "contactName"
			},
			{
				"fieldName": "contactMobile"
			},
			{
				"fieldName": "travellingTraderStatus"
			},
			{
				"fieldName": "travellingTraderBankStatus"
			},
			{
				"fieldName": "riskScore"
			},
			{
				"fieldName": "riskLevel"
			},
			{
				"fieldName": "rater"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "auditUser",
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
				"fieldName": "crmStatus"
			},
			{
				"fieldName": "certificationMessageStatus"
			},
			{
				"fieldName": "createdAt"
			},
			{
				"fieldName": "defaultCreateType"
			}
		]
	},
	"paging": {
		"no": 1,
		"size": 10
	},
	"order": {
		"by": "createdAt",
		"isAsc": False
	}
}
# 风险评分配置详情 url1
data13 = {
	"frontendContext": {},
	"singleResult": True,
	"targetModel": "master_data_admin_MDRiskAllocationVO",
	"sourceModel": "master_data_admin_MDRiskAllocationVO",
	"dataSource": {
		"actionKey": "master_data_admin_MDRiskAllocationVO_to_risk_allocation_view"
	},
	"result": {
		"fields": [
			{
				"fieldName": "scoringTask"
			},
			{
				"fieldName": "id"
			},
			{
				"fieldName": "riskLevelList",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "name"
					},
					{
						"fieldName": "riskScoreMin"
					},
					{
						"fieldName": "riskScoreMax"
					},
					{
						"fieldName": "isSendNotice"
					},
					{
						"fieldName": "roleVOs",
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
					}
				],
				"page": {
					"curPage": 1,
					"pageSize": 650
				}
			},
			{
				"fieldName": "mdRiskDimensionList",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "name"
					},
					{
						"fieldName": "scoringMethod"
					},
					{
						"fieldName": "score"
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
#项目管理 url5
data14 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "partner_center_Project",
	"sourceModel": "partner_center_Project",
	"dataSource": {
		"actionKey": "partner_center_Project_platform_project_list_all"
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
				"fieldName": "performanceProjectStatus"
			},
			{
				"fieldName": "dataSource"
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
				"fieldName": "defaultCreateType"
			},
			{
				"fieldName": "quotationHeadStr"
			},
			{
				"fieldName": "performanceHeadStr"
			},
			{
				"fieldName": "salesHeadStr"
			},
			{
				"fieldName": "salesSupportStr"
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
# 供应商名册管理 url1
data15 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_MDEnterprise",
	"sourceModel": "master_data_server_MDEnterprise",
	"dataSource": {
		"actionKey": "master_data_server_MDEnterprise_supplier_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "auditStatus"
			},
			{
				"fieldName": "code"
			},
			{
				"fieldName": "name"
			},
			{
				"fieldName": "unifiedSocialCreditCode"
			},
			{
				"fieldName": "contactName"
			},
			{
				"fieldName": "contactPhone"
			},
			{
				"fieldName": "dataSource"
			},
			{
				"fieldName": "b2bPartner",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "name"
					},
					{
						"fieldName": "status"
					},
					{
						"fieldName": "auditStatus"
					},
					{
						"fieldName": "roleType"
					}
				]
			},
			{
				"fieldName": "grade"
			},
			{
				"fieldName": "enterpriseExpand",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "travellingTraderStatus"
					},
					{
						"fieldName": "travellingTraderBankStatus"
					}
				]
			},
			{
				"fieldName": "expandAuditStatus"
			},
			{
				"fieldName": "displayExpandType"
			},
			{
				"fieldName": "certificationMessage",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "status"
					}
				]
			},
			{
				"fieldName": "createdAt"
			},
			{
				"fieldName": "updatedAt"
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
data16 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_MDEnterprise",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "master_data_server_MDEnterprise_to_settled_supplier_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "auditStatus"
			},
			{
				"fieldName": "code"
			},
			{
				"fieldName": "name"
			},
			{
				"fieldName": "unifiedSocialCreditCode"
			},
			{
				"fieldName": "contactName"
			},
			{
				"fieldName": "contactPhone"
			},
			{
				"fieldName": "grade"
			},
			{
				"fieldName": "b2bPartner",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "name"
					},
					{
						"fieldName": "roleType"
					}
				]
			},
			{
				"fieldName": "displayExpandType"
			},
			{
				"fieldName": "enterpriseExpand",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "source"
					}
				]
			},
			{
				"fieldName": "createdAt"
			},
			{
				"fieldName": "updatedAt"
			},
			{
				"fieldName": "smsSendCount"
			},
			{
				"fieldName": "smsSendTime"
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
# 供应商信息变更
data17 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_MDEnterpriseChangeLog",
	"sourceModel": "master_data_server_MDEnterpriseChangeLog",
	"dataSource": {
		"actionKey": "master_data_server_MDEnterpriseChangeLog_supplier_changelog_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "afterChange",
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
						"fieldName": "unifiedSocialCreditCode"
					},
					{
						"fieldName": "b2bPartner",
						"fields": [
							{
								"fieldName": "id"
							},
							{
								"fieldName": "name"
							},
							{
								"fieldName": "roleType"
							}
						]
					},
					{
						"fieldName": "auditStatus"
					},
					{
						"fieldName": "editType"
					}
				]
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
				"fieldName": "approvalBy",
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
				"fieldName": "approvalAt"
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
# 经销商管理
data18 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_MDEnterpriseBrandDistributeRelation",
	"sourceModel": "master_data_server_MDEnterpriseBrandDistributeRelation",
	"dataSource": {
		"actionKey": "master_data_server_MDEnterpriseBrandDistributeRelation_to_admin_enterprise_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "brandBusiness",
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
						"fieldName": "unifiedSocialCreditCode"
					}
				]
			},
			{
				"fieldName": "distributeBusiness",
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
						"fieldName": "unifiedSocialCreditCode"
					}
				]
			},
			{
				"fieldName": "relationType"
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
# 供货范围管理
data19 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_MDEnterprise",
	"sourceModel": "master_data_server_MDEnterprise",
	"dataSource": {
		"actionKey": "master_data_server_MDEnterprise_operate_supply_scope_list"
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
				"fieldName": "b2bPartner",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "name"
					},
					{
						"fieldName": "roleType"
					}
				]
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
# QD黑名单
data20 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_QDBlacklist",
	"sourceModel": "master_data_server_QDBlacklist",
	"dataSource": {
		"actionKey": "master_data_server_QDBlacklist_qd_blacklist_import_record_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "enterpriseId"
			},
			{
				"fieldName": "mdEnterprise",
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
						"fieldName": "b2bPartner",
						"fields": [
							{
								"fieldName": "id"
							},
							{
								"fieldName": "name"
							},
							{
								"fieldName": "auditStatus"
							},
							{
								"fieldName": "status"
							}
						]
					}
				]
			},
			{
				"fieldName": "name"
			},
			{
				"fieldName": "unifiedSocialCreditCode"
			},
			{
				"fieldName": "roleType"
			},
			{
				"fieldName": "contact"
			},
			{
				"fieldName": "contactPhone"
			},
			{
				"fieldName": "isSystem"
			},
			{
				"fieldName": "importTime"
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
# 业务联系人管理
data21 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_MDEnterprise",
	"sourceModel": "master_data_server_MDEnterprise",
	"dataSource": {
		"actionKey": "master_data_server_MDEnterprise_operate_business_contact_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "b2bPartner",
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
				"fieldName": "name"
			},
			{
				"fieldName": "contactNameStr"
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
# 用户注册列表
url6='https://staging-gateway.test.lcscm.cn/zhonghai/user-center/isv-user-admin/1004701/api/trantor/data-source'
pro_url6 ='https://gateway.lcscm.cn/zhonghai/user-center/isv-user-admin/1004029/api/trantor/data-source'
data22 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "isv_user_admin_UserVo",
	"sourceModel": "isv_user_admin_UserVo",
	"dataSource": {
		"actionKey": "isv_user_admin_UserVo_to_out_user_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "nickname"
			},
			{
				"fieldName": "mobile"
			},
			{
				"fieldName": "email"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "companyName"
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
#角色
data23 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "parana_user_admin_RoleVO",
	"sourceModel": "parana_user_admin_RoleVO",
	"dataSource": {
		"actionKey": "parana_user_admin_RoleVO_uc_role_toList"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "key"
			},
			{
				"fieldName": "name"
			},
			{
				"fieldName": "type"
			},
			{
				"fieldName": "enterpriseVO",
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
				"fieldName": "desc"
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
# 用户管理 url1
data24 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "parana_user_admin_AuthUserInfoVO",
	"sourceModel": "parana_user_admin_AuthUserInfoVO",
	"dataSource": {
		"actionKey": "parana_user_admin_AuthUserInfoVO_to_auth_user_admin_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "user",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "username"
					},
					{
						"fieldName": "locked"
					},
					{
						"fieldName": "nickname"
					},
					{
						"fieldName": "mobile"
					},
					{
						"fieldName": "email"
					}
				]
			},
			{
				"fieldName": "roleVOs",
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
				"fieldName": "relationRole"
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
# 品牌列表 url1
data25 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_admin_MDBrandVO",
	"sourceModel": "master_data_admin_MDBrandVO",
	"dataSource": {
		"actionKey": "master_data_admin_MDBrandVO_listAll"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "name"
			},
			{
				"fieldName": "shortName"
			},
			{
				"fieldName": "mdEnterprise",
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
				"fieldName": "mdEnterpriseRelationOtherName"
			},
			{
				"fieldName": "digitalSyncStatus"
			},
			{
				"fieldName": "logo"
			},
			{
				"fieldName": "createdAt"
			},
			{
				"fieldName": "updatedAt"
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
# 商品管理
url7 = 'https://staging-gateway.test.lcscm.cn/zhonghai/item-center/itemcenter/1004704/api/trantor/data-source'
pro_url7 = 'https://gateway.lcscm.cn/zhonghai/item-center/itemcenter/1004019/api/trantor/data-source'
data26 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "itemcenter_FrontItemVO",
	"sourceModel": "itemcenter_FrontItemVO",
	"dataSource": {
		"actionKey": "itemcenter_FrontItemVO_admin_listAll"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "putOnSaleCode"
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
				"fieldName": "projectName"
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
# 商品上下架列表
data27 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "itemcenter_ItemOnShelfVO",
	"sourceModel": "itemcenter_ItemOnShelfVO",
	"dataSource": {
		"actionKey": "itemcenter_ItemOnShelfVO_admin_on_shelf_listAll"
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
				"fieldName": "quickOrder"
			},
			{
				"fieldName": "projectName"
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
				"fieldName": "auditStatus"
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
# 安装费模板列表页
data28 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "itemcenter_DeliveryFeeTemplatesVO",
	"sourceModel": "itemcenter_DeliveryFeeTemplatesVO",
	"searchValues": {
		"type": {
			"type": "One",
			"value": "INSTALL_FEE"
		}
	},
	"dataSource": {
		"actionKey": "itemcenter_DeliveryFeeTemplatesVO_Install_listAll"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "name"
			},
			{
				"fieldName": "mdEnterpriseName"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "updatedAt"
			},
			{
				"fieldName": "sourceSystem"
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
# 运费模板列表页
data29 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "itemcenter_DeliveryFeeTemplatesVO",
	"sourceModel": "itemcenter_DeliveryFeeTemplatesVO",
	"searchValues": {
		"type": {
			"type": "One",
			"value": "DELIVERY_FEE"
		}
	},
	"dataSource": {
		"actionKey": "itemcenter_DeliveryFeeTemplatesVO_listAll"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "name"
			},
			{
				"fieldName": "mdEnterpriseName"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "updatedAt"
			},
			{
				"fieldName": "sourceSystem"
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
# 临期商品管理
data30 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "itemcenter_OverdueItemVO",
	"sourceModel": "itemcenter_OverdueItemVO",
	"dataSource": {
		"actionKey": "itemcenter_OverdueItemVO_overdue_item_list"
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
				"fieldName": "code"
			},
			{
				"fieldName": "overdueStatus"
			},
			{
				"fieldName": "supplierName"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "isSpecialItem"
			},
			{
				"fieldName": "contractEndDate"
			},
			{
				"fieldName": "overdueDate"
			},
			{
				"fieldName": "costPrice"
			},
			{
				"fieldName": "price"
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
# 组合模版配置
data31 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "itemcenter_server_CombineItemTemplate",
	"sourceModel": "itemcenter_server_CombineItemTemplate",
	"dataSource": {
		"actionKey": "itemcenter_server_CombineItemTemplate_CombineItemTemplateList"
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
				"fieldName": "type"
			},
			{
				"fieldName": "supplier",
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
				"fieldName": "status"
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
# 组合商品管理
data32 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "itemcenter_FrontItemVO",
	"sourceModel": "itemcenter_FrontItemVO",
	"dataSource": {
		"actionKey": "itemcenter_FrontItemVO_to_combined_item_itemList"
	},
	"result": {
		"fields": [
			{
				"fieldName": "image"
			},
			{
				"fieldName": "name"
			},
			{
				"fieldName": "id"
			},
			{
				"fieldName": "type"
			},
			{
				"fieldName": "brandName"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "category"
			},
			{
				"fieldName": "combineItemTemplate",
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
				"fieldName": "costPriceRange"
			},
			{
				"fieldName": "salePriceRange"
			},
			{
				"fieldName": "leadTrendYn"
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
			},
			{
				"fieldName": "skuList"
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
# 组合商品上下架列表
data33 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "itemcenter_ItemOnShelfVO",
	"sourceModel": "itemcenter_ItemOnShelfVO",
	"dataSource": {
		"actionKey": "itemcenter_ItemOnShelfVO_to_combined_item_OnShelf_List"
	},
	"result": {
		"fields": [
			{
				"fieldName": "image"
			},
			{
				"fieldName": "name"
			},
			{
				"fieldName": "id"
			},
			{
				"fieldName": "type"
			},
			{
				"fieldName": "brandName"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "category"
			},
			{
				"fieldName": "combineItemTemplate",
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
				"fieldName": "costPriceRange"
			},
			{
				"fieldName": "salePriceRange"
			},
			{
				"fieldName": "leadTrendYn"
			},
			{
				"fieldName": "auditStatus"
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
			},
			{
				"fieldName": "skuList"
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
# 报备单管理
data34 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "itemcenter_server_QuotationFilingPO",
	"sourceModel": "itemcenter_server_QuotationFilingPO",
	"dataSource": {
		"actionKey": "itemcenter_server_QuotationFilingPO_filing_admin_list"
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
				"fieldName": "projectName"
			},
			{
				"fieldName": "source"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "createdAt"
			},
			{
				"fieldName": "projectType"
			},
			{
				"fieldName": "purchaserName"
			},
			{
				"fieldName": "purchaserType"
			},
			{
				"fieldName": "brandName"
			},
			{
				"fieldName": "inquiryFullName"
			},
			{
				"fieldName": "attachment"
			},
			{
				"fieldName": "cityAdr"
			},
			{
				"fieldName": "remark"
			},
			{
				"fieldName": "projectCode"
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
# 询价单管理
data35 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "itemcenter_server_AskPricePO",
	"sourceModel": "itemcenter_server_AskPricePO",
	"dataSource": {
		"actionKey": "itemcenter_server_AskPricePO_ask_price_admin_list"
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
				"fieldName": "source"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "crmProject",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "name"
					},
					{
						"fieldName": "zhLnquiryunit"
					}
				]
			},
			{
				"fieldName": "consultBrandNames"
			},
			{
				"fieldName": "askApplyDate"
			},
			{
				"fieldName": "addressName"
			},
			{
				"fieldName": "submitName"
			},
			{
				"fieldName": "quotationFilingCode"
			},
			{
				"fieldName": "askData"
			},
			{
				"fieldName": "quotationCrmCode"
			},
			{
				"fieldName": "remark"
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
# 项目信息共享设置
data36 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "itemcenter_server_QuotationOpenWithinStatisticSetPO",
	"sourceModel": "itemcenter_server_QuotationOpenWithinStatisticSetPO",
	"dataSource": {
		"actionKey": "itemcenter_server_QuotationOpenWithinStatisticSetPO_withinStatisticSet_admin_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "category"
			},
			{
				"fieldName": "mdEnterprise",
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
				"fieldName": "brandName"
			},
			{
				"fieldName": "contactName"
			},
			{
				"fieldName": "contactPhone"
			},
			{
				"fieldName": "startTime"
			},
			{
				"fieldName": "endTime"
			},
			{
				"fieldName": "supplyMode"
			},
			{
				"fieldName": "supplyCycle"
			},
			{
				"fieldName": "payType"
			},
			{
				"fieldName": "warranty"
			},
			{
				"fieldName": "bringInto"
			},
			{
				"fieldName": "scope"
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
# 调价公式管理
data37 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "itemcenter_ModifyPriceExpressionVO",
	"sourceModel": "itemcenter_ModifyPriceExpressionVO",
	"dataSource": {
		"actionKey": "itemcenter_ModifyPriceExpressionVO_modify_price_expression_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "name"
			},
			{
				"fieldName": "mdCategory",
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
				"fieldName": "modifyPriceCycle"
			},
			{
				"fieldName": "isAutomatic"
			},
			{
				"fieldName": "updatedAt"
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
# 调价管理
data38 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "itemcenter_ModifyPriceVO",
	"sourceModel": "itemcenter_ModifyPriceVO",
	"dataSource": {
		"actionKey": "itemcenter_ModifyPriceVO_modify_price_list"
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
				"fieldName": "supplier",
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
				"fieldName": "status"
			},
			{
				"fieldName": "isAutomatic"
			},
			{
				"fieldName": "validDateStr"
			},
			{
				"fieldName": "applyDate"
			},
			{
				"fieldName": "cancelDate"
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
# 报价申请单管理 (价格历史信息)
data39 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "itemcenter_server_PriceHistoryPO",
	"sourceModel": "itemcenter_server_PriceHistoryPO",
	"dataSource": {
		"actionKey": "itemcenter_server_PriceHistoryPO_admin_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "choice"
			},
			{
				"fieldName": "quota"
			},
			{
				"fieldName": "highestPrice"
			},
			{
				"fieldName": "averagePrice"
			},
			{
				"fieldName": "fluctuationRangeStr"
			},
			{
				"fieldName": "date"
			}
		]
	},
	"paging": {
		"no": 1,
		"size": 10
	},
	"order": {
		"by": "date",
		"isAsc": False
	}
}
# 自动调价任务列表
data40 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "itemcenter_server_ModifyPriceJob",
	"sourceModel": "itemcenter_server_ModifyPriceJob",
	"dataSource": {
		"actionKey": "itemcenter_server_ModifyPriceJob_admin_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "modifyPrice",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "code"
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
						"fieldName": "supplier",
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
						"fieldName": "modifyPriceCycle"
					}
				]
			},
			{
				"fieldName": "code"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "date"
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
#采购合同 品牌商
url8 = 'https://staging-gateway.test.lcscm.cn/zhonghai/contract-center/contract-center-admin/1004703/api/trantor/data-source'
pro_url8 = 'https://gateway.lcscm.cn/zhonghai/contract-center/contract-center-admin/1004869/api/trantor/data-source'
data41 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "contract_domain_Contract",
	"sourceModel": "contract_domain_Contract",
	"dataSource": {
		"actionKey": "contract_domain_Contract_to_purchase_contract_list"
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
				"fieldName": "partA",
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
				"fieldName": "system"
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
				"fieldName": "createdAt"
			},
			{
				"fieldName": "updatedAt"
			},
			{
				"fieldName": "isTranslation"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "syncStatus"
			},
			{
				"fieldName": "signCommonStatus"
			},
			{
				"fieldName": "oaStatus"
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
# 采购合同 经销商
data42 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "contract_domain_PurchaseAgreementProtocol",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "contract_domain_PurchaseAgreementProtocol_to_purchase_contract_byDistributor_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
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
						"fieldName": "financeSysCode"
					},
					{
						"fieldName": "partA",
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
						"fieldName": "system"
					},
					{
						"fieldName": "contractType"
					},
					{
						"fieldName": "isTranslation"
					},
					{
						"fieldName": "oaStatus"
					},
					{
						"fieldName": "createdAt"
					},
					{
						"fieldName": "updatedAt"
					}
				]
			},
			{
				"fieldName": "code"
			},
			{
				"fieldName": "name"
			},
			{
				"fieldName": "dealer",
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
				"fieldName": "syncStatus"
			},
			{
				"fieldName": "signCommonStatus"
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
# 集采合同
data43 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "contract_domain_Contract",
	"sourceModel": "contract_domain_Contract",
	"dataSource": {
		"actionKey": "contract_domain_Contract_to_gather_contract_list"
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
				"fieldName": "partA",
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
				"fieldName": "system"
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
				"fieldName": "createdAt"
			},
			{
				"fieldName": "updatedAt"
			},
			{
				"fieldName": "isTranslation"
			},
			{
				"fieldName": "status"
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
# 销售合同 -项目合同
data44 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "contract_domain_Contract",
	"sourceModel": "contract_domain_Contract",
	"searchValues": {
		"tabType": {
			"type": "One",
			"value": "0"
		},
		"client": {
			"type": "One",
			"value": "LC"
		}
	},
	"dataSource": {
		"actionKey": "contract_domain_Contract_to_sales_contract_listAll"
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
					},
					{
						"fieldName": "lcName"
					},
					{
						"fieldName": "quotationHeadStr"
					},
					{
						"fieldName": "performanceHeadStr"
					},
					{
						"fieldName": "salesHeadStr"
					},
					{
						"fieldName": "salesSupportStr"
					},
					{
						"fieldName": "code"
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
					},
					{
						"fieldName": "enterpriseName"
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
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "isTranslation"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "syncStatus"
			},
			{
				"fieldName": "signCommonStatus"
			},
			{
				"fieldName": "oaStatus"
			},
			{
				"fieldName": "contractType"
			},
			{
				"fieldName": "defaultCreateType"
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
# 销售合同 框架协议
data45 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "contract_domain_Contract",
	"sourceModel": "",
	"queryValues": {
		"tabType": {
			"type": "One",
			"value": "1"
		},
		"modelKey": {
			"type": "One",
			"value": "contract_domain_Contract"
		}
	},
	"searchValues": {
		"tabType": {
			"type": "One",
			"value": "1"
		},
		"client": {
			"type": "One",
			"value": "LC"
		}
	},
	"dataSource": {
		"actionKey": "contract_domain_Contract_to_sales_contract_frame_list"
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
					},
					{
						"fieldName": "lcName"
					},
					{
						"fieldName": "quotationHeadStr"
					},
					{
						"fieldName": "performanceHeadStr"
					},
					{
						"fieldName": "salesHeadStr"
					},
					{
						"fieldName": "salesSupportStr"
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
					},
					{
						"fieldName": "enterpriseName"
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
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "isTranslation"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "syncStatus"
			},
			{
				"fieldName": "signCommonStatus"
			},
			{
				"fieldName": "oaStatus"
			},
			{
				"fieldName": "contractType"
			},
			{
				"fieldName": "defaultCreateType"
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
# 销售合同 战略协议
data46 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "contract_domain_Contract",
	"sourceModel": "",
	"queryValues": {
		"tabType": {
			"type": "One",
			"value": "2"
		},
		"modelKey": {
			"type": "One",
			"value": "contract_domain_Contract"
		}
	},
	"searchValues": {
		"tabType": {
			"type": "One",
			"value": "2"
		},
		"client": {
			"type": "One",
			"value": "LC"
		}
	},
	"dataSource": {
		"actionKey": "contract_domain_Contract_to_sales_contract_strategy_list"
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
					},
					{
						"fieldName": "lcName"
					},
					{
						"fieldName": "quotationHeadStr"
					},
					{
						"fieldName": "performanceHeadStr"
					},
					{
						"fieldName": "salesHeadStr"
					},
					{
						"fieldName": "salesSupportStr"
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
					},
					{
						"fieldName": "enterpriseName"
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
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "isTranslation"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "syncStatus"
			},
			{
				"fieldName": "signCommonStatus"
			},
			{
				"fieldName": "oaStatus"
			},
			{
				"fieldName": "contractType"
			},
			{
				"fieldName": "defaultCreateType"
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
# 销售合同 撮合服务
data47 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "contract_domain_Contract",
	"sourceModel": "",
	"queryValues": {
		"tabType": {
			"type": "One",
			"value": "3"
		},
		"modelKey": {
			"type": "One",
			"value": "contract_domain_Contract"
		}
	},
	"searchValues": {
		"tabType": {
			"type": "One",
			"value": "3"
		},
		"client": {
			"type": "One",
			"value": "LC"
		}
	},
	"dataSource": {
		"actionKey": "contract_domain_Contract_to_sales_contract_mate_list"
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
					},
					{
						"fieldName": "lcName"
					},
					{
						"fieldName": "quotationHeadStr"
					},
					{
						"fieldName": "performanceHeadStr"
					},
					{
						"fieldName": "salesHeadStr"
					},
					{
						"fieldName": "salesSupportStr"
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
					},
					{
						"fieldName": "enterpriseName"
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
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "isTranslation"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "syncStatus"
			},
			{
				"fieldName": "signCommonStatus"
			},
			{
				"fieldName": "oaStatus"
			},
			{
				"fieldName": "contractType"
			},
			{
				"fieldName": "defaultCreateType"
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
# 销售合同 补充协议
data48 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "contract_domain_Contract",
	"sourceModel": "",
	"queryValues": {
		"tabType": {
			"type": "One",
			"value": "4"
		},
		"modelKey": {
			"type": "One",
			"value": "contract_domain_Contract"
		}
	},
	"searchValues": {
		"tabType": {
			"type": "One",
			"value": "4"
		},
		"client": {
			"type": "One",
			"value": "LC"
		}
	},
	"dataSource": {
		"actionKey": "contract_domain_Contract_to_sales_contract_supplemental_list"
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
					},
					{
						"fieldName": "lcName"
					},
					{
						"fieldName": "quotationHeadStr"
					},
					{
						"fieldName": "performanceHeadStr"
					},
					{
						"fieldName": "salesHeadStr"
					},
					{
						"fieldName": "salesSupportStr"
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
					},
					{
						"fieldName": "enterpriseName"
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
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "isTranslation"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "syncStatus"
			},
			{
				"fieldName": "signCommonStatus"
			},
			{
				"fieldName": "oaStatus"
			},
			{
				"fieldName": "contractType"
			},
			{
				"fieldName": "defaultCreateType"
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
# 销售合同 全部合同
data49 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "contract_domain_Contract",
	"sourceModel": "",
	"queryValues": {
		"tabType": {
			"type": "One",
			"value": "5"
		},
		"modelKey": {
			"type": "One",
			"value": "contract_domain_Contract"
		}
	},
	"searchValues": {
		"tabType": {
			"type": "One",
			"value": "5"
		},
		"client": {
			"type": "One",
			"value": "LC"
		}
	},
	"dataSource": {
		"actionKey": "contract_domain_Contract_sales_contract_list_total"
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
					},
					{
						"fieldName": "lcName"
					},
					{
						"fieldName": "quotationHeadStr"
					},
					{
						"fieldName": "performanceHeadStr"
					},
					{
						"fieldName": "salesHeadStr"
					},
					{
						"fieldName": "salesSupportStr"
					},
					{
						"fieldName": "code"
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
					},
					{
						"fieldName": "enterpriseName"
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
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "isTranslation"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "syncStatus"
			},
			{
				"fieldName": "signCommonStatus"
			},
			{
				"fieldName": "oaStatus"
			},
			{
				"fieldName": "contractType"
			},
			{
				"fieldName": "defaultCreateType"
			},
			{
				"fieldName": "contractDataType"
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
# 合同标签管理
data50= {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "contract_domain_ContractLabel",
	"sourceModel": "contract_domain_ContractLabel",
	"dataSource": {
		"actionKey": "contract_domain_ContractLabel_contract_label_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "contractLabelName"
			},
			{
				"fieldName": "projectCode"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "updateDate"
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
# 采购合同临期管理
data51 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "contract_domain_Contract",
	"sourceModel": "contract_domain_Contract",
	"dataSource": {
		"actionKey": "contract_domain_Contract_overdue_contract_listAll"
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
				"fieldName": "partA",
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
				"fieldName": "itemNum"
			},
			{
				"fieldName": "overdueStatus"
			},
			{
				"fieldName": "isRemind"
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
# 信用管理
data52 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "contract_center_admin_CreditControlVO",
	"sourceModel": "contract_center_admin_CreditControlVO",
	"dataSource": {
		"actionKey": "contract_center_admin_CreditControlVO_credit_control_list"
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
					},
					{
						"fieldName": "enterpriseName"
					}
				]
			},
			{
				"fieldName": "availableAmount"
			},
			{
				"fieldName": "availableAmountOther"
			},
			{
				"fieldName": "availableAmountTotal"
			},
			{
				"fieldName": "contractExposureSum"
			},
			{
				"fieldName": "purchaserExposureSum"
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
# 保函管理(旧)
data53 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "contract_domain_GuaranteeLetter",
	"sourceModel": "contract_domain_GuaranteeLetter",
	"dataSource": {
		"actionKey": "contract_domain_GuaranteeLetter_to_guaranteeLetter_list"
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
				"fieldName": "providerType"
			},
			{
				"fieldName": "provider",
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
				"fieldName": "guarantor"
			},
			{
				"fieldName": "type"
			},
			{
				"fieldName": "startDate"
			},
			{
				"fieldName": "endDate"
			},
			{
				"fieldName": "amount"
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
			},
			{
				"fieldName": "updatedBy",
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
				"fieldName": "updatedAt"
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
# 授信额度管理
data54 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "contract_domain_GuaranteeLimit",
	"sourceModel": "contract_domain_GuaranteeLimit",
	"dataSource": {
		"actionKey": "contract_domain_GuaranteeLimit_to_guaranteeLimit_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
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
				"fieldName": "guaranteeAmount"
			},
			{
				"fieldName": "canGetGoodsAmount"
			},
			{
				"fieldName": "changeAmount"
			},
			{
				"fieldName": "changeStatus"
			},
			{
				"fieldName": "remark"
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
# 保函接收列表
data55 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "contract_domain_Guarantee",
	"sourceModel": "contract_domain_Guarantee",
	"searchValues": {
		"guaranteeType": {
			"type": "One",
			"value": "RECEIVE"
		},
		"actionType": {
			"type": "One",
			"value": "1"
		}
	},
	"dataSource": {
		"actionKey": "contract_domain_Guarantee_to_guarantee_list_receive"
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
				"fieldName": "offlineGuaranteeCode"
			},
			{
				"fieldName": "companyType"
			},
			{
				"fieldName": "company",
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
				"fieldName": "contractCode"
			},
			{
				"fieldName": "offlineContractCode"
			},
			{
				"fieldName": "contractName"
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
				"fieldName": "beneficiaryName"
			},
			{
				"fieldName": "applyName"
			},
			{
				"fieldName": "type"
			},
			{
				"fieldName": "startDate"
			},
			{
				"fieldName": "endDate"
			},
			{
				"fieldName": "effective"
			},
			{
				"fieldName": "amount"
			},
			{
				"fieldName": "remark"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "amountRatio"
			},
			{
				"fieldName": "attachment"
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
				"fieldName": "updatedBy",
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
				"fieldName": "updatedAt"
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
# 保函额度
data56 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "contract_domain_GuaranteeCreditLine",
	"sourceModel": "",
	"searchValues": {
		"actionType": {
			"type": "One",
			"value": "1"
		}
	},
	"dataSource": {
		"actionKey": "contract_domain_GuaranteeCreditLine_to_guaranteeCreditLine_list_receive"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "guarantee",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "code"
					},
					{
						"fieldName": "offlineGuaranteeCode"
					},
					{
						"fieldName": "offlineContractCode"
					},
					{
						"fieldName": "countType"
					},
					{
						"fieldName": "amount"
					},
					{
						"fieldName": "status"
					}
				]
			},
			{
				"fieldName": "purchaserName"
			},
			{
				"fieldName": "companyName"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "occupyAmount"
			},
			{
				"fieldName": "availableAmount"
			},
			{
				"fieldName": "updatedAt"
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
# 保函开立列表
data57 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "contract_domain_Guarantee",
	"sourceModel": "contract_domain_Guarantee",
	"searchValues": {
		"guaranteeType": {
			"type": "One",
			"value": "OPEN"
		},
		"actionType": {
			"type": "One",
			"value": "3"
		}
	},
	"dataSource": {
		"actionKey": "contract_domain_Guarantee_to_guarantee_list_open"
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
				"fieldName": "companyType"
			},
			{
				"fieldName": "company",
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
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
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
				"fieldName": "beneficiaryName"
			},
			{
				"fieldName": "applyName"
			},
			{
				"fieldName": "type"
			},
			{
				"fieldName": "startDate"
			},
			{
				"fieldName": "endDate"
			},
			{
				"fieldName": "effective"
			},
			{
				"fieldName": "amount"
			},
			{
				"fieldName": "remark"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "amountRatio"
			},
			{
				"fieldName": "attachment"
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
				"fieldName": "updatedBy",
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
				"fieldName": "updatedAt"
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
#其他担保列表
data58 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "contract_domain_Guarantee",
	"sourceModel": "contract_domain_Guarantee",
	"searchValues": {
		"guaranteeType": {
			"type": "One",
			"value": "RECEIVE"
		},
		"actionType": {
			"type": "One",
			"value": "2"
		}
	},
	"dataSource": {
		"actionKey": "contract_domain_Guarantee_to_guarantee_list_other"
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
				"fieldName": "offlineGuaranteeCode"
			},
			{
				"fieldName": "companyType"
			},
			{
				"fieldName": "company",
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
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "type"
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
				"fieldName": "beneficiaryName"
			},
			{
				"fieldName": "applyName"
			},
			{
				"fieldName": "startDate"
			},
			{
				"fieldName": "endDate"
			},
			{
				"fieldName": "effective"
			},
			{
				"fieldName": "amount"
			},
			{
				"fieldName": "countType"
			},
			{
				"fieldName": "remark"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "attachment"
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
				"fieldName": "updatedBy",
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
				"fieldName": "updatedAt"
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
#其他担保额度
data59 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "contract_domain_GuaranteeCreditLine",
	"sourceModel": "",
	"searchValues": {
		"actionType": {
			"type": "One",
			"value": "2"
		}
	},
	"dataSource": {
		"actionKey": "contract_domain_GuaranteeCreditLine_to_guaranteeCreditLine_list_other"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "guarantee",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "code"
					},
					{
						"fieldName": "offlineGuaranteeCode"
					},
					{
						"fieldName": "type"
					},
					{
						"fieldName": "countType"
					},
					{
						"fieldName": "amount"
					},
					{
						"fieldName": "status"
					}
				]
			},
			{
				"fieldName": "purchaserName"
			},
			{
				"fieldName": "companyName"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "occupyAmount"
			},
			{
				"fieldName": "availableAmount"
			},
			{
				"fieldName": "updatedAt"
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
# 销售-需求单管理
url9 ='https://staging-gateway.test.lcscm.cn/zhonghai/trade-center/order-admin-center/1004708/api/trantor/data-source'
pro_url9 ='https://gateway.lcscm.cn/zhonghai/trade-center/order-admin-center/1004871/api/trantor/data-source'
data60 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "order_OrderPO",
	"sourceModel": "order_OrderPO",
	"dataSource": {
		"actionKey": "order_OrderPO_order_operator_supply_to_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "countAmount"
			},
			{
				"fieldName": "code"
			},
			{
				"fieldName": "title"
			},
			{
				"fieldName": "isTranslation"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "settleStatus"
			},
			{
				"fieldName": "qualityAssuranceStatus"
			},
			{
				"fieldName": "projectReceiverName"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "contractCode"
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
				"fieldName": "categoryNames"
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
						"fieldName": "lcName"
					}
				]
			},
			{
				"fieldName": "purchaserName"
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
				"fieldName": "dealerName"
			},
			{
				"fieldName": "brandOwnerName"
			},
			{
				"fieldName": "signStatus"
			},
			{
				"fieldName": "orderDate"
			},
			{
				"fieldName": "takeOrderDate"
			},
			{
				"fieldName": "orderRule"
			},
			{
				"fieldName": "totalAmount"
			},
			{
				"fieldName": "totalTaxAmount"
			},
			{
				"fieldName": "getGoodsAmount"
			},
			{
				"fieldName": "deliveryAmount"
			},
			{
				"fieldName": "reverseAmount"
			},
			{
				"fieldName": "settledAmount"
			},
			{
				"fieldName": "paidAmount"
			},
			{
				"fieldName": "checkedAmount"
			},
			{
				"fieldName": "isAgentOrder"
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
				"fieldName": "orderCreateType"
			},
			{
				"fieldName": "payType"
			},
			{
				"fieldName": "payStatus"
			},
			{
				"fieldName": "receiptStatus"
			}
		]
	},
	"paging": {
		"no": 1,
		"size": 10
	},
	"order": {
		"by": "createdAt",
		"isAsc": False
	}
}
# 销售-订单管理
data61 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "order_GetGoodsOrderPO",
	"sourceModel": "order_GetGoodsOrderPO",
	"searchValues": {
		"searchEventType": {
			"type": "One",
			"value": "SEARCH_GOODS_ORDER_BY_OPERATOR_SUPPLIER"
		}
	},
	"dataSource": {
		"actionKey": "order_GetGoodsOrderPO_operator_supplier_goods_order_to_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "countAmount"
			},
			{
				"fieldName": "code"
			},
			{
				"fieldName": "orderCode"
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
					},
					{
						"fieldName": "isTranslation"
					},
					{
						"fieldName": "purchaserName"
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
							},
							{
								"fieldName": "code"
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
								"fieldName": "lcName"
							}
						]
					},
					{
						"fieldName": "orderRule"
					},
					{
						"fieldName": "payType"
					},
					{
						"fieldName": "orderCreateType"
					},
					{
						"fieldName": "buyer",
						"fields": [
							{
								"fieldName": "id"
							},
							{
								"fieldName": "username"
							}
						]
					},
					{
						"fieldName": "projectReceiverPhone"
					}
				]
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "followDeliveryStatus"
			},
			{
				"fieldName": "followDeliveryUser",
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
				"fieldName": "settleStatus"
			},
			{
				"fieldName": "project"
			},
			{
				"fieldName": "getGoodsAmount"
			},
			{
				"fieldName": "deliveryAmount"
			},
			{
				"fieldName": "expectedArrivalStringDate"
			},
			{
				"fieldName": "orderSubmission"
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
				"fieldName": "confirmDate"
			},
			{
				"fieldName": "existReadyToShipmentPrepayment"
			},
			{
				"fieldName": "dealer",
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
				"fieldName": "supplier",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "name"
					},
					{
						"fieldName": "contactName"
					},
					{
						"fieldName": "contactPhone"
					}
				]
			},
			{
				"fieldName": "remark"
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
# 销售-发货管理
data62 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "order_DeliveryOrderPO",
	"queryValues": {
		"source": {
			"type": "One",
			"value": "saleDeliveryOrdersForOperator"
		}
	},
	"dataSource": {
		"actionKey": "order_DeliveryOrderPO_delivery_order_to_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "isUpload"
			},
			{
				"fieldName": "browseInfo"
			},
			{
				"fieldName": "arrivalRecall"
			},
			{
				"fieldName": "installRecall"
			},
			{
				"fieldName": "arrivalAgainPush"
			},
			{
				"fieldName": "installAgainPush"
			},
			{
				"fieldName": "code"
			},
			{
				"fieldName": "getGoodsOrderCode"
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
						"fieldName": "isTranslation"
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
						"fieldName": "purchaserName"
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
						"fieldName": "orderRule"
					}
				]
			},
			{
				"fieldName": "deliveryOrderCode"
			},
			{
				"fieldName": "getGoodsOrder",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "project"
					}
				]
			},
			{
				"fieldName": "parentDeliveryOrder",
				"fields": [
					{
						"fieldName": "id"
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
								"fieldName": "keyWords"
							}
						]
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
					},
					{
						"fieldName": "keyWords"
					}
				]
			},
			{
				"fieldName": "protocolName"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "platformAuditStatus"
			},
			{
				"fieldName": "deliveryOrderCheckAttachmentPO",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "auditStatus"
					},
					{
						"fieldName": "operationUploadBy",
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
						"fieldName": "supplierUploadBy",
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
						"fieldName": "updatedBy",
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
					}
				]
			},
			{
				"fieldName": "isInstall"
			},
			{
				"fieldName": "countAmount"
			},
			{
				"fieldName": "deliveryAmount"
			},
			{
				"fieldName": "deliveryDate"
			},
			{
				"fieldName": "arrivalDate"
			},
			{
				"fieldName": "arrivalStatus"
			},
			{
				"fieldName": "remark"
			},
			{
				"fieldName": "arrivalSignMode"
			},
			{
				"fieldName": "arrivalSignStatus"
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
# 退/换货管理
data63 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "order_ReverseOrderPO",
	"sourceModel": "order_ReverseOrderPO",
	"dataSource": {
		"actionKey": "order_ReverseOrderPO_operator_seller_reverse_exchange"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "isDisplayInvoice"
			},
			{
				"fieldName": "code"
			},
			{
				"fieldName": "deliveryOrder",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "code"
					},
					{
						"fieldName": "parentDeliveryOrder",
						"fields": [
							{
								"fieldName": "id"
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
										"fieldName": "keyWords"
									}
								]
							}
						]
					}
				]
			},
			{
				"fieldName": "acceptanceOrderCode"
			},
			{
				"fieldName": "type"
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
						"fieldName": "isTranslation"
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
						"fieldName": "title"
					},
					{
						"fieldName": "purchaserName"
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
						"fieldName": "orderRule"
					}
				]
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "categoryName"
			},
			{
				"fieldName": "reverseNum"
			},
			{
				"fieldName": "reverseAmount"
			},
			{
				"fieldName": "settleStatus"
			},
			{
				"fieldName": "reverseDate"
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
# 到货验收单
data64 = {
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
		"no": 1,
		"size": 10
	},
	"order": {
		"by": "updatedAt",
		"isAsc": False
	}
}
#安装验收单
data65 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "order_AcceptanceOrderPO",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "order_AcceptanceOrderPO_operator_seller_receipt_acceptance_install_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "installCode"
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
				"fieldName": "installAcceptanceDate"
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
				"fieldName": "payDate"
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
# 退货单
data66 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "order_ReverseOrderPO",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "order_ReverseOrderPO_receipt_operator_seller_reverse_list"
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
				"fieldName": "deliveryOrder",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "code"
					}
				]
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
						"fieldName": "isTranslation"
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
								"fieldName": "keyWords"
							},
							{
								"fieldName": "contractLabel"
							}
						]
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
						"fieldName": "orderRule"
					}
				]
			},
			{
				"fieldName": "categoryName"
			},
			{
				"fieldName": "reverseNum"
			},
			{
				"fieldName": "reverseAmount"
			},
			{
				"fieldName": "settleStatus"
			},
			{
				"fieldName": "reverseDate"
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
#项目结算
url10 ='https://staging-gateway.test.lcscm.cn/zhonghai/settlement-center/settlement-admin/1004893/api/trantor/data-source'
pro_url10 ='https://gateway.lcscm.cn/zhonghai/settlement-center/settlement-admin/1004923/api/trantor/data-source'
data67 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_ProjectSettlement",
	"sourceModel": "settlement_center_ProjectSettlement",
	"searchValues": {
		"identity": {
			"type": "One",
			"value": "ADMIN"
		}
	},
	"dataSource": {
		"actionKey": "settlement_center_ProjectSettlement_lc_project_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
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
						"fieldName": "corporateCompany",
						"fields": [
							{
								"fieldName": "id"
							},
							{
								"fieldName": "companyName"
							}
						]
					}
				]
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
				"fieldName": "orderSettlementTotal"
			},
			{
				"fieldName": "remainedRetentionMoneyReturned"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "user"
			},
			{
				"fieldName": "purchaseEndTime"
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
# 价款调整
data68 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_PriceAdjust",
	"sourceModel": "settlement_center_PriceAdjust",
	"dataSource": {
		"actionKey": "settlement_center_PriceAdjust_price_adjust_lc_list"
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
				"fieldName": "salesOrderCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "purchaserName"
			},
			{
				"fieldName": "supplierName"
			},
			{
				"fieldName": "signCommon",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "status"
					}
				]
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "totalAmount"
			},
			{
				"fieldName": "salesCheckCode"
			},
			{
				"fieldName": "purchaseCheckCode"
			},
			{
				"fieldName": "changeSubject"
			},
			{
				"fieldName": "remark"
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
# 自助认款 url9
data69 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "order_ApplicationOrderPO",
	"sourceModel": "order_ApplicationOrderPO",
	"dataSource": {
		"actionKey": "order_ApplicationOrderPO_admin_application_order_to_list"
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
				"fieldName": "getGoodsOrderCodes"
			},
			{
				"fieldName": "requirementNo"
			},
			{
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "salesRequestReceiveCode"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "remittanceAmount"
			},
			{
				"fieldName": "unPaidAmount"
			},
			{
				"fieldName": "actualAmount"
			},
			{
				"fieldName": "differenceAmount"
			},
			{
				"fieldName": "approvedUser",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "username"
					}
				]
			},
			{
				"fieldName": "remark"
			},
			{
				"fieldName": "createdAt"
			},
			{
				"fieldName": "lastApprovedDate"
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
# 查询流水  url8
data70 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "contract_domain_Information",
	"sourceModel": "contract_domain_Information",
	"searchValues": {
		"processState": {
			"type": "One",
			"value": "SUSSECE"
		}
	},
	"dataSource": {
		"actionKey": "contract_domain_Information_to_water_information_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "name"
			},
			{
				"fieldName": "swiftSwiftNumber"
			},
			{
				"fieldName": "paymentName"
			},
			{
				"fieldName": "receiptName"
			},
			{
				"fieldName": "amounts"
			},
			{
				"fieldName": "tradeDate"
			},
			{
				"fieldName": "summary"
			},
			{
				"fieldName": "processState"
			},
			{
				"fieldName": "uploadTime"
			},
			{
				"fieldName": "processingTime"
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
				"fieldName": "updatedBy",
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
				"fieldName": "updatedAt"
			},
			{
				"fieldName": "remark"
			},
			{
				"fieldName": "excleRemark"
			},
			{
				"fieldName": "isReceipts"
			},
			{
				"fieldName": "receiptNumber"
			},
			{
				"fieldName": "saleContractLabel"
			},
			{
				"fieldName": "saleContractName"
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
# 采购管理 - 需求单管理 url9
data71 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "order_OrderPO",
	"sourceModel": "order_OrderPO",
	"dataSource": {
		"actionKey": "order_OrderPO_order_operator_purchase_to_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "countAmount"
			},
			{
				"fieldName": "code"
			},
			{
				"fieldName": "title"
			},
			{
				"fieldName": "isTranslation"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "settleStatus"
			},
			{
				"fieldName": "qualityAssuranceStatus"
			},
			{
				"fieldName": "projectReceiverName"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "protocolName"
			},
			{
				"fieldName": "categoryNames"
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
				"fieldName": "parentOrder",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "code"
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
					}
				]
			},
			{
				"fieldName": "purchaserName"
			},
			{
				"fieldName": "dealerName"
			},
			{
				"fieldName": "brandOwnerName"
			},
			{
				"fieldName": "signStatus"
			},
			{
				"fieldName": "orderDate"
			},
			{
				"fieldName": "takeOrderDate"
			},
			{
				"fieldName": "totalAmount"
			},
			{
				"fieldName": "getGoodsAmount"
			},
			{
				"fieldName": "deliveryAmount"
			},
			{
				"fieldName": "reverseAmount"
			},
			{
				"fieldName": "settledAmount"
			},
			{
				"fieldName": "paidAmount"
			},
			{
				"fieldName": "checkedAmount"
			},
			{
				"fieldName": "isAgentOrder"
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
				"fieldName": "orderCreateType"
			},
			{
				"fieldName": "payType"
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
				"fieldName": "id"
			}
		]
	},
	"paging": {
		"no": 1,
		"size": 10
	},
	"order": {
		"by": "createdAt",
		"isAsc": False
	}
}
# 采购管理 - 订单管理
data72 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "order_GetGoodsOrderPO",
	"sourceModel": "order_GetGoodsOrderPO",
	"searchValues": {
		"searchEventType": {
			"type": "One",
			"value": "SEARCH_GOODS_ORDER_BY_OPERATOR_PURCHASER"
		}
	},
	"dataSource": {
		"actionKey": "order_GetGoodsOrderPO_operator_purchase_goods_order_to_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "countAmount"
			},
			{
				"fieldName": "code"
			},
			{
				"fieldName": "orderCode"
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
					},
					{
						"fieldName": "isTranslation"
					},
					{
						"fieldName": "brandOwnerName"
					},
					{
						"fieldName": "purchaserName"
					},
					{
						"fieldName": "parentOrder",
						"fields": [
							{
								"fieldName": "id"
							},
							{
								"fieldName": "code"
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
							}
						]
					},
					{
						"fieldName": "orderCreateType"
					},
					{
						"fieldName": "payType"
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
					}
				]
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "settleStatus"
			},
			{
				"fieldName": "dealerName"
			},
			{
				"fieldName": "project"
			},
			{
				"fieldName": "getGoodsAmount"
			},
			{
				"fieldName": "deliveryAmount"
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
				"fieldName": "expectedArrivalDate"
			},
			{
				"fieldName": "createdAt"
			},
			{
				"fieldName": "confirmDate"
			},
			{
				"fieldName": "remark"
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
# 采购管理 - 收货管理 -全部
data73 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "order_DeliveryOrderPO",
	"queryValues": {
		"tabType": {
			"type": "One",
			"value": "0"
		},
		"source": {
			"type": "One",
			"value": "purchaseDeliveryOrdersForOperator"
		}
	},
	"dataSource": {
		"actionKey": "order_DeliveryOrderPO_receive_order_to_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "browseInfo"
			},
			{
				"fieldName": "arrivalRecall"
			},
			{
				"fieldName": "installRecall"
			},
			{
				"fieldName": "arrivalAgainPush"
			},
			{
				"fieldName": "installAgainPush"
			},
			{
				"fieldName": "code"
			},
			{
				"fieldName": "getGoodsOrderCode"
			},
			{
				"fieldName": "parentDeliveryOrder",
				"fields": [
					{
						"fieldName": "id"
					}
				]
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
						"fieldName": "isTranslation"
					},
					{
						"fieldName": "purchaserName"
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
						"fieldName": "orderRule"
					}
				]
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "platformAuditStatus"
			},
			{
				"fieldName": "getGoodsOrder",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "project"
					}
				]
			},
			{
				"fieldName": "arrivalStatus"
			},
			{
				"fieldName": "dealerName"
			},
			{
				"fieldName": "brandOwner",
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
				"fieldName": "settleStatus"
			},
			{
				"fieldName": "isInstall"
			},
			{
				"fieldName": "limitLevel"
			},
			{
				"fieldName": "deliveryDate"
			},
			{
				"fieldName": "arrivalDate"
			},
			{
				"fieldName": "acceptanceDate"
			},
			{
				"fieldName": "installAcceptanceDate"
			},
			{
				"fieldName": "auditApproveDate"
			},
			{
				"fieldName": "oaDeliveryStatus"
			},
			{
				"fieldName": "arrivalSignMode"
			},
			{
				"fieldName": "arrivalSignStatus"
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
# # 采购管理 - 收货管理 -已发货
data74 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "order_DeliveryOrderPO",
	"sourceModel": "",
	"queryValues": {
		"tabType": {
			"type": "One",
			"value": "1"
		},
		"source": {
			"type": "One",
			"value": "purchaseDeliveryOrdersForOperator"
		}
	},
	"dataSource": {
		"actionKey": "order_DeliveryOrderPO_receive_order_to_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "browseInfo"
			},
			{
				"fieldName": "arrivalRecall"
			},
			{
				"fieldName": "installRecall"
			},
			{
				"fieldName": "arrivalAgainPush"
			},
			{
				"fieldName": "installAgainPush"
			},
			{
				"fieldName": "code"
			},
			{
				"fieldName": "getGoodsOrderCode"
			},
			{
				"fieldName": "parentDeliveryOrder",
				"fields": [
					{
						"fieldName": "id"
					}
				]
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
						"fieldName": "isTranslation"
					},
					{
						"fieldName": "purchaserName"
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
						"fieldName": "orderRule"
					}
				]
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "platformAuditStatus"
			},
			{
				"fieldName": "getGoodsOrder",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "project"
					}
				]
			},
			{
				"fieldName": "arrivalStatus"
			},
			{
				"fieldName": "dealerName"
			},
			{
				"fieldName": "brandOwner",
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
				"fieldName": "settleStatus"
			},
			{
				"fieldName": "isInstall"
			},
			{
				"fieldName": "limitLevel"
			},
			{
				"fieldName": "deliveryDate"
			},
			{
				"fieldName": "arrivalDate"
			},
			{
				"fieldName": "acceptanceDate"
			},
			{
				"fieldName": "installAcceptanceDate"
			},
			{
				"fieldName": "auditApproveDate"
			},
			{
				"fieldName": "oaDeliveryStatus"
			},
			{
				"fieldName": "arrivalSignMode"
			},
			{
				"fieldName": "arrivalSignStatus"
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
#  采购管理 - 收货管理 -已到货验收
data75 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "order_DeliveryOrderPO",
	"sourceModel": "",
	"queryValues": {
		"tabType": {
			"type": "One",
			"value": "2"
		},
		"source": {
			"type": "One",
			"value": "purchaseDeliveryOrdersForOperator"
		}
	},
	"dataSource": {
		"actionKey": "order_DeliveryOrderPO_receive_order_to_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "browseInfo"
			},
			{
				"fieldName": "arrivalRecall"
			},
			{
				"fieldName": "installRecall"
			},
			{
				"fieldName": "arrivalAgainPush"
			},
			{
				"fieldName": "installAgainPush"
			},
			{
				"fieldName": "code"
			},
			{
				"fieldName": "getGoodsOrderCode"
			},
			{
				"fieldName": "parentDeliveryOrder",
				"fields": [
					{
						"fieldName": "id"
					}
				]
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
						"fieldName": "isTranslation"
					},
					{
						"fieldName": "purchaserName"
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
						"fieldName": "orderRule"
					}
				]
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "platformAuditStatus"
			},
			{
				"fieldName": "getGoodsOrder",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "project"
					}
				]
			},
			{
				"fieldName": "arrivalStatus"
			},
			{
				"fieldName": "dealerName"
			},
			{
				"fieldName": "brandOwner",
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
				"fieldName": "settleStatus"
			},
			{
				"fieldName": "isInstall"
			},
			{
				"fieldName": "limitLevel"
			},
			{
				"fieldName": "deliveryDate"
			},
			{
				"fieldName": "arrivalDate"
			},
			{
				"fieldName": "acceptanceDate"
			},
			{
				"fieldName": "installAcceptanceDate"
			},
			{
				"fieldName": "auditApproveDate"
			},
			{
				"fieldName": "oaDeliveryStatus"
			},
			{
				"fieldName": "arrivalSignMode"
			},
			{
				"fieldName": "arrivalSignStatus"
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
# 采购管理 - 收货管理 -已安装验收
data76 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "order_DeliveryOrderPO",
	"sourceModel": "",
	"queryValues": {
		"tabType": {
			"type": "One",
			"value": "3"
		},
		"source": {
			"type": "One",
			"value": "purchaseDeliveryOrdersForOperator"
		}
	},
	"dataSource": {
		"actionKey": "order_DeliveryOrderPO_receive_order_to_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "browseInfo"
			},
			{
				"fieldName": "arrivalRecall"
			},
			{
				"fieldName": "installRecall"
			},
			{
				"fieldName": "arrivalAgainPush"
			},
			{
				"fieldName": "installAgainPush"
			},
			{
				"fieldName": "code"
			},
			{
				"fieldName": "getGoodsOrderCode"
			},
			{
				"fieldName": "parentDeliveryOrder",
				"fields": [
					{
						"fieldName": "id"
					}
				]
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
						"fieldName": "isTranslation"
					},
					{
						"fieldName": "purchaserName"
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
						"fieldName": "orderRule"
					}
				]
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "platformAuditStatus"
			},
			{
				"fieldName": "getGoodsOrder",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "project"
					}
				]
			},
			{
				"fieldName": "arrivalStatus"
			},
			{
				"fieldName": "dealerName"
			},
			{
				"fieldName": "brandOwner",
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
				"fieldName": "settleStatus"
			},
			{
				"fieldName": "isInstall"
			},
			{
				"fieldName": "limitLevel"
			},
			{
				"fieldName": "deliveryDate"
			},
			{
				"fieldName": "arrivalDate"
			},
			{
				"fieldName": "acceptanceDate"
			},
			{
				"fieldName": "installAcceptanceDate"
			},
			{
				"fieldName": "auditApproveDate"
			},
			{
				"fieldName": "oaDeliveryStatus"
			},
			{
				"fieldName": "arrivalSignMode"
			},
			{
				"fieldName": "arrivalSignStatus"
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
# 采购管理 - 收货管理 -已中止
data77 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "order_DeliveryOrderPO",
	"sourceModel": "",
	"queryValues": {
		"tabType": {
			"type": "One",
			"value": "4"
		},
		"source": {
			"type": "One",
			"value": "purchaseDeliveryOrdersForOperator"
		}
	},
	"dataSource": {
		"actionKey": "order_DeliveryOrderPO_receive_order_to_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "browseInfo"
			},
			{
				"fieldName": "arrivalRecall"
			},
			{
				"fieldName": "installRecall"
			},
			{
				"fieldName": "arrivalAgainPush"
			},
			{
				"fieldName": "installAgainPush"
			},
			{
				"fieldName": "code"
			},
			{
				"fieldName": "getGoodsOrderCode"
			},
			{
				"fieldName": "parentDeliveryOrder",
				"fields": [
					{
						"fieldName": "id"
					}
				]
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
						"fieldName": "isTranslation"
					},
					{
						"fieldName": "purchaserName"
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
						"fieldName": "orderRule"
					}
				]
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "platformAuditStatus"
			},
			{
				"fieldName": "getGoodsOrder",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "project"
					}
				]
			},
			{
				"fieldName": "arrivalStatus"
			},
			{
				"fieldName": "dealerName"
			},
			{
				"fieldName": "brandOwner",
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
				"fieldName": "settleStatus"
			},
			{
				"fieldName": "isInstall"
			},
			{
				"fieldName": "limitLevel"
			},
			{
				"fieldName": "deliveryDate"
			},
			{
				"fieldName": "arrivalDate"
			},
			{
				"fieldName": "acceptanceDate"
			},
			{
				"fieldName": "installAcceptanceDate"
			},
			{
				"fieldName": "auditApproveDate"
			},
			{
				"fieldName": "oaDeliveryStatus"
			},
			{
				"fieldName": "arrivalSignMode"
			},
			{
				"fieldName": "arrivalSignStatus"
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
# 采购管理 - 收货管理 -待审批发货单
data78 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "order_DeliveryOrderPO",
	"sourceModel": "",
	"queryValues": {
		"tabType": {
			"type": "One",
			"value": "5"
		},
		"source": {
			"type": "One",
			"value": "purchaseDeliveryOrdersForOperator"
		}
	},
	"dataSource": {
		"actionKey": "order_DeliveryOrderPO_unapprove_delivery_order_to_list"
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
				"fieldName": "getGoodsOrder",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "code"
					},
					{
						"fieldName": "status"
					},
					{
						"fieldName": "project"
					},
					{
						"fieldName": "settleStatus"
					},
					{
						"fieldName": "getGoodsAmount"
					}
				]
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
					},
					{
						"fieldName": "isTranslation"
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
							}
						]
					},
					{
						"fieldName": "purchaserName"
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
						"fieldName": "orderCreateType"
					}
				]
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "platformAuditStatus"
			},
			{
				"fieldName": "oaDeliveryStatus"
			},
			{
				"fieldName": "deliveryOrderCheckAttachmentPO",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "auditStatus"
					}
				]
			},
			{
				"fieldName": "dealer",
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
				"fieldName": "brandOwner",
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
				"fieldName": "isInstall"
			},
			{
				"fieldName": "createdAt"
			},
			{
				"fieldName": "deliveryDate"
			},
			{
				"fieldName": "arrivalDate"
			},
			{
				"fieldName": "deliveryOrderLinePOList",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "deliveryNum"
					}
				],
				"page": {
					"curPage": 1,
					"pageSize": 650
				}
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
# 采购管理 - 退/换货管理
data79 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "order_ReverseOrderPO",
	"sourceModel": "order_ReverseOrderPO",
	"dataSource": {
		"actionKey": "order_ReverseOrderPO_operator_purchase_reverse_exchange"
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
				"fieldName": "deliveryOrder",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "code"
					}
				]
			},
			{
				"fieldName": "acceptanceOrderCode"
			},
			{
				"fieldName": "type"
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
						"fieldName": "isTranslation"
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
						"fieldName": "contract",
						"fields": [
							{
								"fieldName": "id"
							},
							{
								"fieldName": "name"
							},
							{
								"fieldName": "keyWords"
							}
						]
					},
					{
						"fieldName": "protocolName"
					},
					{
						"fieldName": "title"
					},
					{
						"fieldName": "purchaserName"
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
						"fieldName": "dealerName"
					},
					{
						"fieldName": "brandOwnerName"
					}
				]
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "categoryName"
			},
			{
				"fieldName": "reverseNum"
			},
			{
				"fieldName": "reverseAmount"
			},
			{
				"fieldName": "settleStatus"
			},
			{
				"fieldName": "reverseDate"
			},
			{
				"fieldName": "auditStatus"
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
#采购管理 -  到货验收单
data80 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "order_AcceptanceOrderPO",
	"sourceModel": "order_AcceptanceOrderPO",
	"dataSource": {
		"actionKey": "order_AcceptanceOrderPO_operator_purchase_receipt_acceptance_list"
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
						"fieldName": "isTranslation"
					},
					{
						"fieldName": "dealerName"
					},
					{
						"fieldName": "brandOwnerName"
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
						"fieldName": "title"
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
		"no": 1,
		"size": 10
	},
	"order": {
		"by": "updatedAt",
		"isAsc": False
	}
}
# 采购管理 -  安装验收单
data81 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "order_AcceptanceOrderPO",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "order_AcceptanceOrderPO_operator_purchase_receipt_acceptance_install_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "installCode"
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
						"fieldName": "isTranslation"
					},
					{
						"fieldName": "dealer",
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
						"fieldName": "brandOwnerName"
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
						"fieldName": "title"
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
				"fieldName": "installAcceptanceDate"
			},
			{
				"fieldName": "acceptanceOrderLinePOList",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "acceptanceNum"
					},
					{
						"fieldName": "orderLinePO",
						"fields": [
							{
								"fieldName": "id"
							},
							{
								"fieldName": "deliveryFee"
							}
						]
					}
				],
				"page": {
					"curPage": 1,
					"pageSize": 650
				}
			},
			{
				"fieldName": "reverseAmount"
			},
			{
				"fieldName": "payDate"
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
# 购管理 -  退货单
data82 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "order_ReverseOrderPO",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "order_ReverseOrderPO_receipt_operator_purchase_reverse_list"
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
				"fieldName": "deliveryOrder",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "code"
					}
				]
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
						"fieldName": "isTranslation"
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
								"fieldName": "keyWords"
							}
						]
					},
					{
						"fieldName": "protocolName"
					},
					{
						"fieldName": "dealerName"
					},
					{
						"fieldName": "brandOwnerName"
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
						"fieldName": "title"
					}
				]
			},
			{
				"fieldName": "categoryName"
			},
			{
				"fieldName": "reverseNum"
			},
			{
				"fieldName": "reverseAmount"
			},
			{
				"fieldName": "settleStatus"
			},
			{
				"fieldName": "reverseDate"
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
#奖罚管理
data83 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "order_AwardManagePO",
	"sourceModel": "order_AwardManagePO",
	"dataSource": {
		"actionKey": "order_AwardManagePO_award_manage_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "supplierEventCode"
			},
			{
				"fieldName": "objectTypeName"
			},
			{
				"fieldName": "objectCode"
			},
			{
				"fieldName": "objectName"
			},
			{
				"fieldName": "brandOwnerCode"
			},
			{
				"fieldName": "brandOwnerName"
			},
			{
				"fieldName": "performanceProjectCode"
			},
			{
				"fieldName": "performanceProjectName"
			},
			{
				"fieldName": "performanceHeadName"
			},
			{
				"fieldName": "pushDeductPointsTypeName"
			},
			{
				"fieldName": "pushDeductPointsIndexName"
			},
			{
				"fieldName": "pushDeductPointsScore"
			},
			{
				"fieldName": "eventOwnershipDate"
			},
			{
				"fieldName": "awardTypeName"
			},
			{
				"fieldName": "awardOwnershipAccountDate"
			},
			{
				"fieldName": "awardCalculateBaseName"
			},
			{
				"fieldName": "receiptTypeName"
			},
			{
				"fieldName": "receiptName"
			},
			{
				"fieldName": "receiptCode"
			},
			{
				"fieldName": "receiptAmount"
			},
			{
				"fieldName": "awardAmount"
			},
			{
				"fieldName": "statusName"
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
# 销售结算-应收账单 url10
data84 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_ReceivableMergePO",
	"sourceModel": "settlement_center_ReceivableMergePO",
	"dataSource": {
		"actionKey": "settlement_center_ReceivableMergePO_lc_receivable_merge_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "listId"
			},
			{
				"fieldName": "receivableSourceType"
			},
			{
				"fieldName": "receivableSourceCode"
			},
			{
				"fieldName": "purchaserCode"
			},
			{
				"fieldName": "purchaseName"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
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
					}
				]
			},
			{
				"fieldName": "performanceHeadStr"
			},
			{
				"fieldName": "corporateCompanyName"
			},
			{
				"fieldName": "categoryName"
			},
			{
				"fieldName": "paymentConditionName"
			},
			{
				"fieldName": "payableTypeStr"
			},
			{
				"fieldName": "receivableSourceTotalAmount"
			},
			{
				"fieldName": "receivableRate"
			},
			{
				"fieldName": "clearPercent"
			},
			{
				"fieldName": "totalAmount"
			},
			{
				"fieldName": "receivabledAmount"
			},
			{
				"fieldName": "paymentStatus"
			},
			{
				"fieldName": "isReconciliation"
			},
			{
				"fieldName": "salesCheckCode"
			},
			{
				"fieldName": "salesRequestReceiveCode"
			},
			{
				"fieldName": "taxRate"
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
#销售结算-账期销售对账单
data85 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_SalesCheck",
	"sourceModel": "settlement_center_SalesCheck",
	"searchValues": {
		"isFastPayment": {
			"type": "One",
			"value": "IS"
		}
	},
	"dataSource": {
		"actionKey": "settlement_center_SalesCheck_lc_sales_check_list"
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
				"fieldName": "purchaserName"
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
						"fieldName": "financeSysCode"
					},
					{
						"fieldName": "contractLabel"
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
								"fieldName": "quotationHeadStr"
							},
							{
								"fieldName": "performanceHeadStr"
							},
							{
								"fieldName": "salesHeadStr"
							},
							{
								"fieldName": "salesSupportStr"
							}
						]
					}
				]
			},
			{
				"fieldName": "isTranslation"
			},
			{
				"fieldName": "remark"
			},
			{
				"fieldName": "checkAcceptMonth"
			},
			{
				"fieldName": "adjustInvoiceTotal"
			},
			{
				"fieldName": "contractCompletedTotal"
			},
			{
				"fieldName": "advanceTotal"
			},
			{
				"fieldName": "depositTotal"
			},
			{
				"fieldName": "settleTotal"
			},
			{
				"fieldName": "countAmount"
			},
			{
				"fieldName": "finalTotal"
			},
			{
				"fieldName": "outlineCheck"
			},
			{
				"fieldName": "isFastPayment"
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
				"fieldName": "signCommonCurrent",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "status"
					}
				]
			},
			{
				"fieldName": "createdAt"
			},
			{
				"fieldName": "submitTime"
			},
			{
				"fieldName": "confirmTime"
			},
			{
				"fieldName": "usedStatus"
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
#销售结算-非账期销售对账单
data86 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_SalesCheck",
	"sourceModel": "",
	"searchValues": {
		"isFastPayment": {
			"type": "One",
			"value": "NOT"
		}
	},
	"dataSource": {
		"actionKey": "settlement_center_SalesCheck_lc_sales_check_non_account_period_list"
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
				"fieldName": "purchaserName"
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
						"fieldName": "financeSysCode"
					},
					{
						"fieldName": "contractLabel"
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
								"fieldName": "quotationHeadStr"
							},
							{
								"fieldName": "performanceHeadStr"
							},
							{
								"fieldName": "salesHeadStr"
							},
							{
								"fieldName": "salesSupportStr"
							}
						]
					}
				]
			},
			{
				"fieldName": "isTranslation"
			},
			{
				"fieldName": "remark"
			},
			{
				"fieldName": "checkAcceptMonth"
			},
			{
				"fieldName": "adjustInvoiceTotal"
			},
			{
				"fieldName": "contractCompletedTotal"
			},
			{
				"fieldName": "advanceTotal"
			},
			{
				"fieldName": "depositTotal"
			},
			{
				"fieldName": "settleTotal"
			},
			{
				"fieldName": "finalTotal"
			},
			{
				"fieldName": "outlineCheck"
			},
			{
				"fieldName": "isFastPayment"
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
				"fieldName": "signCommonCurrent",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "status"
					}
				]
			},
			{
				"fieldName": "createdAt"
			},
			{
				"fieldName": "submitTime"
			},
			{
				"fieldName": "confirmTime"
			},
			{
				"fieldName": "usedStatus"
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
#销售结算-发票管理
data87 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_SalesInvoice",
	"sourceModel": "settlement_center_SalesInvoice",
	"dataSource": {
		"actionKey": "settlement_center_SalesInvoice_lc_sales_invoice_to_list"
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
				"fieldName": "salesRequestReceiveCode"
			},
			{
				"fieldName": "salesRequestReceiveName"
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
					}
				]
			},
			{
				"fieldName": "salesRequestReceive",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "salesCheckId",
						"fields": [
							{
								"fieldName": "id"
							},
							{
								"fieldName": "salesCheckCode"
							}
						]
					}
				]
			},
			{
				"fieldName": "receivableType"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "purchaserName"
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
				"fieldName": "invoiceType"
			},
			{
				"fieldName": "invoiceHeaderType"
			},
			{
				"fieldName": "salesTotal"
			},
			{
				"fieldName": "contractCompletedTotal"
			},
			{
				"fieldName": "taxAdjustTotal"
			},
			{
				"fieldName": "payMethodAdjustTotal"
			},
			{
				"fieldName": "outContractChangeTotal"
			},
			{
				"fieldName": "reverseAdjustAmount"
			},
			{
				"fieldName": "reverseAmount"
			},
			{
				"fieldName": "createdAt"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "isMail"
			},
			{
				"fieldName": "waybillNo"
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
# 销售结算-邮寄单管理
data88 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_SendOrderManage",
	"sourceModel": "settlement_center_SendOrderManage",
	"dataSource": {
		"actionKey": "settlement_center_SendOrderManage_send_order_manage_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "waybillNo"
			},
			{
				"fieldName": "postOrder"
			},
			{
				"fieldName": "senderName"
			},
			{
				"fieldName": "senderPhone"
			},
			{
				"fieldName": "recipientsAddress"
			},
			{
				"fieldName": "recipientsName"
			},
			{
				"fieldName": "recipientsPhone"
			},
			{
				"fieldName": "postOrdersTime"
			},
			{
				"fieldName": "status"
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
# 账期收款申请
data89 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_SalesRequestReceive",
	"sourceModel": "settlement_center_SalesRequestReceive",
	"searchValues": {
		"salesCheckId.isFastPayment": {
			"type": "One",
			"value": "IS"
		}
	},
	"dataSource": {
		"actionKey": "settlement_center_SalesRequestReceive_sales_request_receive_list"
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
				"fieldName": "swiftSwiftNumber"
			},
			{
				"fieldName": "salesCheckId",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "salesCheckCode"
					},
					{
						"fieldName": "purchaserName"
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
							}
						]
					},
					{
						"fieldName": "outlineCheck"
					},
					{
						"fieldName": "isFastPayment"
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
				"fieldName": "zjCode"
			},
			{
				"fieldName": "countAmount"
			},
			{
				"fieldName": "salesReceiveTotal"
			},
			{
				"fieldName": "salesInvoice",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "code"
					},
					{
						"fieldName": "invoiceDate"
					},
					{
						"fieldName": "status"
					}
				]
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
				"fieldName": "gatewayStatus"
			},
			{
				"fieldName": "refundOaStatus"
			},
			{
				"fieldName": "receivedTotal"
			},
			{
				"fieldName": "createdAt"
			},
			{
				"fieldName": "isClosure"
			},
			{
				"fieldName": "auditStatus"
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
# 非账期收款申请
data90 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_SalesRequestReceive",
	"sourceModel": "",
	"searchValues": {
		"salesCheckId.isFastPayment": {
			"type": "One",
			"value": "NOT"
		}
	},
	"dataSource": {
		"actionKey": "settlement_center_SalesRequestReceive_sales_request_receive_non_account_period_list"
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
				"fieldName": "swiftSwiftNumber"
			},
			{
				"fieldName": "salesCheckId",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "salesCheckCode"
					},
					{
						"fieldName": "purchaserName"
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
							}
						]
					},
					{
						"fieldName": "outlineCheck"
					},
					{
						"fieldName": "isFastPayment"
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
				"fieldName": "zjCode"
			},
			{
				"fieldName": "countAmount"
			},
			{
				"fieldName": "salesReceiveTotal"
			},
			{
				"fieldName": "salesInvoice",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "code"
					},
					{
						"fieldName": "invoiceDate"
					},
					{
						"fieldName": "status"
					}
				]
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
				"fieldName": "gatewayStatus"
			},
			{
				"fieldName": "refundOaStatus"
			},
			{
				"fieldName": "receivedTotal"
			},
			{
				"fieldName": "createdAt"
			},
			{
				"fieldName": "auditStatus"
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
# 撮合合同收款申请
data91 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_ServiceRequestReceive",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "settlement_center_ServiceRequestReceive_service_request_receive_list"
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
				"fieldName": "contractMateReconId",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "partAName"
					},
					{
						"fieldName": "contractName"
					}
				]
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "salesReceiveTotal"
			},
			{
				"fieldName": "receivedTotal"
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
#未分配流水
data92= {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_CorporateCompanySalesVo",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "settlement_center_CorporateCompanySalesVo_no_distribute_corporate_company_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "companyName"
			},
			{
				"fieldName": "distributeMoney"
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
# 流水记录
data93= {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "contract_domain_Information",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "contract_domain_Information_information_distribute_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "swiftSwiftNumber"
			},
			{
				"fieldName": "paymentName"
			},
			{
				"fieldName": "receiptName"
			},
			{
				"fieldName": "amounts"
			},
			{
				"fieldName": "tradeDate"
			},
			{
				"fieldName": "summary"
			},
			{
				"fieldName": "type"
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
#往来明细
data94 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_SalesCheckAdjust",
	"sourceModel": "settlement_center_SalesCheckAdjust",
	"dataSource": {
		"actionKey": "settlement_center_SalesCheckAdjust_sales_check_adjust_operate_list"
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
				"fieldName": "adjustTotal"
			},
			{
				"fieldName": "adjustType"
			},
			{
				"fieldName": "salesCheckCode"
			},
			{
				"fieldName": "attachment"
			},
			{
				"fieldName": "remark"
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
				"fieldName": "usedStatus"
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
# 退货红冲
data95 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_SalesInvoice",
	"sourceModel": "settlement_center_SalesInvoice",
	"dataSource": {
		"actionKey": "settlement_center_SalesInvoice_lc_deficit_invoice_to_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "type"
			},
			{
				"fieldName": "payType"
			},
			{
				"fieldName": "code"
			},
			{
				"fieldName": "salesRequestReceiveCode"
			},
			{
				"fieldName": "salesRequestReceiveName"
			},
			{
				"fieldName": "pastCode"
			},
			{
				"fieldName": "pastSalesRequestReceiveCode"
			},
			{
				"fieldName": "pastSalesRequestReceiveName"
			},
			{
				"fieldName": "purchaserName"
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
				"fieldName": "contractName"
			},
			{
				"fieldName": "invoiceType"
			},
			{
				"fieldName": "pastSalesInvoice",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "invoiceHeaderType"
					},
					{
						"fieldName": "invoiceType"
					}
				]
			},
			{
				"fieldName": "salesTotal"
			},
			{
				"fieldName": "backTotalAmount"
			},
			{
				"fieldName": "deficitTotalAmount"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "invoiceDate"
			},
			{
				"fieldName": "redConfirmNum"
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
# 收款差异记录
data96 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_SalesRequestReceiveClosureRecord",
	"sourceModel": "settlement_center_SalesRequestReceiveClosureRecord",
	"dataSource": {
		"actionKey": "settlement_center_SalesRequestReceiveClosureRecord_sales_request_receive_closure_list"
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
				"fieldName": "salesReceiveCode"
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
				"fieldName": "oaSequenceId"
			},
			{
				"fieldName": "balanceAmount"
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
			},
			{
				"fieldName": "remark"
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
# 应收账单明细
data97 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_Receivable",
	"sourceModel": "settlement_center_Receivable",
	"dataSource": {
		"actionKey": "settlement_center_Receivable_lc_receivable_list"
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
				"fieldName": "purchaser",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "name"
					},
					{
						"fieldName": "code"
					}
				]
			},
			{
				"fieldName": "purchaseName"
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
					}
				]
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "projectName"
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
					}
				]
			},
			{
				"fieldName": "receivableSourceType"
			},
			{
				"fieldName": "receivableSourceCode"
			},
			{
				"fieldName": "paymentConditionName"
			},
			{
				"fieldName": "receivableType"
			},
			{
				"fieldName": "isReconciliation"
			},
			{
				"fieldName": "isQuickPay"
			},
			{
				"fieldName": "paymentStatus"
			},
			{
				"fieldName": "clearPercent"
			},
			{
				"fieldName": "receivableRate"
			},
			{
				"fieldName": "accountPeriod"
			},
			{
				"fieldName": "categoryName"
			},
			{
				"fieldName": "item",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "name"
					},
					{
						"fieldName": "itemCode"
					}
				]
			},
			{
				"fieldName": "itemName"
			},
			{
				"fieldName": "orderPO",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "code"
					},
					{
						"fieldName": "orderRule"
					}
				]
			},
			{
				"fieldName": "taxRate"
			},
			{
				"fieldName": "taxPrice"
			},
			{
				"fieldName": "taxNotPrice"
			},
			{
				"fieldName": "deliveryFee"
			},
			{
				"fieldName": "installFee"
			},
			{
				"fieldName": "itemCount"
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
		"size": 10
	},
	"order": {
		"by": "updatedAt",
		"isAsc": False
	}
}
#撮合对账列表
data98 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_ContractMateRecon",
	"sourceModel": "settlement_center_ContractMateRecon",
	"dataSource": {
		"actionKey": "settlement_center_ContractMateRecon_sales_contract_ContractMateRecon_Internal_list"
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
				"fieldName": "corporateCompany"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "followDate"
			},
			{
				"fieldName": "accountsAmount"
			},
			{
				"fieldName": "createName"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "createDate"
			},
			{
				"fieldName": "commitDate"
			},
			{
				"fieldName": "confirmDate"
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
# 采购结算-应付账单
data99 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_PayableMergePO",
	"sourceModel": "settlement_center_PayableMergePO",
	"dataSource": {
		"actionKey": "settlement_center_PayableMergePO_lc_payableMerge_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "isReconciliation"
			},
			{
				"fieldName": "payableSourceType"
			},
			{
				"fieldName": "payableSourceCode"
			},
			{
				"fieldName": "supplier",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "name"
					},
					{
						"fieldName": "code"
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
						"fieldName": "code"
					}
				]
			},
			{
				"fieldName": "protocol",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "name"
					},
					{
						"fieldName": "code"
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
					}
				]
			},
			{
				"fieldName": "purchaserName"
			},
			{
				"fieldName": "corporateCompanyName"
			},
			{
				"fieldName": "paymentConditionName"
			},
			{
				"fieldName": "payableTypeStr"
			},
			{
				"fieldName": "payableSourceTotalAmount"
			},
			{
				"fieldName": "payableRate"
			},
			{
				"fieldName": "clearPercent"
			},
			{
				"fieldName": "totalAmount"
			},
			{
				"fieldName": "payableMergeStatus"
			},
			{
				"fieldName": "purchaseCheck",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "approveTime"
					},
					{
						"fieldName": "status"
					}
				]
			},
			{
				"fieldName": "purchaseCode"
			},
			{
				"fieldName": "purchaseRequestPayment",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "approveTime"
					},
					{
						"fieldName": "code"
					},
					{
						"fieldName": "status"
					},
					{
						"fieldName": "purchasePaymentTotal"
					}
				]
			},
			{
				"fieldName": "payTime"
			},
			{
				"fieldName": "listId"
			},
			{
				"fieldName": "paymentTotal"
			},
			{
				"fieldName": "taxRate"
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
# 采购结算-对账管理
data100 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_PurchaseCheck",
	"sourceModel": "settlement_center_PurchaseCheck",
	"dataSource": {
		"actionKey": "settlement_center_PurchaseCheck_lc_purchase_check_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "usedStatus"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "purchaseCheckCode"
			},
			{
				"fieldName": "purchaseCheckName"
			},
			{
				"fieldName": "brandOwnerName"
			},
			{
				"fieldName": "supplierName"
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
						"fieldName": "financeSysCode"
					}
				]
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "protocol",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "name"
					},
					{
						"fieldName": "financeSysCode"
					},
					{
						"fieldName": "code"
					}
				]
			},
			{
				"fieldName": "protocolName"
			},
			{
				"fieldName": "cscecGuid"
			},
			{
				"fieldName": "pushGatewayStatus"
			},
			{
				"fieldName": "isTranslation"
			},
			{
				"fieldName": "checkAcceptMonth"
			},
			{
				"fieldName": "adjustInvoiceTotal"
			},
			{
				"fieldName": "contractCompletedTotal"
			},
			{
				"fieldName": "advanceTotal"
			},
			{
				"fieldName": "depositTotal"
			},
			{
				"fieldName": "settleTotal"
			},
			{
				"fieldName": "finalTotal"
			},
			{
				"fieldName": "alreadyPaymentsNumber"
			},
			{
				"fieldName": "alreadyPaymentsAmount"
			},
			{
				"fieldName": "notPaymentsAmount"
			},
			{
				"fieldName": "alreadyRealityPaymentsAmount"
			},
			{
				"fieldName": "notAlreadyRealityPaymentsAmount"
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
				"fieldName": "signCommonCurrent",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "status"
					}
				]
			},
			{
				"fieldName": "submitTime"
			},
			{
				"fieldName": "confirmTime"
			},
			{
				"fieldName": "invoiceTotalAmount"
			},
			{
				"fieldName": "invoiceStatus"
			},
			{
				"fieldName": "returnReansonAndReturnRemark"
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
# 采购结算-付款申请
data101 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_PurchaseRequestPayment",
	"sourceModel": "settlement_center_PurchaseRequestPayment",
	"dataSource": {
		"actionKey": "settlement_center_PurchaseRequestPayment_purchase_request_payment_list"
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
				"fieldName": "purchaseCheckId",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "purchaseCheckCode"
					},
					{
						"fieldName": "brandOwnerName"
					},
					{
						"fieldName": "supplierName"
					},
					{
						"fieldName": "contractCode"
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
								"fieldName": "financeSysCode"
							},
							{
								"fieldName": "isTranslation"
							}
						]
					},
					{
						"fieldName": "protocol",
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
								"fieldName": "financeSysCode"
							}
						]
					},
					{
						"fieldName": "protocolName"
					}
				]
			},
			{
				"fieldName": "cscecGuid"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "purchasePaymentTotal"
			},
			{
				"fieldName": "payedTotal"
			},
			{
				"fieldName": "actualUnpaidAmount"
			},
			{
				"fieldName": "payTime"
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
				"fieldName": "pushGatewayStatus"
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
# 采购结算-往来明细
data102 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_PurchaseCheckAdjust",
	"sourceModel": "settlement_center_PurchaseCheckAdjust",
	"dataSource": {
		"actionKey": "settlement_center_PurchaseCheckAdjust_purchase_check_adjust_list"
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
				"fieldName": "order",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "code"
					},
					{
						"fieldName": "supplierName"
					},
					{
						"fieldName": "contractName"
					},
					{
						"fieldName": "protocolName"
					}
				]
			},
			{
				"fieldName": "adjustTotal"
			},
			{
				"fieldName": "adjustType"
			},
			{
				"fieldName": "purchaseCheckCode"
			},
			{
				"fieldName": "attachment"
			},
			{
				"fieldName": "remark"
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
				"fieldName": "salesCheckAdjust",
				"fields": [
					{
						"fieldName": "id"
					}
				]
			},
			{
				"fieldName": "usedStatus"
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
# 采购结算-应付账单明细
data103 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_Payable",
	"sourceModel": "settlement_center_Payable",
	"dataSource": {
		"actionKey": "settlement_center_Payable_lc_payable_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "payableCode"
			},
			{
				"fieldName": "supplier",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "name"
					},
					{
						"fieldName": "code"
					}
				]
			},
			{
				"fieldName": "supplierName"
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
					}
				]
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "protocol",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "name"
					},
					{
						"fieldName": "code"
					}
				]
			},
			{
				"fieldName": "protocolName"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "orderPO",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "code"
					},
					{
						"fieldName": "parentOrder",
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
								"fieldName": "corporateCompanyName"
							}
						]
					}
				]
			},
			{
				"fieldName": "paymentStatus"
			},
			{
				"fieldName": "payableSourceType"
			},
			{
				"fieldName": "payableSourceCode"
			},
			{
				"fieldName": "paymentConditionName"
			},
			{
				"fieldName": "payableType"
			},
			{
				"fieldName": "payableRate"
			},
			{
				"fieldName": "clearPercent"
			},
			{
				"fieldName": "accountPeriod"
			},
			{
				"fieldName": "isReconciliation"
			},
			{
				"fieldName": "categoryName"
			},
			{
				"fieldName": "item",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "name"
					},
					{
						"fieldName": "itemCode"
					}
				]
			},
			{
				"fieldName": "itemName"
			},
			{
				"fieldName": "taxRate"
			},
			{
				"fieldName": "price"
			},
			{
				"fieldName": "deliveryFee"
			},
			{
				"fieldName": "installFee"
			},
			{
				"fieldName": "itemCount"
			},
			{
				"fieldName": "totalAmount"
			},
			{
				"fieldName": "createdAt"
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
# 采购结算-项目结算汇总表 url9
data104 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "order_SupplierAndProject",
	"sourceModel": "order_SupplierAndProject",
	"dataSource": {
		"actionKey": "order_SupplierAndProject_operator_supplier_project_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "supplierCode"
			},
			{
				"fieldName": "supplierName"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "projectCode"
			},
			{
				"fieldName": "performanceHeadStr"
			},
			{
				"fieldName": "address"
			},
			{
				"fieldName": "totalAmount"
			},
			{
				"fieldName": "getGoodsOrderAmount"
			},
			{
				"fieldName": "deliveryAmount"
			},
			{
				"fieldName": "acceptanceAmount"
			},
			{
				"fieldName": "installAcceptanceAmount"
			},
			{
				"fieldName": "reverseSumAmount"
			},
			{
				"fieldName": "checkedAmount"
			},
			{
				"fieldName": "paidAmount"
			},
			{
				"fieldName": "notPaidAmount"
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
# 签章信息 url1
data105 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_SignMessageVO",
	"sourceModel": "master_data_server_SignMessageVO",
	"dataSource": {
		"actionKey": "master_data_server_SignMessageVO_to_yy_sign_message_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "imagesBase"
			},
			{
				"fieldName": "type"
			},
			{
				"fieldName": "createName"
			},
			{
				"fieldName": "administrators"
			},
			{
				"fieldName": "createAt"
			},
			{
				"fieldName": "status"
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
#签章统计
data106= {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_SignCommon",
	"sourceModel": "settlement_center_SignCommon",
	"dataSource": {
		"actionKey": "settlement_center_SignCommon_lc_sign_common_List"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "name"
			},
			{
				"fieldName": "type"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "signType"
			},
			{
				"fieldName": "signName"
			},
			{
				"fieldName": "partA"
			},
			{
				"fieldName": "partB"
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
# 收入成本报表 url10
data107 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_RevenueCostStatement",
	"sourceModel": "settlement_center_RevenueCostStatement",
	"dataSource": {
		"actionKey": "settlement_center_RevenueCostStatement_revenue_cost_statement_list"
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
				"fieldName": "payableCode"
			},
			{
				"fieldName": "purchaseContractName"
			},
			{
				"fieldName": "salesContractName"
			},
			{
				"fieldName": "brandOwnerName"
			},
			{
				"fieldName": "dealerName"
			},
			{
				"fieldName": "salesContractNameLabel"
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
				"fieldName": "sourceBillType"
			},
			{
				"fieldName": "sourceSalesBillCode"
			},
			{
				"fieldName": "sourcePurchaserBillCode"
			},
			{
				"fieldName": "salesGetGoodsOrderCode"
			},
			{
				"fieldName": "purchaseGetGoodsOrderCode"
			},
			{
				"fieldName": "salesAcceptOrderCode"
			},
			{
				"fieldName": "purchaseAcceptOrderCode"
			},
			{
				"fieldName": "salesInstallOrderCode"
			},
			{
				"fieldName": "purchaseInstallOrderCode"
			},
			{
				"fieldName": "salesReverseOrderCode"
			},
			{
				"fieldName": "purchaseReverseOrderCode"
			},
			{
				"fieldName": "sourceBillDate"
			},
			{
				"fieldName": "payableType"
			},
			{
				"fieldName": "categoryName"
			},
			{
				"fieldName": "itemCode"
			},
			{
				"fieldName": "itemName"
			},
			{
				"fieldName": "rate"
			},
			{
				"fieldName": "itemNum"
			},
			{
				"fieldName": "price"
			},
			{
				"fieldName": "deliveryFee"
			},
			{
				"fieldName": "installFee"
			},
			{
				"fieldName": "unitPrice"
			},
			{
				"fieldName": "sourceAmount"
			},
			{
				"fieldName": "payableRate"
			},
			{
				"fieldName": "totalAmount"
			},
			{
				"fieldName": "accountCheckAt"
			},
			{
				"fieldName": "purchaserPrice"
			},
			{
				"fieldName": "purchaserDeliveryFee"
			},
			{
				"fieldName": "purchaserInstallFee"
			},
			{
				"fieldName": "purchaserUnitPrice"
			},
			{
				"fieldName": "purchaserSourceAmount"
			},
			{
				"fieldName": "purchaserPayableRate"
			},
			{
				"fieldName": "purchaserTotalAmount"
			},
			{
				"fieldName": "purchaserAccountCheckAt"
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
#验收单报表
data108 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_AcceptanceReportVo",
	"queryValues": {
		"source": {
			"type": "One",
			"value": "AcceptanceReportForOperator"
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
		"size": 10
	},
	"order": {
		"by": "updatedAt",
		"isAsc": False
	}
}
#金额汇总报表
data109 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_AmountSummaryReportVO",
	"sourceModel": "settlement_center_AmountSummaryReportVO",
	"dataSource": {
		"actionKey": "settlement_center_AmountSummaryReportVO_amount_summary_report_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "summaryType"
			},
			{
				"fieldName": "amount"
			},
			{
				"fieldName": "description"
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
#退货单报表
data110 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_AcceptanceReportVo",
	"sourceModel": "settlement_center_AcceptanceReportVo",
	"dataSource": {
		"actionKey": "settlement_center_AcceptanceReportVo_return_acceptance_report_list"
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
			},
			{
				"fieldName": "reverseDate"
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
# 历史累计报表
data111 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_HistoricalCumulativeReportVO",
	"sourceModel": "settlement_center_HistoricalCumulativeReportVO",
	"dataSource": {
		"actionKey": "settlement_center_HistoricalCumulativeReportVO_historical_cumulative_report_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "supplierName"
			},
			{
				"fieldName": "purchaseContractName"
			},
			{
				"fieldName": "A"
			},
			{
				"fieldName": "A1"
			},
			{
				"fieldName": "A2"
			},
			{
				"fieldName": "A3"
			},
			{
				"fieldName": "A4"
			},
			{
				"fieldName": "A5"
			},
			{
				"fieldName": "A6"
			},
			{
				"fieldName": "B"
			},
			{
				"fieldName": "B1"
			},
			{
				"fieldName": "B2"
			},
			{
				"fieldName": "B3"
			},
			{
				"fieldName": "B4"
			},
			{
				"fieldName": "B5"
			},
			{
				"fieldName": "B6"
			},
			{
				"fieldName": "B7"
			},
			{
				"fieldName": "B8"
			},
			{
				"fieldName": "B9"
			},
			{
				"fieldName": "C"
			},
			{
				"fieldName": "C1"
			},
			{
				"fieldName": "C2"
			},
			{
				"fieldName": "D"
			},
			{
				"fieldName": "D1"
			},
			{
				"fieldName": "D2"
			},
			{
				"fieldName": "D3"
			},
			{
				"fieldName": "E"
			},
			{
				"fieldName": "F"
			},
			{
				"fieldName": "F1"
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
#退货单基础报表
data112 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_AcceptanceReportVo",
	"sourceModel": "settlement_center_AcceptanceReportVo",
	"dataSource": {
		"actionKey": "settlement_center_AcceptanceReportVo_return_acceptance_report_foundation_list"
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
				"fieldName": "salesAcceptedTotal"
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
				"fieldName": "reverseDate"
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
#验收单基础报表
data113 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_AcceptanceReportVo",
	"queryValues": {
		"source": {
			"type": "One",
			"value": "AcceptanceReportForOperator"
		}
	},
	"dataSource": {
		"actionKey": "settlement_center_AcceptanceReportVo_acceptance_report_foundation_list"
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
				"fieldName": "salesAcceptedTotal"
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
#收入成本基础报表
data114 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_RevenueCostStatement",
	"sourceModel": "settlement_center_RevenueCostStatement",
	"dataSource": {
		"actionKey": "settlement_center_RevenueCostStatement_revenue_cost_statement_foundation_list"
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
				"fieldName": "payableCode"
			},
			{
				"fieldName": "purchaseContractName"
			},
			{
				"fieldName": "salesContractName"
			},
			{
				"fieldName": "brandOwnerName"
			},
			{
				"fieldName": "dealerName"
			},
			{
				"fieldName": "salesContractNameLabel"
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
				"fieldName": "sourceBillType"
			},
			{
				"fieldName": "sourceSalesBillCode"
			},
			{
				"fieldName": "sourcePurchaserBillCode"
			},
			{
				"fieldName": "salesGetGoodsOrderCode"
			},
			{
				"fieldName": "purchaseGetGoodsOrderCode"
			},
			{
				"fieldName": "salesAcceptOrderCode"
			},
			{
				"fieldName": "purchaseAcceptOrderCode"
			},
			{
				"fieldName": "salesInstallOrderCode"
			},
			{
				"fieldName": "purchaseInstallOrderCode"
			},
			{
				"fieldName": "salesReverseOrderCode"
			},
			{
				"fieldName": "purchaseReverseOrderCode"
			},
			{
				"fieldName": "sourceBillDate"
			},
			{
				"fieldName": "payableType"
			},
			{
				"fieldName": "categoryName"
			},
			{
				"fieldName": "itemCode"
			},
			{
				"fieldName": "itemName"
			},
			{
				"fieldName": "rate"
			},
			{
				"fieldName": "itemNum"
			},
			{
				"fieldName": "price"
			},
			{
				"fieldName": "deliveryFee"
			},
			{
				"fieldName": "installFee"
			},
			{
				"fieldName": "unitPrice"
			},
			{
				"fieldName": "sourceAmount"
			},
			{
				"fieldName": "payableRate"
			},
			{
				"fieldName": "totalAmount"
			},
			{
				"fieldName": "accountCheckAt"
			},
			{
				"fieldName": "purchaserTotalAmount"
			},
			{
				"fieldName": "purchaserAccountCheckAt"
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
#用户汇总报表
data115 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_MDUserCountReport",
	"sourceModel": "master_data_server_MDUserCountReport",
	"dataSource": {
		"actionKey": "master_data_server_MDUserCountReport_user_count_report_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "countTime"
			},
			{
				"fieldName": "mallRegistrationMonth"
			},
			{
				"fieldName": "mallRegistrationTotal"
			},
			{
				"fieldName": "userCountMonth"
			},
			{
				"fieldName": "userCountTotal"
			},
			{
				"fieldName": "enterpriseAuthMonth"
			},
			{
				"fieldName": "enterpriseAuthTotal"
			},
			{
				"fieldName": "procureAuthMonth"
			},
			{
				"fieldName": "procureAuthTotal"
			},
			{
				"fieldName": "brandMonth"
			},
			{
				"fieldName": "dealerMonth"
			},
			{
				"fieldName": "supplierTotal"
			}
		]
	},
	"paging": {
		"no": 1,
		"size": 10
	},
	"order": {
		"by": "countTime",
		"isAsc": False
	}
}
# 文章分类
url11='https://staging-gateway.test.lcscm.cn/zhonghai/misc/misc-admin/1005441/api/trantor/data-source'
pro_url11 ='https://gateway.lcscm.cn/zhonghai/misc/misc-admin/1004024/api/trantor/data-source'
data116 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "misc_admin_ArticleCategoryVO",
	"sourceModel": "misc_admin_ArticleCategoryVO",
	"dataSource": {
		"actionKey": "misc_admin_ArticleCategoryVO_articleCategoryList"
	},
	"result": {
		"fields": [
			{
				"fieldName": "name"
			},
			{
				"fieldName": "id"
			},
			{
				"fieldName": "subCategoryList"
			},
			{
				"fieldName": "description"
			},
			{
				"fieldName": "articleNum"
			},
			{
				"fieldName": "sortNum"
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
#文章列表
data117 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "misc_admin_ArticleVO",
	"sourceModel": "misc_admin_ArticleVO",
	"dataSource": {
		"actionKey": "misc_admin_ArticleVO_articleList"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "title"
			},
			{
				"fieldName": "firstAndSecondCategoryName"
			},
			{
				"fieldName": "creatorName"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "articleType"
			},
			{
				"fieldName": "sortNum"
			},
			{
				"fieldName": "updatedAt"
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
# 发票管理  全部 url10
data118 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_ApplyInvoiceInfo",
	"sourceModel": "settlement_center_ApplyInvoiceInfo",
	"dataSource": {
		"actionKey": "settlement_center_ApplyInvoiceInfo_lc_invoice_manage_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "applyInvoiceSerialNo"
			},
			{
				"fieldName": "applyInvoiceSerialMergeNo"
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
							}
						]
					}
				]
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "corporateCompanyName"
			},
			{
				"fieldName": "sourceType"
			},
			{
				"fieldName": "sourceInfoList",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "sourceCode"
					}
				],
				"page": {
					"curPage": 1,
					"pageSize": 650
				}
			},
			{
				"fieldName": "salesCheckCode"
			},
			{
				"fieldName": "paymentType"
			},
			{
				"fieldName": "payRate"
			},
			{
				"fieldName": "paymentAmount"
			},
			{
				"fieldName": "noTaxAmount"
			},
			{
				"fieldName": "taxRate"
			},
			{
				"fieldName": "invoiceStatus"
			},
			{
				"fieldName": "invoiceType"
			},
			{
				"fieldName": "isMail"
			},
			{
				"fieldName": "sendStatus"
			},
			{
				"fieldName": "waybillNo"
			},
			{
				"fieldName": "invoiceNum"
			},
			{
				"fieldName": "applyUser",
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
				"fieldName": "applyDate"
			},
			{
				"fieldName": "invoiceDate"
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
# 发票管理 待开票
data119 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_ApplyInvoiceInfo",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "settlement_center_ApplyInvoiceInfo_lc_invoice_manage_to_audit_waitting_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "applyInvoiceSerialNo"
			},
			{
				"fieldName": "applyInvoiceSerialMergeNo"
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
							}
						]
					}
				]
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "corporateCompanyName"
			},
			{
				"fieldName": "sourceType"
			},
			{
				"fieldName": "sourceInfoList",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "sourceCode"
					}
				],
				"page": {
					"curPage": 1,
					"pageSize": 650
				}
			},
			{
				"fieldName": "salesCheckCode"
			},
			{
				"fieldName": "paymentType"
			},
			{
				"fieldName": "payRate"
			},
			{
				"fieldName": "paymentAmount"
			},
			{
				"fieldName": "noTaxAmount"
			},
			{
				"fieldName": "taxRate"
			},
			{
				"fieldName": "invoiceStatus"
			},
			{
				"fieldName": "invoiceType"
			},
			{
				"fieldName": "isMail"
			},
			{
				"fieldName": "waybillNo"
			},
			{
				"fieldName": "invoiceNum"
			},
			{
				"fieldName": "applyUser",
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
				"fieldName": "applyDate"
			},
			{
				"fieldName": "invoiceDate"
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
# 发票管理 审核中
data120 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_ApplyInvoiceInfo",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "settlement_center_ApplyInvoiceInfo_lc_invoice_manage_to_audit_process_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "applyInvoiceSerialNo"
			},
			{
				"fieldName": "applyInvoiceSerialMergeNo"
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
							}
						]
					}
				]
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "corporateCompanyName"
			},
			{
				"fieldName": "sourceType"
			},
			{
				"fieldName": "sourceInfoList",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "sourceCode"
					}
				],
				"page": {
					"curPage": 1,
					"pageSize": 650
				}
			},
			{
				"fieldName": "salesCheckCode"
			},
			{
				"fieldName": "paymentType"
			},
			{
				"fieldName": "payRate"
			},
			{
				"fieldName": "paymentAmount"
			},
			{
				"fieldName": "noTaxAmount"
			},
			{
				"fieldName": "taxRate"
			},
			{
				"fieldName": "invoiceStatus"
			},
			{
				"fieldName": "invoiceType"
			},
			{
				"fieldName": "isMail"
			},
			{
				"fieldName": "waybillNo"
			},
			{
				"fieldName": "invoiceNum"
			},
			{
				"fieldName": "applyUser",
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
				"fieldName": "applyDate"
			},
			{
				"fieldName": "invoiceDate"
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
# 发票管理 已开票
data121 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_ApplyInvoiceInfo",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "settlement_center_ApplyInvoiceInfo_lc_invoice_manage_to_invoiced_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "applyInvoiceSerialNo"
			},
			{
				"fieldName": "applyInvoiceSerialMergeNo"
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
							}
						]
					}
				]
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "corporateCompanyName"
			},
			{
				"fieldName": "sourceType"
			},
			{
				"fieldName": "sourceInfoList",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "sourceCode"
					}
				],
				"page": {
					"curPage": 1,
					"pageSize": 650
				}
			},
			{
				"fieldName": "salesCheckCode"
			},
			{
				"fieldName": "paymentType"
			},
			{
				"fieldName": "payRate"
			},
			{
				"fieldName": "paymentAmount"
			},
			{
				"fieldName": "noTaxAmount"
			},
			{
				"fieldName": "taxRate"
			},
			{
				"fieldName": "invoiceStatus"
			},
			{
				"fieldName": "invoiceType"
			},
			{
				"fieldName": "isMail"
			},
			{
				"fieldName": "sendStatus"
			},
			{
				"fieldName": "waybillNo"
			},
			{
				"fieldName": "invoiceNum"
			},
			{
				"fieldName": "applyUser",
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
				"fieldName": "applyDate"
			},
			{
				"fieldName": "invoiceDate"
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
# 发票管理 已驳回
data122 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_ApplyInvoiceInfo",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "settlement_center_ApplyInvoiceInfo_lc_invoice_manage_to_rejected_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "applyInvoiceSerialNo"
			},
			{
				"fieldName": "applyInvoiceSerialMergeNo"
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
							}
						]
					}
				]
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "corporateCompanyName"
			},
			{
				"fieldName": "sourceType"
			},
			{
				"fieldName": "sourceInfoList",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "sourceCode"
					}
				],
				"page": {
					"curPage": 1,
					"pageSize": 650
				}
			},
			{
				"fieldName": "salesCheckCode"
			},
			{
				"fieldName": "paymentType"
			},
			{
				"fieldName": "payRate"
			},
			{
				"fieldName": "paymentAmount"
			},
			{
				"fieldName": "noTaxAmount"
			},
			{
				"fieldName": "taxRate"
			},
			{
				"fieldName": "invoiceStatus"
			},
			{
				"fieldName": "invoiceType"
			},
			{
				"fieldName": "isMail"
			},
			{
				"fieldName": "waybillNo"
			},
			{
				"fieldName": "invoiceNum"
			},
			{
				"fieldName": "applyUser",
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
				"fieldName": "applyDate"
			},
			{
				"fieldName": "invoiceDate"
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
# 代客申请开票 url5
data123 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "partner_center_CorporateCompany",
	"sourceModel": "partner_center_CorporateCompany",
	"dataSource": {
		"actionKey": "partner_center_CorporateCompany_lc_valet_invoice_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "companyName"
			},
			{
				"fieldName": "uscc"
			},
			{
				"fieldName": "address"
			},
			{
				"fieldName": "contactMobile"
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
 # 发票查询申请人员 url2
data124 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "base_User",
	"dataSource": {
		"type": "DataStore"
	},
	"result": {
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
	"paging": {
		"no": 1,
		"size": 10
	},
	"order": {
		"by": "updatedAt",
		"isAsc": False
	}
}
# 其他业务申请开票 url10
data125 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_ApplyInvoiceInfo",
	"sourceModel": "settlement_center_ApplyInvoiceInfo",
	"dataSource": {
		"actionKey": "settlement_center_ApplyInvoiceInfo_lc_other_invoice_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "applyInvoiceSerialMergeNo"
			},
			{
				"fieldName": "corporateCompanyName"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "totalAmountTax"
			},
			{
				"fieldName": "taxRate"
			},
			{
				"fieldName": "invoiceStatus"
			},
			{
				"fieldName": "invoiceType"
			},
			{
				"fieldName": "isMail"
			},
			{
				"fieldName": "waybillNo"
			},
			{
				"fieldName": "invoiceNum"
			},
			{
				"fieldName": "sourceInfoList",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "sourceCode"
					}
				],
				"page": {
					"curPage": 1,
					"pageSize": 650
				}
			},
			{
				"fieldName": "invoiceDate"
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
#财务审核 -全部
data126 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_ApplyInvoiceInfoMerge",
	"sourceModel": "settlement_center_ApplyInvoiceInfoMerge",
	"dataSource": {
		"actionKey": "settlement_center_ApplyInvoiceInfoMerge_purchaser_invoice_finance_process_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "applyInvoiceSerialNo"
			},
			{
				"fieldName": "sourceType"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "projectName"
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
							}
						]
					}
				]
			},
			{
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "corporateCompanyName"
			},
			{
				"fieldName": "sourceTypeMerge"
			},
			{
				"fieldName": "sourceCodeMerge"
			},
			{
				"fieldName": "salesCheckCodeMerge"
			},
			{
				"fieldName": "paymentTypeMerge"
			},
			{
				"fieldName": "payRateMerge"
			},
			{
				"fieldName": "paymentAmount"
			},
			{
				"fieldName": "noTaxAmount"
			},
			{
				"fieldName": "taxRate"
			},
			{
				"fieldName": "invoiceStatus"
			},
			{
				"fieldName": "invoiceType"
			},
			{
				"fieldName": "isMail"
			},
			{
				"fieldName": "waybillNo"
			},
			{
				"fieldName": "applyUser",
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
				"fieldName": "applyDate"
			},
			{
				"fieldName": "auditDate"
			},
			{
				"fieldName": "invoiceNum"
			},
			{
				"fieldName": "invoiceDate"
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
#财务审核 -待审核
data127 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_ApplyInvoiceInfoMerge",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "settlement_center_ApplyInvoiceInfoMerge_purchaser_invoice_finance_process_to_audit_waitting_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "applyInvoiceSerialNo"
			},
			{
				"fieldName": "sourceType"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "projectName"
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
							}
						]
					}
				]
			},
			{
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "corporateCompanyName"
			},
			{
				"fieldName": "sourceTypeMerge"
			},
			{
				"fieldName": "sourceCodeMerge"
			},
			{
				"fieldName": "salesCheckCodeMerge"
			},
			{
				"fieldName": "paymentTypeMerge"
			},
			{
				"fieldName": "payRateMerge"
			},
			{
				"fieldName": "paymentAmount"
			},
			{
				"fieldName": "noTaxAmount"
			},
			{
				"fieldName": "taxRate"
			},
			{
				"fieldName": "invoiceStatus"
			},
			{
				"fieldName": "invoiceType"
			},
			{
				"fieldName": "isMail"
			},
			{
				"fieldName": "waybillNo"
			},
			{
				"fieldName": "applyUser",
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
				"fieldName": "applyDate"
			},
			{
				"fieldName": "auditDate"
			},
			{
				"fieldName": "invoiceNum"
			},
			{
				"fieldName": "invoiceDate"
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
#财务审核 -审核中
data128 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_ApplyInvoiceInfoMerge",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "settlement_center_ApplyInvoiceInfoMerge_purchaser_invoice_finance_process_to_audit_process_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "applyInvoiceSerialNo"
			},
			{
				"fieldName": "sourceType"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "projectName"
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
							}
						]
					}
				]
			},
			{
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "corporateCompanyName"
			},
			{
				"fieldName": "sourceTypeMerge"
			},
			{
				"fieldName": "sourceCodeMerge"
			},
			{
				"fieldName": "salesCheckCodeMerge"
			},
			{
				"fieldName": "paymentTypeMerge"
			},
			{
				"fieldName": "payRateMerge"
			},
			{
				"fieldName": "paymentAmount"
			},
			{
				"fieldName": "noTaxAmount"
			},
			{
				"fieldName": "taxRate"
			},
			{
				"fieldName": "invoiceStatus"
			},
			{
				"fieldName": "invoiceType"
			},
			{
				"fieldName": "isMail"
			},
			{
				"fieldName": "waybillNo"
			},
			{
				"fieldName": "applyUser",
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
				"fieldName": "applyDate"
			},
			{
				"fieldName": "auditDate"
			},
			{
				"fieldName": "invoiceNum"
			},
			{
				"fieldName": "invoiceDate"
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
#财务审核 -已开票
data129 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_ApplyInvoiceInfoMerge",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "settlement_center_ApplyInvoiceInfoMerge_purchaser_invoice_finance_process_to_invoiced_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "applyInvoiceSerialNo"
			},
			{
				"fieldName": "sourceType"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "projectName"
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
							}
						]
					}
				]
			},
			{
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "corporateCompanyName"
			},
			{
				"fieldName": "sourceTypeMerge"
			},
			{
				"fieldName": "sourceCodeMerge"
			},
			{
				"fieldName": "salesCheckCodeMerge"
			},
			{
				"fieldName": "paymentTypeMerge"
			},
			{
				"fieldName": "payRateMerge"
			},
			{
				"fieldName": "paymentAmount"
			},
			{
				"fieldName": "noTaxAmount"
			},
			{
				"fieldName": "taxRate"
			},
			{
				"fieldName": "invoiceStatus"
			},
			{
				"fieldName": "invoiceType"
			},
			{
				"fieldName": "isMail"
			},
			{
				"fieldName": "waybillNo"
			},
			{
				"fieldName": "applyUser",
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
				"fieldName": "applyDate"
			},
			{
				"fieldName": "auditDate"
			},
			{
				"fieldName": "invoiceNum"
			},
			{
				"fieldName": "invoiceDate"
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
#财务审核 -已驳回
data130 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_ApplyInvoiceInfoMerge",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "settlement_center_ApplyInvoiceInfoMerge_purchaser_invoice_finance_process_to_rejected_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "applyInvoiceSerialNo"
			},
			{
				"fieldName": "sourceType"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "projectName"
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
							}
						]
					}
				]
			},
			{
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "corporateCompanyName"
			},
			{
				"fieldName": "sourceTypeMerge"
			},
			{
				"fieldName": "sourceCodeMerge"
			},
			{
				"fieldName": "salesCheckCodeMerge"
			},
			{
				"fieldName": "paymentTypeMerge"
			},
			{
				"fieldName": "payRateMerge"
			},
			{
				"fieldName": "paymentAmount"
			},
			{
				"fieldName": "noTaxAmount"
			},
			{
				"fieldName": "taxRate"
			},
			{
				"fieldName": "invoiceStatus"
			},
			{
				"fieldName": "invoiceType"
			},
			{
				"fieldName": "isMail"
			},
			{
				"fieldName": "waybillNo"
			},
			{
				"fieldName": "applyUser",
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
				"fieldName": "applyDate"
			},
			{
				"fieldName": "auditDate"
			},
			{
				"fieldName": "invoiceNum"
			},
			{
				"fieldName": "invoiceDate"
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
# 财务复核-全部
data131 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_ApplyInvoiceInfoMerge",
	"sourceModel": "settlement_center_ApplyInvoiceInfoMerge",
	"dataSource": {
		"actionKey": "settlement_center_ApplyInvoiceInfoMerge_purchaser_invoice_finance_check_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "applyInvoiceSerialNo"
			},
			{
				"fieldName": "sourceType"
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
							}
						]
					}
				]
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "corporateCompanyName"
			},
			{
				"fieldName": "sourceTypeMerge"
			},
			{
				"fieldName": "sourceCodeMerge"
			},
			{
				"fieldName": "salesCheckCodeMerge"
			},
			{
				"fieldName": "paymentTypeMerge"
			},
			{
				"fieldName": "payRateMerge"
			},
			{
				"fieldName": "paymentAmount"
			},
			{
				"fieldName": "noTaxAmount"
			},
			{
				"fieldName": "taxRate"
			},
			{
				"fieldName": "invoiceStatus"
			},
			{
				"fieldName": "invoiceType"
			},
			{
				"fieldName": "isMail"
			},
			{
				"fieldName": "waybillNo"
			},
			{
				"fieldName": "applyUser",
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
				"fieldName": "applyDate"
			},
			{
				"fieldName": "checkDate"
			},
			{
				"fieldName": "invoiceNum"
			},
			{
				"fieldName": "invoiceDate"
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
# 财务复核-待复核
data132 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_ApplyInvoiceInfoMerge",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "settlement_center_ApplyInvoiceInfoMerge_purchaser_invoice_finance_check_to_check_waitting_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "applyInvoiceSerialNo"
			},
			{
				"fieldName": "sourceType"
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
							}
						]
					}
				]
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "corporateCompanyName"
			},
			{
				"fieldName": "sourceTypeMerge"
			},
			{
				"fieldName": "sourceCodeMerge"
			},
			{
				"fieldName": "salesCheckCodeMerge"
			},
			{
				"fieldName": "paymentTypeMerge"
			},
			{
				"fieldName": "payRateMerge"
			},
			{
				"fieldName": "paymentAmount"
			},
			{
				"fieldName": "noTaxAmount"
			},
			{
				"fieldName": "taxRate"
			},
			{
				"fieldName": "invoiceStatus"
			},
			{
				"fieldName": "invoiceType"
			},
			{
				"fieldName": "isMail"
			},
			{
				"fieldName": "waybillNo"
			},
			{
				"fieldName": "applyUser",
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
				"fieldName": "applyDate"
			},
			{
				"fieldName": "checkDate"
			},
			{
				"fieldName": "invoiceNum"
			},
			{
				"fieldName": "invoiceDate"
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
# 财务复核-复核完成
data133 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_ApplyInvoiceInfoMerge",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "settlement_center_ApplyInvoiceInfoMerge_purchaser_invoice_finance_check_to_check_success_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "applyInvoiceSerialNo"
			},
			{
				"fieldName": "sourceType"
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
							}
						]
					}
				]
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "corporateCompanyName"
			},
			{
				"fieldName": "sourceTypeMerge"
			},
			{
				"fieldName": "sourceCodeMerge"
			},
			{
				"fieldName": "salesCheckCodeMerge"
			},
			{
				"fieldName": "paymentTypeMerge"
			},
			{
				"fieldName": "payRateMerge"
			},
			{
				"fieldName": "paymentAmount"
			},
			{
				"fieldName": "noTaxAmount"
			},
			{
				"fieldName": "taxRate"
			},
			{
				"fieldName": "invoiceStatus"
			},
			{
				"fieldName": "invoiceType"
			},
			{
				"fieldName": "isMail"
			},
			{
				"fieldName": "waybillNo"
			},
			{
				"fieldName": "applyUser",
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
				"fieldName": "applyDate"
			},
			{
				"fieldName": "checkDate"
			},
			{
				"fieldName": "invoiceNum"
			},
			{
				"fieldName": "invoiceDate"
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
# 财务复核-已开票
data134 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_ApplyInvoiceInfoMerge",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "settlement_center_ApplyInvoiceInfoMerge_purchaser_invoice_finance_check_to_invoiced_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "applyInvoiceSerialNo"
			},
			{
				"fieldName": "sourceType"
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
							}
						]
					}
				]
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "corporateCompanyName"
			},
			{
				"fieldName": "sourceTypeMerge"
			},
			{
				"fieldName": "sourceCodeMerge"
			},
			{
				"fieldName": "salesCheckCodeMerge"
			},
			{
				"fieldName": "paymentTypeMerge"
			},
			{
				"fieldName": "payRateMerge"
			},
			{
				"fieldName": "paymentAmount"
			},
			{
				"fieldName": "noTaxAmount"
			},
			{
				"fieldName": "taxRate"
			},
			{
				"fieldName": "invoiceStatus"
			},
			{
				"fieldName": "invoiceType"
			},
			{
				"fieldName": "isMail"
			},
			{
				"fieldName": "waybillNo"
			},
			{
				"fieldName": "applyUser",
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
				"fieldName": "applyDate"
			},
			{
				"fieldName": "checkDate"
			},
			{
				"fieldName": "invoiceNum"
			},
			{
				"fieldName": "invoiceDate"
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
# 财务复核-已驳回
data135 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_ApplyInvoiceInfoMerge",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "settlement_center_ApplyInvoiceInfoMerge_purchaser_invoice_finance_check_to_rejected_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "applyInvoiceSerialNo"
			},
			{
				"fieldName": "sourceType"
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
							}
						]
					}
				]
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "corporateCompanyName"
			},
			{
				"fieldName": "sourceTypeMerge"
			},
			{
				"fieldName": "sourceCodeMerge"
			},
			{
				"fieldName": "salesCheckCodeMerge"
			},
			{
				"fieldName": "paymentTypeMerge"
			},
			{
				"fieldName": "payRateMerge"
			},
			{
				"fieldName": "paymentAmount"
			},
			{
				"fieldName": "noTaxAmount"
			},
			{
				"fieldName": "taxRate"
			},
			{
				"fieldName": "invoiceStatus"
			},
			{
				"fieldName": "invoiceType"
			},
			{
				"fieldName": "isMail"
			},
			{
				"fieldName": "waybillNo"
			},
			{
				"fieldName": "applyUser",
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
				"fieldName": "applyDate"
			},
			{
				"fieldName": "checkDate"
			},
			{
				"fieldName": "invoiceNum"
			},
			{
				"fieldName": "invoiceDate"
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
#收入确认单列表
data136 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_ReceiveConfirm",
	"sourceModel": "settlement_center_ReceiveConfirm",
	"dataSource": {
		"actionKey": "settlement_center_ReceiveConfirm_receive_confirm_list"
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
				"fieldName": "receiveType"
			},
			{
				"fieldName": "acceptanceCode"
			},
			{
				"fieldName": "corporateCompanyName"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "acceptanceAmount"
			},
			{
				"fieldName": "reversedAmount"
			},
			{
				"fieldName": "checkedAmount"
			},
			{
				"fieldName": "advanceAmount"
			},
			{
				"fieldName": "receivedAmount"
			},
			{
				"fieldName": "salesCheckDate"
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
#销售对账报表
data137 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_StatementPurchaserReportResponseVO",
	"sourceModel": "settlement_center_StatementPurchaserReportResponseVO",
	"dataSource": {
		"actionKey": "settlement_center_StatementPurchaserReportResponseVO_statement_supplier_sales_report_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "corporateCompanyName"
			},
			{
				"fieldName": "contractAmount"
			},
			{
				"fieldName": "salesName"
			},
			{
				"fieldName": "performanceName"
			},
			{
				"fieldName": "contractPaymentIterm"
			},
			{
				"fieldName": "advanceAmount"
			},
			{
				"fieldName": "acceptanceAmount"
			},
			{
				"fieldName": "acceptanceTotalAmount"
			},
			{
				"fieldName": "invoiceAmount"
			},
			{
				"fieldName": "payableAmount"
			},
			{
				"fieldName": "ensureAmount"
			},
			{
				"fieldName": "maintenanceAmount"
			},
			{
				"fieldName": "confirmContractAmount"
			},
			{
				"fieldName": "confirmCostAmount"
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
# 采购对账报表
data138 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_StatementPurchaserReportResponseVO",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "settlement_center_StatementPurchaserReportResponseVO_statement_purchaser_sales_report_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "corporateCompanyName"
			},
			{
				"fieldName": "contractAmount"
			},
			{
				"fieldName": "contractPaymentIterm"
			},
			{
				"fieldName": "advanceAmount"
			},
			{
				"fieldName": "acceptanceAmount"
			},
			{
				"fieldName": "acceptanceTotalAmount"
			},
			{
				"fieldName": "invoiceAmount"
			},
			{
				"fieldName": "payableAmount"
			},
			{
				"fieldName": "ensureAmount"
			},
			{
				"fieldName": "maintenanceAmount"
			},
			{
				"fieldName": "confirmContractAmount"
			},
			{
				"fieldName": "confirmCostAmount"
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
#应收账款账龄分析表 -按单据明细查询  url1
data139 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_ReceivableAccountsAnalysePO",
	"sourceModel": "master_data_server_ReceivableAccountsAnalysePO",
	"dataSource": {
		"actionKey": "master_data_server_ReceivableAccountsAnalysePO_receivable_accounts_analyse_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "receivableSourceType"
			},
			{
				"fieldName": "receivableSourceCode"
			},
			{
				"fieldName": "salesRequestReceiveCode"
			},
			{
				"fieldName": "salesCheckCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "paymentDesc"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "purchaseName"
			},
			{
				"fieldName": "areaNames"
			},
			{
				"fieldName": "performanceHeadStr"
			},
			{
				"fieldName": "salesHeadStr"
			},
			{
				"fieldName": "salesSupportStr"
			},
			{
				"fieldName": "startCalculateType"
			},
			{
				"fieldName": "startingDate"
			},
			{
				"fieldName": "paymentDayStr"
			},
			{
				"fieldName": "expire"
			},
			{
				"fieldName": "totalAmount"
			},
			{
				"fieldName": "allRelation"
			},
			{
				"fieldName": "surplusRelation"
			},
			{
				"fieldName": "neverMonthAbove"
			},
			{
				"fieldName": "neverMonth"
			},
			{
				"fieldName": "todayExpire"
			},
			{
				"fieldName": "overdueMonth"
			},
			{
				"fieldName": "overdueTwoMonth"
			},
			{
				"fieldName": "overdueThreeMonth"
			},
			{
				"fieldName": "overdueJuneMonth"
			},
			{
				"fieldName": "overdueDecemberMonth"
			},
			{
				"fieldName": "overdueDecemberMonthAbove"
			},
			{
				"fieldName": "riskLevel"
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
#应收账款账龄分析表 -按项目维度统计
data140 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_ReceivableAccountsAnalysePO",
	"sourceModel": "",
	"queryValues": {
		"groupByType": {
			"type": "One",
			"value": "project"
		}
	},
	"dataSource": {
		"actionKey": "master_data_server_ReceivableAccountsAnalysePO_receivable_accounts_analyse_group_by_project"
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
				"fieldName": "contractName"
			},
			{
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "paymentDesc"
			},
			{
				"fieldName": "purchaseName"
			},
			{
				"fieldName": "areaNames"
			},
			{
				"fieldName": "performanceHeadStr"
			},
			{
				"fieldName": "salesHeadStr"
			},
			{
				"fieldName": "salesSupportStr"
			},
			{
				"fieldName": "totalAmount"
			},
			{
				"fieldName": "allRelation"
			},
			{
				"fieldName": "surplusRelation"
			},
			{
				"fieldName": "neverMonthAbove"
			},
			{
				"fieldName": "neverMonth"
			},
			{
				"fieldName": "todayExpire"
			},
			{
				"fieldName": "overdueMonth"
			},
			{
				"fieldName": "overdueTwoMonth"
			},
			{
				"fieldName": "overdueThreeMonth"
			},
			{
				"fieldName": "overdueJuneMonth"
			},
			{
				"fieldName": "overdueDecemberMonth"
			},
			{
				"fieldName": "overdueDecemberMonthAbove"
			},
			{
				"fieldName": "riskLevel"
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
# 应收账款账龄分析表 -按合同维度统计
data141 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_ReceivableAccountsAnalysePO",
	"sourceModel": "",
	"queryValues": {
		"groupByType": {
			"type": "One",
			"value": "contract"
		}
	},
	"dataSource": {
		"actionKey": "master_data_server_ReceivableAccountsAnalysePO_receivable_accounts_analyse_group_by_contract"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "paymentDesc"
			},
			{
				"fieldName": "purchaseName"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "areaNames"
			},
			{
				"fieldName": "performanceHeadStr"
			},
			{
				"fieldName": "salesHeadStr"
			},
			{
				"fieldName": "salesSupportStr"
			},
			{
				"fieldName": "totalAmount"
			},
			{
				"fieldName": "allRelation"
			},
			{
				"fieldName": "surplusRelation"
			},
			{
				"fieldName": "neverMonthAbove"
			},
			{
				"fieldName": "neverMonth"
			},
			{
				"fieldName": "todayExpire"
			},
			{
				"fieldName": "overdueMonth"
			},
			{
				"fieldName": "overdueTwoMonth"
			},
			{
				"fieldName": "overdueThreeMonth"
			},
			{
				"fieldName": "overdueJuneMonth"
			},
			{
				"fieldName": "overdueDecemberMonth"
			},
			{
				"fieldName": "overdueDecemberMonthAbove"
			},
			{
				"fieldName": "riskLevel"
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
# 销售合同价外费用 url10
data142 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_ContractAdditionalCostPO",
	"sourceModel": "settlement_center_ContractAdditionalCostPO",
	"dataSource": {
		"actionKey": "settlement_center_ContractAdditionalCostPO_statement_sales_contract_additional_cost_list"
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
				"fieldName": "order",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "code"
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
						"fieldName": "orderRule"
					}
				]
			},
			{
				"fieldName": "baseAmount"
			},
			{
				"fieldName": "calculateTimeDesc"
			},
			{
				"fieldName": "calculateAccountPeriodTimeDesc"
			},
			{
				"fieldName": "interestRateDesc"
			},
			{
				"fieldName": "calculateFormula"
			},
			{
				"fieldName": "contractAdditionCostsAmount"
			},
			{
				"fieldName": "isChecked"
			},
			{
				"fieldName": "checkCode"
			},
			{
				"fieldName": "adjustAccountPeriodTimeDesc"
			},
			{
				"fieldName": "adjustAmount"
			},
			{
				"fieldName": "requestCode"
			},
			{
				"fieldName": "isPaid"
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
#采购合同价外费用
data143 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_ContractAdditionalCostPO",
	"sourceModel": "settlement_center_ContractAdditionalCostPO",
	"dataSource": {
		"actionKey": "settlement_center_ContractAdditionalCostPO_statement_purchaser_contract_additional_cost_list"
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
				"fieldName": "order",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "code"
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
						"fieldName": "supplier",
						"fields": [
							{
								"fieldName": "id"
							},
							{
								"fieldName": "name"
							}
						]
					}
				]
			},
			{
				"fieldName": "baseAmount"
			},
			{
				"fieldName": "calculateTimeDesc"
			},
			{
				"fieldName": "calculateAccountPeriodTimeDesc"
			},
			{
				"fieldName": "interestRateDesc"
			},
			{
				"fieldName": "calculateFormula"
			},
			{
				"fieldName": "contractAdditionCostsAmount"
			},
			{
				"fieldName": "isChecked"
			},
			{
				"fieldName": "checkCode"
			},
			{
				"fieldName": "adjustAccountPeriodTimeDesc"
			},
			{
				"fieldName": "adjustAmount"
			},
			{
				"fieldName": "requestCode"
			},
			{
				"fieldName": "isPaid"
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
#销售岗报表 --全部
data144 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_PenaltyInfoVO",
	"sourceModel": "settlement_center_PenaltyInfoVO",
	"dataSource": {
		"actionKey": "settlement_center_PenaltyInfoVO_statement_sales_penalty_report_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "invoiceNum"
			},
			{
				"fieldName": "invoiceTitle"
			},
			{
				"fieldName": "contractLableName"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "projectCompanyName"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "purchaserName"
			},
			{
				"fieldName": "salesCheckCode"
			},
			{
				"fieldName": "regionalDirector"
			},
			{
				"fieldName": "headOfSales"
			},
			{
				"fieldName": "salesSupport"
			},
			{
				"fieldName": "invoiceAmount"
			},
			{
				"fieldName": "invoiceDate"
			},
			{
				"fieldName": "betweenZeroAndThirty"
			},
			{
				"fieldName": "betweenThirtyAndSixty"
			},
			{
				"fieldName": "betweenSixtyAndNinety"
			},
			{
				"fieldName": "betweenNinetyAndGreatHundred"
			},
			{
				"fieldName": "betweenGreatHundredAndInfinity"
			},
			{
				"fieldName": "payAmountTotal"
			},
			{
				"fieldName": "noPayAmountTotal"
			},
			{
				"fieldName": "noPayAmountTotalBeOverdueDay"
			},
			{
				"fieldName": "thisMonthPenaltyAmount"
			},
			{
				"fieldName": "adjustReason"
			},
			{
				"fieldName": "adjustPenaltyAmount"
			},
			{
				"fieldName": "thisMonthAdjustPenaltyAmount"
			},
			{
				"fieldName": "penaltyAmountTotal"
			},
			{
				"fieldName": "commissionRate"
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
#销售岗报表 --本月应扣
data145 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_PenaltyInfoVO",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "settlement_center_PenaltyInfoVO_statement_sales_penalty_this_month_report_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "invoiceNum"
			},
			{
				"fieldName": "invoiceTitle"
			},
			{
				"fieldName": "contractLableName"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "projectCompanyName"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "purchaserName"
			},
			{
				"fieldName": "regionalDirector"
			},
			{
				"fieldName": "headOfSales"
			},
			{
				"fieldName": "salesSupport"
			},
			{
				"fieldName": "invoiceAmount"
			},
			{
				"fieldName": "invoiceDate"
			},
			{
				"fieldName": "betweenZeroAndThirty"
			},
			{
				"fieldName": "betweenThirtyAndSixty"
			},
			{
				"fieldName": "betweenSixtyAndNinety"
			},
			{
				"fieldName": "betweenNinetyAndGreatHundred"
			},
			{
				"fieldName": "betweenGreatHundredAndInfinity"
			},
			{
				"fieldName": "payAmountTotal"
			},
			{
				"fieldName": "noPayAmountTotal"
			},
			{
				"fieldName": "noPayAmountTotalBeOverdueDay"
			},
			{
				"fieldName": "thisMonthPenaltyAmount"
			},
			{
				"fieldName": "adjustReason"
			},
			{
				"fieldName": "adjustPenaltyAmount"
			},
			{
				"fieldName": "thisMonthAdjustPenaltyAmount"
			},
			{
				"fieldName": "penaltyAmountTotal"
			},
			{
				"fieldName": "commissionRate"
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
# 履约岗报表--全部
data146 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_SalesPerformanceReportVO",
	"sourceModel": "settlement_center_SalesPerformanceReportVO",
	"dataSource": {
		"actionKey": "settlement_center_SalesPerformanceReportVO_sales_performance_report_manager_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "acceptanceCode"
			},
			{
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "companyName"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "purchaserName"
			},
			{
				"fieldName": "performanceHead"
			},
			{
				"fieldName": "acceptanceDate"
			},
			{
				"fieldName": "acceptanceAmount"
			},
			{
				"fieldName": "checkShouldTime"
			},
			{
				"fieldName": "checkCode"
			},
			{
				"fieldName": "checkConfirmTime"
			},
			{
				"fieldName": "overdueDays"
			},
			{
				"fieldName": "deductionRatio"
			},
			{
				"fieldName": "deductibleAmount"
			},
			{
				"fieldName": "deductibleAmountMonth"
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
# 履约岗报表--本月应扣
data147 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_SalesPerformanceReportVO",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "settlement_center_SalesPerformanceReportVO_sales_performance_instant_report_manager_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "acceptanceCode"
			},
			{
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "companyName"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "purchaserName"
			},
			{
				"fieldName": "performanceHead"
			},
			{
				"fieldName": "acceptanceDate"
			},
			{
				"fieldName": "acceptanceAmount"
			},
			{
				"fieldName": "checkShouldTime"
			},
			{
				"fieldName": "checkCode"
			},
			{
				"fieldName": "checkConfirmTime"
			},
			{
				"fieldName": "overdueDays"
			},
			{
				"fieldName": "deductionRatio"
			},
			{
				"fieldName": "deductibleAmount"
			},
			{
				"fieldName": "deductibleAmountMonth"
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
# 票据岗报表--全部
data148 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_BillPostReportVO",
	"sourceModel": "settlement_center_BillPostReportVO",
	"dataSource": {
		"actionKey": "settlement_center_BillPostReportVO_bill_post_report"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "applyInvoiceSerialMergeNo"
			},
			{
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "companyName"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "purchaseName"
			},
			{
				"fieldName": "auditUserName"
			},
			{
				"fieldName": "noTaxAmount"
			},
			{
				"fieldName": "checkDate"
			},
			{
				"fieldName": "invoiceNum"
			},
			{
				"fieldName": "invoiceDate"
			},
			{
				"fieldName": "overdueDay"
			},
			{
				"fieldName": "deductionRatio"
			},
			{
				"fieldName": "deductibleAmount"
			},
			{
				"fieldName": "instantDeductibleAmount"
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
# 票据岗报表--本月应扣
data149 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_BillPostReportVO",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "settlement_center_BillPostReportVO_bill_post_to_instant_report"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "applyInvoiceSerialMergeNo"
			},
			{
				"fieldName": "contractLabel"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "companyName"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "purchaseName"
			},
			{
				"fieldName": "auditUserName"
			},
			{
				"fieldName": "noTaxAmount"
			},
			{
				"fieldName": "checkDate"
			},
			{
				"fieldName": "invoiceNum"
			},
			{
				"fieldName": "invoiceDate"
			},
			{
				"fieldName": "overdueDay"
			},
			{
				"fieldName": "deductionRatio"
			},
			{
				"fieldName": "deductibleAmount"
			},
			{
				"fieldName": "instantDeductibleAmount"
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
#合同初始化岗报表--全部
data150 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_ContractInitReportVO",
	"sourceModel": "settlement_center_ContractInitReportVO",
	"dataSource": {
		"actionKey": "settlement_center_ContractInitReportVO_contract_init_report"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "companyName"
			},
			{
				"fieldName": "salesSupportUserName"
			},
			{
				"fieldName": "projectCreatedDate"
			},
			{
				"fieldName": "firstEffectiveDate"
			},
			{
				"fieldName": "contractOverdueDay"
			},
			{
				"fieldName": "contractDeductibleAmount"
			},
			{
				"fieldName": "instantContractDeductibleAmount"
			},
			{
				"fieldName": "pushGatewayDate"
			},
			{
				"fieldName": "integrationOverdueDay"
			},
			{
				"fieldName": "integrationDeductibleAmount"
			},
			{
				"fieldName": "instantIntegrationDeductibleAmount"
			},
			{
				"fieldName": "deductibleAmountSum"
			},
			{
				"fieldName": "instantDeductibleAmountSum"
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
#合同初始化岗报表--本月应扣
data151 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_ContractInitReportVO",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "settlement_center_ContractInitReportVO_contract_init_to_instant_report"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "companyName"
			},
			{
				"fieldName": "salesSupportUserName"
			},
			{
				"fieldName": "projectCreatedDate"
			},
			{
				"fieldName": "firstEffectiveDate"
			},
			{
				"fieldName": "contractOverdueDay"
			},
			{
				"fieldName": "contractDeductibleAmount"
			},
			{
				"fieldName": "instantContractDeductibleAmount"
			},
			{
				"fieldName": "pushGatewayDate"
			},
			{
				"fieldName": "integrationOverdueDay"
			},
			{
				"fieldName": "integrationDeductibleAmount"
			},
			{
				"fieldName": "instantIntegrationDeductibleAmount"
			},
			{
				"fieldName": "deductibleAmountSum"
			},
			{
				"fieldName": "instantDeductibleAmountSum"
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
#岗位扣罚汇总表
data152 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_PostDeductionSummaryReportVO",
	"sourceModel": "settlement_center_PostDeductionSummaryReportVO",
	"searchValues": {
		"penaltyMonth": {
			"type": "One",
			"value": 1724227603575
		}
	},
	"dataSource": {
		"actionKey": "settlement_center_PostDeductionSummaryReportVO_post_deduction_summary_report"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "responsibilityUserName"
			},
			{
				"fieldName": "type"
			},
			{
				"fieldName": "thisMonthPenaltyAmount"
			},
			{
				"fieldName": "adjustPenaltyAmount"
			},
			{
				"fieldName": "thisMonthAdjustPenaltyAmount"
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
# 甲指台账 url1
data153 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_MDStandingBookVO",
	"sourceModel": "master_data_server_MDStandingBookVO",
	"dataSource": {
		"actionKey": "master_data_server_MDStandingBookVO_standing_book_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "tenderingUnitName"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "tenderingName"
			},
			{
				"fieldName": "contractCategory"
			},
			{
				"fieldName": "tenderingDueMoney"
			},
			{
				"fieldName": "step"
			},
			{
				"fieldName": "coopBusinessName"
			},
			{
				"fieldName": "coopBusinessSCC"
			},
			{
				"fieldName": "finialMoney"
			},
			{
				"fieldName": "isMaterialClassification"
			},
			{
				"fieldName": "goodsBrandName"
			},
			{
				"fieldName": "partyAType"
			},
			{
				"fieldName": "reason"
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
# 甲指台账统计
data154 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_MDStatisticsDataVO",
	"sourceModel": "master_data_server_MDStatisticsDataVO",
	"dataSource": {
		"actionKey": "master_data_server_MDStatisticsDataVO_standing_book_statistical_reports"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "tenderingUnitName"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "tenderingName"
			},
			{
				"fieldName": "contractCategory"
			},
			{
				"fieldName": "tenderingDueMoney"
			},
			{
				"fieldName": "step"
			},
			{
				"fieldName": "coopBusinessName"
			},
			{
				"fieldName": "coopBusinessScc"
			},
			{
				"fieldName": "finialMoney"
			},
			{
				"fieldName": "isMaterialClassification"
			},
			{
				"fieldName": "info"
			},
			{
				"fieldName": "partyAType"
			},
			{
				"fieldName": "reason"
			},
			{
				"fieldName": "lcProjectName"
			},
			{
				"fieldName": "category"
			},
			{
				"fieldName": "brand"
			},
			{
				"fieldName": "validMoney"
			},
			{
				"fieldName": "acceptanceAmount"
			},
			{
				"fieldName": "reverseAmount"
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
# 系统内置 -- 公司管理 url2
data155 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "base_Company",
	"sourceModel": "base_Company",
	"dataSource": {
		"actionKey": "base_Company_listAll"
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
				"fieldName": "shortName"
			},
			{
				"fieldName": "parent",
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
				"fieldName": "createdAt"
			},
			{
				"fieldName": "country"
			},
			{
				"fieldName": "status"
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
# 付款条件列表  url1
data156 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_MDPaymentIterm",
	"sourceModel": "master_data_server_MDPaymentIterm",
	"dataSource": {
		"actionKey": "master_data_server_MDPaymentIterm_to_payment_term_list"
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
				"fieldName": "describe"
			},
			{
				"fieldName": "radix"
			},
			{
				"fieldName": "type"
			},
			{
				"fieldName": "sort"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "updatedAt"
			}
		]
	},
	"paging": {
		"no": 1,
		"size": 10
	},
	"order": {
		"by": "sort",
		"isAsc": True
	}
}
# 开票品类
data157 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_admin_MDInvoiceCategoryVO",
	"sourceModel": "master_data_admin_MDInvoiceCategoryVO",
	"dataSource": {
		"actionKey": "master_data_admin_MDInvoiceCategoryVO_listAll"
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
				"fieldName": "shortName"
			},
			{
				"fieldName": "summaryFlag"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "updatedAt"
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
#价款调整额度
data158 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_ConfigurationParameters",
	"sourceModel": "settlement_center_ConfigurationParameters",
	"dataSource": {
		"actionKey": "settlement_center_ConfigurationParameters_price_adjust_limit_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "parameterCode"
			},
			{
				"fieldName": "parameterName"
			},
			{
				"fieldName": "parameterValue"
			},
			{
				"fieldName": "remark"
			},
			{
				"fieldName": "updatedAt"
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
#销售合同付款方案
data159 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_MDPaymentGroup",
	"sourceModel": "master_data_server_MDPaymentGroup",
	"dataSource": {
		"actionKey": "master_data_server_MDPaymentGroup_to_operate_sales_payment_group_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "name"
			},
			{
				"fieldName": "desc"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "updatedAt"
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
#采购合同付款方案
data160 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_MDPaymentGroup",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "master_data_server_MDPaymentGroup_to_operate_purchase_payment_group_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "name"
			},
			{
				"fieldName": "desc"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "updatedAt"
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
#登录配置
data161 = {
	"frontendContext": {},
	"singleResult": True,
	"targetModel": "partner_center_WechatBanner",
	"sourceModel": "partner_center_WechatBanner",
	"dataSource": {
		"actionKey": "partner_center_WechatBanner_wechat_banner_detail_view"
	},
	"result": {
		"fields": [
			{
				"fieldName": "bannerImage"
			},
			{
				"fieldName": "intervalTime"
			},
			{
				"fieldName": "id"
			}
		]
	}
}
# 状态释义
data162 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_StatusConfig",
	"sourceModel": "master_data_server_StatusConfig",
	"dataSource": {
		"actionKey": "master_data_server_StatusConfig_to_statusConfig_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "type"
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
#banner配置 url7
data163 ={
	"frontendContext": {},
	"singleResult": True,
	"targetModel": "itemcenter_server_MiniProgramBanner",
	"sourceModel": "itemcenter_server_MiniProgramBanner",
	"dataSource": {
		"actionKey": "itemcenter_server_MiniProgramBanner_mini_program_index_banner"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "interval"
			},
			{
				"fieldName": "bannerImgs",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "img"
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
# 电梯导航配置
data164 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "itemcenter_server_MiniProgramElevatorNavigation",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "itemcenter_server_MiniProgramElevatorNavigation_mini_program_elevator_navigation_list_view"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "menuName"
			},
			{
				"fieldName": "ShowStatus"
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
# 套餐配置
data165 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "itemcenter_server_MiniProgramSetMeal",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "itemcenter_server_MiniProgramSetMeal_mini_program_set_meal_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "name"
			},
			{
				"fieldName": "elevatorNavigation",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "menuName"
					}
				]
			},
			{
				"fieldName": "houseTypeName"
			},
			{
				"fieldName": "rulingPrice"
			},
			{
				"fieldName": "activityPrice"
			},
			{
				"fieldName": "sort"
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
#汇总表  url1
data166 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_SummaryReportPO",
	"sourceModel": "master_data_server_SummaryReportPO",
	"dataSource": {
		"actionKey": "master_data_server_SummaryReportPO_summary_report_manager_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "purchaserName"
			},
			{
				"fieldName": "purchaserCode"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "projectCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "performanceHeadStr"
			},
			{
				"fieldName": "salesHeadStr"
			},
			{
				"fieldName": "address"
			},
			{
				"fieldName": "contractLabelName"
			},
			{
				"fieldName": "orderCode"
			},
			{
				"fieldName": "orderStatus"
			},
			{
				"fieldName": "effectiveAmount"
			},
			{
				"fieldName": "effectiveGetGoodsAmount"
			},
			{
				"fieldName": "effectiveDeliveryAmount"
			},
			{
				"fieldName": "acceptanceAmount"
			},
			{
				"fieldName": "installAmount"
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
				"fieldName": "invoiceIssuedAmount"
			},
			{
				"fieldName": "receivedTotal"
			},
			{
				"fieldName": "orderDate"
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
#需求单报表
data167 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_OrderReportPO",
	"sourceModel": "master_data_server_OrderReportPO",
	"dataSource": {
		"actionKey": "master_data_server_OrderReportPO_order_report_manager_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "purchaserName"
			},
			{
				"fieldName": "purchaserCode"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "projectCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "orderCode"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "totalAmount"
			},
			{
				"fieldName": "effectiveAmount"
			},
			{
				"fieldName": "abortedAmount"
			},
			{
				"fieldName": "closedAmount"
			},
			{
				"fieldName": "orderDate"
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
#订单报表
data168 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_GetGoodsOrderReportPO",
	"sourceModel": "master_data_server_GetGoodsOrderReportPO",
	"dataSource": {
		"actionKey": "master_data_server_GetGoodsOrderReportPO_getGoodsOrder_report_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "purchaserName"
			},
			{
				"fieldName": "purchaserCode"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "projectCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "orderCode"
			},
			{
				"fieldName": "code"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "getGoodsAmount"
			},
			{
				"fieldName": "effectiveGetGoodsAmount"
			},
			{
				"fieldName": "abortedGetGoodsAmount"
			},
			{
				"fieldName": "closedGetGoodsAmount"
			},
			{
				"fieldName": "orderSubmission"
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
#发货单报表
data169 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_DeliveryOrderPOReportPO",
	"sourceModel": "master_data_server_DeliveryOrderPOReportPO",
	"dataSource": {
		"actionKey": "master_data_server_DeliveryOrderPOReportPO_deliveryOrder_report_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "createdAt"
			},
			{
				"fieldName": "purchaserName"
			},
			{
				"fieldName": "purchaserCode"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "projectCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "orderCode"
			},
			{
				"fieldName": "code"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "deliveryAmount"
			},
			{
				"fieldName": "effectiveDeliveryAmount"
			},
			{
				"fieldName": "abortedDeliveryAmount"
			},
			{
				"fieldName": "unacceptedDeliveryAmount"
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
# 退货单报表
data170 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_ReverseReportPO",
	"sourceModel": "master_data_server_ReverseReportPO",
	"dataSource": {
		"actionKey": "master_data_server_ReverseReportPO_reverse_report_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "purchaserName"
			},
			{
				"fieldName": "purchaserCode"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "projectCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "orderCode"
			},
			{
				"fieldName": "code"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "reverseAmount"
			},
			{
				"fieldName": "confirmReverseAmount"
			},
			{
				"fieldName": "waitingReverseAmount"
			},
			{
				"fieldName": "rejectReverseAmount"
			},
			{
				"fieldName": "reverseDate"
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
#到货验收单报表
data171 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_ArrivalAcceptanceReportPO",
	"sourceModel": "master_data_server_ArrivalAcceptanceReportPO",
	"dataSource": {
		"actionKey": "master_data_server_ArrivalAcceptanceReportPO_arrivalAcceptance_report_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "purchaserName"
			},
			{
				"fieldName": "purchaserCode"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "projectCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "orderCode"
			},
			{
				"fieldName": "code"
			},
			{
				"fieldName": "acceptanceAmount"
			},
			{
				"fieldName": "acceptanceDate"
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
#安装验收单报表
data172 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_InstallAcceptanceReportPO",
	"sourceModel": "master_data_server_InstallAcceptanceReportPO",
	"dataSource": {
		"actionKey": "master_data_server_InstallAcceptanceReportPO_installAcceptance_report_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "purchaserName"
			},
			{
				"fieldName": "purchaserCode"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "projectCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "orderCode"
			},
			{
				"fieldName": "installCode"
			},
			{
				"fieldName": "acceptanceAmount"
			},
			{
				"fieldName": "installAcceptanceDate"
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
# 应收单报表
data173 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_ReceivableReportPO",
	"sourceModel": "master_data_server_ReceivableReportPO",
	"dataSource": {
		"actionKey": "master_data_server_ReceivableReportPO_receivable_report_manager_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "purchaserName"
			},
			{
				"fieldName": "purchaserCode"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "projectCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "orderCode"
			},
			{
				"fieldName": "receivableSourceCode"
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
		"size": 10
	},
	"order": {
		"by": "updatedAt",
		"isAsc": False
	}
}
# 对账单报表
data174 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_SalesCheckReportPO",
	"sourceModel": "master_data_server_SalesCheckReportPO",
	"dataSource": {
		"actionKey": "master_data_server_SalesCheckReportPO_sales_check_report_manager_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "purchaserName"
			},
			{
				"fieldName": "purchaserCode"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "projectCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "orderCode"
			},
			{
				"fieldName": "code"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "totalAmount"
			},
			{
				"fieldName": "confirmAmount"
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
#收款单报表
data175 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_server_SalesRequestReceiveReportPO",
	"sourceModel": "master_data_server_SalesRequestReceiveReportPO",
	"dataSource": {
		"actionKey": "master_data_server_SalesRequestReceiveReportPO_sales_request_receive_report_manager_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "purchaserName"
			},
			{
				"fieldName": "purchaserCode"
			},
			{
				"fieldName": "projectName"
			},
			{
				"fieldName": "projectCode"
			},
			{
				"fieldName": "contractName"
			},
			{
				"fieldName": "contractCode"
			},
			{
				"fieldName": "orderCode"
			},
			{
				"fieldName": "code"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "salesReceiveTotal"
			},
			{
				"fieldName": "receivedTotal"
			},
			{
				"fieldName": "waitTotal"
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
# 销售毛利报表-按合同标签汇总 url10
data176 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_SalesGrossProfitReportVO",
	"sourceModel": "settlement_center_SalesGrossProfitReportVO",
	"dataSource": {
		"actionKey": "settlement_center_SalesGrossProfitReportVO_sales_gross_profit_to_contract_lable_report"
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
				"fieldName": "totalSalesPrice"
			},
			{
				"fieldName": "totalCost"
			},
			{
				"fieldName": "grossMargin"
			},
			{
				"fieldName": "salesProportion"
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
# 销售毛利报表-按品牌汇总
data177 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_SalesGrossProfitReportVO",
	"sourceModel": "settlement_center_SalesGrossProfitReportVO",
	"dataSource": {
		"actionKey": "settlement_center_SalesGrossProfitReportVO_sales_gross_profit_to_brand_report"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "brandName"
			},
			{
				"fieldName": "totalSalesPrice"
			},
			{
				"fieldName": "totalCost"
			},
			{
				"fieldName": "grossMargin"
			},
			{
				"fieldName": "markupRate"
			},
			{
				"fieldName": "salesProportion"
			},
			{
				"fieldName": "exteriorTotalSalesPrice"
			},
			{
				"fieldName": "exteriorTotalCost"
			},
			{
				"fieldName": "exteriorGrossMargin"
			},
			{
				"fieldName": "exteriorMarkupRate"
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
data178 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_BrandAvgMarkupRateVO",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "settlement_center_BrandAvgMarkupRateVO_brand_avg_markup_rate_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "brandName"
			},
			{
				"fieldName": "avgMarkupRate202406"
			},
			{
				"fieldName": "avgMarkupRate202312"
			},
			{
				"fieldName": "avgMarkupRate202306"
			},
			{
				"fieldName": "avgMarkupRate202212"
			},
			{
				"fieldName": "avgMarkupRate202206"
			},
			{
				"fieldName": "avgMarkupRate202112"
			},
			{
				"fieldName": "avgMarkupRate202106"
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
data179 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_SalesGrossProfitReportVO",
	"sourceModel": "",
	"dataSource": {
		"actionKey": "settlement_center_SalesGrossProfitReportVO_sales_gross_profit_standard_to_brand_report"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "brandName"
			},
			{
				"fieldName": "totalSalesPrice"
			},
			{
				"fieldName": "totalCost"
			},
			{
				"fieldName": "grossMargin"
			},
			{
				"fieldName": "markupRate"
			},
			{
				"fieldName": "salesProportion"
			},
			{
				"fieldName": "exteriorTotalSalesPrice"
			},
			{
				"fieldName": "exteriorTotalCost"
			},
			{
				"fieldName": "exteriorGrossMargin"
			},
			{
				"fieldName": "exteriorMarkupRate"
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
data180 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_BrandAvgMarkupRateVO",
	"sourceModel": "",
	"queryValues": {
		"modelKey": {
			"type": "One",
			"value": "settlement_center_BrandAvgMarkupRateVO"
		},
		"record": {
			"type": "One",
			"value": {
				"isAggregate": "TRUE"
			}
		}
	},
	"dataSource": {
		"actionKey": "settlement_center_BrandAvgMarkupRateVO_brand_avg_markup_standard_rate_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "brandName"
			},
			{
				"fieldName": "avgMarkupRate202406"
			},
			{
				"fieldName": "avgMarkupRate202312"
			},
			{
				"fieldName": "avgMarkupRate202306"
			},
			{
				"fieldName": "avgMarkupRate202212"
			},
			{
				"fieldName": "avgMarkupRate202206"
			},
			{
				"fieldName": "avgMarkupRate202112"
			},
			{
				"fieldName": "avgMarkupRate202106"
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
# 销售毛利报表-按品类汇总
data181 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_SalesGrossProfitReportVO",
	"sourceModel": "settlement_center_SalesGrossProfitReportVO",
	"dataSource": {
		"actionKey": "settlement_center_SalesGrossProfitReportVO_sales_gross_profit_to_category_report"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "categoryName"
			},
			{
				"fieldName": "totalSalesPrice"
			},
			{
				"fieldName": "totalCost"
			},
			{
				"fieldName": "grossMargin"
			},
			{
				"fieldName": "markupRate"
			},
			{
				"fieldName": "salesProportion"
			},
			{
				"fieldName": "exteriorTotalSalesPrice"
			},
			{
				"fieldName": "exteriorTotalCost"
			},
			{
				"fieldName": "exteriorGrossMargin"
			},
			{
				"fieldName": "exteriorMarkupRate"
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
# 提成数据汇总表
data182 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_SalesCommissionSummaryReportPO",
	"sourceModel": "settlement_center_SalesCommissionSummaryReportPO",
	"dataSource": {
		"actionKey": "settlement_center_SalesCommissionSummaryReportPO_to_sales_commission_summary_report_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "salesContractCodes"
			},
			{
				"fieldName": "offLineContractCode"
			},
			{
				"fieldName": "offLineContractName"
			},
			{
				"fieldName": "contractType"
			},
			{
				"fieldName": "customerName"
			},
			{
				"fieldName": "customerType"
			},
			{
				"fieldName": "region"
			},
			{
				"fieldName": "salesNames"
			},
			{
				"fieldName": "quotationNames"
			},
			{
				"fieldName": "performanceNames"
			},
			{
				"fieldName": "contractAmount"
			},
			{
				"fieldName": "salesMission"
			},
			{
				"fieldName": "performanceReportingDate"
			},
			{
				"fieldName": "signingDate"
			},
			{
				"fieldName": "archiveStatus"
			},
			{
				"fieldName": "archiveDate"
			},
			{
				"fieldName": "orderEffectiveAmount"
			},
			{
				"fieldName": "orderReturnAmount"
			},
			{
				"fieldName": "contractOverdue"
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
#提成数据明细表
data183 ={
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_SalesCommissionDetailReportPO",
	"sourceModel": "settlement_center_SalesCommissionDetailReportPO",
	"dataSource": {
		"actionKey": "settlement_center_SalesCommissionDetailReportPO_to_sales_commission_detail_report_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "getGoodsCode"
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
				"fieldName": "summaryReport",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "offLineContractCode"
					},
					{
						"fieldName": "performanceReportingDate"
					},
					{
						"fieldName": "customerType"
					},
					{
						"fieldName": "salesNames"
					},
					{
						"fieldName": "quotationNames"
					},
					{
						"fieldName": "performanceNames"
					}
				]
			},
			{
				"fieldName": "salesContract",
				"fields": [
					{
						"fieldName": "id"
					},
					{
						"fieldName": "name"
					},
					{
						"fieldName": "code"
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
				"fieldName": "status"
			},
			{
				"fieldName": "getGoodsAmount"
			},
			{
				"fieldName": "effectiveAmount"
			},
			{
				"fieldName": "confirmDate"
			},
			{
				"fieldName": "orderReturnAmount"
			},
			{
				"fieldName": "nowOrderReturnAmount"
			},
			{
				"fieldName": "brandMarkupRate"
			},
			{
				"fieldName": "markupPercentage"
			},
			{
				"fieldName": "incomeRate"
			}
		]
	},
	"paging": {
		"no": 1,
		"size": 10
	},
	"order": {
		"by": "confirmDate",
		"isAsc": False
	}
}
#标准加价率统计表
data184 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "settlement_center_StandardMarkupPercentageStatistics",
	"sourceModel": "settlement_center_StandardMarkupPercentageStatistics",
	"dataSource": {
		"actionKey": "settlement_center_StandardMarkupPercentageStatistics_to_standard_markup_percentage_statistics_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
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
				"fieldName": "markupPercentage202401"
			},
			{
				"fieldName": "markupPercentage2023"
			},
			{
				"fieldName": "formulaStr"
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
# 服务商名册管理 url1
data185 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "master_data_admin_MDServiceProviderVO",
	"sourceModel": "master_data_admin_MDServiceProviderVO",
	"dataSource": {
		"actionKey": "master_data_admin_MDServiceProviderVO_service-providers-list"
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
				"fieldName": "unifiedSocialCreditCode"
			},
			{
				"fieldName": "contactId"
			},
			{
				"fieldName": "contactName"
			},
			{
				"fieldName": "contactPhone"
			},
			{
				"fieldName": "travellingTraderStatus"
			},
			{
				"fieldName": "travellingTraderBankStatus"
			},
			{
				"fieldName": "createdAt"
			},
			{
				"fieldName": "updatedAt"
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
#佣金方案管理 url8
data186 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "contract_center_admin_CommissionManageVO",
	"sourceModel": "contract_center_admin_CommissionManageVO",
	"dataSource": {
		"actionKey": "contract_center_admin_CommissionManageVO_commission_manage_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "applicationScenarios"
			},
			{
				"fieldName": "schemeName"
			},
			{
				"fieldName": "status"
			},
			{
				"fieldName": "effectiveStartDate"
			},
			{
				"fieldName": "effectiveEndDate"
			},
			{
				"fieldName": "grantNotes"
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
# 佣金明细
data187 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "contract_domain_CommissionDetails",
	"sourceModel": "contract_domain_CommissionDetails",
	"dataSource": {
		"actionKey": "contract_domain_CommissionDetails_commission_details_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "detailsNo"
			},
			{
				"fieldName": "partnerIdentity"
			},
			{
				"fieldName": "partnerLevel"
			},
			{
				"fieldName": "partner"
			},
			{
				"fieldName": "orgName"
			},
			{
				"fieldName": "dealCategory"
			},
			{
				"fieldName": "contractNo"
			},
			{
				"fieldName": "region"
			},
			{
				"fieldName": "salesHead"
			},
			{
				"fieldName": "recommendProject"
			},
			{
				"fieldName": "commissionAmount"
			},
			{
				"fieldName": "commissionAmountTax"
			},
			{
				"fieldName": "referenceAmount"
			},
			{
				"fieldName": "rate"
			},
			{
				"fieldName": "createdAt"
			},
			{
				"fieldName": "commissionType"
			},
			{
				"fieldName": "oaApproveStatus"
			},
			{
				"fieldName": "unionPayWallet"
			},
			{
				"fieldName": "enterpriseSign"
			},
			{
				"fieldName": "remark"
			},
			{
				"fieldName": "beforeAdjustCommission"
			},
			{
				"fieldName": "adjustReason"
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
# 提成明细
data188 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "contract_domain_SalesIncentiveDetails",
	"sourceModel": "contract_domain_SalesIncentiveDetails",
	"dataSource": {
		"actionKey": "contract_domain_SalesIncentiveDetails_incentive_details_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "detailsNo"
			},
			{
				"fieldName": "incentiveDate"
			},
			{
				"fieldName": "region"
			},
			{
				"fieldName": "staff",
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
				"fieldName": "incentiveRole"
			},
			{
				"fieldName": "contractInfo",
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
						"fieldName": "corporateCompanyName"
					}
				]
			},
			{
				"fieldName": "collectionAmount"
			},
			{
				"fieldName": "incentiveAmount"
			},
			{
				"fieldName": "oaApproveStatus"
			},
			{
				"fieldName": "beforeAdjustAmount"
			},
			{
				"fieldName": "adjustReason"
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
# 佣金汇总
data189 = {
	"frontendContext": {},
	"singleResult": False,
	"targetModel": "contract_domain_CommissionSummaryVO",
	"sourceModel": "contract_domain_CommissionSummaryVO",
	"dataSource": {
		"actionKey": "contract_domain_CommissionSummaryVO_commission_summary_list"
	},
	"result": {
		"fields": [
			{
				"fieldName": "id"
			},
			{
				"fieldName": "contractNo"
			},
			{
				"fieldName": "contract"
			},
			{
				"fieldName": "recommendCustom"
			},
			{
				"fieldName": "partner"
			},
			{
				"fieldName": "orgName"
			},
			{
				"fieldName": "partnerIdentity"
			},
			{
				"fieldName": "partnerLevel"
			},
			{
				"fieldName": "dealCategory"
			},
			{
				"fieldName": "region"
			},
			{
				"fieldName": "salesHead"
			},
			{
				"fieldName": "signDate"
			},
			{
				"fieldName": "contractTotalAmount"
			},
			{
				"fieldName": "totalReturnAmount"
			},
			{
				"fieldName": "payableCommissionAmount"
			},
			{
				"fieldName": "issuedCommissionAmount"
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











































