import json
import zidonghua.Common.Requests
import zidonghua.Common.Cookies
import zidonghua.Conf.Settings
import zidonghua.Common.Mysql_Con
import random
import zidonghua.Interface.Register

# zidonghua.Conf.Settings.url =zidonghua.Conf.Settings.dev_url
# zidonghua.Common.Mysql_Con.data = zidonghua.Conf.Read_yaml.read_yaml_all('config.yaml')['dev']

def Residency(mobile,unifiedSocialCreditCode):
	random_int_str = ''.join(str(random.randint(0, 9)) for _ in range(18))
	random_int = int(random_int_str)
	sql = "SELECT *  FROM uc_user WHERE mobile = '{}';".format(mobile)
	users = zidonghua.Common.Mysql_Con.sql_select(sql)[0]
	cookies = zidonghua.Common.Cookies.get_cookies(mobile)
	zidonghua.Interface.Register.params1['unifiedSocialCreditCode']=unifiedSocialCreditCode
	response1 = zidonghua.Common.Requests.HttpUtil(
		url=zidonghua.Conf.Settings.url+zidonghua.Interface.Register.api2,
		params=zidonghua.Interface.Register.params1, cookies=cookies).get()
	result = response1['result']
	data2 = zidonghua.Interface.Register.data2
	data2['enterprisesType']="S"  #供应商S 采购P 经销商D
	if data2['enterprisesType'] == "D" or data2['enterprisesType'] == "S":
		data2['partnerIdentify']['unifiedSocialCreditCode'] = unifiedSocialCreditCode
		data2['partnerIdentify']['name'] = result['name']
		data2['partnerIdentify']['legalRepresentativeName'] = result['legalRepresentativeName']
		data2['partnerIdentify']['registrationInformation'] = result['registrationInformation']
		data2['partnerIdentify']['phone'] = result['phone']
		data2['partnerIdentify']['contactName'] = users['nickname']
		data2['partnerIdentify']['contactEmail'] = users['email']
		data2['partnerIdentify']['contactPhone'] = users['mobile']
		data2['partnerIdentify']['contactAddress']=result['registrationInformation']
		data2['partnerIdentify']['bankType']='建行深圳前海支行'
		data2['partnerIdentify']['bankName'] =result['legalRepresentativeName']
		data2['partnerIdentify']['cardNo'] = random_int
		data2['partnerIdentify']['graphicSeal'] ={
                    "files": [
                        {
                            "name": "1.png",
                            "url": "//lcscm-trantor-test.oss-cn-shenzhen.aliyuncs.com/images/2efaf1d6-dc1f-4ff0-ab96-bc0243e4ce38.png",
                            "type": None
                        }
                    ]
                }
	else:
		data2['partnerIdentify']['unifiedSocialCreditCode'] = unifiedSocialCreditCode
		data2['partnerIdentify']['name'] = result['name']
		data2['partnerIdentify']['legalRepresentativeName'] = result['legalRepresentativeName']
		data2['partnerIdentify']['registrationInformation'] = result['registrationInformation']
		data2['partnerIdentify']['phone'] = result['phone']
		data2['partnerIdentify']['contactName'] = users['nickname']
		data2['partnerIdentify']['contactEmail'] = users['email']
		data2['partnerIdentify']['contactPhone'] = users['mobile']
	response2 = zidonghua.Common.Requests.HttpUtil(
		url= zidonghua.Conf.Settings.url+zidonghua.Interface.Register.api1,
		json= data2, cookies=cookies).post()
	return response2.json()


def ship_residency():
	cookies = zidonghua.Common.Cookies.get_cookies('18520611771')
	response3 = zidonghua.Common.Requests.HttpUtil(
		url=zidonghua.Conf.Settings.uat_url1 + zidonghua.Interface.Register.api3,
		json=data3, cookies=cookies).post()
	return response3.json()

if __name__ == '__main__':
	print(Residency('13500000003','913100007416482930'))
