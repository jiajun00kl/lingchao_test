import json
import time
from urllib.parse import quote
import zidonghua.Conf.Datetime
import zidonghua.Common.Mysql_Con
import zidonghua.Common.Requests
import zidonghua.Common.Cookies
import zidonghua.Conf.Settings
import zidonghua.Interface.Add_Goods


def select_shop(mobile,item_id):  # 查询商品
    cookies = zidonghua.Common.Cookies.login_cookies(mobile)
    data1 =zidonghua.Interface.Add_Goods.data1
    data1['searchValues']['itemCode']['value'] = item_id
    response1 = zidonghua.Common.Requests.HttpUtil(
        url= zidonghua.Interface.Add_Goods.url1,
        json= data1, cookies=cookies).post()
    try:
        response1.raise_for_status()
        response1.json().get('res',None).get('data',None)
        return response1.json()['res']['data']

    except Exception as err:
        return  ("查询失败" + str(err))


def look_shop(mobile,item_id):   # 查询商品信息
    cookies = zidonghua.Common.Cookies.login_cookies(mobile)
    queryValues = zidonghua.Interface.Add_Goods.data2['queryValues']
    if select_shop(mobile, item_id):
        result = select_shop(mobile, item_id)[0]
        queryValues['itemCode']['value'] = result['itemCode']
        queryValues['sellerId']['value'] = result['sellerId']
        queryValues['digitalSyncStatus']['value'] = result['digitalSyncStatus']
        queryValues['id']['value'] = result['id']
        queryValues['image']['value'] = result['image']
        queryValues['brandName']['value'] = result['brandName']
        queryValues['version']['value'] = result['version']
        queryValues['name']['value'] = result['name']
        queryValues['leadTrendYn']['value'] = result['leadTrendYn']
        queryValues['status']['value'] = result['status']
        queryValues['itemType']['value'] = result['itemType']
        queryValues['skuList']['values'][0] = result['skuList'][0]['id']
        queryValues['deletable']['value'] = result['deletable']
        queryValues['itemMarkupRate']['value'] = result['itemMarkupRate']
        queryValues['salePriceRange']['value'] = result['salePriceRange']
        queryValues['contractName']['value'] = result['contractName']
        queryValues['quickOrder']['value'] = result['quickOrder']
        queryValues['sourceFrom']['value'] = result['sourceFrom']
        queryValues['editable']['value'] = result['editable']
        queryValues['isSyncDigital']['value'] = result['isSyncDigital']
        queryValues['updatedByName']['value'] = result['updatedByName']
        if result.get('specification') is not None:
            queryValues['specification']['value'] = result['specification']
        else:
            queryValues['specification']['value'] = 'test' + zidonghua.Conf.Datetime.randomstring()
        queryValues['userId']['value'] = result['userId']
        queryValues['userId']['value'] = result['userId']
        if result.get('itemSource') is not None:
            queryValues['itemSource']['value'] = result['itemSource']
        else:
            queryValues['itemSource']['value'] ='中海发展供应链公司'
        queryValues['digitalStatus']['value'] = result['digitalStatus']
        queryValues['category']['value'] = result['category']
        queryValues['businessType']['value'] = result['businessType']
        queryValues['costPriceRange']['value'] = result['costPriceRange']
        response2 = zidonghua.Common.Requests.HttpUtil(
            url=zidonghua.Interface.Add_Goods.url1,
            json=zidonghua.Interface.Add_Goods.data2, cookies=cookies).post()
        try:
            response2.raise_for_status()
            response2.json().get('res', None).get('data', None)
            return response2.json()['res']['data']
        except Exception as err:
            return ("查询失败" + str(err))
    else:
        return "未获取到该商品信息"

