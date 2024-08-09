import zidonghua.Interface.Create_Contract
import zidonghua.Conf.Settings
import zidonghua.Common.Cookies
import zidonghua.Common.Requests
import zidonghua.Common.Mysql_Con
import random,json
import zidonghua.Conf.Settings
import zidonghua.Conf.Datetime

''' 
contractLabel ={'外部客户-TOP100地产':'Outside Customer_top 100','3311中建国际':'Contract Label_3311',
'物业常规业务':'PROPERTY_CONVENTION','外部客户-施工单位':'construction unit','零星':'sporadic',
'中建工程局-EPC业务':'Contract Label_CSCEC_EPC','外部客户-中小型地产客户':'Outside Customer_small',
'0688中海地产-甲指乙供类':'0688','中建工程局-地产业务':'CSCEC_real estate','0688中海地产':'bu_we',
                '精装加载业务':'HARDCOVER_LOADING'}
'''  # 合同标签
import json


def remove_key_recursively(obj, key):
    """
    递归地删除JSON对象（可能是字典或列表）中所有层级的指定键。

    :param obj: JSON对象，可以是字典或列表
    :param key: 要删除的键名
    :return: 修改后的JSON对象
    """
    if isinstance(obj, dict):
        # 如果是字典，则遍历并删除指定键
        for k in list(obj.keys()):
            if k == key:
                del obj[k]
            else:
                remove_key_recursively(obj[k], key)
    elif isinstance(obj, list):
        # 如果是列表，则遍历列表中的每个元素
        for item in obj:
            remove_key_recursively(item, key)
            # 如果obj不是字典或列表，则不需要处理

def select_corporatecompany(companyName):  #获取项目公司
    cookies =zidonghua.Common.Cookies.login_cookies('18520611771')
    response1 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Conf.Settings.url1 + zidonghua.Interface.Create_Contract.api['api1'],
        json=zidonghua.Interface.Create_Contract.data, cookies=cookies).post()
    try:
        response1.raise_for_status()
        res_data = response1.json()
        res_value = res_data.get('res', {})  # 假设res是一个字典或我们将其视为空字典
        data_value = res_value.get('data', '')
        for corporatecompany in data_value:
            if corporatecompany['companyName'] ==companyName:
                return corporatecompany
        return  ("没有查询到名字为:'{}'的项目公司").format(companyName)
    except Exception as e:
        # 处理错误，例如打印错误信息或返回默认值
        return  (f"An error occurred: {e}")

def select_project(companyName,projectname):
    corporatecompany = select_corporatecompany(companyName)
    corp_companyid =corporatecompany['id']
    cookies = zidonghua.Common.Cookies.login_cookies('18520611771')
    sql = "SELECT * FROM partner_center_project  WHERE corporate_company ='{}'".format(corp_companyid)
    projects = zidonghua.Common.Mysql_Con.sql_select(sql)
    for project in projects:
        if project['name']==projectname:
             projectid = project['id']
    data2 = zidonghua.Interface.Create_Contract.data2
    data2['context']['env']= {'projectId': projectid}
    data2['context']['record']={'projectId': projectid}
    response1 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Conf.Settings.url1 + zidonghua.Interface.Create_Contract.api['api2'],
        json=zidonghua.Interface.Create_Contract.data2, cookies=cookies).post()
    try:
        response1.raise_for_status()
        res_data = response1.json()
        res_value = res_data.get('res', {})
        data_value = res_value.get('data', '')
        return data_value
    except Exception as e:
        # 处理错误，例如打印错误信息或返回默认值
        return (f"An error occurred: {e}")

def haha(companyName,projectname):
    data = select_project(companyName, projectname)
    remove_key_recursively(data, "__trantorExtendFields")
    return (data)



