import json
import zidonghua.Common.Requests
import zidonghua.Common.Cookies

url ='https://b2b-mall-uat.test.lcscm.cn/api/partner/b2b/all/businesses/create'
data = {
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
def Residency(mobile):
	cookies = zidonghua.Common.Cookies.get_cookies(mobile)
	response1 = zidonghua.Common.Requests.HttpUtil(
		url=url,
		json=data, cookies=cookies).post()
	return response1.json()

if __name__ == '__main__':
	print(Residency('13500000002'))