def update_shop(mobile,item_id):
    cookies = zidonghua.Common.Cookies.login_cookies(mobile)
    result = look_shop(mobile, item_id)
    data3 =zidonghua.Interface.Add_Goods.data3
    record = data3['context']['record'][0]
    record['category']['id'] = result['category']['id']
    record['type'] = result['type']
    record['itemCode'] = result['itemCode']
    record['name'] = result['name']
    record['shortName'] = result['shortName']
    record['b2bPartnerVO'] = result['b2bPartnerVO']  # 供应商
    record['brand'] = result['brand']  # 品牌名称
    record['contract'] = result['contract']
    if result.get('itemLevel') is not None: # 商品档次
        record['itemLevel'] = result['itemLevel']
    else:
        record['itemLevel'] ='S'
    record['invoiceCategoryVO'] = result['invoiceCategoryVO']  # 开票品类
    record['taxRate'] = result['taxRate']  # 税率
    record['supplyCycle'] = result['supplyCycle']  # 供货周期
    record['minOrderNumber'] = result['minOrderNumber']  # 起订量
    record['deliveryFeeTemplates'] = None  # 运费模板
    record['installFeeTemplates'] = None  # 安装费模板
    record['unit'] = 'PCS'  # 单位
    record['leadTrendYn'] = result['leadTrendYn']  # 是否领潮严选
    if result.get('specialYn','')  in (0,1):
        record['specialYn'] = result['specialYn']  # 是否特殊商品
    else:
        record['specialYn'] = 1
    record['priceAdjustYn'] = result['priceAdjustYn']  # 是否参与调价
    record['isSpecialItem'] = result['isSpecialItem']  # 是否专供商品
    if result.get('specialSupply') is not None: # 专供客户
        print(result['specialSupply'])
        supplylist = []
        for i in range(len(result['specialSupply'])):
            supply = {}
            supply['id'] = result['specialSupply'][i]['id']
            supply['name'] = result['specialSupply'][i]['name']
            supply['code'] = result['specialSupply'][i]['code']
            supply['unifiedSocialCreditCode'] = result['specialSupply'][i]['unifiedSocialCreditCode']
            supplylist.append(supply)
    else:
        supplylist =[{
						"name": "湖北家家有限公司",
						"id": 138013
					}]
    if result['isSpecialItem'] ==1:
        record['specialSupply'] = supplylist
    else:
        record['specialSupply'] = None
    record['projectName'] = None  # 项目名称
    record['videoUrl'] = None  # 视频链接
    if result.get('specification') is not None: # 规格型号
        record['specification'] = result['specification']
    else:
        record['specification'] = 'test' + zidonghua.Conf.Datetime.randomstring()
    record['isSyncDigital'] = result['isSyncDigital']  # 是否同步产品数字化平台
    record['digitalStatus'] = result['digitalStatus']
    record['digitalSyncStatus'] = result['digitalSyncStatus']
    record['advertise'] = None  # 广告语
    record['keyword'] = None  # 关键词
    record['mainImageAttachment'] = result['mainImageAttachment']  # 商品主图
    record['itemChartlet'] = None  # 商品贴图
    record['itemModel'] = None # 商品模型
    record['showVirtualPrice'] = result['showVirtualPrice']  # 是否展示商品虚拟价
    if result.get('itemSource') is not None:
        record['itemSource'] = result['itemSource']
    else:
        record['itemSource'] = None
    record['id'] = result['id']
    record['categoryAttributes'] = result['categoryAttributes']
    record['skuList'] = result['skuList']
    if record['skuList'][0].get('priceExclusive') is not None:
        pass
    else:
           # 成本太低,修改价格
        record['skuList'][0]['price'] = result['skuList'][0]['price']+100
        record['skuList'][0]['itemMarkupRate'] =(
            round(record['skuList'][0]['price']/record['skuList'][0]['costPrice'],2))

        record['skuList'][0]['priceExclusive'] = (
            round(record['skuList'][0]['price']/(1+float(int(record['taxRate'].replace('%', ''))/100)),2))
    # print(record['skuList'])
    record['skuAttributes'] = result['skuAttributes']
    record['otherAttributes'][0]['otherAttributes'] = result['otherAttributes'][0]['otherAttributes']
    if result['otherAttributes'][0].get('otherAttributes')[0].get('id') is not None:
        for i in range (len(result['otherAttributes'][0]['otherAttributes'])):
            if result['otherAttributes'][0]['otherAttributes'][i]['id']== 8798:
                record['otherAttributes'][0]['otherAttributes'][i] = {
								"id": 40090,
								"attrKey": "二级分类",
								"group": "BASIC",
								"attrVal": "电缆"
							}
            elif result['otherAttributes'][0]['otherAttributes'][i]['id']== 8800:
                record['otherAttributes'][0]['otherAttributes'][i]['id'] = '40092'
            elif result['otherAttributes'][0]['otherAttributes'][i]['id']== 8801:
                record['otherAttributes'][0]['otherAttributes'][i] ={
                        "id": 128001,
                        "attrKey": "52049 线密度(kg/m)",
                        "group": "BASIC",
                        "attrVal": result['otherAttributes'][0]['otherAttributes'][i]['attrVal']
                    }
            elif result['otherAttributes'][0]['otherAttributes'][i]['id']== 8777:
                record['otherAttributes'][0]['otherAttributes'][i] ={
                        "id": 128001,
                        "attrKey": "52049 线密度(kg/m)",
                        "group": "BASIC",
                        "attrVal": result['otherAttributes'][0]['otherAttributes'][i]['attrVal']
                    }
            elif result['otherAttributes'][0]['otherAttributes'][i]['id']== 8779:
                record['otherAttributes'][0]['otherAttributes'][i] ={
								"id": 40095,
								"attrKey": "绝缘材料",
								"group": "BASIC",
								"attrVal": "绝缘材料1"
                    }
            elif result['otherAttributes'][0]['otherAttributes'][i]['id'] == 8780:
                record['otherAttributes'][0]['otherAttributes'][i] = {
								"id": 40096,
								"attrKey": "防火等级",
								"group": "BASIC",
								"attrVal": "3级"
							}
            elif result['otherAttributes'][0]['otherAttributes'][i]['id'] == 8795:
                record['otherAttributes'][0]['otherAttributes'][i] = {
                    "id": 40111,
                    "attrKey": "二级分类",
                    "group": "BASIC",
                    "attrVal": "电缆配件"
                }
    else:
        record['otherAttributes'] = [
            {
                "group": "BASIC",
                "otherAttributes": [
                    {
                        "id": 128001,
                        "attrKey": "52049 线密度(kg/m)",
                        "group": "BASIC",
                        "attrVal": zidonghua.Conf.Datetime.generate_random_n_digit_integer(2)
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
    # print(json.dumps(data3,ensure_ascii=False))
    response3 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Add_Goods.url3,
        json=data3, cookies= cookies).post()
    return  response3.json()

def daike_shop():
    sql1 = "SELECT item_code FROM parana_item  WHERE contract_id='73' and item_code >110202900112759 ;"
    result = zidonghua.Common.Mysql_Con.sql_select(sql1)
    for i in range(len(result)):
        print(result[i]['item_code'])
        print(update_shop(mobile='18520611771', item_id= result[i]['item_code']))

def grounding(mobile,item_code):   # 商品上架
    cookies = zidonghua.Common.Cookies.login_cookies(mobile)
    data4 =zidonghua.Interface.Add_Goods.data4
    data4['queryValues']['id']['value'] = item_code
    response7 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Add_Goods.url1,
        json=data4, cookies=cookies).post()
    data5 = zidonghua.Interface.Add_Goods.data5
    data5['context']['env']['itemId'] = item_code
    response8 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Add_Goods.url3,
        json=data5, cookies=cookies).post()
    data6 = zidonghua.Interface.Add_Goods.data6
    data6['context']['env']['itemId'] = item_code
    data6['context']['record'][0]['id'] = item_code
    response9 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Add_Goods.url3,
        json=data6, cookies=cookies).post()
    return response9.json()