def creat_contract(companyName,projectname,startDateType=0):
    corp_company = select_corporatecompany(companyName)
    project = haha(companyName,projectname)
    cookies = zidonghua.Common.Cookies.login_cookies('18520611771')
    random_int_str = ''.join(str(random.randint(0, 9)) for _ in range(10))
    startdate, enddate = zidonghua.Conf.Datetime.time_13()
    data1 = zidonghua.Interface.Create_Contract.data1
    # data1['actionKey']='contract_domain_Contract_ContractAction::editAndSubmitSaleContract' #编辑提交合同
    data1['actionKey'] = 'contract_domain_Contract_ContractAction::createAndSubmitSaleContract'  # 新增提交合同
    record= data1['context']['record'][0]
    sql ="select MAX(id) id from contract_center_contract "
    max_id = zidonghua.Common.Mysql_Con.sql_select(sql)[0]['id']
    sql1 = "select MAX(id) id from contract_center_contract_expand "
    max_id1 = zidonghua.Common.Mysql_Con.sql_select(sql1)[0]['id']
    sql2 = "select MAX(id) id from quotation_list "
    max_id2 = zidonghua.Common.Mysql_Con.sql_select(sql2)[0]['id']
    record['id']= max_id+1
    record['projectCode']=project['code']
    record['code'] = 'HTSH'+ random_int_str
    record['name'] = record['code']+'合同'
    record['corporateCompany']= corp_company
    record['project'] = project
    record['contractExpand']['id'] = max_id1+1
    if startDateType == 1:
        record['contractExpand']['startDateType'] ='SIGNED_START'   # 合同开始日期,签约之日起
    else:
        record['contractExpand']['startDateType'] = 'FIXED_DATE'  # 合同开始日期 固定日期
        record['startDate'] = startdate
    invoiceInfo ={}
    invoiceInfo['id']= record['id']
    invoiceInfo['invoiceCompany'] = corp_company['invoiceInfo']['invoiceCompany']
    invoiceInfo['taxpayerCode'] = corp_company['invoiceInfo']['taxpayerCode']
    invoiceInfo['invoiceAddress'] = corp_company['invoiceInfo']['invoiceAddress']
    invoiceInfo['invoiceMobile'] = corp_company['invoiceInfo']['invoiceMobile']
    invoiceInfo['invoiceType'] = corp_company['invoiceInfo']['invoiceType']
    invoiceInfo['invoiceBank'] = corp_company['invoiceInfo']['invoiceBank']
    invoiceInfo['invoiceAccount'] = corp_company['invoiceInfo']['invoiceAccount']
    record['contractExpand']['invoiceInfo'] = invoiceInfo
    record['contractExpand']['invoiceRemark'] = project['invoiceRemark']
    record['endDate']=enddate
    record['signDate'] = startdate  # 签约日期
    record['contractType'] = 'SALE_CONTRACT'
    record['type'] = 'SALE_CONTRACT'
    record['contractTypeAttribute'] = 'COMMODITY_SALES'
    record['contractTotalAmount'] = 333333
    record['contractTaxRateSale']  = 9
    record['contractAmountExcludingTax']= round(record['contractTotalAmount']/(1 + record['contractTaxRateSale']/100),2)
    record['contractTax']= round(record['contractTotalAmount']-record['contractAmountExcludingTax'],2)
    record['contractLabel'] = "Outside Customer_small" # 合同标签
    record['askPriceId'] = None  # 询价单ID
    record['isframeworkAgreement'] = "NO" # 是否框架协议
    # record['frameworkAgreement'] = None
    record['quotationId']['id']= max_id2+1
    record['quotationId'].pop('quotationFilingSonId')
    record['depositId'] = None # 定金
    # record['depositId']['id'] = record['id']
    # record['letterOfGuaranteeId'] = None  # 保函
    record['letterOfGuaranteeId']['id']= record['id']
    record['oaStatus'] = "TO_DO_SUBMIT"
    record['contractOption'] == "OFFLINE"
    if  record['contractOption']== "OFFLINE":  # 线上线下合同 ONLINE，OFFLINE
        record.pop('contractTemplateFileTypeId')
        record['accessories'] = {"files":
                                    [{"name":"测试附件1.pdf","type":"pdf",
                                      "url":"//lcscm-trantor-test.oss-cn-shenzhen.aliyuncs.com"
                                            "/trantor/attachments/097c6545-dc4f-46a9-abc6-32534721bcba.pdf"}]}
    else:
        record['contractOption'] = "ONLINE"
        record['accessories'] = None
    record['contractSignOption'] == "ONLINE_SIGN"   # 线上签署ONLINE_SIGN，线下签署OFFLINE_SIGN
    if record['contractSignOption'] =="ONLINE_SIGN":
        record['contractExpand']['signCommonType'] = 'COMPANY_LEGAL_PERSON'  # 签章类型 公司公章+法人名章
        record['contractExpand']['signCommonFileNumber'] = 4  # 线上签章文件份数
        record['contractExpand']['otherSealAttachment'] = None  # 线上签署-其他盖章附件
    else:
        record['contractSignOption'] = "OFFLINE_SIGN"
        record['contractExpand']['signCommonType'] = None  # 签章类型 公司公章+法人名章
        record['contractExpand']['signCommonFileNumber'] = None  # 线上签章文件份数
        record['contractExpand']['otherSealAttachment'] = None  # 线上签署-其他盖章附件
    record['isOaOption'] = True # 是否推送OA False
    record.pop('designatedDistributor')
    # record['designatedDistributor'] = [] # 指定供应商
    record['partAContactName'] ='甲方联系人'
    record['partAContactMobile']='13311111111'
    record['partAContactEmail']='13311111111@qq.com'
    record['partBContactName']='乙方联系人'
    record['partBContactMobile']='13322222222'
    record['partBContactEmail']='13322222222@qq.com'
    # print(json.dumps(data1, ensure_ascii=False))
    response1 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Conf.Settings.url1 + zidonghua.Interface.Create_Contract.api['api3'],
        json=data1, cookies=cookies).post()
    return response1.json()

if __name__ == '__main__':

    print(creat_contract(companyName='湖北家家有限公司',projectname='test1采购项目',startDateType=1))





