import zidonghua.Common.Requests
import zidonghua.Interface.Oa_Approve
import zidonghua.Common.Cookies
import zidonghua.Common.Select_Order


def oa_approver(so_code):   # 发货OA审批
    zidonghua.Interface.Oa_Approve.data['type']= 'DELIVERY'
# 付款：PAYMENT ；收款：RECEIPT；发票：INVOICE；保证额度：GUARANTEE；合同：CONTRACT;质量问题：QUALITYISSUES;
    # QMS费用账单：QMS_ACCOUNT_ORDER;退款：REFUND;保函：GUARANTEE_LETTER;发货审批: DELIVERY
    so_delivery_order, po_delivery_order = (
        zidonghua.Common.Select_Order.order(so_code).parana_delivery_order())
    zidonghua.Interface.Oa_Approve.data['instanceId'] = po_delivery_order[0]['oa_instance_id']
    response = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Interface.Oa_Approve.url,
        json = zidonghua.Interface.Oa_Approve.data ).post()
    return response.json()

if __name__ =='__main__':
    print(oa_approver('SO20240822000003'))