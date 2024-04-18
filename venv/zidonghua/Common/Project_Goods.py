import zidonghua.Common.Account
import zidonghua.Conf.Read_yaml
import zidonghua.Common.Mysql_Con

class transaction:

    def account_write(self,mobile):
        account = zidonghua.Common.Account.Accounts(mobile)
        user = account.get_uc_user()
        zidonghua.Conf.Read_yaml.write_key_yaml('user', data=user,
                                                file_yaml='user.yaml')
        account.get_enterprise()
        project_company,enterprise = account.get_enterprise()
        zidonghua.Conf.Read_yaml.write_key_yaml('enterprise',data= enterprise[0],
                                                file_yaml='enterprise.yaml')
        projects = account.select_project()
        zidonghua.Conf.Read_yaml.write_key_yaml('projects',data= projects,
                                            file_yaml='projects.yaml')

    def purse_write(self,mobile,projectname):
        purse = zidonghua.Common.Account.Purses(mobile,projectname)
        project = purse.get_project()
        zidonghua.Conf.Read_yaml.write_key_yaml('project',data= project,
                                                file_yaml= 'project.yaml')
        project_adress = purse.get_project_adress()
        zidonghua.Conf.Read_yaml.write_key_yaml('project_adress',data= project_adress,
                                                file_yaml='project_adress.yaml')

        invoice_info = purse.get_invoice_info()
        zidonghua.Conf.Read_yaml.write_key_yaml('invoice_info',data= invoice_info,
                                                file_yaml='invoice_info.yaml')

        contracts = purse.get_contract()
        zidonghua.Conf.Read_yaml.write_key_yaml('contracts',data= contracts,
                                                file_yaml='contracts.yaml')

        payment = purse.get_payment()
        zidonghua.Conf.Read_yaml.write_key_yaml('payment',data= payment,
                                            file_yaml='payment.yaml')




    def goods_write(self,mobile,item_code):
        project_company,supplier_enterprse = zidonghua.Common.Account.Accounts(mobile).get_enterprise()
        zidonghua.Conf.Read_yaml.write_key_yaml('supplier_enterprse', data = supplier_enterprse,
                                                file_yaml='supplier_enterprse.yaml')
        supplier = zidonghua.Common.Account.Supplier(mobile,item_code)
        item = supplier.get_parana_item()
        zidonghua.Conf.Read_yaml.write_key_yaml('item', data=item,
                                                file_yaml='item.yaml')
        sku = supplier.get_parana_sku()
        zidonghua.Conf.Read_yaml.write_key_yaml('sku', data=sku,
                                                file_yaml='sku.yaml')

        purse_contract = supplier.get_purchase_contract()
        zidonghua.Conf.Read_yaml.write_key_yaml('purse_contract', data=purse_contract,
                                                file_yaml='purse_contract.yaml')





