'''
def add_goods(category,suppliername='深圳哈哈',):
    cookies = zidonghua.Common.Cookies.login_cookies(mobile='18520611771')
    searchText = quote(category)
    url4 = ("https://staging-gateway.test.lcscm.cn/zhonghai/item-center/itemcenter/1004704"
        "/api/trantor/container/tree/search?modelKey=itemcenter_BackCategoryVO&parentField=pid&"
        "searchText={}&leafOnly=true&"
        "dataActionKey=itemcenter_BackCategoryVO_BackCategoryTreeFormConfigDSAction").format(searchText)
    data4 ={}
    try:
        response1 = zidonghua.Common.Requests.HttpUtil(
            url=url4,json=data4, cookies=cookies).post()   # 返回类目信息，可模糊查询
        response1.raise_for_status()
        # print(response1.json())
    except Exception as e:
        print(e)
    categoryId = response1.json()['res'][0]['id']  # 获取类目ID
    url5 = ("https://staging-gateway.test.lcscm.cn"
        "/zhonghai/item-center/itemcenter/1004704/api/trantor/container/tree/reverse-build?"
        "modelKey=itemcenter_BackCategoryVO&recordParentId={}&parentField=pid&"
        "dataActionKey=itemcenter_BackCategoryVO_BackCategoryTreeFormConfigDSAction").format(categoryId)
    data5 ={"result":{"fields":[{"fieldName":"id"},{"fieldName":"name"},{"fieldName":"pid",
             "fields":[{"fieldName":"id"},{"fieldName":"name"}]},{"fieldName":"hasChildren"}]}}
    response2 = zidonghua.Common.Requests.HttpUtil(
        url=url5, json=data5, cookies=cookies).post()
    # print(response2.json())
    data7 =zidonghua.Interface.Add_Goods.data7
    data7['queryValues']['category']['value']= categoryId
    response3 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Add_Goods.url1, json= data7, cookies=cookies).post()  # 获取类目属性
    # print(response3.json())
    result =response3.json()['res']['data']
    categoryNameList = result['categoryNameList']
    categoryAttributes =[]
    for i in range(len(result['categoryAttributes'])):
        categoryAttributes.append(result['categoryAttributes'][i]['id'])
    data8 =zidonghua.Interface.Add_Goods.data8
    data8['queryValues']['specialRelationEnterpriseId']['value']=result['specialRelationEnterpriseId']
    data8['queryValues']['categoryNameList']['value']= categoryNameList
    data8['queryValues']['categoryAttributes']['values'] = categoryAttributes
    data8['queryValues']['category']['value'] = categoryId
    data8['fuzzyValue']= suppliername   # 供应商名称（模糊查询）
    response4 = zidonghua.Common.Requests.HttpUtil(
        url= zidonghua.Interface.Add_Goods.url8, json=data8, cookies=cookies).post()
    result1 = response4.json()['res']['data']  # 供应商信息
    # print(result1)
    enterpriseId = result1[0]['enterpriseId']
    data9 = zidonghua.Interface.Add_Goods.data9
    data9['queryValues']['enterpriseId']['value'] =enterpriseId
    response5 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Add_Goods.url9, json=data9, cookies=cookies).post()
    result2 =response5.json()['res']['data']      #查品牌
    # print(result2[0])
    brind = result2[0]['id'] # 选择品牌
    data10 = zidonghua.Interface.Add_Goods.data10
    data10['queryValues']['categoryNameList']['value'] = categoryNameList
    data10['queryValues']['categoryAttributes']['values'] = categoryAttributes
    data10['queryValues']['category']['value'] = categoryId
    data10['queryValues']['specialRelationEnterpriseId']['value'] = result['specialRelationEnterpriseId']
    data10['queryValues']['brand']['value'] = brind
    data10['queryValues']['b2bPartnerVO']['value']=result1[0]['id']
    response6 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Add_Goods.url10, json=data10, cookies=cookies).post()
    result3 = response6.json()['res']['data'] # 查找采购合同信息
    # print(result3)
    contract =result3[0]['id']  # 选择采购合同
    data11 = zidonghua.Interface.Add_Goods.data11
    data11['queryValues']['categoryNameList']['value'] = categoryNameList
    data11['queryValues']['categoryAttributes']['values'] = categoryAttributes
    data11['queryValues']['category']['value'] = categoryId
    data11['queryValues']['specialRelationEnterpriseId']['value'] = result['specialRelationEnterpriseId']
    data11['queryValues']['brand']['value'] = brind
    data11['queryValues']['b2bPartnerVO']['value'] = result1[0]['id']
    data11['queryValues']['contract']['value'] =contract
    data11['fuzzyValue'] = '电线'   #  category.split('(')[0]  开票品类名称
    response7 = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Add_Goods.url11, json=data11, cookies=cookies).post()
    result4 = response7.json()['res']['data'] # 查询开票品类
    # print(result4)
    record =zidonghua.Interface.Add_Goods.data12['context']['record'][0]
    record['category']['id'] =categoryId
    record['name'] ='自动创建test商品{}'.format(zidonghua.Conf.Datetime.generate_random_n_digit_integer(3))
    record['shortName'] = record['name']
    record['b2bPartnerVO'] = result1[0]
    record['brand']['name'] =  result2[0]['name']
    record['brand']['id'] = brind
    record['contract']['name']=result3[0]['name']
    record['contract']['id'] = contract
    record['itemLevel'] ='S'
    record['districtList'] = None   # 销售范围
    record['originPlace'] = None     # 产地
    record['invoiceCategoryVO'] =result4[0]  # 开票品类
    record['taxRate'] = "13%"  # 税率
    record['supplyCycle'] =3
    record['minOrderNumber'] = 3
    record['deliveryFeeTemplates'] = None   #  运费模版
    record['installFeeTemplates'] = None   # 安装费模版
    record['unit'] = "PCS"     # 单位
    record['leadTrendYn'] = 1     # 是否领潮严选
    record['specialYn'] = 1  # 是否特殊商品（价格无差别显示
    record['priceAdjustYn'] = 1  # 是否参与调价
    record['isSpecialItem'] = 0  # 是否专供商品
    record['projectName'] = None  # 项目名称
    record['videoUrl'] = None  # 视频链接
    record['specification'] = zidonghua.Conf.Datetime.generate_random_n_digit_integer(5)  # 规格型号
    record['isSyncDigital'] = 0  # 是否同步产品数字化平台
    record['advertise'] = '广告语'  # 广告语
    record['keyword'] = '不是关键词'  # 关键词
    record['mainImageAttachment'] = {
					"files": [
						{
							"name": "a1",
							"__trantorExtendFields": {},
							"id": "3cdf9b03-8113-4a5e-88ab-18dbea664a1b",
							"url": "https://lcscm-trantor-test.oss-cn-shenzhen.aliyuncs.com/images/manage/1000001/e77dfd97-bfec-43d6-819d-3f47f516b5f3/3cdf9b03-8113-4a5e-88ab-18dbea664a1b.jpg",
							"checked": True,
							"status": "done",
							"uid": "efd65752-3b8e-4b0e-9a38-9b0b4099e12e",
							"type": "jpg"
						}
					]
				}    #商品主图
    record['itemChartlet'] = None   # 商品贴图
    record['itemModel'] = None     # 商品模型
    record['showVirtualPrice'] = 'IS'  # 是否展示商品虚拟价
    record['categoryAttributes'] = result['categoryAttributes']
    record['skuList'][0]['id'] =  zidonghua.Conf.Datetime.generate_random_n_digit_integer(14)

'''


if __name__ == '__main__':
   print(update_shop(mobile='18520611771',item_id= '110202900112761'))
   # daike_shop()
   # add_goods(category='电线(戴科)')
