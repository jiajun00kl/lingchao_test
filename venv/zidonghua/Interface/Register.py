api = '/api/user/web/sign-up/new/register-by-sms-code'
data = {
  'nickname': '',
  'mobile': '',
  'email':'',
  'captcha_img': '1111',
  'smsCode': '111111',
  'password': 'a1234567',
  'confirm': 'a1234567',
  'agree': True,
  'prefix': '86',
  'channelType': 'out_user'
}


api1 ='/api/partner/b2b/all/businesses/create'
api2 ="/api/partner/b2b/sky-eye-check/info?"
params1 ={"unifiedSocialCreditCode":"914201036791099094"}
data2 = {
	"id": "",
	"enterprisesType": "P",
	"partnerIdentify": {
		"unifiedSocialCreditCode": "911101157906543745",
		"name": "北京泰和佳科技股份有限公司",
		"legalRepresentativeName": "袁潇",
		"registrationInformation": "北京市大兴区黄村镇海鑫北路9号7栋1层",
		"phone": "010-57795066",
		"contactName": "自动化创建test13505",
		"contactEmail": "13500000005@qq.com",
		"contactPhone": "13500000005",
		"businessLicense": {
			"files": [
				{
					"name": "1dc541c7dbad43bca21de57aa323b60b_2016385579.png",
					"url": "//lcscm-trantor-test.oss-cn-shenzhen.aliyuncs.com/images/9e7d9cc6-0d3f-4f20-b732-ba2f015a903d.png",
					"uid": "origin-1712108157513-2"
				}
			]
		},
		"businessBeginAt": None,
		"businessEndAt": None,
		"foundAt": None,
		"creditReportDate": None,
		"registrationTaxAccess": {
			"files": []
		},
		"architectureDiagram": {
			"files": []
		},
		"creditReport": {
			"files": []
		},
		"financialStatements": {
			"files": []
		},
		"qualificationCertificate": {
			"files": []
		},
		"certificateRepresentative": {
			"files": []
		},
		"powerAttorney": {
			"files": []
		},
		"electronicSignatureAttorney": {
			"files": []
		},
		"graphicSeal": {
			"files": []
		},
		"certificationAtt": {
			"files": []
		},
		"mdCooperationProjectsParams": []
	},
	"auditStatus": "TO_AUDIT"
}

api3 =("/zhonghai/master-data/master-data-admin/1005691/api/trantor/action/exe")

data3={
    "frontendContext": {},
    "actionKey": "master_data_server_MDEnterprise_MDEnterpriseAction::approvedPass",
    "context": {
        "modelKey": "master_data_server_MDEnterprise",
        "actionLabel": "审核通过",
        "record": [
            {
                "isMonopolyUnit": False,
                "idRelationUnit": False,
                "priceValidityBeginAt": None,
                "priceValidityEndAt": None,
                "auditComments": "通过",
                "id": 252026,
                "b2bPartner": {
                    "id": 238026,
                    "roleType": "S"
                },
                "name": "山东泽龙机电设备有限公司"
            }
        ]
    }
}










