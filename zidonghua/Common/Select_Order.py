import zidonghua.Common.Mysql_Con

class order():
    def __init__(self,so_code):
        self.so_code = so_code
        self.so_id = None
        self.po_id = None

    @property
    def po_id(self):
        return self._po_id
    @po_id.setter
    def po_id(self,poId):
        sql= "SELECT *  FROM parana_order WHERE parent_order_code ='{}'; ".format(self.so_code)
        po_order = zidonghua.Common.Mysql_Con.sql_select(sql)
        self._po_id = po_order[0]['id']

    @property
    def so_id(self):
        return self._so_id
    @so_id.setter
    def so_id(self,soId):
        sql = "SELECT *  FROM parana_order WHERE code ='{}'; ".format(self.so_code)
        so_order = zidonghua.Common.Mysql_Con.sql_select(sql)
        self._so_id = so_order[0]['id']

    def parana_order(self):  # 需求单
        sql = "SELECT *  FROM parana_order WHERE id= '{}';".format(self.so_id)
        so_order = zidonghua.Common.Mysql_Con.sql_select(sql)[0]

        sql1 = "SELECT *  FROM parana_order WHERE id ='{}'; ".format(self.po_id)
        po_order = zidonghua.Common.Mysql_Con.sql_select(sql1)[0]
        return so_order,po_order

    def parana_order_line(self):  # 需求单行表
        sql = ("SELECT *  FROM parana_order_line WHERE order_id= '{}' ;").format(self.so_id)
        so_order_line = zidonghua.Common.Mysql_Con.sql_select(sql)[0]

        sql1 = ("SELECT *  FROM parana_order_line WHERE order_id= '{}' ;").format(self.po_id)
        po_order_line = zidonghua.Common.Mysql_Con.sql_select(sql1)[0]
        return so_order_line, po_order_line

    def parana_get_goods_order(self):  # 订单
        sql = ("SELECT * FROM parana_get_goods_order "
               "WHERE `order`='{}' ORDER BY `code` DESC;").format(self.so_id)
        so_goods_order = zidonghua.Common.Mysql_Con.sql_select(sql)

        sql1=("SELECT * FROM parana_get_goods_order "
              "WHERE `order`='{}' ORDER BY `code` DESC;").format(self.po_id)
        po_goods_order = zidonghua.Common.Mysql_Con.sql_select(sql1)
        return so_goods_order,po_goods_order

    def parana_get_goods_order_line(self):
        sql =("SELECT * FROM parana_get_goods_order_line "
              "WHERE get_goods_order_line_id in (SELECT id FROM "
              "parana_get_goods_order WHERE `order`='{}' ORDER BY `code` DESC);").format(self.so_id)
        so_goods_order_line = zidonghua.Common.Mysql_Con.sql_select(sql)

        sql1 = ("SELECT * FROM parana_get_goods_order_line "
              "WHERE get_goods_order_line_id in (SELECT id FROM parana_get_goods_order"
                " WHERE `order`='{}' ORDER BY `code` DESC);").format(self.po_id)
        po_goods_order_line = zidonghua.Common.Mysql_Con.sql_select(sql1)
        return so_goods_order_line,po_goods_order_line

    def parana_delivery_order(self): # 发货
        sql = ("SELECT * FROM parana_delivery_order "
               "WHERE `order` ='{}' ORDER BY `code` DESC;").format(self.so_id)
        so_delivery_order = zidonghua.Common.Mysql_Con.sql_select(sql)

        sql1 = ("SELECT * FROM parana_delivery_order "
                "WHERE `order` ='{}' ORDER BY `code` DESC;").format(self.po_id)
        po_delivery_order = zidonghua.Common.Mysql_Con.sql_select(sql1)
        return so_delivery_order,po_delivery_order

    def parana_delivery_order_line(self):
        sql = ("SELECT * FROM parana_delivery_order_line  "
               "WHERE delivery_order_line_id IN (SELECT id FROM parana_delivery_order"
               " WHERE `order` ='{}' ORDER BY `code` DESC);").format(self.so_id)
        so_delivery_order_line = zidonghua.Common.Mysql_Con.sql_select(sql)

        sql1 = ("SELECT * FROM parana_delivery_order_line  "
               "WHERE delivery_order_line_id IN (SELECT id FROM parana_delivery_order"
               " WHERE `order` ='{}' ORDER BY `code` DESC);").format(self.po_id)
        po_delivery_order_line = zidonghua.Common.Mysql_Con.sql_select(sql1)
        return so_delivery_order_line,po_delivery_order_line

    def parana_acceptance_order(self):  # 到货安装
        sql = ("SELECT * FROM parana_acceptance_order  "
               "WHERE  `order` ='{}' ORDER BY `code` DESC ;").format(self.so_id)
        so_acceptance_order = zidonghua.Common.Mysql_Con.sql_select(sql)

        sql1 = ("SELECT * FROM parana_acceptance_order  "
                "WHERE  `order` ='{}' ORDER BY `code` DESC ;").format(self.so_id)
        po_acceptance_order = zidonghua.Common.Mysql_Con.sql_select(sql1)
        return so_acceptance_order,po_acceptance_order

    def parana_acceptance_order_line(self):
        sql = ("SELECT * FROM parana_acceptance_order_line  "
               "where  acceptance_order_line_id IN (SELECT id FROM parana_acceptance_order "
               " where  `order` ='{}' ORDER BY `code` DESC) ;").format(self.so_id)
        so_acceptance_order_line = zidonghua.Common.Mysql_Con.sql_select(sql)

        sql1 = ("SELECT * FROM parana_acceptance_order_line  "
               "where  acceptance_order_line_id IN (SELECT id FROM parana_acceptance_order "
               " where  `order` ='{}' ORDER BY `code` DESC) ;").format(self.po_id)
        po_acceptance_order_line = zidonghua.Common.Mysql_Con.sql_select(sql1)
        return so_acceptance_order_line,po_acceptance_order_line

    def parana_reverse_order(self): # 退货
        sql = ("SELECT   * FROM parana_reverse_order "
                "WHERE  `order` ='{} ORDER BY `code` ';").format(self.so_id)
        so_reverse_order = zidonghua.Common.Mysql_Con.sql_select(sql)

        sql1 = ("SELECT   * FROM parana_reverse_order "
               "WHERE  `order` ='{} ORDER BY `code` ';").format(self.po_id)
        po_reverse_order = zidonghua.Common.Mysql_Con.sql_select(sql1)
        return so_reverse_order,po_reverse_order

    def parana_reverse_order_line(self):
        sql = ("SELECT   * FROM parana_reverse_order_line "
               "where  reverse_order_id in (SELECT id FROM parana_reverse_order"
               " WHERE  `order` ='{}' and reverse_num > 0 );").format(self.so_id)
        so_reverse_order_line = zidonghua.Common.Mysql_Con.sql_select(sql)

        sql1 = ("SELECT   * FROM parana_reverse_order_line "
               "where  reverse_order_id in (SELECT id FROM parana_reverse_order"
               " WHERE  `order` ='{}' and reverse_num > 0 );").format(self.po_id)
        po_reverse_order_line = zidonghua.Common.Mysql_Con.sql_select(sql1)
        return so_reverse_order_line,po_reverse_order_line

    def settlement_center__receivable(self): # 应收
        sql = ("select * from settlement_center__receivable scr "
               "where order_id='{}';").format(self.so_id)
        receivable = zidonghua.Common.Mysql_Con.sql_select(sql)
        return receivable

    def settlement_center__payable(self):  # 应付
        sql = ("SELECT * FROM settlement_center__payable scp "
               " where order_id='{}';").format(self.po_id)
        payable = zidonghua.Common.Mysql_Con.sql_select(sql)
        return payable

    def sales_check_line(self): # 通过订单查找对应对账单行表，查询对应的对账单
        sql = ("SELECT * FROM  sales_check_line WHERE `order` ='{}';").format(self.so_id)
        sales_checks = zidonghua.Common.Mysql_Con.sql_select(sql)
        sales_check_id = sales_checks[0]['sales_check_id']
        sql1 = ("SELECT * FROM  sales_check_line WHERE sales_check_id ='{}';").format(sales_check_id)
        sales_check_line = zidonghua.Common.Mysql_Con.sql_select(sql1)
        sql2 = ("SELECT * FROM  sales_check  WHERE id ='{}';").format(sales_check_id)
        sales_check =  zidonghua.Common.Mysql_Con.sql_select(sql2)
        return sales_check


if __name__ == '__main__':
    so = order('SO20240110000003')
    so_order,po_order = so.parana_order()
    so_order_line, po_order_line = so.parana_order_line()
    so_goods_order,po_goods_order = so.parana_get_goods_order()
    so_goods_order_line,po_goods_order_line = so.parana_get_goods_order_line()
    so_delivery_order,po_delivery_order = so.parana_delivery_order()
    so_delivery_order_line,po_delivery_order_line = so.parana_delivery_order_line()
    so_acceptance_order,po_acceptance_order = so.parana_acceptance_order()
    so_acceptance_order_line,po_acceptance_order_line = so.parana_acceptance_order_line()
    so_reverse_order,po_reverse_order = so.parana_reverse_order()
    so_reverse_order_line,po_reverse_order_line = so.parana_reverse_order_line()














    

    


































