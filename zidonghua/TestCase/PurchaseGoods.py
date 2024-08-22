import datetime
import json
import zidonghua.Common.Cookies
import zidonghua.Common.Requests
import zidonghua.Interface.Purchase_Goods
import zidonghua.Conf.Read_yaml
import zidonghua.Conf.Settings
import decimal

def purchase_goods(mobile,projectname,item_code):  # 下单

    project = zidonghua.Conf.Read_yaml.read_yaml_all('project.yaml')['project']
    data = zidonghua.Interface.Purchase_Goods.data
    data['projectId'] = project['id']
    #  data['paymentType'] = "offline"
    data['isQuickGetOrder'] = False
    data['projectName'] = project['name']
    address = json.loads(project['address'])
    data['address']['address'] = address['address']
    data['address']['detail'] = address['detail']
    data['address']['region'] = address['address'][2]
    data['address']['city'] = address['address'][1]
    data['address']['province'] = address['address'][0]
    data['orderAddress'] = ((address)['address'][0]['name'] + address['address'][1]['name'] +
        address['address'][1]['name'] +address['detail'])
    enterprise = zidonghua.Conf.Read_yaml.read_yaml_all('enterprise.yaml')['enterprise']
    data['orderTitle'] = (datetime.datetime.now().strftime('%Y%m%d')
        + str(enterprise['name']) + str(project['name']))
    user = zidonghua.Conf.Read_yaml.read_yaml_all('user.yaml')['user']
    data['orderUserName'] = user['nickname']
    data['orderPhone'] = user['mobile']
    data['projectContactName'] = user['nickname']
    data['projectContactPhone'] = user['mobile']
    data['orderContactId'] = user['id']
    contract = zidonghua.Conf.Read_yaml.read_yaml_all('contracts.yaml')['contracts'][0]
    data['salesContractId'] = contract['id']
    invoice_info = zidonghua.Conf.Read_yaml.read_yaml_all('invoice_info.yaml')['invoice_info'][0]
    data['invoice']['id'] = invoice_info['id']
    data['invoice']['invoiceType'] = invoice_info['invoice_type']
    data['invoice']['titleType'] = invoice_info['title_type']
    data['invoice']['invoiceCompany'] = (
        invoice_info)['invoice_company']
    data['invoice']['invoicePersonal'] =\
        invoice_info['invoice_personal']
    data['invoice']['title'] = invoice_info['title']
    data['invoice']['taxpayerCode'] = invoice_info['taxpayer_code']
    data['invoice']['uscc'] = invoice_info['uscc']
    data['invoice']['invoiceBank'] = invoice_info['invoice_bank']
    data['invoice']['invoiceAccount'] = (
        invoice_info)['invoice_account']
    data['invoice']['recipientName'] = (
        invoice_info)['recipient_name']
    data['invoice']['recipientPhone'] =\
        invoice_info['recipient_phone']
    data['invoice']['recipientAddress'] = (
        invoice_info)['recipient_address']
    data['invoice']['invoiceRemark'] = project['invoice_remark']
    data['invoice']['invoiceAddress'] =\
        invoice_info['invoice_address']
    data['invoice']['invoiceMobile'] = invoice_info['invoice_mobile']
    supplier_enterprse = (
        zidonghua.Conf.Read_yaml.read_yaml_all('supplier_enterprse.yaml'))['supplier_enterprse'][0]
    data['orderList'][0]['supplierId'] = supplier_enterprse['id']
    payment = zidonghua.Conf.Read_yaml.read_yaml_all('payment.yaml')['payment']
    data['orderList'][0]['paymentId'] = payment[2]['id']
    data['orderList'][0]['paymentRadix'] = payment[2]['radix']
    item = zidonghua.Conf.Read_yaml.read_yaml_all('item.yaml')['item']
    sku = zidonghua.Conf.Read_yaml.read_yaml_all('sku.yaml')['sku']
    data['orderList'][0]['orderContactId'] = user['id']
    data['orderList'][0]['brandOwnerId'] = supplier_enterprse['id']
    price = float(sku['price'].quantize(decimal.Decimal('0.00')))
    quantity = item['min_order_number']
    data['orderList'][0]['itemTotalAmount'] = price * quantity
    data['orderList'][0]['installTotalAmount'] = item['install_fee_factor']
    data['orderList'][0]['totalAmount'] = price * payment[2]['radix']*quantity
    data['orderList'][0]['totalAmountprice'] = price * quantity
    data['orderList'][0]['totalAmountPriceExclusive'] = (price
                *float(sku['tax_rate'])*quantity/100)
    data['orderList'][0]['orderLineList'][0]['itemId'] = sku['item_id']
    data['orderList'][0]['orderLineList'][0]['skuId'] = sku['id']
    data['orderList'][0]['orderLineList'][0]['skuCode'] = sku['sku_code']
    data['orderList'][0]['orderLineList'][0]['minOrderNum'] = quantity
    data['orderList'][0]['orderLineList'][0]['quantity'] = quantity
    data['orderList'][0]['orderLineList'][0]['shopId'] = item['seller_id']
    data['orderList'][0]['orderLineList'][0]['lineId'] = item['item_code']
    data['orderList'][0]['orderLineList'][0]['categoryId'] = item['category_id']
    data['orderList'][0]['orderLineList'][0]['skuName'] = item['name']
    data['orderList'][0]['orderLineList'][0]['mainImage'] = item['main_image']
    data['orderList'][0]['orderLineList'][0]['status'] = item['status']
    data['orderList'][0]['orderLineList'][0]['salePrice'] = price
    data['orderList'][0]['orderLineList'][0]['itemCode'] = item['item_code']
    data['orderList'][0]['orderLineList'][0]['contractId'] = item['contract_id']
    data['orderList'][0]['orderLineList'][0]['shopName'] = item['seller_name']
    data['orderList'][0]['orderLineList'][0]['categoryIds'] =json.loads ((
        json.loads(item['extra_json']))['categoryList'])
    data['orderList'][0]['orderLineList'][0]['brandId'] = item['brand_id']
    data['orderList'][0]['orderLineList'][0]['brandName'] = item['brand_name']
    data['orderList'][0]['orderLineList'][0]['specification'] = item['specification']
    data['orderList'][0]['orderLineList'][0]['name'] = item['name']
    data['orderList'][0]['orderLineList'][0]['unit'] = item['unit']
    data['orderList'][0]['orderLineList'][0]['taxRate'] = float(sku['tax_rate'])
    data['orderList'][0]['orderLineList'][0]['preferSalePrice'] = (
            price * payment[2]['radix']*quantity)
    data['orderList'][0]['orderLineList'][0]['priceRanges'] = sku['range_price_json']
    data['orderList'][0]['orderLineList'][0]['taxPriceMoney'] = price * quantity
    data['orderList'][0]['orderLineList'][0]['taxPrice'] = price * quantity
    data['orderList'][0]['orderLineList'][0]['totalPrice'] = (
        price *quantity)
    data['orderList'][0]['orderLineList'][0]['totalPriceExclusive'] = (price
                *float(sku['tax_rate'])*quantity/100)
    data['orderList'][0]['orderLineList'][0]['subtotal'] = (
            price * payment[2]['radix']*quantity)
    cookies = zidonghua.Common.Cookies.get_cookies(mobile)
    response = zidonghua.Common.Requests.HttpUtil(
        url = zidonghua.Conf.Settings.url + zidonghua.Interface.Purchase_Goods.api,
        json = data,cookies = cookies).post()
    orderCodes =response.json()['result']['orderCodes']
    if data['paymentType'] == "offline" :
        zidonghua.Interface.Purchase_Goods.data1['orderCodes'] =orderCodes
        zidonghua.Interface.Purchase_Goods.data1['projectId'] = project['id']
        cookies = zidonghua.Common.Cookies.get_cookies(mobile)
        response1 = zidonghua.Common.Requests.HttpUtil(
            url=zidonghua.Conf.Settings.url + zidonghua.Interface.Purchase_Goods.api1,
            json=zidonghua.Interface.Purchase_Goods.data1, cookies=cookies).post()
        return response.json(),response1.json()
    else:
        return response.json()

if __name__ == '__main__':
    response = (
        purchase_goods('18178952878','武汉的项目','210204601003301'))
    print(response)





