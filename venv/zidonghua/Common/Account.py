import zidonghua.Common.Mysql_Con

class Accounts:
    def __init__(self,mobile):
        self.mobile = mobile

    def get_uc_user(self):
        sql="SELECT *  FROM uc_user WHERE mobile = '{}';".format(self.mobile)
        users = zidonghua.Common.Mysql_Con.sql_select(sql)[0]
        return  users

    def get_enterprise(self):
        sql = "select * from md_enterprise where contactPhone = '{}';".format(self.mobile)
        users = zidonghua.Common.Mysql_Con.sql_select(sql)
        project_company = []
        enterprise = []
        if len(users)>2:
            for i in  range(len(users)):
                if users[i]['unified_social_credit_code'] is not None :
                    if users[i]['enterprise_type'] == 'COC':
                        project_company.append(users[i])
                    else:
                        enterprise.append(users[i])
        else:
            for i in range(len(users)):
                if users[i]['enterprise_type'] == 'COC':
                    project_company.append(users[i])
                else:
                    enterprise.append(users[i])
        return project_company,enterprise

    def select_project(self):   # 查项目
        project_company, enterprise = Purses.get_enterprise(self)
        project_purse_id = enterprise[0]['id']
        sql = ("SELECT * FROM partner_center_project  where purchaser_id = '{}'"
               "and  isAvailable='1' and isDeleted='0' and `status`='ENABLED'").format(project_purse_id)
        projects = zidonghua.Common.Mysql_Con.sql_select(sql)
        return projects


class Purses(Accounts):  # 采购商
    def __init__(self, mobile,projectname):
        self.mobile = mobile
        self.projectname = projectname

    def get_project(self):  # 项目名查项目
        project_company, enterprise = Purses.get_enterprise(self)
        project_purse_id = enterprise[0]['id']
        sql = ("SELECT * FROM partner_center_project  where purchaser_id = '{}'"
               "and  isAvailable='1' and isDeleted='0' and `status`='ENABLED'").format(project_purse_id)
        projects = zidonghua.Common.Mysql_Con.sql_select(sql)
        for i in range(len(projects)):
            if self.projectname == projects[i]['name']:
                return projects[i]
        return projects[i]

    def get_project_adress(self):  # 项目查项目默认地址
        projects = Purses.get_project(self)
        sql = ("SELECT * FROM  partner_center_project_address  "
                   "where partner_center_project_id ='{}';").format(projects['id'])
        projectadress = zidonghua.Common.Mysql_Con.sql_select(sql)
        for j in range(len(projectadress)):
            if projectadress[j]['type'] =='1':
                projectadress[j]
        return projectadress[j]

    def get_contract(self):  # 项目查销售合同
        projects = Purses.get_project(self)
        sql =("SELECT * FROM contract_center_contract where project ='{}' "
                  " and isDeleted= '0' and `status` ='ENABLE';").format(projects['id'])
        contracts = zidonghua.Common.Mysql_Con.sql_select(sql)
        return contracts

    def get_invoice_info(self):  #项目查项目公司的开票信息
        projects = Purses.get_project(self)
        sql = ("select * from partner_center_corporate_company   WHERE id ='{}'"
                   " and isAvailable='1' and uscc is not NULL ").format(projects['corporate_company'])
        corporate_company = zidonghua.Common.Mysql_Con.sql_select(sql)[0]
        sql1 =("select *  from   partner_center_invoice_info "
                   "where id ='{}'").format(corporate_company['invoice_info'])
        invoice_infos = zidonghua.Common.Mysql_Con.sql_select(sql1)
        return invoice_infos

    def get_payment(self):   #项目合同的付款条件
        projects = Purses.get_project(self)
        sql = ("SELECT * FROM contract_center_contract where project ='{}' "
                   " and isDeleted= '0' and `status` ='ENABLE';").format(projects['id'])
        contracts = zidonghua.Common.Mysql_Con.sql_select(sql)[0]
        sql1 =("select * from contract_center_contract_payment_iterm "
                   "where ContractContractPaymentIterm='{}';").format(contracts['id'])
        payment = zidonghua.Common.Mysql_Con.sql_select(sql1)
        return payment

class Supplier(Accounts):  # 供应商
    def __init__(self,mobile,item):
        self.mobile = mobile
        self.item = item

    def get_parana_item(self):   # 供应上下通过item的id查找商品信息
        project_company, enterprise = Supplier.get_enterprise(self)
        sql = "select * from parana_item  where item_code='{}'".format(self.item)
        goods = zidonghua.Common.Mysql_Con.sql_select(sql)[0]
        if  goods['seller'] == enterprise[0]['id']:
                return  goods
        return goods

    def get_parana_sku(self): # 通过item找对应价格信息
        good = Supplier.get_parana_item(self)
        if good is not None:
            item_id = good['id']
        sql = "SELECT * FROM parana_sku  where item_id ='{}';".format(item_id)
        parana_sku = zidonghua.Common.Mysql_Con.sql_select(sql)
        return parana_sku[0]

    def get_purchase_contract(self):  #  通过item找合同
        good = Supplier.get_parana_item(self)
        sql =("SELECT * FROM  contract_center_contract "
              " where  id='{}' and   isDeleted= '0' ;").format(good['contract_id'])
        purchase_contract = zidonghua.Common.Mysql_Con.sql_select(sql)
        return purchase_contract





































































