import time
import zidonghua.TestCase.SettlementOrders
import zidonghua.TestCase.SettlementConfirmation
import zidonghua.TestCase.SalesCheck
import zidonghua.TestCase.ConfirmSales
import zidonghua.TestCase.GeneratePayment


def settlementreconciliation(Cmobile,Gmobile,Pmobile,so_code):
    print("-----供应商发起需求单结算-----")
    response1 = zidonghua.TestCase.SettlementOrders.settlement_orders(Gmobile,so_code)
    print(response1)
    time.sleep(5)
    print("-----采购商对账单确认-----")
    response2 = zidonghua.TestCase.SettlementConfirmation.settlement_confirmation(Pmobile,so_code)
    print(response2)
    time.sleep(3)
    print("-----平台销售结算对账单生成-----")
    response3 = zidonghua.TestCase.SalesCheck.sales_check(Pmobile,so_code)
    print(response3)
    time.sleep(3)
    print("-----采购商确认对账单-----")
    response4 = zidonghua.TestCase.ConfirmSales.TestConfirmSales(Cmobile,so_code)
    print(response4)
    time.sleep(3)
    print("-----平台生成收款单-----")
    response5 = zidonghua.TestCase.GeneratePayment.generate_payment(Pmobile,so_code)
    print(response5)
    time.sleep(3)

if __name__ == '__main__':
    Cmobile = '18178952878'
    Gmobile = '18178952877'
    Pmobile = '18520611771'
    settlementreconciliation(Cmobile,Gmobile,Pmobile,so_code='SO20240222000006')








