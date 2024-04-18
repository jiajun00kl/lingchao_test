import zidonghua.Common.Mysql_Con
import zidonghua.Common.Select_Order




def order_settlement(so_code):
    order = zidonghua.Common.Select_Order.order(so_code)
    sql = "select * from  order_settlement where `order` ='{}' ;".format(order.so_id)
    so_settlement = zidonghua.Common.Mysql_Con.sql_select(sql)
    sql = "select * from  order_settlement where `order` ='{}' ;".format(order.po_id)
    po_settlement = zidonghua.Common.Mysql_Con.sql_select(sql)
    return so_settlement,po_settlement

def settlement_receivable(so_code):
    order = zidonghua.Common.Select_Order.order(so_code)
    sql = "select * from  settlement_center__receivable where order_id ='{}' ;".format(order.so_id)
    receivable = zidonghua.Common.Mysql_Con.sql_select(sql)
    return receivable

def settlement_payable(so_code):
    order = zidonghua.Common.Select_Order.order(so_code)
    sql1 = ("select payable_source_code,payable_source_type from  settlement_center__payable "
           "where order_id ='{}'GROUP BY payable_source_code,payable_source_type ;").format(order.po_id)
    payable1 = zidonghua.Common.Mysql_Con.sql_select(sql1)
    sql = ("select * from  settlement_center__payable "
           "where order_id ='{}' ;").format(order.po_id)
    payable = zidonghua.Common.Mysql_Con.sql_select(sql)
    return payable,payable1

def sale_check(so_code):
    order = zidonghua.Common.Select_Order.order(so_code)
    sql =("select * from sales_check where id in("
          "SELECT sales_check_id FROM  sales_check_line WHERE `order` ='{}');").format(order.so_id)
    salecheck = zidonghua.Common.Mysql_Con.sql_select(sql)
    return salecheck







if __name__ == '__main__':

    payable,payable1= settlement_payable('SO20240119000001')
    print(payable1)


