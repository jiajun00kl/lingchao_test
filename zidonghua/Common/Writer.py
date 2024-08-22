import zidonghua.Conf.Read_yaml
import zidonghua.Common.Mysql_Con
import zidonghua.TestCase.SelectGoodsDetail
import zidonghua.TestCase.SelectProjectDetails

def writer_project(mobile,project_name):
    project_detail = zidonghua.TestCase.SelectProjectDetails.select_project_details(mobile,project_name)
    zidonghua.Conf.Read_yaml.write_key_yaml('project_detail',
               data = project_detail['res']['data'],file_yaml = 'project_detail.yaml')

    sql = ("select *  from contract_center_contract "
           "where project='{}' and contract_type = 'SALE_CONTRACT'"
           "").format(project_detail['res']['data']['id'])
    contracts = zidonghua.Common.Mysql_Con.sql_select(sql)
    zidonghua.Conf.Read_yaml.write_key_yaml('contracts',
                                                      data= contracts,
                                                      file_yaml='contracts.yaml')

def write_contract_payment(salesContractId):
    sql = ("SELECT * FROM contract_center_contract_payment_iterm"
           " WHERE ContractContractPaymentIterm='{}';").format(salesContractId)
    payment = zidonghua.Common.Mysql_Con.sql_select(sql)
    zidonghua.Conf.Read_yaml.write_key_yaml('payment',data = payment,file_yaml='payment.yaml')


def write_payment_codition(paymentId):
    sql1 = ("SELECT * FROM contract_center_contract_payment_condition"
            " WHERE contract_payment_iterm ='{}';").format(paymentId)
    payment_condition = zidonghua.Common.Mysql_Con.sql_select(sql1)
    zidonghua.Conf.Read_yaml.write_key_yaml('payment_condition',
                                            data= payment_condition, file_yaml='payment_condition.yaml')

def writer_goods_detail(mobile,item_id):
    goods_detail = zidonghua.TestCase.SelectGoodsDetail.select_goods_detail(mobile,item_id)
    zidonghua.Conf.Read_yaml.write_key_yaml('goods_detail',
               data = goods_detail['res']['data'],file_yaml = 'goods_detail.yaml')
def repair_writer_goods_detail(mobile,item_id):
    goods_detail = zidonghua.TestCase.SelectGoodsDetail.select_goods_detail(mobile, item_id)
    zidonghua.Conf.Read_yaml.write_key_yaml('goods_detail',
                            data=goods_detail['res']['data'], file_yaml='goods_detail.yaml')


# writer_project('18178952878','test1采购项目')
# writer_goods_detail('admin','210204601003306')
# repair_writer_goods_detail('admin','210204601003306')

