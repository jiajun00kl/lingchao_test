import zidonghua.Common.Project_Goods
import zidonghua.TestCase.PurchaseGoods
import zidonghua.TestCase.SupplierAcceptanceOrder
import zidonghua.TestCase.OrderGoods
import zidonghua.TestCase.ConfirmOrder
import zidonghua.TestCase.ApplyShipment
import zidonghua.TestCase.ToShip
import zidonghua.TestCase.OaApprover
import zidonghua.TestCase.OrderAccept
import zidonghua.TestCase.InstallAccept
import time


mobile = '18178952878'
proiectname ='test1采购项目'
mobile1 = '18178952877'
item_code ='210204601003301'

def automatic():
    transaction = zidonghua.Common.Project_Goods.transaction()
    transaction.account_write(mobile)
    transaction.purse_write(mobile,proiectname)
    transaction.goods_write(mobile1,item_code)
    print('---------开始下单---------')
    order = zidonghua.TestCase.PurchaseGoods.purchase_goods(mobile,proiectname,item_code)
    so_code = order['result']['orderCodes'][0]
    if so_code is None:
        print("下单失败")
    else:
        print(order)
    time.sleep(20)
    print('---------开始接单---------')
    jiedan = zidonghua.TestCase.SupplierAcceptanceOrder.SupplierAcceptanceOrder(mobile1,so_code)
    print(jiedan)
    time.sleep(20)
    print('---------开始订货---------')
    dinghuo = zidonghua.TestCase.OrderGoods.order_goods(mobile1,so_code)
    print(dinghuo)
    time.sleep(20)
    print('---------开始确认订货---------')
    queren = zidonghua.TestCase.ConfirmOrder.confirm_orders(mobile1,so_code)
    print(queren)
    time.sleep(20)
    print('---------开始申请发货---------')
    shenqing = zidonghua.TestCase.ApplyShipment.apply_shipment(mobile1,so_code)
    print(shenqing)
    time.sleep(20)
    print('---------发货审核---------')
    shenhe = zidonghua.TestCase.ToShip.to_ship('18520611771',so_code)
    print(shenhe)
    print('---------开始oa审批---------')
    oa = zidonghua.TestCase.OaApprover.oa_approver(so_code)
    print(oa)
    time.sleep(20)
    print('---------到货验收---------')
    daohuo = zidonghua.TestCase.OrderAccept.order_accept(mobile,so_code)
    print(daohuo)
    time.sleep(20)
    print('---------安装验收---------')
    anzhuang = zidonghua.TestCase.InstallAccept.InstallAccept(mobile,so_code)
    print(anzhuang)


if __name__ == '__main__':
    automatic()

















