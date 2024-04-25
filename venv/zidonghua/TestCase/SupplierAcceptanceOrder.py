import zidonghua.Common.Requests
import zidonghua.Interface.Supplier_Acceptance_Orders
import zidonghua.Common.Cookies
import zidonghua.Common.Account
import zidonghua.Common.Select_Order


def SupplierAcceptanceOrder(mobile,so_code):   # 供应商接单
    super = zidonghua.Common.Account.Accounts(mobile)
    user = super.get_uc_user()
    project_company,enterprise = super.get_enterprise()
    so_order,po_order = zidonghua.Common.Select_Order.order(so_code).parana_order()
    cookies = zidonghua.Common.Cookies.get_cookies(mobile)
    data = zidonghua.Interface.Supplier_Acceptance_Orders.data
    data['context']['env']['datas']['id'] = po_order['id']
    data['context']['env']['datas']['supplier']['id'] =  enterprise[0]['id']
    data['context']['env']['datas']['supplier']['website'] = enterprise[0]['website']
    data['context']['env']['datas']['supplierContact']['id'] = user['id']
    data['context']['env']['datas']['supplierContact']['mobile'] = user['mobile']
    data['context']['env']['datas']['supplierContact']['nickname'] = user['nickname']
    data['context']['record'][0]['id'] = po_order['id']
    data['context']['record'][0]['supplier']['id'] = enterprise[0]['id']
    data['context']['record'][0]['supplier']['website'] = enterprise[0]['website']
    data['context']['record'][0]['supplierContact']['id'] = user['id']
    data['context']['record'][0]['supplierContact']['mobile'] = user['mobile']
    data['context']['record'][0]['supplierContact']['nickname'] = user['nickname']
    if po_order['status'] == 'PENDING_RECEIVE':
        response = zidonghua.Common.Requests.HttpUtil(
            url=zidonghua.Interface.Supplier_Acceptance_Orders.url,
            json=data, cookies = cookies).post()
        return response.json()
    else:
        return ("该订单为'{}'，无需操作").format(po_order['status'])

if __name__ == '__main__':
    print(SupplierAcceptanceOrder('18178952878','SO20240425000008'))


